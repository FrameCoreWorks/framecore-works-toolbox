#!/usr/bin/env python3
"""Check the toolbox manifests against the repo rules in CLAUDE.md / AGENTS.md.

Checks:
- both manifests parse and share the same marketplace name;
- every Claude Code entry uses a github, url or git-subdir source pinned to a
  full 40-character commit SHA (never a branch alone, never a local path);
- every entry has reviews/<name>.md (Status: active, Eligibility filled in,
  Commit: <same SHA>) and
  docs/<name>.md mentioning the same SHA;
- the Codex manifest lists the same entries, pinned to the same SHA, with
  policy and category, unless the review records "Codex-Pin: limitation: ...";
- reviews marked "Status: removed" are not listed in any manifest;
- CLAUDE.md and AGENTS.md are identical;
- no ZIP files are kept in the repo outside the ignored dist/ folder.

Usage: python3 scripts/check_marketplace.py [repo_root]
Exit code 0 when clean, 1 when any check fails.
"""

import json
import re
import sys
from pathlib import Path

CLAUDE_MANIFEST = ".claude-plugin/marketplace.json"
CODEX_MANIFEST = ".agents/plugins/marketplace.json"
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


def entries_by_name(plugins, label, errors):
    by_name = {}
    for i, entry in enumerate(plugins):
        name = entry.get("name") if isinstance(entry, dict) else None
        if not name:
            errors.append(f"{label} plugins[{i}]: missing name")
            continue
        if name in by_name:
            errors.append(f"{label}: Duplicate entry name '{name}'")
        by_name[name] = entry
    return by_name


def pinned_sha(source):
    if isinstance(source, dict) and source.get("source") in GIT_SOURCES:
        sha = source.get("sha", "")
        return sha if FULL_SHA.match(sha) else None
    return None


def check(root):
    root = Path(root)
    errors = []
    claude = load_json(root / CLAUDE_MANIFEST, errors)
    codex = load_json(root / CODEX_MANIFEST, errors)
    if claude is None or codex is None:
        return errors

    for key in ("name", "owner", "plugins"):
        if key not in claude:
            errors.append(f"{CLAUDE_MANIFEST}: missing '{key}'")
    for key in ("name", "plugins"):
        if key not in codex:
            errors.append(f"{CODEX_MANIFEST}: missing '{key}'")
    if not codex.get("interface", {}).get("displayName"):
        errors.append(f"{CODEX_MANIFEST}: missing interface.displayName")
    if claude.get("name") != codex.get("name"):
        errors.append("Marketplace name differs between Claude Code and Codex manifests")

    claude_entries = entries_by_name(claude.get("plugins", []), "Claude Code", errors)
    codex_entries = entries_by_name(codex.get("plugins", []), "Codex", errors)

    for name, entry in claude_entries.items():
        source = entry.get("source")
        sha = pinned_sha(source)
        if not isinstance(source, dict) or source.get("source") not in GIT_SOURCES:
            errors.append(f"Claude Code '{name}': source must be github, url or git-subdir")
        if sha is None:
            errors.append(f"Claude Code '{name}': source needs a full 40-character lowercase 'sha'")

        fields = review_fields(root / "reviews" / f"{name}.md")
        if fields is None:
            errors.append(f"'{name}': reviews/{name}.md is missing")
            continue
        if fields.get("Status") == "removed":
            errors.append(f"'{name}': review is marked removed but the entry is still listed")
        elif fields.get("Status") != "active":
            errors.append(f"'{name}': review Status must be 'active'")
        if not fields.get("Eligibility") or fields["Eligibility"].startswith("<"):
            errors.append(f"'{name}': review needs an Eligibility line (upstream manifest or documented skills)")
        if sha and fields.get("Commit") != sha:
            errors.append(f"'{name}': review Commit does not match the pinned sha {sha}")

        docs = root / "docs" / f"{name}.md"
        if not docs.is_file():
            errors.append(f"'{name}': docs/{name}.md is missing")
        elif sha and sha not in docs.read_text(encoding="utf-8"):
            errors.append(f"'{name}': docs/{name}.md does not mention the pinned sha")

        codex_pin = fields.get("Codex-Pin", "")
        limitation = codex_pin.startswith("limitation:") and len(codex_pin) > len("limitation:") + 3
        codex_entry = codex_entries.get(name)
        if codex_entry is None:
            if not limitation:
                errors.append(f"'{name}': missing from the Codex manifest and no Codex-Pin limitation recorded")
            continue
        policy = codex_entry.get("policy", {})
        if not policy.get("installation") or not policy.get("authentication"):
            errors.append(f"Codex '{name}': policy.installation and policy.authentication are required")
        if not codex_entry.get("category"):
            errors.append(f"Codex '{name}': category is required")
        codex_sha = pinned_sha(codex_entry.get("source"))
        if codex_sha is None:
            if not limitation:
                errors.append(f"Codex '{name}': no full 'sha' pin and no Codex-Pin limitation recorded in the review")
        elif sha and codex_sha != sha:
            errors.append(f"Codex '{name}': sha {codex_sha} differs from Claude Code sha {sha}")

    for name in codex_entries.keys() - claude_entries.keys():
        errors.append(f"Codex '{name}': not listed in the Claude Code manifest")

    rules = [root / "CLAUDE.md", root / "AGENTS.md"]
    if all(p.is_file() for p in rules) and rules[0].read_bytes() != rules[1].read_bytes():
        errors.append("CLAUDE.md and AGENTS.md must be identical")

    for zip_path in root.rglob("*.zip"):
        rel = zip_path.relative_to(root)
        if rel.parts[0] not in ("dist", ".git"):
            errors.append(f"{rel}: ZIP files must not be committed")

    return errors


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    errors = check(root)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    with open(root / CLAUDE_MANIFEST, encoding="utf-8") as f:
        count = len(json.load(f)["plugins"])
    print(f"OK: {count} entries, manifests consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
