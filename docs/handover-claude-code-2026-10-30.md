# Claude handover — Toolbox 1.3.3 Earshot full fix, 2026-10-30

Read `CHANGELOG.md` (1.3.3) first; this note only says where the work stands.

## State

- Toolbox 1.3.3 on `main`: the Earshot full lock pins Transformers 4.57.6 so the CLAP
  `audio=` call in Earshot 0.4.0 works; engine caches stay under `<root>/cache`.
- Creative Studio's root `.claude-plugin/marketplace.json` names the Toolbox version and
  commit; it was updated in the same task.
- Owner evidence: 1.3.2 full install and model download on an Apple Silicon Mac
  PASS_REPORTED; `describe`/`match` failed there with "You have to specify either text or
  audios". Real-model inference on the 1.3.3 lock: NOT_RUN (Hugging Face and the PyTorch
  CPU index are blocked in cloud sessions).

## 2026-10-31: Toolbox 1.3.4

- Fixes from the Codex retest report: Earshot light size text (about 470 MB) and
  `attach-source` staging inside the runtime root. The 1.3.3 lock and steps below are
  unchanged; on the Mac, update to 1.3.4 instead of 1.3.3.
- Still open in another thread: the iso-glow archive hash changed upstream (report U2).

## Next step for the owner's Mac

1. Update Toolbox to 1.3.3.
2. `python3.12 <runtime> --root <new> install --tier full` and then with `--yes`.
3. `python3.12 <runtime> --root <new> fetch-models --from <old root>` and then with `--yes`
   (reuses the 1.1 GB models, no download).
4. `run describe` and `run match` on `selftest/test.wav`; record the result as
   PASS_REPORTED or the exact error.

## Rules kept

No upstream code changed or copied; the torch platform split from 1.3.2 is unchanged;
the old root is preserved, not overwritten.
