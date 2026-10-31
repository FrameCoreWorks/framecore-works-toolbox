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
- every entry except the index has a category from CATEGORIES;
- first-party plugins (entry metadata.firstParty) live in ./plugins/<name>
  with docs/<name>.md, and the "toolbox" index skill lists exactly the other
  entries and the built-in capabilities, each under the heading of its category,
  with columns Plugin | What it is for | How it helps Studio | Runs | Works in | Menu,
  where Runs is one of RUNS and Menu is "<group>: <few words>" with a group from MENU_GROUPS;
- built-in capabilities (plugins/toolbox/capabilities.json, kind "built-in")
  are not marketplace entries, have their folder with UPSTREAM.md naming the
  reviewed commit, and reviews/<name>.md (Status: active, Kind: built-in) and
  docs/<name>.md with the same commit;
- app notes (plugins/toolbox/apps.json: desktop apps and archives that are
  not plugins) are not marketplace entries, have a category, a pin (full
  commit SHA or sha256:<hex>), reviews/<name>.md (Status: active, Kind: app,
  Pin: <same pin>) and docs/<name>.md naming the pin, and are listed in the index;
- every SKILL.md under plugins/ has a description of at most 1024 characters
  without angle brackets (claude.ai cuts or strips anything else on sync);
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
APP_PIN = re.compile(r"^(?:[0-9a-f]{40}|sha256:[0-9a-f]{64})$")
FIELD = re.compile(r"^- ([A-Za-z-]+): *(.*)$", re.MULTILINE)
INDEX_ROW = re.compile(r"^\|\s*`([a-z0-9][a-z0-9._-]*)`\s*\|", re.MULTILINE)
INDEX = "toolbox"
HEADING = re.compile(r"^#+\s*(.+?)\s*$")
# Entry "category" slug -> heading in the toolbox index. Add new categories here and in CLAUDE.md.
# claude.ai keeps at most this many description characters and strips angle brackets.
DESCRIPTION_LIMIT = 1024
# Index "Runs" column: "ready" works as soon as the plugin is on; "session-install" installs
# programs (Node, ffmpeg, a browser, Python packages) into the current conversation only;
# "computer" needs something that cannot be installed in a session (a desktop app).
RUNS = {"ready", "session-install", "computer"}
# Index "Menu" column groups, in the order the catalog menu shows them.
MENU_GROUPS = ("Design & web", "Writing", "Video & animation", "Sound", "Marketing", "Code")
MENU_LINE = re.compile(r"^(" + "|".join(re.escape(g) for g in MENU_GROUPS) + r"): \S.*$")
CATEGORIES = {"creative": "Creative", "dev-tools": "Dev tools", "marketing": "Marketing & growth"}


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


def check_first_party(root, name, source, errors):
    """Our own plugin in plugins/<name>: no upstream, so no review or sha."""
    expected = f"./plugins/{name}"
    if not isinstance(source, str) or source.rstrip("/") != expected:
        errors.append(f"'{name}': a first-party plugin must use the local source {expected}")
        return
    plugin = root / expected
    if not (plugin / ".claude-plugin/plugin.json").is_file():
        errors.append(f"'{name}': {expected}/.claude-plugin/plugin.json is missing")
    if (plugin / "bin").exists():
        errors.append(f"'{name}': {expected}/bin is not allowed (claude.ai and Cowork refuse it)")
    if not (root / "docs" / f"{name}.md").is_file():
        errors.append(f"'{name}': docs/{name}.md is missing")


def check_builtins(root, entries, errors):
    """Capabilities built into the index plugin; returns {catalog name: pseudo-entry with its category}."""
    caps = root / "plugins" / INDEX / "capabilities.json"
    if not caps.is_file():
        return {}
    data = load_json(caps, errors) or {}
    found = {}
    for cap in data.get("capabilities", []):
        if not isinstance(cap, dict) or cap.get("kind") != "built-in":
            continue
        name = cap.get("catalog_name") or cap.get("id")
        if not name:
            errors.append(f"plugins/{INDEX}/capabilities.json: a built-in capability needs catalog_name")
            continue
        if name in entries:
            errors.append(f"'{name}': is both a marketplace entry and a built-in capability")
        if cap.get("category") not in CATEGORIES:
            errors.append(f"'{name}': built-in category must be one of {sorted(CATEGORIES)}")
        found[name] = {"category": cap.get("category")}
        fields = review_fields(root / "reviews" / f"{name}.md")
        if fields is None:
            errors.append(f"'{name}': reviews/{name}.md is missing")
            continue
        if fields.get("Status") != "active":
            errors.append(f"'{name}': review Status must be 'active'")
        if fields.get("Kind") != "built-in":
            errors.append(f"'{name}': a built-in capability needs 'Kind: built-in' in the review")
        sha = fields.get("Commit", "")
        if not FULL_SHA.match(sha):
            errors.append(f"'{name}': review Commit must be the full 40-character upstream commit")
            sha = None
        folder = root / "plugins" / INDEX / str(cap.get("path", ""))
        if not cap.get("path") or not folder.is_dir():
            errors.append(f"'{name}': plugins/{INDEX}/{cap.get('path')} is missing")
        elif not (folder / "UPSTREAM.md").is_file() or (sha and sha not in (folder / "UPSTREAM.md").read_text(encoding="utf-8")):
            errors.append(f"'{name}': plugins/{INDEX}/{cap['path']}/UPSTREAM.md must name the reviewed upstream commit")
        docs = root / "docs" / f"{name}.md"
        if not docs.is_file():
            errors.append(f"'{name}': docs/{name}.md is missing")
        elif sha and sha not in docs.read_text(encoding="utf-8"):
            errors.append(f"'{name}': docs/{name}.md does not mention the pinned sha")
    return found


def check_apps(root, entries, errors):
    """App notes listed by the index plugin; returns {name: pseudo-entry with its category}."""
    path = root / "plugins" / INDEX / "apps.json"
    if not path.is_file():
        return {}
    data = load_json(path, errors)
    if data is None:
        return {}
    if not isinstance(data, dict):
        errors.append(f"plugins/{INDEX}/apps.json must be an object with an 'apps' list")
        return {}
    apps = data.get("apps")
    if not isinstance(apps, list):
        errors.append(f"plugins/{INDEX}/apps.json: 'apps' must be a list")
        return {}
    found = {}
    for app in apps:
        name = app.get("name") if isinstance(app, dict) else None
        if not name:
            errors.append(f"plugins/{INDEX}/apps.json: an app note needs a name")
            continue
        if name in found:
            errors.append(f"'{name}': listed twice in apps.json")
            continue
        if name in entries:
            errors.append(f"'{name}': is both a marketplace entry and an app note")
        if app.get("category") not in CATEGORIES:
            errors.append(f"'{name}': app category must be one of {sorted(CATEGORIES)}")
        pin = str(app.get("pin", ""))
        if not APP_PIN.match(pin):
            errors.append(f"'{name}': app pin must be a full commit SHA or sha256:<64 hex>")
            pin = None
        found[name] = {"category": app.get("category")}
        fields = review_fields(root / "reviews" / f"{name}.md")
        if fields is None:
            errors.append(f"'{name}': reviews/{name}.md is missing")
            continue
        if fields.get("Status") != "active":
            errors.append(f"'{name}': review Status must be 'active'")
        if fields.get("Kind") != "app":
            errors.append(f"'{name}': an app note needs 'Kind: app' in the review")
        if pin and fields.get("Pin") != pin:
            errors.append(f"'{name}': review Pin does not match apps.json pin {pin}")
        docs = root / "docs" / f"{name}.md"
        if not docs.is_file():
            errors.append(f"'{name}': docs/{name}.md is missing")
        elif pin and pin not in docs.read_text(encoding="utf-8"):
            errors.append(f"'{name}': docs/{name}.md does not mention the pin")
    return found


def check_index(root, entries, errors):
    """The toolbox skill must list exactly the other entries, each under its category heading."""
    skill = root / "plugins" / INDEX / "skills" / INDEX / "SKILL.md"
    if not skill.is_file():
        errors.append(f"'{INDEX}': plugins/{INDEX}/skills/{INDEX}/SKILL.md is missing")
        return
    listed, heading = {}, None
    for line in skill.read_text(encoding="utf-8").splitlines():
        if m := HEADING.match(line):
            heading = m.group(1)
        elif m := INDEX_ROW.match(line):
            if m.group(1) in listed:
                errors.append(f"'{INDEX}': SKILL.md lists '{m.group(1)}' more than once")
            listed[m.group(1)] = heading
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4 or not cells[2]:
                errors.append(f"'{m.group(1)}': index row needs a 'How it helps Studio' text")
            if len(cells) < 4 or cells[3] not in RUNS:
                errors.append(f"'{m.group(1)}': index row needs Runs 'ready', 'session-install' or 'computer'")
            if len(cells) < 6 or not MENU_LINE.match(cells[5]):
                errors.append(f"'{m.group(1)}': index row needs a Menu line '<group>: <few words>'")
    for name, entry in sorted(entries.items()):
        expected = CATEGORIES.get(entry.get("category"))
        if name not in listed:
            errors.append(f"'{INDEX}': SKILL.md does not list '{name}'")
        elif expected and listed[name] != expected:
            errors.append(f"'{INDEX}': SKILL.md lists '{name}' under '{listed[name]}', expected under '{expected}'")
    for name in sorted(listed.keys() - entries.keys()):
        errors.append(f"'{INDEX}': SKILL.md lists '{name}', which is not in the marketplace, a built-in capability or an app note")


def skill_description(text):
    """The frontmatter description of a SKILL.md, folded the way YAML folds '>' blocks."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            return None
        if not line.startswith("description:"):
            continue
        value = line[len("description:"):].strip()
        if value[:1] in (">", "|"):
            block = []
            for nxt in lines[i + 1:]:
                if nxt and not nxt[0].isspace():
                    break
                block.append(nxt.strip())
            joiner = " " if value[0] == ">" else "\n"
            return joiner.join(part for part in block if part)
        return value.strip("'\"")
    return None


def check_skill_descriptions(root, errors):
    """claude.ai cuts descriptions over the limit and strips angle brackets on sync."""
    for skill in sorted((root / "plugins").glob("*/skills/*/SKILL.md")):
        rel = skill.relative_to(root)
        description = skill_description(skill.read_text(encoding="utf-8"))
        if description is None:
            continue
        if len(description) > DESCRIPTION_LIMIT:
            errors.append(f"{rel}: description has {len(description)} characters; claude.ai keeps at most {DESCRIPTION_LIMIT}")
        if "<" in description or ">" in description:
            errors.append(f"{rel}: description must not contain angle brackets (claude.ai strips them)")


def check(root):
    root = Path(root)
    errors = []
    manifest = load_json(root / MANIFEST, errors)
    if manifest is None:
        return errors

    for key in ("name", "owner", "plugins"):
        if key not in manifest:
            errors.append(f"{MANIFEST}: missing '{key}'")

    entries = entries_by_name(manifest.get("plugins", []), errors)
    for name, entry in entries.items():
        source = entry.get("source")
        if name != INDEX and entry.get("category") not in CATEGORIES:
            errors.append(f"'{name}': category must be one of {sorted(CATEGORIES)}")
        # claude.ai skips an inline-manifest entry unless strict is false
        if "skills" in entry and entry.get("strict") is not False:
            errors.append(f"'{name}': an entry that declares 'skills' needs 'strict': false (claude.ai skips it otherwise)")
        if (entry.get("metadata") or {}).get("firstParty") is True:
            check_first_party(root, name, source, errors)
            continue
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

    if INDEX in entries:
        listed = {n: e for n, e in entries.items() if n != INDEX}
        builtins = check_builtins(root, listed, errors)
        apps = check_apps(root, {**listed, **builtins}, errors)
        check_index(root, {**apps, **builtins, **listed}, errors)

    check_skill_descriptions(root, errors)

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
