"""Exercise package isolation, portability drift and non-destructive installation."""
import json
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import package_plugins
import install_codex


class DistributionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.repo = self.base / 'repo'
        self.plugin = self.repo / 'plugins/toolbox'
        shutil.copytree(ROOT / 'plugins/toolbox', self.plugin)
        self.commit = 'a' * 40

    def tearDown(self):
        self.temp.cleanup()

    def test_zip_is_reproducible_complete_and_standalone(self):
        (self.repo / '.claude-plugin').mkdir()
        (self.repo / '.claude-plugin/marketplace.json').write_text('{}')
        first = package_plugins.build(self.repo, 'toolbox', self.base / 'one')
        second = package_plugins.build(self.repo, 'toolbox', self.base / 'two')
        self.assertEqual(first.read_bytes(), second.read_bytes())
        with zipfile.ZipFile(first) as archive:
            names = set(archive.namelist())
            self.assertIn('plugin.json', names)
            self.assertIn('.codex-plugin/plugin.json', names)
            self.assertIn('.claude-plugin/plugin.json', names)
            self.assertIn('skills/toolbox/references/installation.md', names)
            self.assertNotIn('.claude-plugin/marketplace.json', names)
            for name in names:
                self.assertEqual(archive.read(name), (self.plugin / name).read_bytes())

    def test_missing_overlay_and_identity_drift_are_rejected(self):
        path = self.plugin / '.codex-plugin/plugin.json'
        original = path.read_text()
        path.unlink()
        with self.assertRaises(ValueError):
            package_plugins.validate_plugin(self.plugin)
        data = json.loads(original)
        data['version'] = '99.0.0'
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'version'):
            package_plugins.validate_plugin(self.plugin)

    def test_package_rejects_links_and_environment_files(self):
        target = self.base / 'outside'; target.write_text('private')
        link = self.plugin / 'linked'; link.symlink_to(target)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            package_plugins.build(self.repo, 'toolbox', self.base / 'dist')
        link.unlink()
        (self.plugin / '.env').write_text('secret')
        with self.assertRaisesRegex(ValueError, 'environment'):
            package_plugins.build(self.repo, 'toolbox', self.base / 'dist')

    def test_archive_cannot_be_written_inside_repository(self):
        with self.assertRaises(ValueError):
            package_plugins.build(self.repo, 'toolbox', self.repo / 'dist')

    def run_install(self, action):
        return install_codex.run(action, self.repo, self.base / 'skills',
                                 self.base / 'bundle', self.commit)

    def test_plan_install_repeat_and_verify(self):
        self.assertEqual(self.run_install('plan')['status'], 'READY')
        self.assertFalse((self.base / 'skills').exists())
        self.assertEqual(self.run_install('install')['status'], 'FILES_VERIFIED')
        entry = self.base / 'skills/toolbox/SKILL.md'
        self.assertIn(str(self.base / 'bundle/skills/toolbox/SKILL.md'), entry.read_text())
        before = entry.stat().st_mtime_ns
        self.assertEqual(self.run_install('install')['status'], 'already_up_to_date')
        self.assertEqual(entry.stat().st_mtime_ns, before)
        self.assertEqual(self.run_install('verify')['host_activation'], 'NOT_RUN')

    def test_edited_bundle_and_entry_are_preserved(self):
        self.run_install('install')
        skill = self.base / 'bundle/skills/toolbox/SKILL.md'
        skill.write_text('user changes')
        with self.assertRaises(ValueError):
            self.run_install('install')
        self.assertEqual(skill.read_text(), 'user changes')
        with self.assertRaises(ValueError):
            self.run_install('verify')

    def test_partial_install_and_overlapping_paths_are_rejected(self):
        (self.base / 'bundle').mkdir()
        with self.assertRaises(ValueError):
            self.run_install('install')
        with self.assertRaises(ValueError):
            install_codex.run('install', self.repo, self.base / 'skills',
                              self.base / 'skills/bundle', self.commit)


if __name__ == '__main__':
    unittest.main()
