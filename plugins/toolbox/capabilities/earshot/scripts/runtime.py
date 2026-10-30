#!/usr/bin/env python3
"""Toolbox Earshot launcher: a pinned, verified local Earshot runtime and an allowlist of local commands.

    python3 runtime.py status [--json]
    python3 runtime.py install --tier light|full [--yes]
    python3 runtime.py fetch-models [--from <other root>] [--yes]
    python3 runtime.py attach-source [--yes]
    python3 runtime.py [--allow-unlocked] run [--threads N] <command> [args...]
    python3 runtime.py [--allow-unlocked] python <real-sound script> [args...]
    python3 runtime.py [--allow-unlocked] exec [python args...]   the venv interpreter with the offline cache: {{PY}}

Standard library only. `status` never writes and only lists other runtime roots it finds, never selecting one;
`install`, `fetch-models` and `attach-source` print their plan and write nothing without --yes. The engine comes from one pinned upstream commit, and every file is checked against upstream.json before
anything is installed. The `llm` (audio upload to Gemini) and `mcp` (server) commands are outside this plugin and are
refused before any process starts. Runs are offline: models must already be in the cache.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import stat
import struct
import urllib.request
import zipfile
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent   # plugins/toolbox/capabilities/earshot
TOOLBOX = PLUGIN.parents[1]                        # the Toolbox plugin root
PREFIX = 'toolbox/earshot: '
REQUIREMENTS = PLUGIN / 'requirements'


def _toolbox_version():
    try:
        return json.loads((TOOLBOX / 'plugin.json').read_text(encoding='utf-8'))['version']
    except (OSError, ValueError, KeyError):
        return 'unknown'


WRAPPER_VERSION = _toolbox_version()
# Runtime roots made by earlier routes; status lists them, the user chooses.
LEGACY_ROOTS = ('.framecore-studio/extensions/earshot',)
PIN = {'repository': 'https://github.com/Leonxlnx/earshot', 'tag': 'v0.4.0',
       'commit': '591fa3e028032e6dce56620a20e932e35667e8d8', 'tree': 'd6f2dbc43f7b38b2147cfd04bbd7aa9055701f1a'}
ALLOWED = frozenset({'doctor', 'measure', 'describe', 'match', 'rank', 'find', 'compare', 'ab', 'realness', 'timeline',
                     'sheet', 'critique', 'profile', 'forge', 'fit', 'sfx', 'kit', 'gallery'})
TORCH_INDEX = 'https://download.pytorch.org/whl/cpu'
MODELS = ('laion/larger_clap_general', 'MIT/ast-finetuned-audioset-10-10-0.4593')
MODEL_PINS = {
    MODELS[0]: {'revision': '16c8cc3159a3c8a31e8ff5ef1f66b0d9ab3667db',
                'files': ['config.json', 'preprocessor_config.json', 'merges.txt', 'special_tokens_map.json',
                          'tokenizer.json', 'tokenizer_config.json', 'vocab.json', 'model.safetensors']},
    MODELS[1]: {'revision': 'f826b80d28226b62986cc218e5cec390b1096902',
                'files': ['config.json', 'preprocessor_config.json', 'model.safetensors']},
}
OFFLINE = {'EARSHOT_OFFLINE': '1', 'HF_HUB_OFFLINE': '1', 'TRANSFORMERS_OFFLINE': '1'}
SIZES = {'light': 'about 360 MB (engine, NumPy, SciPy, librosa and friends; measured 358 MB on 2026-10-30)',
         'full': 'about 1.5 GB (light plus CPU PyTorch and transformers); models are a separate fetch-models step, about 1.1 GB'}


class Refused(Exception):
    pass


def default_root():
    return Path(os.environ.get('EARSHOT_NATIVE_ROOT') or Path.home() / '.framecore-works' / 'earshot')


def real_command(argv):
    """The earshot subcommand after any global options (`--threads N` or `--threads=N`)."""
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == '--threads':
            i += 2
        elif arg.startswith('-'):
            i += 1
        else:
            return arg
    return None


def check_command(argv):
    name = real_command(argv)
    if name is None:
        raise Refused('no earshot command given')
    if name not in ALLOWED:
        raise Refused(f'`{name}` is not available in Toolbox Earshot (local commands only: {", ".join(sorted(ALLOWED))})')
    if name == 'doctor' and any(a == '--fetch' or a.startswith('--fetch=') for a in argv):
        raise Refused('model downloads go through `runtime.py fetch-models --yes`, not doctor --fetch')


def real_sound_script(name, root=None):
    source = Path(root or default_root()) / 'upstream'
    folder = source / 'skills' / 'real-sound' / 'scripts'
    if Path(name).name != name or not name.endswith('.py'):
        raise Refused('name a Python real-sound script, without a path')
    path = folder / name
    if not path.is_file() or path.is_symlink():
        raise Refused('real-sound source is unavailable; add it with `runtime.py attach-source --yes` or install a new root')
    problems = verify_tree(source, load_manifest()['files'])
    if problems:
        raise Refused('real-sound source differs from the pinned snapshot: ' + ', '.join(problems[:3]))
    return path


def venv_python(root):
    for candidate in (Path(root) / 'venv' / 'bin' / 'python', Path(root) / 'venv' / 'Scripts' / 'python.exe'):
        if candidate.exists():
            return candidate
    return None


def load_manifest():
    return json.loads((PLUGIN / 'upstream.json').read_text(encoding='utf-8'))


def verify_tree(src, manifest):
    """Paths that differ from the manifest: changed, missing or extra (the .git folder is ignored)."""
    src = Path(src)
    found = {p.relative_to(src).as_posix(): p for p in src.rglob('*') if p.is_file() and '.git' not in p.relative_to(src).parts}
    links = [p.relative_to(src).as_posix() for p in src.rglob('*') if p.is_symlink() and '.git' not in p.relative_to(src).parts]
    problems = [path for path, digest in manifest.items()
                if path not in found or hashlib.sha256(found[path].read_bytes()).hexdigest() != digest]
    problems += [path for path in found if path not in manifest]
    return sorted(set(problems + links))


def fetch_source(dest):
    """The pinned upstream source in dest: git at the exact commit (tree checked), else the commit's archive."""
    dest = Path(dest)
    if shutil.which('git'):
        repo = dest / 'earshot'
        steps = [['git', 'init', '-q', str(repo)], ['git', '-C', str(repo), 'fetch', '-q', '--depth=1', PIN['repository'], PIN['commit']],
                 ['git', '-C', str(repo), 'checkout', '-q', 'FETCH_HEAD']]
        try:
            for step in steps:
                subprocess.run(step, check=True, capture_output=True, timeout=600)
            tree = subprocess.run(['git', '-C', str(repo), 'rev-parse', 'HEAD^{tree}'], check=True, capture_output=True, text=True).stdout.strip()
            if tree == PIN['tree']:
                return repo
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            pass
        shutil.rmtree(repo, ignore_errors=True)
    archive = dest / 'earshot.zip'
    # A stalled download must not hang the install: the same 600 s bound as the git route.
    with urllib.request.urlopen(f"{PIN['repository']}/archive/{PIN['commit']}.zip", timeout=600) as response, \
            open(archive, 'wb') as out:
        shutil.copyfileobj(response, out)
    with zipfile.ZipFile(archive) as zf:
        for member in zf.infolist():
            path = Path(member.filename)
            if path.is_absolute() or '..' in path.parts or '\\' in member.filename or stat.S_ISLNK(member.external_attr >> 16):
                raise OSError('unsafe path in upstream archive')
        zf.extractall(dest / 'unzipped')
    return next((dest / 'unzipped').iterdir())


def _python_ok(python, modules):
    try:
        return subprocess.run([str(python), '-c', f'import {", ".join(modules)}'], capture_output=True, timeout=120).returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def model_cache_status(root):
    """Check exact pinned snapshots and file structure; never claim inference."""
    reports = {}
    for model, pin in MODEL_PINS.items():
        snapshot = Path(root) / 'cache' / 'hf' / ('models--' + model.replace('/', '--')) / 'snapshots' / pin['revision']
        problems = []
        for name in pin['files']:
            path = snapshot / name
            try:
                size = path.stat().st_size
                if size == 0:
                    raise ValueError('empty')
                if name.endswith('.json'):
                    if size > 64 * 1024 * 1024:
                        raise ValueError('oversized JSON')
                    json.loads(path.read_text())
                elif name.endswith('.safetensors'):
                    with path.open('rb') as handle:
                        length = struct.unpack('<Q', handle.read(8))[0]
                        if length == 0 or length > 64 * 1024 * 1024 or length + 8 >= size:
                            raise ValueError('invalid safetensors header size')
                        header = json.loads(handle.read(length))
                    tensors = [v for k, v in header.items() if k != '__metadata__']
                    if not tensors:
                        raise ValueError('no tensors')
                    for tensor in tensors:
                        start, end = tensor['data_offsets']
                        if not isinstance(start, int) or not isinstance(end, int) or not 0 <= start < end <= size - length - 8:
                            raise ValueError('truncated tensor data')
            except (OSError, ValueError, TypeError, KeyError, AttributeError, struct.error) as error:
                problems.append(name + ': ' + str(error))
        reports[model] = {'revision': pin['revision'], 'snapshot': str(snapshot),
                          'complete': not problems, 'problems': problems}
    return reports


def _norm(name):
    return re.sub(r'[-_.]+', '-', name).lower()


def lock_pins(tier):
    """{normalized distribution: version} from the hash-locked requirements file of a tier, or from its .in file
    (following -r) when an installation without the hash locks has only that (ChatGPT Work text install)."""
    pins = {}
    def read(name):
        for line in (REQUIREMENTS / name).read_text(encoding='utf-8').splitlines():
            included = re.match(r'^-r\s+(\S+)', line)
            if included:
                read(included.group(1))
            match = re.match(r'^([A-Za-z0-9][A-Za-z0-9._-]*)==([^\s\\;]+)', line)
            if match:
                pins[_norm(match.group(1))] = match.group(2)
    read(tier + '.txt' if (REQUIREMENTS / (tier + '.txt')).is_file() else tier + '.in')
    return pins


def lock_conformance(root, tier):
    """'match' when every locked package is installed at its locked version, 'mismatch' if not, 'unknown' unreadable."""
    venv = Path(root) / 'venv'
    sites = [*venv.glob('lib/python*/site-packages'), *venv.glob('Lib/site-packages')]
    if not sites:
        return 'unknown'
    installed = {}
    for site in sites:
        for info in site.glob('*.dist-info'):
            name, _, version = info.name[:-len('.dist-info')].rpartition('-')
            if name:
                key = _norm(name)
                # Two records for one package (a stale one after a failed upgrade) cannot be trusted.
                installed[key] = version if installed.get(key, version) == version else None
    try:
        pins = lock_pins(tier if tier in SIZES else 'full')
    except OSError:
        return 'unknown'
    return 'match' if all(installed.get(name) == version for name, version in pins.items()) else 'mismatch'


def read_engine(root):
    marker = Path(root) / 'engine.json'
    try:
        engine = json.loads(marker.read_text()) if marker.is_file() else {}
    except (OSError, ValueError):
        engine = {}
    return engine if isinstance(engine, dict) else {}


def unlocked(root):
    """A pinned engine that this launcher's locks did not build (an older route, or drifted packages)."""
    engine = read_engine(root)
    if not venv_python(root) or engine.get('commit') != PIN['commit']:
        return False
    return not engine.get('wrapper_version') or lock_conformance(root, engine.get('tier', 'full')) == 'mismatch'


def candidates(chosen):
    """Other runtime roots on this machine, described read-only; never selected."""
    paths = [Path.home() / rel for rel in LEGACY_ROOTS]
    for extra in (os.environ.get('EARSHOT_NATIVE_ROOT'), Path.home() / '.framecore-works' / 'earshot'):
        if extra:
            paths.append(Path(extra))
    found, seen = [], {str(Path(chosen))}
    for path in paths:
        if str(path) in seen or not path.is_dir():
            continue
        seen.add(str(path))
        engine = read_engine(path)
        found.append({'path': str(path), 'engine_commit': engine.get('commit'), 'tier': engine.get('tier'),
                      'wrapper_version': engine.get('wrapper_version'),
                      'models_cached': all(m['complete'] for m in model_cache_status(path).values()),
                      'real_sound_available': (path / 'upstream' / 'skills' / 'real-sound' / 'scripts').is_dir(),
                      'lock_conformance': lock_conformance(path, engine.get('tier', 'full'))})
    return found


def status(root):
    root = Path(root)
    python = venv_python(root)
    engine = read_engine(root)
    light = bool(python) and _python_ok(python, ['earshot', 'numpy', 'scipy', 'soundfile', 'librosa', 'pyloudnorm'])
    full = light and _python_ok(python, ['torch', 'transformers'])
    hub = root / 'cache' / 'hf'
    models = model_cache_status(root)
    cached = all(item['complete'] for item in models.values())
    report = {'root': str(root), 'venv': str(python) if python else None, 'engine_commit': engine.get('commit'),
              'pinned_commit': PIN['commit'], 'wrapper_version': WRAPPER_VERSION,
              'light_ready': light, 'full_ready': full, 'models_cached': cached, 'models': models,
              'model_inference_verified': False, 'real_sound_root': str(root / 'upstream' / 'skills' / 'real-sound'),
              'real_sound_available': (root / 'upstream' / 'skills' / 'real-sound' / 'scripts').is_dir(),
              'ffmpeg': shutil.which('ffmpeg'), 'ffprobe': shutil.which('ffprobe')}
    report['lock_conformance'] = lock_conformance(root, engine.get('tier', 'full')) if python else 'unknown'
    report['state'] = 'ready_full' if full and cached else 'ready_light' if light else 'unavailable'
    if python and engine.get('commit') != PIN['commit']:   # an older route's venv, or an unfinished install
        report['state'] = 'unavailable'
        report['note'] = 'the engine here is not the pinned, completed install of this launcher; reinstall into a new --root with install --yes'
    elif unlocked(root):
        report['state'] = 'unlocked_legacy'
        report['note'] = ('pinned engine without this launcher\'s package locks; runs need --allow-unlocked, or install a '
                          'new root and reuse these models with fetch-models --from')
    report['candidates'] = candidates(root)
    return report


def plan(tier, root):
    return {'action': f'install --tier {tier}', 'root': str(root), 'writes': [str(Path(root) / name) for name in ('venv', 'upstream', 'engine.json')],
            'source': f"{PIN['repository']} at {PIN['commit']} ({PIN['tag']}), every file checked against upstream.json",
            'size': SIZES[tier], 'requirements': str(REQUIREMENTS / (tier + '.txt')),
            'python': 'CPython 3.12; wheel availability is required; full tier uses CPU PyTorch',
            'not_installed': ['mcp and llm extras', 'models (fetch-models)'],
            'confirm': 'run again with --yes after the user agrees'}


def install(tier, root):
    root = Path(root)
    if sys.version_info[:2] != (3, 12):
        raise OSError('the dependency locks target Python 3.12; run setup with python3.12')
    missing = [name for name in ('build.txt', tier + '.txt') if not (REQUIREMENTS / name).is_file()]
    if missing:
        raise OSError('the hash locks ' + ', '.join(missing) + ' are not in this Toolbox installation (a ChatGPT Work text '
                      'install leaves them out); update Toolbox with the complete package first')
    if root.exists() and any(root.iterdir()):
        raise OSError('runtime destination is not empty; preserve it and select a new --root for this version')
    for parent in (root, *root.parents):
        if parent.is_symlink():
            raise OSError('runtime destination must not contain symlinks')
    root.mkdir(parents=True, exist_ok=True)
    # Stage the download inside --root so nothing is written elsewhere, whatever TMPDIR is.
    with tempfile.TemporaryDirectory(prefix='.earshot-src-', dir=root) as tmp:
        src = fetch_source(tmp)
        problems = verify_tree(src, load_manifest()['files'])
        if problems:
            print(PREFIX + 'the downloaded source differs from the pinned upstream; nothing was installed:\n  '
                  + '\n  '.join(problems[:20]), file=sys.stderr)
            return 1
        # Keep upstream resources outside the plugin, before the package build can add files.
        shutil.copytree(src, root / 'upstream', ignore=shutil.ignore_patterns('.git'))
        subprocess.run([sys.executable, '-m', 'venv', str(root / 'venv')], check=True)
        python = str(venv_python(root))
        pip = [python, '-m', 'pip', 'install', '-q', '--disable-pip-version-check', '--no-warn-conflicts']
        locked = ['--require-hashes', '--only-binary=:all:', '--index-url', 'https://pypi.org/simple']
        subprocess.run(pip + locked + ['-r', str(REQUIREMENTS / 'build.txt')], check=True)
        dependencies = pip + locked
        if tier == 'full':
            dependencies += ['--extra-index-url', TORCH_INDEX]
        subprocess.run(dependencies + ['-r', str(REQUIREMENTS / (tier + '.txt'))], check=True)
        subprocess.run(pip + ['--no-deps', '--no-build-isolation', '--no-index', str(src)], check=True)
        disable_remote_modules(engine_package(python))
    (root / 'engine.json').write_text(json.dumps({**PIN, 'tier': tier, 'wrapper_version': WRAPPER_VERSION}, indent=2) + '\n')
    print(json.dumps(status(root), indent=2))
    return 0


REMOTE_MODULES = ('llm.py', 'mcp_server.py')
STUB = ('"""Removed by Toolbox Earshot: this runtime runs Earshot locally only, with no audio upload and no MCP server."""\n'
        'raise ImportError("Toolbox Earshot: the audio-LLM upload and the MCP server are not part of this installation")\n')


def engine_package(python):
    """The installed earshot package folder in the venv, or None."""
    try:
        out = subprocess.run([str(python), '-c', 'import earshot, os; print(os.path.dirname(earshot.__file__))'],
                             capture_output=True, text=True, timeout=120).stdout
        folder = Path(str(out).strip())
        return folder if folder.is_dir() else None
    except (OSError, subprocess.TimeoutExpired, TypeError, ValueError):
        return None


def disable_remote_modules(package):
    """Replace the engine's upload (llm) and server (mcp) modules in the venv with an ImportError stub."""
    if not package:
        raise OSError('the earshot package is not in the venv, so the upload stub could not be applied')
    for name in REMOTE_MODULES:
        (Path(package) / name).write_text(STUB)   # also when absent: an import fails loudly either way


def engine_env(root, offline=True):
    env = {k: v for k, v in os.environ.items() if k not in ('GEMINI_API_KEY', 'GOOGLE_API_KEY')}
    env.update({'HF_HUB_DISABLE_TELEMETRY': '1', 'DO_NOT_TRACK': '1', 'PYTHONDONTWRITEBYTECODE': '1',
                'EARSHOT_CLAP': MODELS[0], 'EARSHOT_AST': MODELS[1],
                'EARSHOT_CLAP_REVISION': MODEL_PINS[MODELS[0]]['revision'],
                'EARSHOT_AST_REVISION': MODEL_PINS[MODELS[1]]['revision']})
    env['EARSHOT_HOME'] = str(Path(root) / 'cache')   # the cache fetch-models fills; keys dropped, nothing to upload with
    if offline:
        env.update(OFFLINE)
    return env


def split_passthrough(argv):
    """(root, command, rest, allow_unlocked) for `run`, `python` and `exec`, whose arguments pass untouched; else None."""
    root, allow, i = None, False, 0
    while i < len(argv):
        if argv[i] == '--root' and i + 1 < len(argv):
            root, i = Path(argv[i + 1]), i + 2
        elif argv[i].startswith('--root='):
            root, i = Path(argv[i].split('=', 1)[1]), i + 1
        elif argv[i] == '--allow-unlocked':
            allow, i = True, i + 1
        else:
            break
    if i < len(argv) and argv[i] in ('run', 'python', 'exec'):
        return root, argv[i], argv[i + 1:], allow
    return None


def check_exec(args):
    """`-m earshot <command>` goes through the allowlist; any other earshot module run directly is refused."""
    if '-m' in args:
        module = args[args.index('-m') + 1] if args.index('-m') + 1 < len(args) else ''
        if module == 'earshot':
            check_command(args[args.index('-m') + 2:])
        elif module.startswith('earshot.'):
            raise Refused(f'`-m {module}` is not available in Toolbox Earshot; use `-m earshot <command>`')


def passthrough(root, command, rest, allow_unlocked=False):
    if unlocked(root):
        if not allow_unlocked:
            print(PREFIX + f'{root} is an unlocked legacy runtime; ask the user, then add --allow-unlocked, or install a new '
                  'root and reuse its models with `fetch-models --from`', file=sys.stderr)
            return 2
        print(PREFIX + f'warning: running the unlocked legacy runtime in {root} (packages differ from the locks)', file=sys.stderr)
    if command == 'exec':
        try:
            check_exec(rest)
        except Refused as error:
            print(PREFIX + str(error), file=sys.stderr)
            return 2
        python = venv_python(root)
        if not python:
            print(PREFIX + 'the engine is not installed here; see `runtime.py install --tier light`', file=sys.stderr)
            return 1
        return subprocess.run([str(python), *rest], env=engine_env(root)).returncode
    if command == 'run':
        try:
            check_command(rest)
        except Refused as error:
            print(PREFIX + str(error), file=sys.stderr)
            return 2
        python = venv_python(root)
        if not python:
            print(PREFIX + 'the engine is not installed here; see `runtime.py install --tier light`', file=sys.stderr)
            return 1
        return subprocess.run([str(python), '-m', 'earshot', *rest], env=engine_env(root)).returncode
    if not rest:
        print(PREFIX + 'name a real-sound script', file=sys.stderr)
        return 2
    try:
        script = real_sound_script(rest[0], root)
        if rest[0] == 'audit.py' and any(x == '--fetch' or x.startswith('--fetch=') or x == '--fetch-all' for x in rest[1:]):
            raise Refused('audit downloads are outside this wrapper; supply local recordings and their source records')
    except Refused as error:
        print(PREFIX + str(error), file=sys.stderr)
        return 2
    python = venv_python(root)
    if not python:
        print(PREFIX + 'the engine is not installed here; see `runtime.py install --tier light`', file=sys.stderr)
        return 1
    return subprocess.run([str(python), '-I', str(script), *rest[1:]], env=engine_env(root)).returncode


def reuse_models(source, root, yes):
    """Place another root's verified pinned model snapshots in this root without a download; the source is only read."""
    targets = {m: Path(r['snapshot']) for m, r in model_cache_status(root).items()}
    if not yes:
        print(json.dumps({'action': 'reuse-models', 'from': str(source), 'into': str(Path(root) / 'cache'),
                          'models': list(MODELS), 'download': False,
                          'method': 'hard links on the same disk, else copies (about 1.1 GB); the source is not changed; '
                                    'linked files share their data with the source root, which Earshot only reads',
                          'confirm': 'run again with --yes after the user agrees'}, indent=2))
        return 0
    found = model_cache_status(source)
    if not all(r['complete'] for r in found.values()):
        print(PREFIX + f'the models in {source} are incomplete or not the pinned revisions; nothing was placed', file=sys.stderr)
        return 2
    if Path(source).resolve() == Path(root).resolve() or any(t.exists() for t in targets.values()):
        print(PREFIX + 'this root already has model snapshots; nothing was placed', file=sys.stderr)
        return 2
    if not venv_python(root) or not status(root).get('full_ready'):
        print(PREFIX + 'models need the full tier: `runtime.py install --tier full --yes` first', file=sys.stderr)
        return 1
    cache = Path(root) / 'cache'
    had_cache = cache.exists()
    try:
        for model, pin in MODEL_PINS.items():
            source_dir, target = Path(found[model]['snapshot']), targets[model]
            target.mkdir(parents=True)
            for name in pin['files']:
                real = (source_dir / name).resolve()   # Hugging Face snapshots link into blobs/
                try:
                    os.link(real, target / name)
                except OSError:
                    shutil.copy2(real, target / name)
        if not all(r['complete'] for r in model_cache_status(root).values()):
            raise OSError('the placed models did not verify')
    except (Exception, KeyboardInterrupt) as error:
        # Remove only what this call made, so a retry starts clean.
        if not had_cache:
            shutil.rmtree(cache, ignore_errors=True)
        else:
            for target in targets.values():
                shutil.rmtree(target, ignore_errors=True)
        print(PREFIX + f'model reuse stopped ({error}); nothing was kept', file=sys.stderr)
        if isinstance(error, KeyboardInterrupt):
            raise
        return 1
    print(json.dumps({'action': 'reuse-models', 'from': str(source), 'into': str(Path(root) / 'cache'), 'placed': list(MODELS)}, indent=2))
    return 0


def attach_source(root, yes):
    """Add the verified pinned upstream source (`upstream/`) to a root that lacks it; nothing else in the root changes."""
    root = Path(root)
    if not yes:
        print(json.dumps({'action': 'attach-source', 'root': str(root), 'writes': [str(root / 'upstream')],
                          'source': f"{PIN['repository']} at {PIN['commit']} ({PIN['tag']}), every file checked against upstream.json",
                          'unchanged': ['venv', 'cache', 'engine.json'], 'confirm': 'run again with --yes after the user agrees'}, indent=2))
        return 0
    if (root / 'upstream').exists():
        print(PREFIX + f'{root / "upstream"} already exists; nothing was changed', file=sys.stderr)
        return 2
    if read_engine(root).get('commit') != PIN['commit']:
        print(PREFIX + 'this root does not hold the pinned engine; nothing was changed', file=sys.stderr)
        return 2
    staging = root / '.upstream.partial'
    try:
        with tempfile.TemporaryDirectory(prefix='earshot-src-') as tmp:
            src = fetch_source(tmp)
            problems = verify_tree(src, load_manifest()['files'])
            if problems:
                print(PREFIX + 'the downloaded source differs from the pinned upstream; nothing was changed:\n  '
                      + '\n  '.join(problems[:20]), file=sys.stderr)
                return 1
            shutil.rmtree(staging, ignore_errors=True)
            shutil.copytree(src, staging, ignore=shutil.ignore_patterns('.git'))
            staging.rename(root / 'upstream')   # appears complete or not at all
    except (Exception, KeyboardInterrupt) as error:
        shutil.rmtree(staging, ignore_errors=True)
        print(PREFIX + f'attach-source stopped ({error}); nothing was kept', file=sys.stderr)
        if isinstance(error, KeyboardInterrupt):
            raise
        return 1
    print(json.dumps({'action': 'attach-source', 'root': str(root), 'added': str(root / 'upstream')}, indent=2))
    return 0


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    split = split_passthrough(argv)
    if split:
        root, command, rest, allow = split
        return passthrough(root or default_root(), command, rest, allow)
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--root', type=Path, default=None, help='runtime folder (default ~/.framecore-works/earshot)')
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('status')
    p.add_argument('--json', action='store_true')
    p.add_argument('--root', type=Path, default=argparse.SUPPRESS)
    p = sub.add_parser('install')
    p.add_argument('--tier', choices=('light', 'full'), required=True)
    p.add_argument('--yes', action='store_true')
    p.add_argument('--root', type=Path, default=argparse.SUPPRESS)
    p = sub.add_parser('fetch-models')
    p.add_argument('--from', dest='source', type=Path, default=None, help='reuse the pinned models of another root')
    p.add_argument('--yes', action='store_true')
    p.add_argument('--root', type=Path, default=argparse.SUPPRESS)
    p = sub.add_parser('attach-source')
    p.add_argument('--yes', action='store_true')
    p.add_argument('--root', type=Path, default=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    root = Path(args.root) if args.root else default_root()

    if args.cmd == 'status':
        report = status(root)
        print(json.dumps(report, indent=2) if args.json else
              f"{report['state']}: light {report['light_ready']}, full {report['full_ready']}, models cached {report['models_cached']}, "
              f"engine {report['engine_commit'] or 'not installed'} (pinned {PIN['commit'][:7]})")
        return 0
    if args.cmd == 'install':
        if not args.yes:
            print(json.dumps(plan(args.tier, root), indent=2))
            return 0
        try:
            return install(args.tier, root)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError) as error:
            what = ' '.join(map(str, error.cmd[-2:])) if isinstance(error, (subprocess.CalledProcessError, subprocess.TimeoutExpired)) else str(error)
            print(PREFIX + f'install stopped at `{what}` (network, proxy or disk); nothing beyond it was installed; '
                  f'see `runtime.py status`', file=sys.stderr)
            return 1
    if args.cmd == 'attach-source':
        return attach_source(root, args.yes)
    if args.cmd == 'fetch-models' and args.source:
        return reuse_models(Path(args.source), root, args.yes)
    if args.cmd == 'fetch-models':
        python = venv_python(root)
        if not args.yes:
            print(json.dumps({'action': 'fetch-models', 'downloads': list(MODELS), 'size': 'about 1.1 GB, pinned revisions',
                              'into': str(root / 'cache'), 'confirm': 'run again with --yes after the user agrees'}, indent=2))
            return 0
        if not python or not status(root).get('full_ready'):
            print(PREFIX + 'models need the full tier: `runtime.py install --tier full --yes` first', file=sys.stderr)
            return 1
        return subprocess.run([str(python), '-m', 'earshot', 'doctor', '--fetch'], env=engine_env(root, offline=False)).returncode
    return 2


if __name__ == '__main__':
    sys.exit(main())
