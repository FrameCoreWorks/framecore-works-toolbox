"""The catalog welcome in the toolbox skill is a byte-exact copy of the English asset."""
import re
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / 'plugins' / 'toolbox' / 'skills' / 'toolbox'


class WelcomeTest(unittest.TestCase):
    def test_embedded_welcome_matches_asset(self):
        text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        found = re.findall(r'<!-- welcome:start -->\n(.*?)\n<!-- welcome:end -->', text, re.S)
        self.assertEqual(len(found), 1)
        asset = (SKILL / 'assets' / 'startup-welcome.en.md').read_text(encoding='utf-8')
        self.assertEqual(found[0] + '\n', asset)

    def test_welcome_shape(self):
        asset = (SKILL / 'assets' / 'startup-welcome.en.md').read_text(encoding='utf-8')
        self.assertTrue(asset.startswith('I am FrameCore Works Toolbox.'))
        self.assertIn('Earshot (built in)', asset)
        self.assertEqual(len(re.findall(r'^- ', asset, re.M)), 2)   # Earshot and plugin groups; reel styles moved to FrameMotion in 1.17.0
        self.assertTrue(asset.rstrip().endswith('Choose the numbers you want to add:'))
        self.assertNotIn('Creative Studio', asset)

    def test_reply_format_opens_with_welcome(self):
        text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        for phrase in ('1. Open with the welcome below', 'copy it', 'translate all of it',
                       '](assets/startup-welcome.en.md)'):
            self.assertIn(phrase, text)
        self.assertNotIn('tools I recommend next to Creative', text)


if __name__ == '__main__':
    unittest.main()
