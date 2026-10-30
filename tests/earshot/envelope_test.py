"""The Earshot task envelope: one launcher operation in, one validated framecore-task-result/1 out. No network."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[2] / 'plugins' / 'toolbox' / 'capabilities' / 'earshot' / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import envelope  # noqa: E402


def quiet(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = envelope.main(argv)
    return code, out.getvalue(), err.getvalue()


class Envelope(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.ready = {'state': 'ready_light', 'lock_conformance': 'match', 'root': str(self.base / 'rt')}

    def tearDown(self):
        self.tmp.cleanup()

    def run_with(self, launcher_code, launcher_out='', extra=(), outputs=()):
        def fake(argv):
            for path in outputs:
                Path(path).write_bytes(b'wav')
            return launcher_code, launcher_out + '\n', 'toolbox/earshot: refused\n' if launcher_code == 2 else ''
        result = self.base / 'result.json'
        result.unlink(missing_ok=True)
        with mock.patch.object(envelope, 'launch', side_effect=fake), \
                mock.patch.object(envelope.runtime, 'status', return_value=self.ready):
            code, out, err = quiet(['--result-out', str(result), *extra, '--', 'run', 'measure', 'a.wav'])
        return code, (json.loads(result.read_text()) if result.exists() else None), err

    def test_success_records_outputs_with_hashes_and_validates(self):
        wav = self.base / 'hit.wav'
        source = self.base / 'a.wav'; source.write_bytes(b'in')
        code, doc, _ = self.run_with(0, '{"lufs": -14.1}', ['--task-id', 't-1', '--requester', 'framecore-work-creative-studio',
                                                           '--input', str(source), '--output', str(wav)], [wav])
        self.assertEqual(code, 0)
        self.assertEqual(envelope.contract.validate(doc, 'result'), [])
        self.assertEqual((doc['status'], doc['origin'], doc['task_id']), ('succeeded', 'studio', 't-1'))
        self.assertEqual(doc['outputs'][0]['sha256'], hashlib.sha256(b'wav').hexdigest())
        self.assertEqual(doc['inputs'][0]['sha256'], hashlib.sha256(b'in').hexdigest())
        self.assertEqual(doc['provider']['capability'], 'earshot')
        self.assertEqual(doc['provider']['operation'], 'run')
        self.assertEqual(doc['provider']['command'], 'measure')
        self.assertEqual(doc['readiness']['state'], 'ready_light')
        self.assertEqual(doc['commands_run'][0]['exit_code'], 0)
        self.assertEqual(doc['audio']['stdout_json'], {'lufs': -14.1})

    def request(self, **change):
        doc = {'contract': 'framecore-task-request/1', 'task_id': 't-9', 'origin': 'studio',
               'requester': {'plugin': 'framecore-work-creative-studio', 'version': '1.159.0'},
               'owner': 'studio', 'host': 'codex', 'model': 'gpt-6-astra',
               'provider': {'plugin': 'toolbox', 'capability': 'earshot', 'operation': 'run', 'command': 'measure'},
               **change}
        path = self.base / f'request-{len(list(self.base.glob("request-*.json")))}.json'
        path.write_text(json.dumps(doc))
        return path

    def test_a_request_document_supplies_task_requester_host_and_model(self):
        # 2026-10-30 Codex test: the envelope took no request JSON and wrote host/model as null.
        code, doc, err = self.run_with(0, '{"lufs": -14.0}', ['--request', str(self.request())])
        self.assertEqual(code, 0, err)
        self.assertEqual(envelope.contract.validate(doc, 'result'), [])
        self.assertEqual((doc['task_id'], doc['origin'], doc['owner']), ('t-9', 'studio', 'studio'))
        self.assertEqual(doc['requester'], {'plugin': 'framecore-work-creative-studio', 'version': '1.159.0'})
        self.assertEqual((doc['host'], doc['model']), ('codex', 'gpt-6-astra'))

    def test_host_model_and_requester_version_flags_are_kept(self):
        _, doc, _ = self.run_with(0, extra=['--task-id', 't-2', '--requester', 'framecore-work-creative-studio@1.159.0',
                                            '--host', 'claude_code', '--model', 'claude-opus-5-5'])
        self.assertEqual(doc['requester'], {'plugin': 'framecore-work-creative-studio', 'version': '1.159.0'})
        self.assertEqual(doc['origin'], 'studio')
        self.assertEqual((doc['host'], doc['model']), ('claude_code', 'claude-opus-5-5'))

    def test_an_invalid_or_conflicting_request_is_refused_before_running(self):
        bad = self.request(provider={'plugin': 'framecore-open-assets', 'capability': 'search', 'operation': 'search'})
        for extra in (['--request', str(bad)],
                      ['--request', str(self.request(contract='framecore-task-result/1'))],
                      ['--request', str(self.request()), '--host', 'chatgpt_work']):
            with mock.patch.object(envelope, 'launch') as launched:
                code, _, err = quiet(['--result-out', str(self.base / 'r.json'), *extra, '--', 'run', 'measure', 'a.wav'])
            self.assertEqual(code, 2, extra)
            self.assertIn('toolbox/earshot:', err)
            launched.assert_not_called()

    def test_refusal_and_failure_map_to_contract_statuses(self):
        self.assertEqual(self.run_with(2)[1]['status'], 'refused')
        self.assertEqual(self.run_with(1)[1]['status'], 'failed')

    def test_a_plan_without_yes_is_needs_consent(self):
        _, doc, _ = self.run_with(0, '{"action": "install --tier light", "confirm": "run again with --yes"}')
        self.assertEqual(doc['status'], 'needs_consent')
        self.assertTrue(doc['unexecuted_checks'])

    def test_unlocked_runs_carry_a_warning(self):
        self.ready = {'state': 'unlocked_legacy', 'lock_conformance': 'mismatch', 'root': 'x'}
        _, doc, _ = self.run_with(0)
        self.assertTrue(any('unlocked' in w for w in doc['warnings']))

    def test_missing_declared_output_makes_the_result_partial(self):
        _, doc, _ = self.run_with(0, extra=['--output', str(self.base / 'never.wav')])
        self.assertEqual(doc['status'], 'partial')
        self.assertEqual(doc['errors'][0]['code'], 'output_missing')

    def test_exec_is_not_a_wire_operation_and_existing_results_are_kept(self):
        result = self.base / 'result.json'
        with mock.patch.object(envelope, 'launch') as launched:
            code, _, err = quiet(['--result-out', str(result), '--', 'exec', '-c', 'print(1)'])
        self.assertEqual(code, 2)
        launched.assert_not_called()
        result.write_text('keep')
        with mock.patch.object(envelope, 'launch') as launched:
            code, _, err = quiet(['--result-out', str(result), '--', 'status'])
        self.assertEqual((code, result.read_text()), (2, 'keep'))
        launched.assert_not_called()

    def test_missing_input_is_refused_before_the_operation_runs(self):
        result = self.base / 'r.json'
        with mock.patch.object(envelope, 'launch') as launched:
            code, _, err = quiet(['--result-out', str(result), '--input', str(self.base / 'nope.wav'), '--', 'status'])
        self.assertEqual(code, 2)
        launched.assert_not_called()
        self.assertFalse(result.exists())

    def test_result_path_equal_to_an_output_by_another_spelling_is_refused(self):
        import os
        cwd = os.getcwd(); os.chdir(self.base)
        try:
            with mock.patch.object(envelope, 'launch') as launched:
                code, _, _ = quiet(['--result-out', 'x.json', '--output', str(self.base / 'x.json'), '--', 'status'])
        finally:
            os.chdir(cwd)
        self.assertEqual(code, 2)
        launched.assert_not_called()

    def test_result_created_meanwhile_is_not_lost(self):
        result = self.base / 'r.json'
        def fake(argv):
            result.write_text('other')
            return 0, '', ''
        with mock.patch.object(envelope, 'launch', side_effect=fake), \
                mock.patch.object(envelope.runtime, 'status', return_value=self.ready):
            code, _, err = quiet(['--result-out', str(result), '--', 'status'])
        self.assertEqual(code, 2)
        self.assertEqual(result.read_text(), 'other')
        self.assertIn('framecore-task-result/1', err)

    def test_equals_forms_of_from_and_root_are_understood(self):
        op, _, root = envelope.operation(['fetch-models', '--from=/old', '--root=/new', '--yes'])
        self.assertEqual((op, root), ('reuse_models', Path('/new')))

    def test_exit_2_without_a_launcher_refusal_is_a_failure(self):
        def fake(argv):
            return 2, '', 'usage: earshot ...\n'
        result = self.base / 'r.json'
        with mock.patch.object(envelope, 'launch', side_effect=fake), \
                mock.patch.object(envelope.runtime, 'status', return_value=self.ready):
            quiet(['--result-out', str(result), '--', 'run', 'measure'])
        self.assertEqual(json.loads(result.read_text())['status'], 'failed')

    def test_import_source_record_is_not_advertised_as_an_envelope_operation(self):
        caps = json.loads((SCRIPTS.parents[2] / 'capabilities.json').read_text())
        for op in caps['capabilities'][0]['operations']:
            self.assertIn(op, envelope.OPERATIONS)

    def test_schema_copy_is_the_pinned_contract(self):
        self.assertEqual(hashlib.sha256(envelope.contract.SCHEMA_PATH.read_bytes()).hexdigest(),
                         'e7cc0f4e612395768e8c8c6cf2a033a555bc69b4c8ea5ca45c4db019a342897a')


if __name__ == '__main__':
    unittest.main()
