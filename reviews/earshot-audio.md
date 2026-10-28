# Review: earshot-audio

## Entry

- Name: earshot-audio
- Status: active
- Upstream: https://github.com/Leonxlnx/earshot
- Author: Leon Lin; FrameCore Works wrapper
- License: MIT
- Commit: 591fa3e028032e6dce56620a20e932e35667e8d8
- Upstream version: 0.4.0
- Kind: adapted
- Eligibility: adapted: independent local audio launcher and workflow, explicitly requested by the owner
- Source: local wrapper ./plugins/earshot-audio
- Reviewed on: 2026-10-28
- Reviewer: ChatGPT Work; source review and wrapper tests
- Owner approval: Kamil on 2026-10-28: "Wprowadź", followed by "Spróbować earshot do toolboxa"; prior instructions require an independent FrameCore adaptation

## What it is

One portable `earshot` skill, a FrameCore launcher, a source-record importer,
three host manifests, dependency locks and source-hash metadata. The original
engine supplies audio measurements, semantic matching, sound banks, synthesis
and real-recording workflows. It remains external to the repository and package.
This explicitly approved adapter is an exception to the ordinary full-upstream
entry rule, retaining the owned Work wrapper's local-only command scope.

## Files reviewed

Upstream was fetched into a separate temporary checkout at the full commit and
its tree and all 282 SHA-256 file hashes were checked. Read `pyproject.toml`,
`LICENSE`, relevant README installation/command sections, `earshot/cli.py`,
`config.py`, `doctor.py`, `models/hub.py`, network/upload paths in `llm.py` and
`mcp_server.py`, and real-sound audit, QA and licence-handling code. Searched
engine and real-sound source for network/process calls. No upstream scripts,
installers, hooks or tests were executed during this review.

Wrapper source started from the user's owned Work 1.1.0 release, read back as
unchanged during this task. The older uploaded 1.0.9 archive was not treated as
the current source. Reviewed the wrapper diff, manifests, locks, generic importer,
setup/execution boundaries, native-entry helper and archive inventory.

## What it installs and writes

Plugin installation writes only the wrapper's files. Engine setup defaults to
`~/.framecore-works/earshot`, or a user-selected root, and requires the explicit
`--yes` step after its plan. It keeps a verified upstream snapshot, creates a venv,
installs hash-locked dependencies and the pinned engine, disables its upload/server
modules in the venv, and records completion. The source snapshot is unchanged.
Nonempty destinations are preserved. Model setup separately fills the runtime
cache. Analysis and rendering write requested project outputs. No unrelated host
configuration, Studio files or other plugins are installed or changed.

## Hooks

None in the wrapper. No MCP server or automatic install/startup command.

## Network traffic and data sent outside

Authorized setup reads GitHub, codeload.github.com, pypi.org and
files.pythonhosted.org; full dependencies additionally use download.pytorch.org.
Authorized model setup reads pinned Hugging Face files and its delivery hosts.
Hub telemetry is disabled by the wrapper. Normal engine calls use offline flags.
The wrapper refuses `llm`, `mcp`, `doctor --fetch` and real-sound audit downloads;
it uses a dedicated explicit model-fetch action. It does not upload input media.

Upstream itself includes an opt-in Gemini critique API and an optional MCP server;
neither is exposed here. Arbitrary user Python (`exec`) and code recipes can make
their own calls: this adapter is not a sandbox. Use trusted code and local media.
The source-record importer decodes local bytes without fetching source URLs.

## Changes to prompts or tool results

The skill guides sound measurement and evidence reporting. It does not inject
always-on context, rewrite other tool outputs or invoke companion skills. Generic
handoffs retain attribution, hashes and `not_reviewed` creative status.
Creative Studio owns any cross-plugin workflow; no peer dependency is introduced.

## Requirements and install tests

Python 3.12 for automatic dependency setup, wheel availability, FFmpeg/FFprobe for
media decoding and Node.js for optional mux. Full tier additionally needs CPU
PyTorch, Transformers and separately downloaded model weights. No API credentials.
Locks were resolved from package metadata with builds disabled: 37 light packages,
53 full packages and 3 build packages. This is not engine execution evidence.

- Wrapper tests: PASS, 24 tests; command refusals, source checks, non-destructive
  setup, model container checks and source-record decoding/rejections.
- Repository/distribution tests: PASS, 37 tests; includes a standalone Earshot
  ZIP and native Codex file installation without sibling plugins.
- Portable package and marketplace checks: PASS.
- Claude Code isolated installation/validation: NOT_RUN; CLI unavailable.
- claude.ai / Cowork UI: NOT_RUN until the owner reports the result.
- ChatGPT Work saved-plugin update/activation: NOT_RUN in this repo-only addition.
- Codex client activation: NOT_RUN; filesystem installation alone is not activation.
- Fresh engine installation, real sound rendering, full-tier model inference:
  NOT_RUN; no new runtime or model download was requested by this catalog change.

## Risks and verdict

Accept with conditions: explicit adaptation request, pinned source and hash-locked
setup, no automatic installation/upload, and independent packaging. Actual host
activation and engine compatibility must be checked in the chosen host. Model
container checks do not validate all tensor contents or prove inference. Source
records are assertions plus byte evidence, not proof of rights or creative fit.
Other OS/CPU wheel availability is Unknown; do not silently relax lock versions.
The earlier Work plugin remains a separate saved release until explicitly updated.

## History

- 2026-10-28: added FrameCore wrapper 1.2.0 at upstream `591fa3e`; catalog 1.0.1.
