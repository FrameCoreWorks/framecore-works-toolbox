#!/usr/bin/env python3
"""Validate and package one portable local plugin. Standard library; no network."""
import argparse
import hashlib
import json
import re
import stat
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
EXCLUDED = {'.git', '__pycache__', '.venv', 'node_modules'}


def inventory(directory):
    files = {}
    if directory.is_symlink():
        raise ValueError('Refusing symlink plugin directory')
    for path in sorted(directory.rglob('*')):
        relative = path.relative_to(directory)
        if path.is_symlink():
            raise ValueError('Refusing symlink: ' + str(relative))
        if EXCLUDED.intersection(relative.parts):
            continue
        if path.is_dir():
            continue
        if not path.is_file():
            raise ValueError('Refusing non-regular file: ' + str(relative))
        if path.name == '.env' or path.name.startswith('.env.'):
            raise ValueError('Refusing environment file: ' + str(relative))
        if path.suffix in {'.pyc', '.zip'} or path.name == 'marketplace.json':
            raise ValueError('Unexpected package member: ' + str(relative))
        files[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return files


def read_json(path):
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as error:
        raise ValueError('Unreadable manifest: ' + str(path)) from error
    if not isinstance(data, dict):
        raise ValueError('Expected manifest object: ' + str(path))
    return data


def validate_plugin(plugin):
    manifest = read_json(plugin / 'plugin.json')
    name, version = manifest.get('name'), manifest.get('version', '')
    if name != plugin.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name or ''):
        raise ValueError('Plugin name must match its directory')
    if not re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', version):
        raise ValueError('Use a stable semantic version')
    if manifest.get('$schema') != SCHEMA:
        raise ValueError('Missing portable schema declaration')
    if {'interface', 'skills', 'mcpServers', 'apps'}.intersection(manifest):
        raise ValueError('Legacy fields at portable manifest root')
    interface = manifest.get('extensions', {}).get('com.openai', {}).get('interface', {})
    for key in ('displayName', 'shortDescription', 'longDescription', 'developerName', 'category'):
        if not isinstance(interface.get(key), str) or not interface[key].strip():
            raise ValueError('Missing presentation field: ' + key)
    if len(interface['shortDescription']) > 30:
        raise ValueError('Listing subtitle exceeds 30 characters')
    if not isinstance(interface.get('capabilities'), list):
        raise ValueError('Capabilities must be a list')
    for relative in ('.claude-plugin/plugin.json', '.codex-plugin/plugin.json'):
        overlay = read_json(plugin / relative)
        for key in ('name', 'version', 'description', 'author'):
            if overlay.get(key) != manifest.get(key):
                raise ValueError(relative + ': inconsistent ' + key)
        if relative.startswith('.codex') and overlay.get('interface') != interface:
            raise ValueError('Codex presentation differs from portable manifest')
    skills = sorted((plugin / 'skills').glob('*/SKILL.md'))
    if not skills:
        raise ValueError('Expected at least one portable skill')
    for skill in skills:
        text = skill.read_text(encoding='utf-8')
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            raise ValueError('Missing skill frontmatter: ' + str(skill))
        front = text.split('---\n', 2)[1]
        if not re.search(r'^name: ' + re.escape(skill.parent.name) + r'\s*$', front, re.M):
            raise ValueError('Skill name differs from directory')
        if not re.search(r'^description:\s*\S', front, re.M):
            raise ValueError('Skill description missing')
    if (plugin / 'bin').exists():
        raise ValueError('Top-level bin/ is not portable to Claude apps')
    inventory(plugin)
    return manifest


def build(repo, name, output):
    repo, output = Path(repo).resolve(), Path(output).resolve()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
        raise ValueError('Invalid local plugin name')
    if output == repo or repo in output.parents:
        raise ValueError('Write archives outside the repository')
    plugin = repo / 'plugins' / name
    manifest = validate_plugin(plugin)
    files = inventory(plugin)
    output.mkdir(parents=True, exist_ok=True)
    archive = output / (name + '-' + manifest['version'] + '.zip')
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipped:
        for relative in files:
            info = zipfile.ZipInfo(relative, date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            zipped.writestr(info, (plugin / relative).read_bytes(),
                           compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    with zipfile.ZipFile(archive) as zipped:
        actual = {name: hashlib.sha256(zipped.read(name)).hexdigest() for name in zipped.namelist()}
    if actual != files:
        raise ValueError('Archive differs from source inventory')
    receipt = {'plugin': name, 'version': manifest['version'], 'files': files,
               'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}
    archive.with_suffix('.zip.inventory.json').write_text(json.dumps(receipt, indent=2) + '\n')
    return archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugin', default='toolbox')
    parser.add_argument('--output-dir', type=Path)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.plugin):
        parser.error('Invalid plugin name')
    if args.check:
        manifest = validate_plugin(ROOT / 'plugins' / args.plugin)
        print('OK: portable package', manifest['name'], manifest['version'])
    elif args.output_dir is None:
        parser.error('--output-dir is required when building')
    else:
        print(build(ROOT, args.plugin, args.output_dir))


if __name__ == '__main__':
    main()
