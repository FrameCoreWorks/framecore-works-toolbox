# Review: ffmpeg-skill

## Entry

- Name: ffmpeg-skill
- Status: removed
- Upstream: https://github.com/kajisho5/ffmpeg-skill
- Author: kajisho5
- License: MIT
- Commit: 1ae1bdf1ca0adbb1606fbca493948b1bbb2f83ff
- Upstream version: 2.17.3
- Kind: app
- Pin: 1ae1bdf1ca0adbb1606fbca493948b1bbb2f83ff
- Eligibility: app note: a Claude plugin with a top-level `bin/`, which claude.ai and Cowork refuse; listed in plugins/toolbox/apps.json with manual Claude Code install steps, never installed from the marketplace
- Source: none (manual Claude Code install from a clone at the pin)
- Reviewed on: 2026-10-28
- Reviewer: ChatGPT Work for Kamil, FrameCore Works
- Owner approval: yes, 2026-10-28: "dolaczamy gfo do toolboxa"

## What it is

The original provides 42 local FFmpeg video/audio tools, a root skill,
argparse-derived input contracts and an optional stdio MCP server. It supports
recording synchronization/drift, multicam switching, HDR-to-SDR, cutting,
captions and delivery checks. It is independently usable without Studio or
other Toolbox entries. The catalog points at the complete pinned upstream;
it does not copy the upstream code or configure its MCP server.

## Files reviewed

`README.md`, `SKILL.md`, `.claude-plugin/plugin.json`,
`.claude-plugin/marketplace.json`, `package.json`, `LICENSE`,
`scripts/_contract.py`, `scripts/_common/`, `scripts/sync.py`,
`scripts/multicam.py`, `scripts/color.py`, `mcp/server.py`,
`bin/install.js`, `docs/contract.md`, relevant `docs/design-decisions.md`
and selected test cases. The checkout was pinned at the commit above; the
prior review ran selected synthetic tests. After the owner requested inclusion,
the original native installer was run against an isolated temporary directory.

## Installation and writes

A Claude marketplace source references the complete original Git repository;
it does not run the npm installer automatically. The standalone installer
copies the skill and supporting scripts, templates, references, docs and MCP
into the selected host skill directory, refreshing an existing destination.
Media operations write requested outputs and optional plans/audit records;
existing output refusal and overwrite controls are part of the contract.
No runtime, provider, model or server is installed by the Toolbox catalog.

## Hooks, network and data

No plugin hook configuration or automatic MCP registration was found. The
upstream server is local stdio and is started only by a separate configuration.
No default media-upload or telemetry behavior was identified in the reviewed
core paths. Optional transcription engines run locally but some can download
model weights from Hugging Face or OpenAI on first use; this is a separate
network/setup action. This was a bounded review, not a complete security audit.
The skill supplies instructions when loaded; no prompt rewriting hook was found.

## Requirements and limits

Python 3.10+, FFmpeg/FFprobe 6.1+ recommended, with operation-specific filters
and encoders. Speech transcription requires an additional engine and model.
Audio correlation is not lip-sync verification; neither crop nor contact-sheet
tools track faces or subjects. Source plans fingerprint size and head/tail bytes,
not a full-file hash for large files. Dry runs may run measurements; verify
performs real checks and plans are written when requested. The repository has
a top-level `bin/`: claude.ai / Cowork compatibility is unverified.

## Install and runtime tests

- Isolated native skill-directory installation: PASS, `node bin/install.js --dir`
  against a new scratch directory, without touching a user skill directory.
  `SKILL.md` and all 145 files in the installed `scripts`, `templates`,
  `references`, `docs` and `mcp` payload folders matched the pinned checkout;
  the installed static contract reports 42 tools. This is a filesystem install,
  not a test of Codex/Claude skill discovery.
- Work local CLI: earlier seven synthetic source tests PASS, covering contract,
  default 12 MCP listings, changed-input refusal, sync and drift, multicam and
  HDR-to-SDR metadata. Python 3.12.14, FFmpeg 6.1.1-3ubuntu5. No actual client
  media or perceptual color/lip-sync acceptance was tested.
- Claude Code isolated marketplace install and `claude plugin validate`: NOT_RUN,
  CLI unavailable. claude.ai / Cowork, fresh Codex and native Work activation:
  NOT_RUN. The tool's own doctor warned based on the FFmpeg version; package
  backport status was not investigated and doctor success is not a security audit.

## Verdict

Accept as the owner's chosen pinned catalog entry, with host-specific installation
and media capability checks kept explicit. It fills sync, multicam and HDR-prep
gaps while overlapping some existing FrameCut, caption and audio operations.
The catalog entry itself is not proof of a working marketplace installation.

## History

- 2026-10-28: added at `1ae1bdf` after owner request.
- 2026-10-29: moved to an app note (Toolbox 1.2.3). claude.ai and Cowork skip any plugin with a top-level `bin/` (marketplace sync at 47e9378, 2026-10-29), so the entry moved from the marketplace to an app note installed by hand in Claude Code at the same pin; the upstream still ships `bin/` (ffmpeg-skill main at 432cc1b; pixel-plugin unchanged since dee3506). Manual install test: `claude plugin marketplace add` of a clone at the pin, then `claude plugin install ffmpeg-skill@ffmpeg-skill`, PASS in an isolated Claude Code 2.1.312 config (2026-10-29); plugin enabled at the pinned version.
- 2026-10-31: removed by owner decision: Toolbox keeps only entries that install without accounts, API keys or separate desktop apps; it is installed by hand at the pin (top-level bin/, not claude.ai or Cowork).
