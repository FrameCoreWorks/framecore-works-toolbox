# Review: lemo-opuscar

## Entry

- Name: lemo-opuscar
- Status: rejected
- Upstream: https://github.com/lemomo-ai/lemo-opuscar
- Author: Lemomo (LemoLab)
- License: MIT
- Commit: 9eb7739a0fca4c6990fe966cb8b87b1930f7193a
- Upstream version: none
- Kind: plugin
- Eligibility: upstream ships .claude-plugin/marketplace.json (marketplace "lemolab") with the plugin in ./plugin
- Source: none (not listed)
- Reviewed on: 2026-11-11
- Reviewer: Claude (thread "Opieka nad repo FrameCore", research intake Phase C, re-review at the moved HEAD)
- Owner approval: not required (rejected at the reject gate)

## What it is

A film-making skill from LemoLab: the agent directs, draws, scores and mixes a film in one of the library's code-rendered styles. Creative Studio already adapted LemoLab's styles in its own words as the 66-look film-style library (Studio 1.167.0).

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, styled code-rendered films | None beyond the existing film-style library | Not admitted; nothing run |

## Files reviewed

README.md (install), .claude-plugin/marketplace.json, plugin/skills/lemo-opuscar/SKILL.md (setup step), plugin/skills/lemo-opuscar/scripts/setup.sh (git operations), LICENSE; read through raw GitHub at the commit above. Nothing was cloned or run.

## What it installs and writes

The plugin installs from its marketplace. On first use, `scripts/setup.sh` makes a sparse clone of the upstream **main branch** into `~/lemo-opuscar` (or `$LEMO_OPUSCAR_HOME`) and updates it on later runs; the README says the library "updates itself on the next film". Film projects go in the current folder.

## Hooks

None found in the reviewed files.

## Network traffic

GitHub at install and at every setup run (clone or update of the main branch). `tools/fetch.sh` downloads big assets on demand (not reviewed).

## Changes to prompts or tool results

None found beyond the skill itself.

## Data sent outside

None found.

## Requirements

Node 20+, ffmpeg 7+, Python 3.11+ or uv; "the agent installs the rest" (README).

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): NOT_RUN (rejected at the gate)
- claude.ai / Cowork (Customize > Plugins): NOT_RUN

## Risks

1. Clones and updates unpinned code (main branch) at run time, outside the project, in the home folder.
2. Further dependencies installed by the agent, unpinned.

## Verdict

reject: clones and updates the unpinned main branch into ~/lemo-opuscar at run time (reject gate). Studio keeps its own-words film-style library.

## History

- 2026-11-11: re-reviewed at 9eb7739 (HEAD moved since the Studio handover review); rejected.
