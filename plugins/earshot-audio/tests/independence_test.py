"""Behavior at the adapter's external source, setup and model-cache boundaries."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import struct
import tempfile
import unittest
from unittest import mock

PLUGIN = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('independent_earshot_runtime', PLUGIN / 'scripts/runtime.py')
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)


class IndependentRuntime(unittest.TestCase):
    def test_real_sound_uses_verified_external_snapshot_and_rejects_tampering(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'upstream'
            script = source / 'skills/real-sound/scripts/audit.py'
            script.parent.mkdir(parents=True)
            script.write_text('# source fixture, never executed\n')
            files = {script.relative_to(source).as_posix(): hashlib.sha256(script.read_bytes()).hexdigest()}
            with mock.patch.object(runtime, 'load_manifest', return_value={'files': files}):
                self.assertEqual(runtime.real_sound_script('audit.py', root), script)
                script.write_text('# changed')
                with self.assertRaises(runtime.Refused):
                    runtime.real_sound_script('audit.py', root)

    def test_existing_runtime_is_not_overwritten_or_downloaded_into(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); marker = root / 'user-file'; marker.write_text('keep')
            with mock.patch.object(runtime, 'fetch_source') as fetched:
                with self.assertRaises(OSError):
                    runtime.install('light', root)
                fetched.assert_not_called()
            self.assertEqual(marker.read_text(), 'keep')

    def test_empty_model_directories_never_mean_ready(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for model in runtime.MODELS:
                (root / 'cache/hf' / ('models--' + model.replace('/', '--'))).mkdir(parents=True)
            report = runtime.model_cache_status(root)
            self.assertFalse(any(r['complete'] for r in report.values()))

    def test_pinned_snapshot_checks_json_and_truncated_weights_without_inference(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            header = json.dumps({'test': {'dtype': 'F32', 'shape': [1], 'data_offsets': [0, 4]}}).encode()
            tensor = struct.pack('<Q', len(header)) + header + b'\x00' * 4
            for model, pin in runtime.MODEL_PINS.items():
                folder = root / 'cache/hf' / ('models--' + model.replace('/', '--')) / 'snapshots' / pin['revision']
                folder.mkdir(parents=True)
                for name in pin['files']:
                    (folder / name).write_bytes(tensor if name.endswith('.safetensors') else b'{}' if name.endswith('.json') else b'text')
            self.assertTrue(all(r['complete'] for r in runtime.model_cache_status(root).values()))
            (folder / 'model.safetensors').write_bytes(tensor[:-1])
            self.assertFalse(runtime.model_cache_status(root)[model]['complete'])
            (folder / 'model.safetensors').write_bytes(tensor)
            (folder / 'config.json').write_text('{broken')
            self.assertFalse(runtime.model_cache_status(root)[model]['complete'])

    def test_source_verification_rejects_symlink_even_when_bytes_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root / 'source'; source.mkdir()
            outside = root / 'outside'; outside.write_text('same')
            (source / 'file').symlink_to(outside)
            self.assertEqual(runtime.verify_tree(source, {'file': hashlib.sha256(b'same').hexdigest()}), ['file'])

    def test_audit_cannot_start_a_download(self):
        with mock.patch.object(runtime, 'real_sound_script', return_value=Path('/fixture/audit.py')), \
                mock.patch.object(runtime.subprocess, 'run') as started, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(runtime.passthrough(Path('/runtime'), 'python', ['audit.py', '--fetch']), 2)
            started.assert_not_called()

    def test_engine_environment_pins_model_revisions_and_disables_telemetry(self):
        with mock.patch.dict(runtime.os.environ, {'EARSHOT_CLAP_REVISION': 'main', 'EARSHOT_AST': 'other/model'}):
            env = runtime.engine_env(Path('/runtime'))
        self.assertEqual(env['EARSHOT_AST'], runtime.MODELS[1])
        self.assertEqual(env['EARSHOT_CLAP_REVISION'], runtime.MODEL_PINS[runtime.MODELS[0]]['revision'])
        self.assertEqual(env['HF_HUB_DISABLE_TELEMETRY'], '1')
        self.assertEqual(env['PYTHONDONTWRITEBYTECODE'], '1')


if __name__ == '__main__':
    unittest.main()
