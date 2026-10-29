# Changes

## Toolbox 1.2.1 — 2026-10-29

- New app note `scenario-kinetic-film` (owner decision 2026-10-29): Scenario's kinetic-type
  film skill, a skill archive from scenario.com pinned by SHA-256 `2217ab5dbd452185a5c3c1509994da46b1ac20d2ebeaa888536244372ce73ebf`.
  Listed for discovery with manual install steps; not a marketplace entry (no Git repository,
  no code licence in the archive, unpinned Playwright install upstream). No upstream code copied.

## Toolbox 1.2.0 — 2026-10-29

Toolbox becomes the single place for the tools Creative Studio used to recommend
(owner decision 2026-10-29: move the recommended repositories from Studio to Toolbox):

- Six new marketplace entries, pinned to the commits Studio reviewed: `pixel-plugin`,
  `taste-skill`, `hairline`, `huashu-art-motion`, `anatomy` (Creative) and `rea`
  (Dev tools; our own wrapper `plugins/rea` with its own skill and the pinned
  `rea-agents@6.5.0` MCP server, because the upstream skill runs `@latest` and `setup`).
- Two app notes in the new `plugins/toolbox/apps.json`: `voicebox` and `iso-glow`
  (archive pinned by SHA-256). They are listed in the index with manual install
  steps and are never marketplace entries.
- Rejected by the reject gate (default telemetry, found in code review): `upscayl`
  (PostHog on launch) and `opencreator` (opt-out usage reports). Their reviews are
  kept with `Status: rejected`.
- Seven tools Studio also recommended were already here (`animate`,
  `motion-designer`, `meta-ads-designer`, `logo-design`, `antislop`, `hallmark`,
  `open-design`); Toolbox's pins stay the source of truth.
- Not moved, by owner decision: VoxCPM, OmniVoice, MOSS-TTS, MOSS-TTSD,
  MoneyPrinterTurbo, Agent Reach and Adobe Skills (removed from recommendations).
- Check: `scripts/check_marketplace.py` validates app notes (category, pin, review
  `Kind: app` and `Pin:`, docs, index row, no marketplace duplicate), with tests.
- Install test: all six new entries installed in an isolated Claude config and their
  skills were listed in a headless session; MCP servers were not started (NOT_RUN).

## Toolbox 1.1.0 — 2026-10-29

Earshot becomes a capability built into Toolbox (owner decisions D-1..D-8):

- Launcher, locks, pins and attribution move to `plugins/toolbox/capabilities/earshot/`;
  instructions to the Toolbox skill's `references/earshot/`; tests to `tests/earshot/`.
- The separate `earshot-audio` plugin and its marketplace object are removed in this
  release. The catalog name, review and docs stay; the index lists it as built in.
- Launcher: Toolbox version and `toolbox/earshot:` messages; `status` reports
  `lock_conformance` and read-only `candidates`; new `unlocked_legacy` state with
  `--allow-unlocked`; `fetch-models --from` (model reuse, no download) and
  `attach-source` (verified `upstream/` only), both plans until `--yes`.
- New `envelope.py` writes a validated `framecore-task-result/1`; new
  `capabilities.json` and the shared contract schema (SHA-256 `e7cc0f4e…897a`).
- Source-record outputs are refused anywhere inside the Toolbox plugin.
- Checks: the index may list built-in capabilities; the package check validates
  `capabilities.json` and the schema hash. CI runs the Earshot tests on Python 3.12.

## Toolbox catalog 1.0.3 — 2026-10-28

Owner-approved complete removal (historical record):

- `archify`.
- `hud`.
- `linkedin-agent`.
- `notfair`.
- `planning-with-files`.
- `ponytail`.
- `wondelai-code-craftsmanship`.
- `wondelai-marketing-cro`.
- `wondelai-metaskills`.
- `wondelai-product-innovation`.
- `wondelai-product-strategy`.
- `wondelai-sales-influence`.
- `wondelai-strategy-growth`.
- `wondelai-systems-architecture`.
- `wondelai-team-motivation`.

Delete all 30 dedicated docs/reviews, their catalog rows and detail sections,
and the repository's sole dedicated environment setting. Preserve the independent
work rules. The owner explicitly overrides review retention for this list only.
The marketplace now has 17 tools plus its index (18 entries); all surviving tool
objects, pins and packages remain unchanged. In particular, the retained UX entry
keeps its shared Wondelai source and skill list.

Adopt the owner's prospective admission rule: tools, assets and repositories must
have fully demonstrated, concrete benefit to FrameCore repositories, recorded in
the review template. Global/client installations and user data are untouched.
See the [complete handover](docs/handover-claude-code-2026-10-28.md) for configuration
scope, verification, retained tools and pending hosted synchronization.

## Toolbox catalog 1.0.2 — 2026-10-28

- Add the owner's selected `ffmpeg-skill` entry as a separately installed upstream
  plugin pinned to `1ae1bdf1ca0adbb1606fbca493948b1bbb2f83ff` (2.17.3, MIT).
- Record isolated installer and synthetic runtime evidence alongside per-host
  installation gaps; no FFmpeg engine, speech model or MCP server is installed
  merely by installing this catalog.

## Toolbox catalog 1.0.1 / Earshot Audio 1.2.0 — 2026-10-28

- Add the independently installable FrameCore Works Earshot adapter to the Creative category.
- Preserve the pinned upstream engine, move original source resources outside the repo and lock dependency setup.
- Support the Earshot bundle in the Codex native-entry helper and test it without sibling plugins.
- Keep input/output handoffs generic; cross-plugin orchestration belongs to Creative Studio.

## Toolbox catalog 1.0.0 — 2026-10-28

- Preserve the existing Claude marketplace and all 30 third-party entries.
- Add portable and Codex compatibility manifests to the existing `toolbox`
  plugin; synchronize its Claude manifest and marketplace version.
- Make catalog instructions host-aware and distinguish the catalog's
  portability from each third-party tool's independently verified support.
- Add deterministic single-plugin packaging and a native Codex entry backed
  by the complete bundle, with receipt verification and conflict preservation.
- Add per-host installation guides, distribution tests and CI.
- Keep Studio orchestration and sibling plugins independent of Toolbox.

Earlier unversioned catalog history remains in Git and the per-entry reviews.
