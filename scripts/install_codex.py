#!/usr/bin/env python3
"""Install one native local-plugin entry backed by the complete bundle; no network."""
import argparse
import json
import re
import shutil
from pathlib import Path
from package_plugins import ROOT, inventory, validate_plugin


def reject_symlinks(path):
    for candidate in (path, *path.parents):
        if candidate.is_symlink():
            raise ValueError('Refusing symlink destination: ' + str(candidate))


def overlaps(a, b):
    return a == b or a in b.parents or b in a.parents


def entry_text(bundle, name='toolbox', skill='toolbox', description='Show the FrameCore Works Toolbox catalog and installation routes.'):
    return ('---\nname: ' + name + '\ndescription: ' + json.dumps(description) + '\n---\n\n'
            '# ' + name + '\n\n'
            f'Read `{bundle / "skills" / skill / "SKILL.md"}` and follow its instructions.\n'
            'Resolve all references from that bundled skill location. Use the actual host\n'
            'and the user\'s language. Installed files do not establish engine readiness.\n')


def run(action, repo, skills, bundle, source_commit, plugin_name="toolbox"):
    if action not in {'plan', 'install', 'verify'}:
        raise ValueError('Unknown action')
    if not re.fullmatch('[0-9a-f]{40}', source_commit):
        raise ValueError('Use a verified full source commit')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', plugin_name):
        raise ValueError('Invalid plugin name')
    repo = Path(repo).resolve()
    for path in (skills, bundle):
        if not path.is_absolute() or any(c in str(path) for c in ('\n', '\r', '`')):
            raise ValueError('Use absolute destination paths without line breaks or backticks')
        reject_symlinks(path)
    skills, bundle = skills.resolve(), bundle.resolve()
    if overlaps(skills, bundle) or overlaps(repo, bundle) or overlaps(repo, skills):
        raise ValueError('Keep destinations separate and outside the source repository')
    target = skills / plugin_name
    reject_symlinks(target)
    source = repo / 'plugins' / plugin_name
    manifest = validate_plugin(source)
    files = inventory(source)
    entrypoints = list((source / 'skills').glob('*/SKILL.md'))
    if len(entrypoints) != 1:
        raise ValueError('Native entry helper requires exactly one declared entry skill')
    entry = entry_text(bundle, plugin_name, entrypoints[0].parent.name, manifest['description'])
    receipt = {'plugin': plugin_name, 'version': manifest['version'],
               'source_commit': source_commit, 'bundle_dir': str(bundle), 'files': files}

    def verify():
        try:
            reject_symlinks(target / 'SKILL.md')
            reject_symlinks(target / 'installation.json')
            if inventory(bundle) != files or (target / 'SKILL.md').read_text() != entry:
                raise ValueError('Installation differs from source; preserve and inspect edits')
            if json.loads((target / 'installation.json').read_text()) != receipt:
                raise ValueError('Installation receipt differs from requested source')
            if {p.name for p in target.iterdir()} != {'SKILL.md', 'installation.json'}:
                raise ValueError('Entry contains additional local content; inspect it')
        except (OSError, json.JSONDecodeError) as error:
            raise ValueError('Partial or unreadable installation; inspect before recovery') from error

    result = {'status': 'FILES_VERIFIED', 'version': manifest['version'],
              'files': len(files), 'host_activation': 'NOT_RUN'}
    if action == 'verify':
        verify()
        return result
    if target.exists() or bundle.exists():
        verify()
        return {**result, 'status': 'already_up_to_date', 'writes': 0}
    if action == 'plan':
        return {**result, 'status': 'READY', 'writes': 0,
                'entry': str(target), 'bundle': str(bundle)}
    # Exclusive creation: no overwrite or cleanup of existing user content.
    # A failure leaves observable partial state for inspection, never a success receipt.
    skills.mkdir(parents=True, exist_ok=True)
    bundle.parent.mkdir(parents=True, exist_ok=True)
    bundle.mkdir(exist_ok=False)
    for relative in files:
        destination = bundle / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / relative, destination)
    target.mkdir(exist_ok=False)
    (target / 'SKILL.md').write_text(entry, encoding='utf-8')
    (target / 'installation.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    verify()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['plan', 'install', 'verify'])
    parser.add_argument('--plugin', default='toolbox')
    parser.add_argument('--skills-dir', type=Path, required=True)
    parser.add_argument('--bundle-dir', type=Path, required=True)
    parser.add_argument('--source-commit', required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.action, ROOT, args.skills_dir, args.bundle_dir,
                         args.source_commit, args.plugin), indent=2))


if __name__ == '__main__':
    main()
