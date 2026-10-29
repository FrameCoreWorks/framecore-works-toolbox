# Portable catalog verification

## Toolbox 1.2.3, claude.ai sync fixes — 2026-10-29

Baseline: GitHub `main` at `47e9378`. Owner's claude.ai sync at that commit: 2 plugins skipped
(`ffmpeg-skill`, `pixel-plugin`: top-level `bin/`), 5 warnings (`toolbox` description over 1,024
characters; `motion-designer` `$schema`; `hallmark` angle brackets). Source checks PASS: 55
repository tests, 52 Earshot tests on Python 3.12, marketplace check (21 entries), portable
package check for `toolbox` 1.2.3, `claude plugin validate .` and `plugins/toolbox`;
`toolbox` 1.2.3 installed in an isolated Claude config; manual Claude Code install of both
new app notes from a clone at the pin PASS in an isolated config. claude.ai re-sync after
the push: NOT_RUN at commit time.

## Toolbox 1.2.2, app note scenario-kinetic-film removed — 2026-10-29

Baseline: GitHub `main` at `a656a4a`. Source checks PASS: repository tests, Earshot tests on
Python 3.12, marketplace check (23 entries), portable package check for `toolbox` 1.2.2,
`claude plugin validate .`; `toolbox` 1.2.2 installed in an isolated Claude config.

## Toolbox 1.2.1, app note scenario-kinetic-film — 2026-10-29

Baseline: GitHub `main` at `215068b`. Source checks PASS: 52 repository tests, Earshot
tests on Python 3.12, marketplace check (23 entries), portable package check for
`toolbox` 1.2.1, `claude plugin validate .`. Isolated Claude config: `toolbox` 1.2.1
installed and its cache holds the new `apps.json` and index rows. Archive: SHA-256
matches the hash in the upstream download URL; unzip into a temporary HOME skills
folder and removal PASS. NOT_RUN: rendering a film, Scenario MCP generation, host
invocation of the skill, ZIP hash of the portable package.

## Toolbox 1.2.0, recommended tools moved from Creative Studio — 2026-10-29

Baseline: GitHub `main` at `343f74f`. Source checks PASS: 52 repository tests
(including 8 new app-note tests), 52 Earshot tests on Python 3.12, marketplace check
(23 entries, 2 app notes, Earshot built in), portable package checks for `toolbox`
and the new `rea` wrapper, `claude plugin validate .` and `claude plugin validate plugins/rea`.
Toolbox ZIP: 31 files (adds `apps.json`), SHA-256 `7ed68164ef32dae45a875be079363e6411b699ed12ab4ed65ef27a8fa6048a58`.

Isolated Claude config: marketplace add, then `claude plugin install` PASS for
`pixel-plugin`, `taste-skill`, `hairline`, `huashu-art-motion`, `anatomy` and `rea`
(wrapper), and for `toolbox` 1.2.0 (cache holds `apps.json`). A headless `claude -p`
session listed every new skill: 9 `pixel-plugin:` skills and commands,
`taste-skill:taste-skill`, `hairline:hairline-create` and `hairline:hairline-adopt`,
`huashu-art-motion:huashu-art-motion`, `anatomy:anatomy`, `rea:rea`.

Code review (independent subagent, read-only): 3 blockers, 3 important, 2 minor.
Fixed: `upscayl` and `opencreator` rejected for default telemetry; `rea` moved to our
own wrapper because the upstream skill runs `rea-agents@latest` and `setup`;
`check_apps` hardened (duplicates, malformed file) with tests; pixel-plugin Cowork
wording and Windows bash note; CLAUDE.md app-note gate line; README app-note table.
Not changed: no cross-check of `apps.json` upstream/version against the review (minor).

NOT_RUN: starting any MCP server (`aseprite` prebuilt binary, `rea-agents@6.5.0`
from npm), using each skill on a real task, Voicebox app, iso-glow archive re-download
(isoglow.dev blocked by this session's proxy; Studio's 2026-10-18 checksum stands),
claude.ai/Cowork installs, ChatGPT Work and Codex. Saved Work update: pending
(Kamil updates Work from this repository).

## Toolbox 1.1.0, Earshot built in — 2026-10-29

Baseline: GitHub `main` before this release. Source checks PASS: 44 repository
tests (`python3 -m unittest discover -s tests`), 52 Earshot tests on Python 3.12
(`tests/earshot/`: 24 moved, 15 capability including the import guard, 13 envelope), marketplace
check (17 entries), portable package check, `claude plugin validate .`.
The Toolbox ZIP has 30 files, one skill, the capability, the contract schema
(SHA-256 `e7cc0f4e612395768e8c8c6cf2a033a555bc69b4c8ea5ca45c4db019a342897a`) and
the Leon Lin attribution; ZIP SHA-256
`1ffcd5f312465a6ff1db62399c78c992525635ff77b9e860b1cd8e4369978695`. Code review (0 blockers; 3 important and 7 of 9 minor fixed; kept: origin wording, stale lock-file
header comments kept byte-identical), plugin validator PASS and skill review fixes applied.

Isolated Claude config: marketplace add and `toolbox` install PASS at 1.1.0, the
cached package contains `capabilities/earshot/scripts/runtime.py`; installing
`earshot-audio` fails as expected (not in the marketplace). Unmocked envelope run
of `status` on an empty root: `succeeded`, readiness `unavailable`, nothing
written to the root; `install --tier light` without `--yes`: `needs_consent`.

NOT_RUN: engine installation, model reuse on a real root (owner's Mac root),
full-tier inference, fresh client invocations in Claude apps, ChatGPT Work and
Codex. Saved Work update: pending (prompt in the shared handover folder).

## Catalog cleanup 1.0.3 — 2026-10-28

Owner-approved removal: 33 entries before, 18 after (17 tools plus the index).
The [historical removal handover](handover-claude-code-2026-10-28.md) records the
exact IDs, configuration scope, preservation evidence and client-state limits.

Source checks PASS: 37 repository tests, 24 Earshot tests (existing Python 3.12),
marketplace consistency, both portable package checks/builds, Claude marketplace
validation and git diff whitespace. All 17 retained marketplace tool objects,
Earshot source, scripts/tests, UX records and four old removed reviews are unchanged.
All 30 dedicated files are absent. An 82-term scan includes hidden/ignored files,
aliases, unique source addresses and configuration keys; only clearly historical
removal records may name removed tools. The six-file catalog ZIP matches source
exactly and contains no removed-tool reference. SHA-256:
`03518f89a31fdb956f4cdd024fd12904a1a0e4aa76c8a57c5df295b536d1ff91`.

Isolated Claude marketplace add, catalog installation and list PASS at 1.0.3;
a removed-entry installation fails as expected after source verification.
Isolated Codex catalog-file plan/install/verify PASS (FILES_VERIFIED; baseline
commit used as fixture marker, candidate content checked separately).
Temporary scope only: no normal user installation was changed. Fresh client
invocations remain NOT_RUN. The existing Claude validation advisory is recorded
in the handover; it does not fail validation.

Saved Work synchronization is pending: no verified editable Toolbox identity was
found, and no duplicate was created. The handover contains the exact update
prompt and requires explicit file deletion plus complete inventory readback.
All earlier sections below are historical evidence for earlier releases.

## ffmpeg-skill catalog entry — 2026-10-28

Catalog 1.0.2 adds the upstream `kajisho5/ffmpeg-skill` version 2.17.3 pinned to
`1ae1bdf1ca0adbb1606fbca493948b1bbb2f83ff`. No upstream implementation is
bundled in the catalog. A separate temporary skill-directory install reproduced
the skill and 145 source files in its five payload folders byte-for-byte; its
installed static contract reports 42 tools. Earlier synthetic tests passed for
contract, MCP exposure, changed-source refusal, audio offset/drift, multicam
and HDR-to-SDR. Catalog source checks: 37 repository tests and 24 Earshot tests
PASS; marketplace check reports 33 entries; both local packages validate.
The six-file 1.0.2 catalog ZIP matches its source and contains the new row.
An isolated native Codex catalog helper install and verify returned
`FILES_VERIFIED` (synthetic source-commit marker; host activation NOT_RUN).
The upstream plugin's marketplace install, Claude validation,
fresh Work/Codex/Claude client discovery, speech engines and real footage
remain NOT_RUN. Its root `bin/` is present; claude.ai / Cowork compatibility
is not established. See the [review](../reviews/ffmpeg-skill.md) for scope.

## Earshot addition — 2026-10-28

Catalog 1.0.1 and Earshot Audio wrapper 1.2.0, based on GitHub
`e77cb913fad54d840bec02e42fd9a6d805b335e8`. Source checks: 37 repository tests
and 24 Earshot wrapper tests PASS; marketplace has 32 entries. Both portable
packages validate and build independently. The native Codex test installs Earshot
without the Toolbox catalog or any sibling plugin. All 282 files in the selected
upstream checkout match the recorded source hashes. Only package metadata was
resolved for dependency locks; no upstream engine or model installation ran.

Fresh host activation, engine rendering and full-tier inference remain NOT_RUN.
The existing saved Work Earshot 1.1.0 release was inspected and remains unchanged.
See [Earshot review](../reviews/earshot-audio.md) for scope and limitations.

## Original portable catalog release

Date: 2026-10-28. Version: 1.0.0.
GitHub baseline: `e0e023432f7258792ecad07745306ea330e9c400`.
Imported repository tree: `ecaf375b0f5cb5ac7af5f59aca9d4d500c83b455`;
all 77 original files matched their Git blob identities before edits.

| Check | Result | Scope |
| --- | --- | --- |
| Existing marketplace tests | PASS, 29 tests | Existing pins, categories and catalog consistency |
| Distribution tests | PASS, 7 tests | Complete reproducible ZIP, manifest drift, prohibited files, isolated install/verify, repeat and conflict preservation |
| Marketplace check | PASS, 31 entries | No catalog entries added or removed |
| Portable package check | PASS | Three matching manifests and discoverable skills |
| Archive readback | PASS | Exactly one complete plugin; SHA-256 equality with source |
| Codex native file installation | PASS in temporary directories | No user installation or host activation implied |
| Current Claude CLI validation and install | NOT_RUN | Claude CLI unavailable in this environment |
| Fresh Claude, ChatGPT Work and Codex invocation | NOT_RUN | Requires actual host installation/activation |
| Third-party tools on Work / Codex | Unknown | This change does not adapt or execute catalog entries |
| Remote GitHub Actions | NOT_RUN at source preparation | Inspect the workflow for the published commit |

The prior Claude owner/CLI results in `docs/toolbox.md` remain historical evidence
for the older package. They are not tests of the new portable release.
Maintainer plugins listed in `CLAUDE.md` (Superpowers, plugin-dev and review
agents) are not available in this session; direct source review and the checks
above were used. No upstream installers, hooks or tests were executed.

Open Assets already has all three manifests at version 0.2.1. Its GitHub main
was `dcb26ae1f779e034a13442bbb4c50075abc8f6d7`; the saved Work source was read
back and checked during this task. Its package was not changed by this release.

Saving or updating an owned Work plugin is a separate deployment step. This
repository change prepares installation packages and guides; it does not create
an account plugin, install catalog tools or modify Creative Studio.
