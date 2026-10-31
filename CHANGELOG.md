# Changes

## Toolbox 1.5.2 — 2026-10-31

Trigger: owner requirement 2026-10-31: even when nothing was picked at setup, a task that needs
a tool gets it installed on demand with a notice of how long it lasts.

- New index section "Installs during work": install only what the task needs (Earshot's
  engine or an installed entry's programs), announced in one line with the host's lifetime
  (this conversation in the Claude apps, a cloud session or ChatGPT Work; once on the user's
  computer in Claude Code or Codex); ask first above about 300 MB; offer a missing entry once.
- Host runs: NOT_RUN.

## Toolbox 1.5.1 — 2026-10-31

Trigger: owner requirements 2026-10-31 for the first-install list: say what can be installed,
where and for how long; let the user pick numbers or "all"; let them come back later.

- The menu opens with one line for the current host from the new "Where installs go"
  section: on the user's computer (Claude Code desktop or terminal, Codex) entries and their
  programs stay; in the Claude apps an entry turned on in Customize > Plugins stays on the
  account while programs last for the conversation; in a Claude Code cloud session and in
  ChatGPT Work programs last only for that session or conversation.
- The second block is now "Also installs programs", with the same host-specific lifetime.
- The question accepts "all" (every entry installable on this host), and the menu ends with
  "type toolbox to see this list again and add more".
- Host runs: NOT_RUN.

## Toolbox 1.5.0 — 2026-10-31

Trigger: owner report 2026-10-31: the numbered catalog menu shown in Claude web was hard to
read, and entries such as animate and motion-designer were listed as "needs your computer"
although their tools (Node, Playwright Chromium, ffmpeg, python3) install inside a session.

- New catalog menu format: two blocks, "Ready to use" and "Installs tools for this
  conversation", grouped by purpose (Design & web, Writing, Video & animation, Sound,
  Marketing, Code), one short line per entry from the new index column "Menu". The full
  descriptions, "Works in", "Use" and "Watch out" notes are shown when the user asks about
  one number.
- "Runs" values are now `ready`, `session-install` and `computer`. Re-checked every entry:
  Earshot, animate, motion-designer, brag, huashu-art-motion and rea install their tools for
  the conversation (Claude Code desktop, cloud and phone, Cowork; Earshot also in Codex and
  ChatGPT Work with public internet access on). No entry needs only a desktop computer now;
  rea's native-binary analysis still needs Ghidra, IDA or Hopper. The menu says that a
  session install lasts only for that conversation and asks before downloads over about
  300 MB.
- Removed `video-shotcraft` by owner decision: it overlaps with Creative Studio's Remotion
  and cinematography skills, and Studio already adapted its sound-timing methods. Its docs
  page is deleted; its review stays with Status: removed.
- `scripts/check_marketplace.py` checks the new Runs values and the Menu column (tests first).
- Host runs: NOT_RUN.

## Toolbox 1.4.0 — 2026-10-31

Trigger: owner decision 2026-10-31 after the catalog review of 2026-10-30: Toolbox lists only
tools that install without trouble and work on their own, with no account, no required API
key and no separate desktop app. Libraries and runtimes that install cleanly (Node, Python,
ffmpeg, a browser) and the built-in Earshot engine stay allowed.

- Removed from the marketplace: `open-design` (needs the Open Design desktop app),
  `blender-agent-skills` (needs Blender), `meta-ads-designer` (needs a fal.ai key or another
  image tool to make images).
- Removed app notes: `pixel-plugin` (paid Aseprite app, manual Claude Code-only install),
  `voicebox` (desktop app), `iso-glow` (manual archive install; the upstream archive has also
  changed since review), `ffmpeg-skill` (manual install at the pin). `apps.json` is now empty.
- Their docs pages are deleted; their reviews stay with Status: removed and a History line.
  README, the index skill and `docs/toolbox.md` are updated. Users who installed one keep their
  copy; it can no longer be installed or updated from Toolbox.
- Host runs: NOT_RUN.

## Toolbox 1.3.4 — 2026-10-31

Trigger: the 2026-10-31 Codex desktop retest of Toolbox 1.3.3 (report U4 and U14).

- Earshot light is described as about 470 MB: a light install of 1.3.3 measured 469 MB
  (venv 458 MB), not the 358 MB measured on 2026-10-30. `runtime.py` `SIZES`,
  `capabilities.json` and `docs/earshot-audio.md` agree.
- `attach-source` stages the download in a hidden temporary folder inside the runtime root,
  like `install` already did, so nothing lands in the system temporary folder.
- Verified here: two new or changed `runtime_test` cases fail on 1.3.3 and pass on 1.3.4.
  A new light install measurement and host runs: NOT_RUN.

## Toolbox 1.3.3 — 2026-10-30

Trigger: after the 1.3.2 full install on the owner's Mac mini (Apple Silicon, Python 3.12,
torch 2.6.0, transformers 4.48.3) and the model download, `earshot describe` and
`earshot match` on `selftest/test.wav` stopped with "You have to specify either text or
audios. Both cannot be none." Earshot 0.4.0 calls the CLAP processor with `audio=`
(`earshot/models/clap.py`, `_forward`); `ClapProcessor` accepts that keyword only from
Transformers 4.57.0 and before that drops it.

- `requirements/full.in` and `full.txt`: `transformers==4.57.6` (last 4.x; 5.x not reviewed
  with torch 2.6.0), `huggingface-hub==0.36.0`, `tokenizers==0.22.2` and the new
  `hf-xet==1.8.0` dependency, all hashed. The torch platform split from 1.3.2 is unchanged.
  The upstream code is not changed.
- Engine runs set `HF_HUB_CACHE` (Earshot's model folder), `HF_HOME`, `TORCH_HOME` and
  `MPLCONFIGDIR` under `<root>/cache`, so nothing writes to `~/.cache` or `~/.config`, and
  `HF_HUB_DISABLE_XET=1` keeps model downloads on plain HTTPS. `TRANSFORMERS_CACHE` is not
  set: Transformers 4.57 deprecates it and reads `HF_HUB_CACHE`.
- New `tests/earshot/transformers_compat_test.py`: the locked Transformers must be at least
  4.57 on every platform, `full.in` and `full.txt` must agree, the reviewed `clap.py` hash is
  pinned, and, in an interpreter that has the full packages, the `audio=` call Earshot makes
  must reach the feature extractor (offline, tiny local tokenizer).
- Upgrading from 1.3.2: `status` reports the old root as `unlocked_legacy` (its packages
  differ from the new lock). Install a new root with `install --tier full --yes` and reuse
  the downloaded models with `fetch-models --root <new> --from <old> --yes`.
- Verified here: the new test fails on the 1.3.2 lock with Transformers 4.48.3 and the
  owner's exact error, and passes with 4.57.6. The pinned Earshot 0.4.0 `Clap._forward`,
  text features and `AST._forward` run on random-initialised models with torch 2.6.0 and
  Transformers 4.57.6 (CLAP 1x512 audio and text, AST 1x527), and fail on 4.48.3 with the
  owner's error. `uv pip install --dry-run` with `--require-hashes` resolves every locked
  wheel for macOS arm64, Linux x86_64/aarch64 and Windows x86_64 (Linux/Windows torch from
  the CPU index unchanged and not re-fetched: the index is blocked here). Loading the real
  pinned CLAP and AST checkpoints and a real `describe`/`match`: NOT_RUN (Hugging Face is
  blocked in this session). Host runs: NOT_RUN.

## Toolbox 1.3.2 — 2026-10-30

Trigger: the owner's Earshot full install on a Mac mini (Apple Silicon, Python 3.12) on
2026-10-30 stopped with "No matching distribution found for torch==2.6.0+cpu": the full
lock pinned only the CPU-index build, which PyTorch publishes for Linux and Windows.

- `requirements/full.in` and `full.txt` split torch by platform: `torch==2.6.0+cpu` from the
  CPU index off macOS, `torch==2.6.0` with the PyPI `macosx_11_0_arm64` wheel hashes on
  macOS. Every other locked package already had a hashed macOS arm64 wheel (checked against
  PyPI for all 53 full and 37 light entries). On macOS the installer no longer adds the
  PyTorch index.
- Full install on an Intel Mac is refused before any write (PyTorch 2.6.0 has no macOS
  x86_64 wheels); the message points to `--tier light`.
- A failed install that left files in a new root now says to delete that folder or choose a
  new `--root`, and a pip failure names "no wheel for this platform" among the causes.
- `lock_pins` follows the platform markers, so lock conformance reads `2.6.0` on macOS.
- Verified here: `uv pip install --dry-run --python-platform aarch64-apple-darwin` resolves
  all 53 full packages with hashes (the 1.3.1 lock reproduces the owner's error); the cp312
  macOS torch wheel downloaded with `--require-hashes` matches its hash; pip honours the
  marker-split duplicate entries under `--require-hashes`. A real install on a Mac and full
  inference: NOT_RUN. Host runs: NOT_RUN.

## Toolbox 1.3.1 — 2026-10-30

Trigger: fresh-install test of Studio, Toolbox and Open Assets on 2026-10-30 (report
`raporty/2026-10-30-test-instalacji-trzech-pluginow.md`, items 3, 5–9).

- Earshot `envelope.py` takes the caller's `framecore-task-request/1` (`--request`) and
  `--host`/`--model`; the result no longer writes host and model as null, and a
  `--requester name@version` keeps its version. An invalid, misaddressed or contradicted
  request is refused before anything runs.
- Earshot install stages the downloaded source inside `--root`, so nothing is written
  outside the runtime root when `TMPDIR` is unset.
- Earshot light is described as about 360 MB (358 MB measured), not about 200 MB.
- Catalog: `ffmpeg-skill` lists its reviewed Codex route instead of "Claude Code only";
  `rea` gains Codex steps for its existing `.codex-plugin` package; the iso-glow review
  names its one install-time download.
- Tests resolve the macOS `/var` temp symlink, so the suite also passes on a Mac.
- Host runs: NOT_RUN.

## Toolbox 1.3.0 — 2026-10-30

Trigger: owner request 2026-10-30 (thread "Ujednolić instalację trzech pluginów z
linku"): after installing Creative Studio a non-technical user gets Toolbox's
recommendations as a numbered list, each with what it does and how it improves Studio,
split into tools that work right away in a session (chat, cloud, phone) and tools that
need the user's own computer.

- Every catalog row gains "How it helps Studio" and "Runs" (`session` or `computer`);
  `scripts/check_marketplace.py` fails when either is missing (three new tests).
- The `toolbox` skill's reply format is now that numbered two-group list ending with
  "Which numbers do you want?", in plain words; a new section installs the picked numbers
  per host, including the Claude Code cloud-session case (container only; keep it through
  claude.ai Customize > Plugins). In ChatGPT Work and Codex third-party entries without a
  reviewed route stay listed as "(Claude only)".
- `references/installation.md` and `INSTALL.md` describe the repository as public (the
  private-repository sentence was stale since 2026-10-30).
- Host runs: NOT_RUN.

## Toolbox 1.2.5 — 2026-10-30

Trigger: right after saving Toolbox 1.2.4 in ChatGPT Work (owner's screenshot,
2026-10-30), Work started downloading and analysing the third-party catalog entries
to "adapt" Claude packages to the Work format.

- The `toolbox` skill, `references/installation.md` and `CHATGPT_INSTALL.md` now say
  plainly: installing Toolbox ends with the readback; never inspect, download, convert,
  repackage or adapt a catalog entry for another host; an entry without its own reviewed
  package for Work or Codex is listed as Claude-only. Toolbox never rebuilds upstream code.

## Toolbox 1.2.4 — 2026-10-30

Trigger: the owner's ChatGPT Work installation attempt on 2026-10-30 (Toolbox at
`133edbb`) stopped: Plugin Creator's `create_plugin` takes only a ZIP path in code
execution, code execution has no network and the GitHub connector writes no files.

- `CHATGPT_INSTALL.md` "Update without a ZIP": the model writes each file read through the
  connector into code execution, checks every git blob hash in one cell that then builds
  the ZIP, and calls `create_plugin` or `update_plugin` with that archive. The owner is
  never asked for a file.
- A Work installation without network may leave out the Earshot hash locks
  `requirements/light.txt` and `full.txt` (230 KB; 29 files and 150 KB remain). The
  launcher handles that: `install` names the missing locks and stops before any download,
  and `status` reads the pinned versions from the `.in` files. New Earshot test for it.
- Hosted run: NOT_RUN.

## Toolbox 1.2.3 — 2026-10-29

Trigger: the owner's claude.ai marketplace sync at `47e9378` skipped two plugins and
reported five warnings.

- `ffmpeg-skill` and `pixel-plugin` move from the marketplace to app notes at the same
  pins: both upstreams ship a top-level `bin/`, which claude.ai and Cowork refuse, and no
  upstream commit drops it (`ffmpeg-skill` main at `432cc1b` still has `bin/install.js`).
  They stay in the catalog with manual Claude Code install steps (a clone at the pin added
  as its own marketplace), tested in an isolated Claude Code config. 20 tools plus the
  index: 21 marketplace entries; four app notes.
- The `toolbox` skill description is shortened to 1,018 characters (claude.ai cuts at 1,024).
- `scripts/check_marketplace.py` now fails when a skill under `plugins/` has a description
  over 1,024 characters or with angle brackets.
- Not fixed here, upstream only and harmless: `motion-designer`'s `plugin.json` carries a
  `$schema` key (claude.ai drops it) and `hallmark`'s skill description contains
  placeholders such as `<path>` (claude.ai strips the brackets). Both plugins sync and work.

## Toolbox 1.2.2 — 2026-10-29

- App note `scenario-kinetic-film` removed (owner decision 2026-10-29): it needs a Scenario
  account, so Toolbox no longer recommends it. Its review is kept with `Status: removed`;
  its docs page is deleted. Creative Studio 1.155.0 carries its best knowledge as Studio's
  own kinetic film kit, written from scratch.

## Records — 2026-10-29: old Earshot Audio plugin retired

- Owner decision 2026-10-29 (stage 6b of the Earshot migration): every installed copy of
  the separate `earshot-audio` plugin is retired. [Retirement steps](docs/earshot-audio.md#retiring-installed-copies-owner-decision-2026-10-29)
  per host (Claude Code, Claude apps, ChatGPT Work release `plugins_6ada290e…`, Codex
  native entry); the owner runs them, the engine runtime folder stays. Install guides
  point to them. No plugin package changed, so no version bump.

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
