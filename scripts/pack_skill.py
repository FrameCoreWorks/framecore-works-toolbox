#!/usr/bin/env python3
"""Fetch one skill folder from an upstream repo at a pinned commit and ZIP it
for manual upload to the Claude apps (or to unpack for ChatGPT knowledge files).

Usage:
  python3 scripts/pack_skill.py <owner>/<repo> <40-char-sha> <path/to/skill> [out_dir]

Writes <out_dir>/<skill-name>-<short-sha>.zip (default out_dir: dist/, which is
ignored by git). Upstream files are treated as data: nothing from the upstream
repo is executed, git hooks are disabled, symlinks are skipped, and LFS
smudging is off.
"""

import os
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def git(args, cwd):
    env = dict(os.environ, GIT_LFS_SKIP_SMUDGE="1", GIT_TERMINAL_PROMPT="0")
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd, env=env, check=True)


def main(argv):
    if len(argv) not in (4, 5):
        print(__doc__)
        return 2
    repo, sha, skill_path = argv[1], argv[2], argv[3].strip("/")
    out_dir = Path(argv[4] if len(argv) == 5 else Path(__file__).resolve().parent.parent / "dist")
    if not REPO.match(repo):
        sys.exit(f"Invalid repo '{repo}', expected owner/repo")
    if not FULL_SHA.match(sha):
        sys.exit("The commit must be a full 40-character lowercase SHA")
    if ".." in Path(skill_path).parts:
        sys.exit("The skill path must stay inside the repo")

    with tempfile.TemporaryDirectory(prefix="pack-skill-") as tmp:
        git(["init", "-q"], tmp)
        git(["remote", "add", "origin", f"https://github.com/{repo}.git"], tmp)
        git(["fetch", "-q", "--depth", "1", "origin", sha], tmp)
        git(["checkout", "-q", "FETCH_HEAD"], tmp)

        skill_dir = Path(tmp, skill_path)
        if not (skill_dir / "SKILL.md").is_file():
            sys.exit(f"No SKILL.md in {skill_path} at {sha}")

        out_dir.mkdir(parents=True, exist_ok=True)
        zip_path = out_dir / f"{skill_dir.name}-{sha[:12]}.zip"
        skipped = []
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in sorted(skill_dir.rglob("*")):
                if path.is_symlink():
                    skipped.append(path.relative_to(skill_dir))
                elif path.is_file():
                    zf.write(path, Path(skill_dir.name) / path.relative_to(skill_dir))
    for path in skipped:
        print(f"Skipped symlink: {path}")
    print(zip_path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
