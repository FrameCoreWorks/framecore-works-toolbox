# Claude handover — Toolbox 1.7.0, stabilization, 2026-11-05

The current Toolbox handover. Read `CLAUDE.md` first, then this note, then the top of `CHANGELOG.md`.
The handovers of 2026-10-28 (1.0.3 removal record) and 2026-10-30 (Earshot 1.3.3 fix) are history.

## State

- **Toolbox 1.7.0** on `main` (`bfce3e7`): 17 catalog entries plus the `toolbox` index (18 marketplace
  entries) and the built-in Earshot capability (engine 0.4.0 at `591fa3e`). No Git tags; the version
  lives in the three plugin manifests and `.claude-plugin/marketplace.json`.
- **Owner decision 2026-11-05: stabilization.** No new entries or features until the owner says
  otherwise; only defect and consistency fixes. A repository the owner sends for review still follows
  the workflow in `CLAUDE.md`, but adding it waits for the owner's explicit yes. The owner made one such
  exception on 2026-11-05: `pixelfx` (below).
- **ChatGPT Work:** the owner updates the hosted plugins from `main`; treat Work as equal to `main` and
  do not upload without the owner's request. Creative Studio's update prompt updates Toolbox with it.
- Creative Studio pins this release (Toolbox 1.7.0, `bfce3e7`) in its extension and companion registries from Studio 1.171.1.

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
- 1.7.0 (owner request 2026-11-05): new Creative entry `pixelfx` (patch-gg/pixelfx at `a841596`, 0.3.0,
  MIT) through our own wrapper `plugins/pixelfx`. The upstream skill first clones the unpinned default
  branch, so the wrapper's skill asks once, clones the upstream into the project at the pin and then
  follows the upstream skill. The Patch Pixel font in the upstream `gallery/fonts` is not MIT. Studio
  1.171.0 adds its own-words pixel VFX craft reference and routes to this entry.

## Checks (2026-11-05, cloud container, on `bfce3e7`)

`python3 -m unittest discover -s tests` (73 tests), `scripts/check_marketplace.py`,
`scripts/package_plugins.py --check` (also `--plugin pixelfx`), Earshot tests under Python 3.12 (74 tests, 2 skipped) and
`claude plugin validate .`: PASS; isolated Claude install of `pixelfx` PASS. CI on `e9fe001`: run 41909115045 success.

## Open

- Earshot real-model inference on the full lock (`describe`/`match`) on the owner's Mac: NOT_RUN since
  the 1.3.3 fix (Hugging Face and the PyTorch CPU index are blocked in cloud sessions).
- Huashu Art Motion in Work works only when called directly (`@Huashu Art Motion`); Studio's routing to
  it in Work is not fixed, by the owner's choice (Studio handover, 2026-11-04).
- `pixelfx`: the wrapper's pinned clone, the upstream render tools, claude.ai, Cowork, Codex and Work: NOT_RUN.
- Fresh host activation of most catalog entries in Work and Codex: NOT_RUN (see each review).
