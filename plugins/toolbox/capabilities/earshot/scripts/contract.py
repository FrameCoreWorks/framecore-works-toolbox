"""FrameCore task contract 1 for Toolbox: a small offline validator for the shared schema.

The schema file (the Toolbox plugin's contracts/framecore-task.schema.json) is byte-identical across Creative Studio,
Toolbox and Open Assets; no code is shared. Only the JSON Schema keywords that schema uses are implemented.
"""
import json
from pathlib import Path
import re

SCHEMA_PATH = Path(__file__).resolve().parents[3] / 'contracts' / 'framecore-task.schema.json'
TYPES = {'object': dict, 'array': list, 'string': str, 'boolean': bool, 'null': type(None)}


def schema():
    return json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))


def _is(value, name):
    if name == 'integer':
        return isinstance(value, int) and not isinstance(value, bool)
    if name == 'number':
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return isinstance(value, TYPES[name])


def _check(value, rule, root, path, errors):
    if '$ref' in rule:
        rule = root['$defs'][rule['$ref'].rsplit('/', 1)[-1]]
    if 'anyOf' in rule:
        if not any(not _errors(value, r, root, path) for r in rule['anyOf']):
            errors.append(f'{path}: matches no allowed shape')
        return
    if 'const' in rule and value != rule['const']:
        errors.append(f'{path}: expected {rule["const"]!r}')
    if 'enum' in rule and value not in rule['enum']:
        errors.append(f'{path}: {value!r} not in {rule["enum"]}')
    if 'type' in rule:
        names = rule['type'] if isinstance(rule['type'], list) else [rule['type']]
        if not any(_is(value, n) for n in names):
            errors.append(f'{path}: expected {"/".join(names)}')
            return
    if isinstance(value, str):
        if len(value) < rule.get('minLength', 0):
            errors.append(f'{path}: too short')
        if 'pattern' in rule and not re.search(rule['pattern'], value):
            errors.append(f'{path}: does not match {rule["pattern"]}')
    if _is(value, 'number') and 'minimum' in rule and value < rule['minimum']:
        errors.append(f'{path}: below {rule["minimum"]}')
    if isinstance(value, dict):
        for key in rule.get('required', []):
            if key not in value:
                errors.append(f'{path}: missing {key}')
        for key, sub in rule.get('properties', {}).items():
            if key in value:
                _check(value[key], sub, root, f'{path}.{key}', errors)
    if isinstance(value, list) and 'items' in rule:
        for i, item in enumerate(value):
            _check(item, rule['items'], root, f'{path}[{i}]', errors)


def _errors(value, rule, root, path):
    errors = []
    _check(value, rule, root, path, errors)
    return errors


def validate(document, kind):
    """Problems with `document` as a `kind` (request, result or capabilities); empty means it conforms."""
    root = schema()
    return _errors(document, root['$defs'][kind], root, kind)
