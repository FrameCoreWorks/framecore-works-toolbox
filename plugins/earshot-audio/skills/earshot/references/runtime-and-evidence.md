# Runtime and evidence

Use `../../../scripts/runtime.py` from this reference directory. The skill-local
`../scripts/runtime.py` is a compatibility forwarding entry for the same launcher.
Upstream 0.4.0 is pinned in `upstream.json`; the wrapper version is 1.2.0.

`status --json` and setup without `--yes` make no installation writes. Status may
run lightweight import checks in an existing venv. Setup downloads from GitHub
(archive fallback may redirect to codeload.github.com), PyPI/files.pythonhosted.org,
and, for full tier, download.pytorch.org. Model setup uses Hugging Face's model
and file-delivery hosts. State actual blocked hosts; do not change sources silently.

Automatic setup uses Python 3.12 and exact dependency locks with hashes and wheels
only. Full tier pins CPU PyTorch 2.6.0 and Transformers 4.48.3. `requirements/*.in`
records the resolution inputs; `.txt` locks are consumed by pip. Their versions
were resolved, not a proof of successful full-tier installation. Upstream build
uses the separately locked build tools with no dependency or build-isolation fetch.

The default root is `~/.framecore-works/earshot`; `EARSHOT_NATIVE_ROOT` or `--root`
selects another. A nonempty target is never overwritten. A failed install may
leave a partial root: inspect it and choose a fresh destination for retry, rather
than deleting or treating it as complete. Successful setup writes `engine.json`.
The preserved `upstream/` snapshot supplies real-sound files and retains attribution.

Readiness has distinct levels: readable skill; importable light dependencies;
importable full dependencies; complete pinned model file containers; actual task
execution. `model_inference_verified` is always false in status. The model check
requires the selected revisions, nonempty required files, readable JSON and tensor
offsets within the safetensors file. It does not hash tensor data or run inference.
Use `run doctor --load --json` for separate authorized loading evidence.

The wrapper fixes model IDs/revisions and sets offline flags for normal runs,
disables Hub telemetry and removes Gemini keys. It refuses `llm`, `mcp` and
`doctor --fetch`; dedicated `fetch-models --yes` owns model downloads.
`exec` permits authorized Python and is not an OS sandbox or network firewall.
Do not call the bare venv interpreter for ordinary tasks, as that bypasses these
wrapper settings. Do not run untrusted recipes, scripts or remote media URLs.
