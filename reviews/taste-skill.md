# Review: taste-skill

## Entry

- Name: taste-skill
- Status: active
- Upstream: https://github.com/Leonxlnx/taste-skill
- Author: Leonxlnx
- License: MIT
- Commit: f6b76575f949707b4e3c37cd86cb44b0b98643e8
- Upstream version: 2.5.1
- Kind: skills
- Eligibility: upstream presents skills/taste-skill as an installable skill and ships its own marketplace.json (unpinned, default branch)
- Source: github (inline manifest, skills ./skills/taste-skill, strict false)
- Reviewed on: 2026-11-11 (update from 2.1.5 reviewed 2026-10-29)
- Reviewer: Claude (thread "Opieka nad repo FrameCore", research intake Phase C)
- Owner approval: "yes" from Kamil on 2026-11-11 for 2.5.1 with its Stop hook ("TasteSkill: update to 2.5.1, Stop hook approved, still run the Toolbox review and isolated install test", recorded in the Studio implementation handover); earlier "yes" on 2026-10-29 for 2.1.5

## What it is

One skill, `design-taste-frontend`, for professional company websites (figma.com and x.ai as the stated bar): researched art direction, real photographs or licensed stand-ins, icon sets, effects kept for tech and gaming pages, and a checker plus a finish gate that inspect the built page in a real browser. 2.5.1 (about 39 MB of skill files) adds the finish gate `scripts/gate.mjs` and declares it as a Stop hook in SKILL.md.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, landing pages and app screens (previously Studio's recommended extension `taste-skill`) | Researched art direction and a real-browser check beyond Studio's restated craft rules; 2.5.1 adds an automatic finish gate on the built page | Studio review 2026-10-26 at 12af471; 2.5.1 source review 2026-11-11; install result below; invocation and gate on a real page NOT_RUN |

Moved from Creative Studio's recommended-extension registry to Toolbox by owner decision 2026-10-29: Toolbox becomes the single source of installable recommendations and Studio points here.

## Files reviewed

2.5.1: upstream cloned as data at f6b7657 into a temporary folder; no scripts, hooks or installers were run. Read: .claude-plugin/marketplace.json, SKILL.md front matter (hook), scripts/gate.mjs (process, write and network calls), scripts/icons.mjs and scripts/photos.mjs (download hosts and pins), a host inventory of all scripts, LICENSE; diff against 12af471 (1,664 files changed). 2.1.5 review at 12af471 as before.

## What it installs and writes

The plugin cache (about 39 MB for the skill folder). Pages and images the user asks for, in the project; the checker and gate write `.taste-skill/` (build.json, reports, Chrome profiles `chrome-*`) in the project, or a temporary folder for profiles; an icon cache in the system temporary folder.

## Hooks

One, declared in the skill's front matter (active only while the skill is loaded in Claude Code): `Stop`, a shell command that finds `scripts/gate.mjs` in the skill or plugin folder and runs `node gate.mjs --hook claude`, timeout 600 s, always exiting 0. The gate checks the page built in this session in a local headless Chrome (spawning `copy-lint.mjs` and a watchdog) and writes its results to `.taste-skill/`; when the gate is missing it writes `.taste-skill/gate-hook-missing.txt`. The owner approved this hook on 2026-11-11.

## Network traffic

Only when the skill searches pictures or icons: Wikimedia Commons and other open collections, Lorem Picsum; icon data at pinned versions (gilbarbara/logos at a commit, @iconify-json/vscode-icons 1.2.30, @iconify-json/lucide 1.2.100, simple-icons 16.30.0); fonts from Google Fonts and scripts from jsDelivr in generated pages. The gate and checkers talk only to the local Chrome (127.0.0.1). No unpinned code install found.

## Changes to prompts or tool results

The skill loads by description on front-end design tasks.

## Data sent outside

Image search queries go to the open collections above when the skill searches; no telemetry found.

## Requirements

Node 22 or newer and Chrome, Edge or Chromium (ffmpeg optional).

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-11-11 for 2.5.1 (Claude Code 2.1.318): `claude plugin marketplace add` of this repository, `claude plugin install taste-skill@framecore-works-toolbox` succeeded, `claude plugin list` showed 2.5.1 enabled (cache 40 MB, SKILL.md present); a headless session and the Stop hook were NOT_RUN. Earlier: PASS 2026-10-29 in an isolated CLAUDE_CONFIG_DIR: `claude plugin marketplace add` of this repository, `claude plugin install taste-skill@framecore-works-toolbox` succeeded, `claude plugin list` showed it enabled, and a headless `claude -p` session listed its skills (`taste-skill:taste-skill`).
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Found images keep their own licences (CC BY-SA adaptations stay BY-SA). 2. Its site records describe real sites: never rebuild a named site for a client. 3. The Stop hook adds up to 600 s at the end of a turn while the skill is loaded and writes `.taste-skill/` into the project.

## Verdict

accept (2.5.1 with its Stop hook, owner-approved 2026-11-11).

## History

- 2026-10-29: added at 12af471, moved from Creative Studio's recommended extensions.
- 2026-11-11: updated to 2.5.1 at f6b7657 (finish gate as a Stop hook, owner-approved).
