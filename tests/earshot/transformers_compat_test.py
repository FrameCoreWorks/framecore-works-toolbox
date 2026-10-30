"""Full tier: the locked Transformers must accept the processor call the pinned Earshot makes.

2026-10-30 owner run on a Mac mini (arm64, Python 3.12, torch 2.6.0, transformers 4.48.3): `earshot describe` and
`earshot match` on selftest/test.wav failed with "You have to specify either text or audios. Both cannot be none."
Earshot 0.4.0 calls `self.proc(audio=chunk, ...)` (earshot/models/clap.py, `_forward`); ClapProcessor takes the
`audio` keyword only from Transformers 4.57.0, and silently drops it before that."""
import importlib.util
import json
import pathlib
import tempfile
import unittest

PLUGIN = pathlib.Path(__file__).resolve().parents[2] / 'plugins' / 'toolbox' / 'capabilities' / 'earshot'
spec = importlib.util.spec_from_file_location('earshot_runtime', PLUGIN / 'scripts/runtime.py')
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)

FIRST_AUDIO_KEYWORD = (4, 57)
# earshot/models/clap.py at the pinned upstream commit, read for this check. A new hash means the processor calls
# changed: re-read them against the locked Transformers before updating it.
REVIEWED_CLAP = '67926497f69e9e30b27a60d020bcf2bf75b3914a866c60bf9297a90e2f731d40'


def version_tuple(text):
    return tuple(int(part) for part in text.split('+')[0].split('.')[:2])


class LockedTransformers(unittest.TestCase):
    def test_every_platform_locks_a_transformers_whose_clap_processor_takes_audio(self):
        for system in ('darwin', 'linux', 'win32'):
            with self.subTest(system=system):
                version = runtime.lock_pins('full', system)['transformers']
                self.assertGreaterEqual(version_tuple(version), FIRST_AUDIO_KEYWORD, version)
                self.assertLess(version_tuple(version), (5, 0), 'Transformers 5 is not reviewed with torch 2.6.0')

    def test_full_in_and_full_txt_agree(self):
        lines = (runtime.REQUIREMENTS / 'full.in').read_text(encoding='utf-8').splitlines()
        for name in ('transformers', 'huggingface-hub', 'safetensors'):
            with self.subTest(name=name):
                self.assertIn(f"{name}=={runtime.lock_pins('full', 'darwin')[name]}", lines)

    def test_the_reviewed_clap_module_is_the_pinned_one(self):
        files = json.loads((PLUGIN / 'upstream.json').read_text(encoding='utf-8'))['files']
        self.assertEqual(files['earshot/models/clap.py'], REVIEWED_CLAP)


@unittest.skipUnless(importlib.util.find_spec('transformers') and importlib.util.find_spec('numpy'),
                     'needs the full tier packages (run with the Earshot venv interpreter)')
class InstalledProcessor(unittest.TestCase):
    """Runs offline with a tiny local tokenizer, so no model download is needed; torch is not needed either."""

    def processor(self):
        from transformers import ClapFeatureExtractor, ClapProcessor, RobertaTokenizerFast
        folder = pathlib.Path(tempfile.mkdtemp())
        vocab = {token: i for i, token in enumerate(['<s>', '<pad>', '</s>', '<unk>', '<mask>', 'a'])}
        (folder / 'vocab.json').write_text(json.dumps(vocab), encoding='utf-8')
        (folder / 'merges.txt').write_text('#version: 0.2\n', encoding='utf-8')
        tokenizer = RobertaTokenizerFast(vocab_file=str(folder / 'vocab.json'), merges_file=str(folder / 'merges.txt'))
        return ClapProcessor(ClapFeatureExtractor(), tokenizer)

    def test_installed_transformers_is_the_locked_one(self):
        import transformers
        self.assertEqual(transformers.__version__, runtime.lock_pins('full')['transformers'])

    def test_the_audio_keyword_earshot_uses_reaches_the_feature_extractor(self):
        import numpy as np
        chunk = [np.zeros(48000, np.float32), np.zeros(48000, np.float32)]
        features = self.processor()(audio=chunk, sampling_rate=48000, return_tensors='np')
        self.assertEqual(features['input_features'].shape[0], 2)


if __name__ == '__main__':
    unittest.main()
