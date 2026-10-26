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


def entry(name="demo", sha=SHA, **source):
    src = {"source": "github", "repo": "acme/demo", "sha": sha}
    src.update(source)
    return {"name": name, "source": src, "description": "Demo", "category": "dev-tools"}


def review_text(name="demo", sha=SHA, status="active", kind="plugin",
                eligibility="upstream ships .claude-plugin/plugin.json"):
    return (
        f"# Review: {name}\n\n## Entry\n\n- Name: {name}\n- Status: {status}\n- Kind: {kind}\n"
        f"- Eligibility: {eligibility}\n- Commit: {sha}\n"
    )


class CheckMarketplaceTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        for d in (".claude-plugin", "reviews", "docs"):
            (self.root / d).mkdir(parents=True)
        self.write_manifest([])

    def tearDown(self):
        shutil.rmtree(self.root)

    def write_manifest(self, plugins):
        data = {"name": "toolbox", "owner": {"name": "X"}, "plugins": plugins}
        (self.root / ".claude-plugin/marketplace.json").write_text(json.dumps(data))

    def write_entry_files(self, name="demo", sha=SHA, **review_kwargs):
        (self.root / f"reviews/{name}.md").write_text(review_text(name, sha, **review_kwargs))
        (self.root / f"docs/{name}.md").write_text(f"Pinned commit: {sha}\n")

    def write_wrapper(self, name="demo", sha=SHA):
        plugin = self.root / "plugins" / name
        (plugin / ".claude-plugin").mkdir(parents=True)
        (plugin / ".claude-plugin/plugin.json").write_text(json.dumps({"name": name}))
        (plugin / "UPSTREAM.md").write_text(f"Upstream acme/demo at {sha}\n")
        return plugin

    def errors(self):
        return check_marketplace.check(self.root)

    def assert_error(self, text):
        errs = self.errors()
        self.assertTrue(any(text in e for e in errs), errs)

    def test_empty_toolbox_passes(self):
        self.assertEqual(self.errors(), [])

    def test_valid_entry_passes(self):
        self.write_manifest([entry()])
        self.write_entry_files()
        self.assertEqual(self.errors(), [])

    def test_git_subdir_source_passes(self):
        e = entry()
        e["source"] = {"source": "git-subdir", "url": "https://github.com/acme/demo.git",
                       "path": "plugins/demo", "sha": SHA}
        self.write_manifest([e])
        self.write_entry_files()
        self.assertEqual(self.errors(), [])

    def test_branch_only_source_fails(self):
        e = entry()
        del e["source"]["sha"]
        e["source"]["ref"] = "main"
        self.write_manifest([e])
        self.write_entry_files()
        self.assert_error("40-character")

    def test_short_sha_fails(self):
        self.write_manifest([entry(sha="0123456")])
        self.write_entry_files()
        self.assert_error("40-character")

    def test_unknown_source_type_fails(self):
        e = entry()
        e["source"] = {"source": "npm", "package": "demo"}
        self.write_manifest([e])
        self.write_entry_files()
        self.assert_error("github, url or git-subdir")

    def test_missing_review_fails(self):
        self.write_manifest([entry()])
        (self.root / "docs/demo.md").write_text(f"{SHA}\n")
        self.assert_error("reviews/demo.md")

    def test_review_with_other_commit_fails(self):
        self.write_manifest([entry()])
        self.write_entry_files(sha=OTHER_SHA)
        self.assert_error("Commit")

    def test_review_without_eligibility_fails(self):
        self.write_manifest([entry()])
        self.write_entry_files(eligibility="")
        self.assert_error("Eligibility")

    def test_missing_docs_fails(self):
        self.write_manifest([entry()])
        (self.root / "reviews/demo.md").write_text(review_text())
        self.assert_error("docs/demo.md")

    def test_removed_review_still_in_manifest_fails(self):
        self.write_manifest([entry()])
        self.write_entry_files(status="removed")
        self.assert_error("removed")

    def test_duplicate_names_fail(self):
        self.write_manifest([entry(), entry()])
        self.write_entry_files()
        self.assert_error("Duplicate")

    def test_adapted_wrapper_passes(self):
        self.write_wrapper()
        self.write_manifest([{"name": "demo", "source": "./plugins/demo", "category": "creative"}])
        self.write_entry_files(kind="adapted")
        self.assertEqual(self.errors(), [])

    def test_local_source_needs_adapted_kind(self):
        self.write_wrapper()
        self.write_manifest([{"name": "demo", "source": "./plugins/demo", "category": "creative"}])
        self.write_entry_files()
        self.assert_error("adapted")

    def test_wrapper_must_name_reviewed_commit(self):
        self.write_wrapper(sha=OTHER_SHA)
        self.write_manifest([{"name": "demo", "source": "./plugins/demo", "category": "creative"}])
        self.write_entry_files(kind="adapted")
        self.assert_error("UPSTREAM.md")

    def test_wrapper_with_bin_fails(self):
        (self.write_wrapper() / "bin").mkdir()
        self.write_manifest([{"name": "demo", "source": "./plugins/demo", "category": "creative"}])
        self.write_entry_files(kind="adapted")
        self.assert_error("bin")

    def test_local_source_outside_plugins_fails(self):
        self.write_manifest([{"name": "demo", "source": "./elsewhere/demo", "category": "creative"}])
        self.write_entry_files(kind="adapted")
        self.assert_error("./plugins/demo")

    def write_index(self, listed=("demo",), heading="Dev tools"):
        plugin = self.root / "plugins/toolbox"
        (plugin / ".claude-plugin").mkdir(parents=True)
        (plugin / ".claude-plugin/plugin.json").write_text(json.dumps({"name": "toolbox"}))
        skill = plugin / "skills/toolbox"
        skill.mkdir(parents=True)
        rows = "".join(f"| `{n}` | x |\n" for n in listed)
        (skill / "SKILL.md").write_text(f"## Catalog\n\n### {heading}\n\n{rows}\n### Creative\n\n")
        (self.root / "docs/toolbox.md").write_text("Toolbox index\n")
        return {"name": "toolbox", "source": "./plugins/toolbox", "metadata": {"firstParty": True}}

    def test_first_party_index_passes(self):
        self.write_manifest([self.write_index(), entry()])
        self.write_entry_files()
        self.assertEqual(self.errors(), [])

    def test_index_must_list_every_entry(self):
        self.write_manifest([self.write_index(listed=()), entry()])
        self.write_entry_files()
        self.assert_error("does not list 'demo'")

    def test_index_lists_entry_under_its_category(self):
        self.write_manifest([self.write_index(heading="Creative"), entry()])
        self.write_entry_files()
        self.assert_error("under 'Dev tools'")

    def test_index_must_not_list_entry_twice(self):
        index = self.write_index()
        skill = self.root / "plugins/toolbox/skills/toolbox/SKILL.md"
        skill.write_text(skill.read_text() + "| `demo` | dup |\n")
        self.write_manifest([index, entry()])
        self.write_entry_files()
        self.assert_error("more than once")

    def test_entry_needs_known_category(self):
        e = entry()
        e["category"] = "productivity"
        self.write_manifest([e])
        self.write_entry_files()
        self.assert_error("category")

    def test_entry_without_category_fails(self):
        e = entry()
        del e["category"]
        self.write_manifest([e])
        self.write_entry_files()
        self.assert_error("category")

    def test_index_must_not_list_unknown_entries(self):
        self.write_manifest([self.write_index(listed=("demo", "gone")), entry()])
        self.write_entry_files()
        self.assert_error("'gone'")

    def test_first_party_needs_docs(self):
        index = self.write_index(listed=())
        (self.root / "docs/toolbox.md").unlink()
        self.write_manifest([index])
        self.assert_error("docs/toolbox.md")

    def test_first_party_must_be_local(self):
        e = entry(name="toolbox")
        e["metadata"] = {"firstParty": True}
        self.write_manifest([e])
        (self.root / "docs/toolbox.md").write_text("x\n")
        self.assert_error("./plugins/toolbox")

    def test_committed_zip_fails(self):
        (self.root / "docs/skill.zip").write_bytes(b"PK")
        self.assert_error("ZIP")

    def test_manifest_missing_owner_fails(self):
        (self.root / ".claude-plugin/marketplace.json").write_text(json.dumps({"name": "t", "plugins": []}))
        self.assert_error("owner")


if __name__ == "__main__":
    unittest.main()
