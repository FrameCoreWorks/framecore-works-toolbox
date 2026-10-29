#!/usr/bin/env python3
"""Run one Toolbox Earshot operation and write its framecore-task-result/1 envelope.

    python3 envelope.py --result-out result.json [--task-id ID] [--requester PLUGIN] [--owner NAME]
                        [--input FILE ...] [--output FILE ...] -- <runtime.py arguments>

The launcher runs unchanged and its own output passes through. The envelope records the operation, the readiness of
the runtime root, the exit code, SHA-256 of the declared inputs and outputs, warnings and what did not run, and is
validated against the shared schema before it is written to a new file. `exec` (arbitrary venv Python) is a
user-invoked operation, not a task operation, and is refused here. Standard library only; no network of its own.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

import contract
import runtime

STUDIO = 'framecore-work-creative-studio'
OPERATIONS = ('status', 'plan_install', 'install', 'plan_fetch_models', 'fetch_models', 'plan_reuse_models',
              'reuse_models', 'plan_attach_source', 'attach_source', 'run', 'real_sound_script')
RESULT = 'framecore-task-result/1'


def launch(argv):
    """(exit code, stdout, stderr) of the launcher run as its own process."""
    done = subprocess.run([sys.executable, str(Path(runtime.__file__).resolve()), *argv], capture_output=True, text=True)
    return done.returncode, done.stdout, done.stderr


def operation(argv):
    """(operation, run command, runtime root) named by launcher arguments, global options first."""
    root, i = None, 0
    while i < len(argv) and argv[i].startswith('--'):
        if argv[i] == '--root' and i + 1 < len(argv):
            root, i = Path(argv[i + 1]), i + 2
        else:
            if argv[i].startswith('--root='):
                root = Path(argv[i].split('=', 1)[1])
            i += 1
    name, rest = (argv[i], argv[i + 1:]) if i < len(argv) else (None, [])
    for j, arg in enumerate(rest):
        if arg == '--root' and j + 1 < len(rest):
            root = Path(rest[j + 1])
        elif arg.startswith('--root='):
            root = Path(arg.split('=', 1)[1])
    yes = '--yes' in rest
    reuse = any(a == '--from' or a.startswith('--from=') for a in rest)
    op = {'status': 'status', 'attach-source': 'attach_source' if yes else 'plan_attach_source',
          'install': 'install' if yes else 'plan_install', 'run': 'run', 'python': 'real_sound_script',
          'exec': 'exec'}.get(name)
    if name == 'fetch-models':
        op = ('reuse_models' if reuse else 'fetch_models') if yes else ('plan_reuse_models' if reuse else 'plan_fetch_models')
    command = runtime.real_command(rest) if name == 'run' else rest[0] if name == 'python' and rest else None
    return op, command, root or runtime.default_root()


def file_record(path, **extra):
    data = Path(path).read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data), **extra}


def build(args, argv, code, stdout, stderr, inputs, started, duration):
    op, command, root = operation(argv)
    observed = datetime.now(timezone.utc).isoformat(timespec='seconds')
    try:
        readiness = runtime.status(root)
    except OSError:
        readiness = {'state': 'unavailable'}
    try:
        parsed = json.loads(stdout) if stdout.strip() else None
    except ValueError:
        parsed = None
    warnings, errors, unexecuted, outputs = [], [], [], []
    if readiness.get('state') == 'unlocked_legacy':
        warnings.append('ran on an unlocked legacy runtime: installed packages differ from the Toolbox locks')
    if readiness.get('lock_conformance') == 'mismatch':
        warnings.append('lock_conformance: mismatch')
    for path in args.output:
        if Path(path).is_file():
            outputs.append(file_record(path, media_kind='audio' if Path(path).suffix.lower() in ('.wav', '.flac') else None))
        else:
            errors.append({'code': 'output_missing', 'message': f'declared output {path} was not produced',
                           'next_action': 'read the launcher error and status'})
    if code == 0 and isinstance(parsed, dict) and 'confirm' in parsed:
        status = 'needs_consent'
        unexecuted.append({'check': op or 'operation', 'reason': 'plan only; the user has not agreed to --yes'})
    elif code == 0:
        status = 'partial' if errors else 'succeeded'
    elif code == 2 and stderr.startswith('toolbox/earshot: '):   # the launcher's own refusal
        status = 'refused'
    else:
        status = 'failed'
    if code != 0:
        errors.append({'code': f'exit_{code}', 'message': 'the launcher stopped; see its stderr', 'next_action': None})
    unexecuted.append({'check': 'listening_review', 'reason': 'model readings are evidence, not a human listening test'})
    requester = {'plugin': args.requester} if args.requester else None
    origin = 'studio' if args.requester == STUDIO and args.task_id else 'standalone' if not args.requester else 'other'
    return {
        'contract': RESULT, 'task_id': args.task_id, 'origin': origin, 'requester': requester, 'owner': args.owner,
        'provider': {'plugin': 'toolbox', 'version': runtime.WRAPPER_VERSION, 'capability': 'earshot',
                     'operation': op, 'command': command},
        'status': status, 'host': None, 'model': None,
        'inputs': inputs,
        'outputs': outputs,
        'readiness': {'state': readiness.get('state', 'unavailable'), 'command': 'runtime.py status --json',
                      'observed_at': observed, 'details': {'root': str(root),
                                                          'lock_conformance': readiness.get('lock_conformance')}},
        'commands_run': [{'argv': ['runtime.py', *argv], 'exit_code': code, 'started': started,
                          'duration_s': round(duration, 3)}],
        'verification_evidence': [{'check': 'output_sha256', 'result': 'pass' if outputs and not errors else 'not_run',
                                   'scope': 'declared outputs hashed after the run', 'detail': None}],
        'warnings': warnings, 'errors': errors, 'unexecuted_checks': unexecuted,
        'audio': {'engine': f"earshot {runtime.PIN['tag']} at {runtime.PIN['commit']}", 'stdout_json': parsed},
    }


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if '--' not in argv:
        print('toolbox/earshot: put the launcher arguments after --', file=sys.stderr)
        return 2
    split = argv.index('--')
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--result-out', required=True, type=Path)
    parser.add_argument('--task-id')
    parser.add_argument('--requester')
    parser.add_argument('--owner')
    parser.add_argument('--input', action='append', default=[], type=Path)
    parser.add_argument('--output', action='append', default=[], type=Path)
    args = parser.parse_args(argv[:split])
    launcher = argv[split + 1:]
    op, _, _ = operation(launcher)
    if op not in OPERATIONS:
        print('toolbox/earshot: name a task operation (exec stays a user-invoked command)', file=sys.stderr)
        return 2
    declared = {p.resolve() for p in (*args.input, *args.output)}
    if args.result_out.exists() or args.result_out.is_symlink() or args.result_out.resolve() in declared:
        print(f'toolbox/earshot: {args.result_out} exists or is an input or output; choose a new result file', file=sys.stderr)
        return 2
    try:
        inputs = [file_record(p) for p in args.input]   # before anything runs
    except OSError as error:
        print(f'toolbox/earshot: input unreadable ({error}); nothing was run', file=sys.stderr)
        return 2
    started = datetime.now(timezone.utc).isoformat(timespec='seconds')
    clock = time.monotonic()
    code, stdout, stderr = launch(launcher)
    sys.stdout.write(stdout)
    sys.stderr.write(stderr)
    document = build(args, launcher, code, stdout, stderr, inputs, started, time.monotonic() - clock)
    problems = contract.validate(document, 'result')
    if problems:
        print('toolbox/earshot: envelope not written: ' + '; '.join(problems[:5]), file=sys.stderr)
        return 2
    text = json.dumps(document, indent=2) + '\n'
    try:
        args.result_out.parent.mkdir(parents=True, exist_ok=True)
        with args.result_out.open('x', encoding='utf-8') as handle:
            handle.write(text)
    except OSError as error:
        print(f'toolbox/earshot: result file not written ({error}); the envelope follows:\n' + text, file=sys.stderr)
        return 2
    return code


if __name__ == '__main__':
    sys.exit(main())
