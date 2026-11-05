# Claude handover — Toolbox 1.6.3, stabilization, 2026-11-05

The current Toolbox handover. Read `CLAUDE.md` first, then this note, then the top of `CHANGELOG.md`.
The handovers of 2026-10-28 (1.0.3 removal record) and 2026-10-30 (Earshot 1.3.3 fix) are history.

## State

- **Toolbox 1.6.3** on `main` (`e9fe001`): 16 catalog entries plus the `toolbox` index (17 marketplace
  entries) and the built-in Earshot capability (engine 0.4.0 at `591fa3e`). No Git tags; the version
  lives in the three plugin manifests and `.claude-plugin/marketplace.json`.
- **Owner decision 2026-11-05: stabilization.** No new entries or features until the owner says
  otherwise; only defect and consistency fixes. A repository the owner sends for review still follows
  the workflow in `CLAUDE.md`, but adding it waits for the owner's explicit yes.
- **ChatGPT Work:** the owner updates the hosted plugins from `main`; treat Work as equal to `main` and
  do not upload without the owner's request. Creative Studio's update prompt updates Toolbox with it.
- Creative Studio pins this release (Toolbox 1.6.3, `e9fe001`) in its registry and root marketplace.

## What changed since the 2026-10-30 handover

- 1.3.4: Earshot light size text and `attach-source` staging inside the runtime root.
- 1.4.0: only self-contained tools (no account, required API key or desktop app); seven entries and the
  four app notes removed.
- 1.5.0 to 1.5.2: readable numbered menu, "where installs go and for how long", installs on demand.
- 1.6.0: in Work a picked entry is saved as its own private plugin from the upstream skill files at the
  reviewed pin, with the upstream author and licence in the description.
- 1.6.1: Earshot says the engine lasts only for the conversation in Work.
- 1.6.2 and 1.6.3: GPT Astra audit fixes (Earshot task binding, REA wrapper, one Work entry route,
  a cancelled result for an interrupted Earshot envelope run).

## Checks (2026-11-05, cloud container, on `e9fe001`)

`python3 -m unittest discover -s tests` (73 tests), `scripts/check_marketplace.py`,
`scripts/package_plugins.py --check`, Earshot tests under Python 3.12 (74 tests, 2 skipped) and
`claude plugin validate .`: PASS. CI run 41909115045: success.

## Open

- Earshot real-model inference on the full lock (`describe`/`match`) on the owner's Mac: NOT_RUN since
  the 1.3.3 fix (Hugging Face and the PyTorch CPU index are blocked in cloud sessions).
- Huashu Art Motion in Work works only when called directly (`@Huashu Art Motion`); Studio's routing to
  it in Work is not fixed, by the owner's choice (Studio handover, 2026-11-04).
- Fresh host activation of most catalog entries in Work and Codex: NOT_RUN (see each review).
