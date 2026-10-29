# Review: earshot-audio

## Entry

- Name: earshot-audio
- Status: active
- Upstream: https://github.com/Leonxlnx/earshot
- Author: Leon Lin; FrameCore Works launcher
- License: MIT
- Commit: 591fa3e028032e6dce56620a20e932e35667e8d8
- Upstream version: 0.4.0
- Kind: built-in
- Eligibility: built-in capability of the toolbox plugin: local audio launcher and workflow, explicitly requested by the owner
- Source: built-in ./plugins/toolbox/capabilities/earshot (instructions ./plugins/toolbox/skills/toolbox/references/earshot/)
- Reviewed on: 2026-10-28; built-in move reviewed 2026-10-29
- Reviewer: ChatGPT Work; source review and wrapper tests. Built-in move: Claude Code (cloud), launcher tests and package checks
- Owner approval: Kamil on 2026-10-28: "Wprowadź", followed by "Spróbować earshot do toolboxa"; prior instructions require an independent FrameCore adaptation

## What it is

Since Toolbox 1.1.0 (2026-10-29) this is a capability built into the `toolbox`
plugin, not a separate marketplace entry: owner decisions D-1 (clean cut of the
separate plugin in the same release), D-3 (keep this catalog name and review) and
D-7 (`attach-source`). The engine pin, dependency locks and command scope did not
change. The text below describes the reviewed 1.2.0 wrapper; paths now live under
`plugins/toolbox/capabilities/earshot/` and its instructions under the Toolbox
skill's `references/earshot/`.

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

## Built-in move (Toolbox 1.1.0)

- Launcher: version from the Toolbox manifest; messages prefixed `toolbox/earshot:`;
  `status --json` adds `lock_conformance` and a read-only `candidates[]` of other
  roots (never selected); a pinned engine without this launcher's lock record, or
  with drifted packages, is `unlocked_legacy` and runs on it need `--allow-unlocked`.
- New consented writes, each a plan without `--yes`: `fetch-models --from <root>`
  places another root's verified pinned model snapshots by hard link or copy (no
  download, source unchanged); `attach-source` adds only a verified `upstream/`.
- `envelope.py` wraps one operation and writes a schema-validated
  `framecore-task-result/1` to a new file; `exec` is refused there.
- `import_source_record.py` refuses outputs anywhere inside the Toolbox plugin.
- No new network host, hook or MCP server. Upstream code is still not copied.

## Improvement evidence

| Repository / task | Improvement | Verification |
| --- | --- | --- |
| Creative Studio motion sound (cue effects, sync check) | One engine route through Toolbox instead of three (Studio launcher, separate plugin, local binary) | Launcher tests PASS (python3.12, `tests/earshot/`); Studio routing change is Stage 4, NOT_RUN here |
| Existing runtime on the owner's Mac (pinned engine, off-lock packages) | Reported as `unlocked_legacy` with `lock_conformance: mismatch` instead of silently `ready_full`; models reusable without a 1.1 GB download | Fixture tests PASS; the real Mac root NOT_RUN |
| Studio task handoff | Results come back as validated `framecore-task-result/1` with hashes | `envelope_test.py` PASS; Studio intake NOT_RUN |

Fresh host activation of Toolbox 1.1.0, engine install and full-tier inference: NOT_RUN.
Isolated Claude Code install of `toolbox` 1.1.0: PASS (see docs/verification.md);
`earshot-audio` is no longer installable from the marketplace (expected).

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
- 2026-10-29: moved into Toolbox 1.1.0 as a built-in capability; the separate `earshot-audio` plugin and its marketplace object were removed in the same release (owner decisions D-1..D-8). Upstream pin unchanged.
