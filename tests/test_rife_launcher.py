"""Offline checks of the rife-interpolate launcher: pins, consent and frame math."""
import importlib.util
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins/rife-interpolate'
spec = importlib.util.spec_from_file_location('rife', PLUGIN / 'skills/rife-interpolate/scripts/rife.py')
rife = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rife)


class RifeLauncherTest(unittest.TestCase):
    def test_pins_match_upstream_note_and_review(self):
        upstream = (PLUGIN / 'UPSTREAM.md').read_text()
        review = (ROOT / 'reviews/rife-interpolate.md').read_text()
        self.assertIn(rife.COMMIT, upstream)
        self.assertIn('Commit: ' + rife.COMMIT, review)
        for asset in rife.ASSETS.values():
            self.assertRegex(asset['sha256'], r'^[0-9a-f]{64}$')
            self.assertIn(asset['sha256'], upstream)
            self.assertIn(asset['sha256'], review)

    def test_install_needs_yes_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.environ['FRAMECORE_RIFE_HOME'] = tmp
            try:
                args = type('A', (), {'yes': False, 'models': None})()
                out = io.StringIO()
                with redirect_stdout(out):
                    code = rife.cmd_install(args)
            finally:
                del os.environ['FRAMECORE_RIFE_HOME']
            self.assertEqual(code, 4)
            self.assertEqual(json.loads(out.getvalue())['status'], 'needs_consent')
            self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_target_frames_keep_duration(self):
        self.assertEqual(rife.target_frames(48, Fraction(24), fps=60), 120)
        self.assertEqual(rife.target_frames(30, Fraction(30000, 1001), fps=60), 60)
        self.assertEqual(rife.target_frames(10, Fraction(24), factor=4), 40)
        self.assertEqual(rife.target_frames(10, Fraction(24)), 20)

    def test_only_power_of_two_multiples_work_without_v4(self):
        self.assertTrue(rife.ratio_needs_v4(Fraction(24), 60))
        self.assertTrue(rife.ratio_needs_v4(Fraction(30), 90))
        self.assertFalse(rife.ratio_needs_v4(Fraction(30), 60))
        self.assertFalse(rife.ratio_needs_v4(Fraction(15), 60))
        self.assertFalse(rife.ratio_needs_v4(Fraction(24)))

    def test_never_uses_the_broken_cpu_switch(self):
        source = (PLUGIN / 'skills/rife-interpolate/scripts/rife.py').read_text()
        self.assertNotIn('"-g", "-1"', source)
        self.assertEqual(source.count('["ffmpeg", "-nostdin"'), source.count('["ffmpeg"'))

    def test_model_names_cannot_escape_the_cache(self):
        with self.assertRaises(SystemExit), redirect_stdout(io.StringIO()):
            rife.parse_models('../etc')


if __name__ == '__main__':
    unittest.main()
