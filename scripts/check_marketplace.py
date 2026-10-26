#!/usr/bin/env python3
"""Check the toolbox marketplace against the repo rules in CLAUDE.md.

Checks:
- .claude-plugin/marketplace.json parses and has name, owner and plugins;
- every entry uses a github, url or git-subdir source pinned to a full
  40-character commit SHA (never a branch alone), or, for adapted entries
  (review "Kind: adapted"), the local wrapper ./plugins/<name> with
  .claude-plugin/plugin.json, no bin/, and UPSTREAM.md naming the reviewed
  commit;
- every entry has reviews/<name>.md (Status: active, Eligibility filled in,
  Commit: <same SHA>) and docs/<name>.md mentioning the same SHA;
- reviews marked "Status: removed" are not listed in the manifest;
- no ZIP files are kept in the repo.

Usage: python3 scripts/check_marketplace.py [repo_root]
Exit code 0 when clean, 1 when any check fails.
"""

import json
import re
import sys
from pathlib import Path

MANIFEST = ".claude-plugin/marketplace.json"
GIT_SOURCES = {"github", "url", "git-subdir"}
FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
FIELD = re.compile(r"^- ([A-Za-z-]+): *(.*)$", re.MULTILINE)


def load_json(path, errors):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{path.name}: file missing ({path})")
    except json.JSONDecodeError as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
    return None


def review_fields(path):
    """Return the "- Key: value" fields of a review, or None if it is missing."""
    if not path.is_file():
        return None
    return {k: v.strip() for k, v in FIELD.findall(path.read_text(encoding="utf-8"))}


def entries_by_name(plugins, errors):
    by_name = {}
    for i, entry in enumerate(plugins):
        name = entry.get("name") if isinstance(entry, dict) else None
        if not name:
            errors.append(f"plugins[{i}]: missing name")
            continue
        if name in by_name:
            errors.append(f"Duplicate entry name '{name}'")
        by_name[name] = entry
    return by_name


def pinned_sha(source):
    if isinstance(source, dict) and source.get("source") in GIT_SOURCES:
        sha = source.get("sha", "")
        return sha if FULL_SHA.match(sha) else None
    return None


def check_wrapper(root, name, path, sha, fields, errors):
    expected = f"./plugins/{name}"
    if path.rstrip("/") != expected:
        errors.append(f"'{name}': a local source must be {expected}")
        return
    if fields is not None and fields.get("Kind") != "adapted":
        errors.append(f"'{name}': a local wrapper source needs 'Kind: adapted' in the review")
    plugin = root / expected
    if not (plugin / ".claude-plugin/plugin.json").is_file():
        errors.append(f"'{name}': {expected}/.claude-plugin/plugin.json is missing")
    if (plugin / "bin").exists():
        errors.append(f"'{name}': {expected}/bin is not allowed (claude.ai and Cowork refuse it)")
    upstream = plugin / "UPSTREAM.md"
    if not upstream.is_file() or (sha and sha not in upstream.read_text(encoding="utf-8")):
        errors.append(f"'{name}': {expected}/UPSTREAM.md must name the reviewed upstream commit")


def check(root):
    root = Path(root)
    errors = []
    manifest = load_json(root / MANIFEST, errors)
    if manifest is None:
        return errors

    for key in ("name", "owner", "plugins"):
        if key not in manifest:
            errors.append(f"{MANIFEST}: missing '{key}'")

    for name, entry in entries_by_name(manifest.get("plugins", []), errors).items():
        source = entry.get("source")
        fields = review_fields(root / "reviews" / f"{name}.md")
        if isinstance(source, str):
            # Adapted entry: our own wrapper in plugins/<name>, pinned to the reviewed upstream commit.
            sha = fields.get("Commit") if fields and FULL_SHA.match(fields.get("Commit", "")) else None
            check_wrapper(root, name, source, sha, fields, errors)
        else:
            sha = pinned_sha(source)
            if not isinstance(source, dict) or source.get("source") not in GIT_SOURCES:
                errors.append(f"'{name}': source must be github, url or git-subdir")
            if sha is None:
                errors.append(f"'{name}': source needs a full 40-character lowercase 'sha'")

        if fields is None:
            errors.append(f"'{name}': reviews/{name}.md is missing")
            continue
        if fields.get("Status") == "removed":
            errors.append(f"'{name}': review is marked removed but the entry is still listed")
        elif fields.get("Status") != "active":
            errors.append(f"'{name}': review Status must be 'active'")
        if not fields.get("Eligibility") or fields["Eligibility"].startswith("<"):
            errors.append(f"'{name}': review needs an Eligibility line (upstream manifest or documented skills)")
        if sha is None and isinstance(source, str):
            errors.append(f"'{name}': review Commit must be the full 40-character upstream commit")
        elif sha and fields.get("Commit") != sha:
            errors.append(f"'{name}': review Commit does not match the pinned sha {sha}")

        docs = root / "docs" / f"{name}.md"
        if not docs.is_file():
            errors.append(f"'{name}': docs/{name}.md is missing")
        elif sha and sha not in docs.read_text(encoding="utf-8"):
            errors.append(f"'{name}': docs/{name}.md does not mention the pinned sha")

    for zip_path in root.rglob("*.zip"):
        rel = zip_path.relative_to(root)
        if rel.parts[0] != ".git":
            errors.append(f"{rel}: ZIP files must not be committed")

    return errors


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    errors = check(root)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    with open(root / MANIFEST, encoding="utf-8") as f:
        count = len(json.load(f)["plugins"])
    print(f"OK: {count} entries, marketplace consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
