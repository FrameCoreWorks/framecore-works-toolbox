# Runtime and evidence

Use `../../../../capabilities/earshot/scripts/runtime.py` from this reference directory
(`capabilities/earshot/scripts/runtime.py` in the Toolbox plugin root). Upstream 0.4.0 is
pinned in `capabilities/earshot/upstream.json`; the launcher reports the Toolbox version
as `wrapper_version`.

`status --json` and setup without `--yes` make no installation writes. Status may
run lightweight import checks in an existing venv. Setup downloads from GitHub
(archive fallback may redirect to codeload.github.com), PyPI/files.pythonhosted.org,
and, for full tier, download.pytorch.org. Model setup uses Hugging Face's model
and file-delivery hosts. State actual blocked hosts; do not change sources silently.

Automatic setup uses Python 3.12 and exact dependency locks with hashes and wheels
only. Full tier pins CPU PyTorch 2.6.0 and Transformers 4.57.6, the first line whose CLAP
processor takes the `audio` keyword Earshot 0.4.0 passes (with 4.48.3, up to Toolbox 1.3.2,
`describe` and `match` stop with "You have to specify either text or audios"). `requirements/*.in`
records the resolution inputs; `.txt` locks are consumed by pip. Their versions
were resolved, not a proof of successful full-tier installation. Upstream build
uses the separately locked build tools with no dependency or build-isolation fetch.
A ChatGPT Work installation without network may leave out `light.txt` and
`full.txt`: `install` then names the missing locks and stops before any download,
and `status` reads the pinned versions from the `.in` files.

Engine runs keep library caches in `<root>/cache` (`HF_HUB_CACHE`, `HF_HOME`, `TORCH_HOME`,
`MPLCONFIGDIR`), not in `~/.cache` or `~/.config`; Hugging Face Xet downloads stay off.

The default root is `~/.framecore-works/earshot`; `EARSHOT_NATIVE_ROOT` or `--root`
selects another. A nonempty target is never overwritten. A failed install may
leave a partial root: inspect it and choose a fresh destination for retry, rather
than deleting or treating it as complete. Successful setup writes `engine.json`.
The preserved `upstream/` snapshot supplies real-sound files and retains attribution.

Other roots are listed read-only in `status --json` under `candidates` (path, engine
commit, tier, wrapper version, models, real-sound source, `lock_conformance`); none is
selected. A pinned engine whose `engine.json` has no `wrapper_version`, or whose
installed packages differ from the tier lock, is `unlocked_legacy`: runs on it are
refused without `--allow-unlocked`, and each allowed run prints a warning to carry into
the result. Preferred reuse is a new locked root plus `fetch-models --from <old root>
--yes`, which verifies the old root's pinned snapshots and places them by hard link
or copy with no download, leaving the old root unchanged. `attach-source --yes` adds
only a verified `upstream/` to a pinned root that lacks it. A root whose engine commit
differs from the pin stays `unavailable`.

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
