"""Earshot as a built-in Toolbox capability: identity, legacy roots, model reuse and source attachment. No network."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import struct
import tempfile
import unittest
from unittest import mock

TOOLBOX = Path(__file__).resolve().parents[2] / 'plugins' / 'toolbox'
CAPABILITY = TOOLBOX / 'capabilities' / 'earshot'
spec = importlib.util.spec_from_file_location('toolbox_earshot_runtime', CAPABILITY / 'scripts/runtime.py')
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)


def quiet(fn, *args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = fn(*args)
    return code, out.getvalue(), err.getvalue()


def write_models(root):
    header = json.dumps({'t': {'dtype': 'F32', 'shape': [1], 'data_offsets': [0, 4]}}).encode()
    tensor = struct.pack('<Q', len(header)) + header + b'\x00' * 4
    for model, pin in runtime.MODEL_PINS.items():
        folder = Path(root) / 'cache/hf' / ('models--' + model.replace('/', '--')) / 'snapshots' / pin['revision']
        folder.mkdir(parents=True)
        for name in pin['files']:
            (folder / name).write_bytes(tensor if name.endswith('.safetensors') else b'{}' if name.endswith('.json') else b't')


def legacy_root(root, wrapper_version=None, packages=None):
    """A runtime made by an older route: pinned engine commit, venv, maybe no wrapper version or lock."""
    root = Path(root)
    (root / 'venv/bin').mkdir(parents=True)
    (root / 'venv/bin/python').write_text('')
    engine = {**runtime.PIN, 'tier': 'full'}
    if wrapper_version:
        engine['wrapper_version'] = wrapper_version
    (root / 'engine.json').write_text(json.dumps(engine))
    site = root / 'venv/lib/python3.12/site-packages'
    site.mkdir(parents=True)
    for name, version in (packages or {}).items():
        (site / f'{name}-{version}.dist-info').mkdir()
    return root


class Identity(unittest.TestCase):
    def test_wrapper_version_is_the_toolbox_version(self):
        manifest = json.loads((TOOLBOX / 'plugin.json').read_text())
        self.assertEqual(runtime.WRAPPER_VERSION, manifest['version'])

    def test_messages_name_the_toolbox_capability(self):
        with mock.patch.object(runtime.subprocess, 'run'):
            _, _, err = quiet(runtime.main, ['run', 'llm', 'x.wav'])
        self.assertTrue(err.startswith('toolbox/earshot: '), err)
        self.assertNotIn('earshot-audio', runtime.STUB)

    def test_launcher_paths_resolve_inside_the_toolbox_package(self):
        self.assertEqual(runtime.PLUGIN, CAPABILITY)
        self.assertEqual(runtime.TOOLBOX, TOOLBOX)
        self.assertTrue((runtime.REQUIREMENTS / 'full.txt').is_file())


class LegacyRoots(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_lock_conformance_compares_installed_versions_with_the_tier_lock(self):
        pins = runtime.lock_pins('full')
        self.assertEqual(runtime.lock_pins('full', 'linux')['torch'], '2.6.0+cpu')
        good = legacy_root(self.base / 'good', '1.2.0', {n: v for n, v in pins.items()})
        drift = legacy_root(self.base / 'drift', '1.2.0', {**pins, 'torch': '2.14.1'})
        self.assertEqual(runtime.lock_conformance(good, 'full'), 'match')
        self.assertEqual(runtime.lock_conformance(drift, 'full'), 'mismatch')
        self.assertEqual(runtime.lock_conformance(self.base / 'absent', 'full'), 'unknown')

    def test_pinned_engine_without_wrapper_lock_is_unlocked_legacy_not_ready(self):
        root = legacy_root(self.base / 'old', None, {'torch': '2.14.1', 'transformers': '5.20.2'})
        write_models(root)
        with mock.patch.object(runtime, '_python_ok', return_value=True):
            report = runtime.status(root)
        self.assertEqual(report['state'], 'unlocked_legacy')
        self.assertEqual(report['lock_conformance'], 'mismatch')
        self.assertTrue(report['models_cached'])
        self.assertFalse(report['real_sound_available'])

    def test_runs_on_an_unlocked_root_need_explicit_consent(self):
        root = legacy_root(self.base / 'old', None, {'torch': '2.14.1'})
        with mock.patch.object(runtime.subprocess, 'run') as started:
            code, _, err = quiet(runtime.main, ['--root', str(root), 'run', 'measure', 'x.wav'])
        self.assertEqual(code, 2)
        self.assertIn('--allow-unlocked', err)
        started.assert_not_called()
        with mock.patch.object(runtime.subprocess, 'run', return_value=mock.Mock(returncode=0)) as started:
            code, _, _ = quiet(runtime.main, ['--root', str(root), '--allow-unlocked', 'run', 'measure', 'x.wav'])
        self.assertEqual(code, 0)
        started.assert_called_once()

    def test_status_lists_candidates_but_never_selects_them(self):
        home = self.base / 'home'
        legacy = legacy_root(home / '.framecore-studio/extensions/earshot', None)
        chosen = self.base / 'chosen'
        with mock.patch.object(runtime.Path, 'home', return_value=home), \
                mock.patch.dict(runtime.os.environ, {}, clear=False), \
                mock.patch.object(runtime, '_python_ok', return_value=False):
            runtime.os.environ.pop('EARSHOT_NATIVE_ROOT', None)
            report = runtime.status(chosen)
        self.assertEqual(report['root'], str(chosen))
        paths = [c['path'] for c in report['candidates']]
        self.assertIn(str(legacy), paths)
        self.assertNotIn(str(chosen), paths)
        self.assertFalse(chosen.exists())


class ModelReuse(unittest.TestCase):
    def test_models_from_another_root_are_linked_after_consent_and_the_source_is_untouched(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp) / 'old', legacy_root(Path(tmp) / 'new', '1.1.0')
            write_models(source)
            before = {p: p.read_bytes() for p in source.rglob('*') if p.is_file()}
            code, out, _ = quiet(runtime.main, ['--root', str(target), 'fetch-models', '--from', str(source)])
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(out)['action'], 'reuse-models')
            self.assertFalse((target / 'cache').exists())
            with mock.patch.object(runtime.subprocess, 'run') as started, \
                    mock.patch.object(runtime, 'status', return_value={'full_ready': True}):
                code, _, _ = quiet(runtime.main, ['--root', str(target), 'fetch-models', '--from', str(source), '--yes'])
            self.assertEqual(code, 0)
            started.assert_not_called()
            self.assertTrue(all(r['complete'] for r in runtime.model_cache_status(target).values()))
            self.assertEqual({p: p.read_bytes() for p in source.rglob('*') if p.is_file()}, before)

    def test_incomplete_source_models_are_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp) / 'old', legacy_root(Path(tmp) / 'new', '1.1.0')
            (source / 'cache/hf').mkdir(parents=True)
            with mock.patch.object(runtime, 'status', return_value={'full_ready': True}):
                code, _, err = quiet(runtime.main, ['--root', str(target), 'fetch-models', '--from', str(source), '--yes'])
            self.assertEqual(code, 2)
            self.assertIn('incomplete', err)
            self.assertFalse((target / 'cache').exists())


class AttachSource(unittest.TestCase):
    def test_attach_source_adds_only_a_verified_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = legacy_root(Path(tmp) / 'old', None)
            keep = {p: p.read_bytes() for p in root.rglob('*') if p.is_file()}
            fixture = Path(tmp) / 'src'
            (fixture / 'skills/real-sound/scripts').mkdir(parents=True)
            (fixture / 'skills/real-sound/scripts/qa.py').write_text('# fixture\n')
            files = {'skills/real-sound/scripts/qa.py': hashlib.sha256(b'# fixture\n').hexdigest()}
            code, out, _ = quiet(runtime.main, ['--root', str(root), 'attach-source'])
            self.assertEqual((code, json.loads(out)['action']), (0, 'attach-source'))
            self.assertFalse((root / 'upstream').exists())
            with mock.patch.object(runtime, 'fetch_source', return_value=fixture), \
                    mock.patch.object(runtime, 'load_manifest', return_value={'files': files}):
                code, _, _ = quiet(runtime.main, ['--root', str(root), 'attach-source', '--yes'])
            self.assertEqual(code, 0)
            self.assertTrue((root / 'upstream/skills/real-sound/scripts/qa.py').is_file())
            self.assertEqual({p: p.read_bytes() for p in keep}, keep)

    def test_attach_source_refuses_an_existing_snapshot_and_a_tampered_download(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = legacy_root(Path(tmp) / 'old', None)
            fixture = Path(tmp) / 'src'; fixture.mkdir(); (fixture / 'x.py').write_text('changed')
            with mock.patch.object(runtime, 'fetch_source', return_value=fixture), \
                    mock.patch.object(runtime, 'load_manifest', return_value={'files': {'x.py': '0' * 64}}):
                code, _, _ = quiet(runtime.main, ['--root', str(root), 'attach-source', '--yes'])
            self.assertEqual(code, 1)
            self.assertFalse((root / 'upstream').exists())
            (root / 'upstream').mkdir()
            code, _, err = quiet(runtime.main, ['--root', str(root), 'attach-source', '--yes'])
            self.assertEqual(code, 2)
            self.assertIn('already', err)


class SourceRecordGuard(unittest.TestCase):
    def test_import_outputs_are_refused_anywhere_inside_the_toolbox_plugin(self):
        import sys
        sys.path.insert(0, str(CAPABILITY / 'scripts'))
        import import_source_record as bridge
        inside = TOOLBOX / 'skills' / 'toolbox' / 'not-a-project-file.json'
        argv = ['import_source_record.py', '--sidecar', 'x.asset.json', '--root', '.', '--need', 'click', '--out', str(inside)]
        with mock.patch.object(sys, 'argv', argv), mock.patch.object(bridge, 'prepare') as prepared:
            code, out, _ = quiet(bridge.main)
        self.assertEqual(code, 2)
        self.assertIn('outside the plugin', json.loads(out)['error'])
        prepared.assert_not_called()
        self.assertFalse(inside.exists())


class ReviewFixes(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_failed_model_reuse_leaves_nothing_and_can_be_retried(self):
        source, target = self.base / 'old', legacy_root(self.base / 'new', '1.1.0')
        write_models(source)
        with mock.patch.object(runtime, 'status', return_value={'full_ready': True}), \
                mock.patch.object(runtime.os, 'link', side_effect=OSError('cross-device')), \
                mock.patch.object(runtime.shutil, 'copy2', side_effect=OSError('disk full')):
            code, _, err = quiet(runtime.main, ['--root', str(target), 'fetch-models', '--from', str(source), '--yes'])
        self.assertEqual(code, 1)
        self.assertIn('disk full', err)
        self.assertFalse((target / 'cache').exists())
        with mock.patch.object(runtime, 'status', return_value={'full_ready': True}):
            code, _, _ = quiet(runtime.main, ['--root', str(target), 'fetch-models', '--from', str(source), '--yes'])
        self.assertEqual(code, 0)

    def test_interrupted_attach_source_leaves_no_partial_snapshot(self):
        root = legacy_root(self.base / 'old', None)
        with mock.patch.object(runtime, 'fetch_source', side_effect=RuntimeError('bad archive')):
            code, _, err = quiet(runtime.main, ['--root', str(root), 'attach-source', '--yes'])
        self.assertEqual(code, 1)
        self.assertFalse((root / 'upstream').exists())
        self.assertEqual([p.name for p in root.iterdir() if p.name.startswith('.upstream')], [])

    def test_duplicate_dist_info_versions_are_a_mismatch(self):
        pins = runtime.lock_pins('full')
        root = legacy_root(self.base / 'dup', '1.1.0', pins)
        site = next(root.glob('venv/lib/python*/site-packages'))
        (site / 'torch-2.14.1.dist-info').mkdir()
        self.assertEqual(runtime.lock_conformance(root, 'full'), 'mismatch')


if __name__ == '__main__':
    unittest.main()
