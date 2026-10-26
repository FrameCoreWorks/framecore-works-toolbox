"""Tests for scripts/check_marketplace.py. Run: python3 -m unittest discover -s tests"""

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_marketplace  # noqa: E402

SHA = "0123456789abcdef0123456789abcdef01234567"
OTHER_SHA = "fedcba9876543210fedcba9876543210fedcba98"


def claude_entry(name="demo", sha=SHA, **source):
    src = {"source": "github", "repo": "acme/demo", "sha": sha}
    src.update(source)
    return {"name": name, "source": src, "description": "Demo"}


def codex_entry(name="demo", sha=SHA):
    src = {"source": "url", "url": "https://github.com/acme/demo.git"}
    if sha:
        src["sha"] = sha
    return {
        "name": name,
        "source": src,
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }


def review_text(name="demo", sha=SHA, status="active", codex_pin="sha",
                eligibility="upstream ships .claude-plugin/plugin.json"):
    return (
        f"# Review: {name}\n\n## Entry\n\n- Name: {name}\n- Status: {status}\n"
        f"- Eligibility: {eligibility}\n- Commit: {sha}\n- Codex-Pin: {codex_pin}\n"
    )


class CheckMarketplaceTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        for d in (".claude-plugin", ".agents/plugins", "reviews", "docs"):
            (self.root / d).mkdir(parents=True)
        self.write_manifests([], [])

    def tearDown(self):
        shutil.rmtree(self.root)

    def write_manifests(self, claude_plugins, codex_plugins):
        claude = {"name": "toolbox", "owner": {"name": "X"}, "plugins": claude_plugins}
        codex = {"name": "toolbox", "interface": {"displayName": "Toolbox"}, "plugins": codex_plugins}
        (self.root / ".claude-plugin/marketplace.json").write_text(json.dumps(claude))
        (self.root / ".agents/plugins/marketplace.json").write_text(json.dumps(codex))

    def write_entry_files(self, name="demo", sha=SHA, **review_kwargs):
        (self.root / f"reviews/{name}.md").write_text(review_text(name, sha, **review_kwargs))
        (self.root / f"docs/{name}.md").write_text(f"Pinned commit: {sha}\n")

    def errors(self):
        return check_marketplace.check(self.root)

    def test_empty_toolbox_passes(self):
        self.assertEqual(self.errors(), [])

    def test_valid_entry_passes(self):
        self.write_manifests([claude_entry()], [codex_entry()])
        self.write_entry_files()
        self.assertEqual(self.errors(), [])

    def test_git_subdir_source_passes(self):
        entry = claude_entry()
        entry["source"] = {"source": "git-subdir", "url": "https://github.com/acme/demo.git",
                           "path": "plugins/demo", "sha": SHA}
        self.write_manifests([entry], [codex_entry()])
        self.write_entry_files()
        self.assertEqual(self.errors(), [])

    def test_branch_only_source_fails(self):
        entry = claude_entry()
        del entry["source"]["sha"]
        entry["source"]["ref"] = "main"
        self.write_manifests([entry], [codex_entry()])
        self.write_entry_files()
        self.assertTrue(any("40-character" in e for e in self.errors()))

    def test_short_sha_fails(self):
        self.write_manifests([claude_entry(sha="0123456")], [codex_entry()])
        self.write_entry_files()
        self.assertTrue(any("40-character" in e for e in self.errors()))

    def test_relative_path_source_fails(self):
        entry = claude_entry()
        entry["source"] = "./plugins/demo"
        self.write_manifests([entry], [codex_entry()])
        self.write_entry_files()
        self.assertTrue(any("source" in e for e in self.errors()))

    def test_missing_review_fails(self):
        self.write_manifests([claude_entry()], [codex_entry()])
        (self.root / "docs/demo.md").write_text(f"{SHA}\n")
        self.assertTrue(any("reviews/demo.md" in e for e in self.errors()))

    def test_review_with_other_commit_fails(self):
        self.write_manifests([claude_entry()], [codex_entry()])
        self.write_entry_files(sha=OTHER_SHA)
        self.assertTrue(any("Commit" in e for e in self.errors()))

    def test_review_without_eligibility_fails(self):
        self.write_manifests([claude_entry()], [codex_entry()])
        self.write_entry_files(eligibility="")
        self.assertTrue(any("Eligibility" in e for e in self.errors()))

    def test_missing_docs_fails(self):
        self.write_manifests([claude_entry()], [codex_entry()])
        (self.root / "reviews/demo.md").write_text(review_text())
        self.assertTrue(any("docs/demo.md" in e for e in self.errors()))

    def test_removed_review_still_in_manifest_fails(self):
        self.write_manifests([claude_entry()], [codex_entry()])
        self.write_entry_files(status="removed")
        self.assertTrue(any("removed" in e for e in self.errors()))

    def test_entry_missing_from_codex_fails(self):
        self.write_manifests([claude_entry()], [])
        self.write_entry_files()
        self.assertTrue(any("Codex" in e for e in self.errors()))

    def test_codex_sha_mismatch_fails(self):
        self.write_manifests([claude_entry()], [codex_entry(sha=OTHER_SHA)])
        self.write_entry_files()
        self.assertTrue(any("differs" in e for e in self.errors()))

    def test_codex_without_sha_needs_recorded_limitation(self):
        self.write_manifests([claude_entry()], [codex_entry(sha=None)])
        self.write_entry_files()
        self.assertTrue(any("Codex-Pin" in e for e in self.errors()))

    def test_codex_limitation_allows_missing_codex_entry(self):
        self.write_manifests([claude_entry()], [])
        self.write_entry_files(codex_pin="limitation: no Codex manifest, install skills with npx skills")
        self.assertEqual(self.errors(), [])

    def test_codex_entry_needs_policy_and_category(self):
        entry = codex_entry()
        del entry["policy"]
        del entry["category"]
        self.write_manifests([claude_entry()], [entry])
        self.write_entry_files()
        errs = self.errors()
        self.assertTrue(any("policy" in e for e in errs))
        self.assertTrue(any("category" in e for e in errs))

    def test_codex_only_entry_fails(self):
        self.write_manifests([], [codex_entry()])
        self.write_entry_files()
        self.assertTrue(any("Claude Code" in e for e in self.errors()))

    def test_duplicate_names_fail(self):
        self.write_manifests([claude_entry(), claude_entry()], [codex_entry()])
        self.write_entry_files()
        self.assertTrue(any("Duplicate" in e for e in self.errors()))

    def test_rules_files_must_be_identical(self):
        (self.root / "CLAUDE.md").write_text("rules\n")
        (self.root / "AGENTS.md").write_text("other rules\n")
        self.assertTrue(any("identical" in e for e in self.errors()))

    def test_committed_zip_fails(self):
        (self.root / "docs/skill.zip").write_bytes(b"PK")
        self.assertTrue(any("ZIP" in e for e in self.errors()))

    def test_marketplace_names_must_match(self):
        path = self.root / ".agents/plugins/marketplace.json"
        data = json.loads(path.read_text())
        data["name"] = "other"
        path.write_text(json.dumps(data))
        self.assertTrue(any("name" in e for e in self.errors()))


if __name__ == "__main__":
    unittest.main()
