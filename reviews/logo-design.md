# Review: logo-design

## Entry

- Name: logo-design
- Status: active
- Upstream: https://github.com/kaankiziltug/logo-design-skill
- Author: Kaan Kızıltuğ (GitHub user kaankiziltug)
- License: MIT
- Commit: 734090317a2155c5bf1ae8bd4cc85c6848a0128f
- Upstream version: 1.4.5
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own `.claude-plugin/marketplace.json`
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks, MCP or network)

GitHub metadata at review time: 4637 stars, 353 forks, created 2026-09-26, last commit 2026-10-20.

## What it is

One skill, `logo-design`, for designing, critiquing and delivering logos: brief, concepts, geometric SVG construction, optical refinement, colour, typography, testing, presentation and brand guidelines, with a searchable library of 1,400+ classified SVG logos. Ships dependency-free Python 3 scripts (SVG audit, PNG render and similar) under `skills/logo-design/scripts/`. No commands, agents, hooks or MCP servers. `TRADEMARKS.md` covers the logo library.

## Files reviewed

`.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `skills/logo-design/SKILL.md` (header and script usage), `skills/logo-design/scripts/render_png.py` (imports), `README.md`, and a scan of all code for URLs, process execution, environment variables and home-directory writes (none found besides local process calls). Repo cloned as data at the pinned commit; nothing was run.

## What it installs and writes

- Install: the whole repo (1,560 files, mostly the SVG library) is copied into the plugin cache.
- At use: SVG and PNG files in the user's project.

## Hooks

None.

## Network traffic

None found.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions or MCP tools when they are used.

## Data sent outside

Nothing.

## Requirements

python3 for the scripts (standard library only); a local SVG renderer may be needed for PNG export (Unknown which; `render_png.py` probes for one).

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code 2.1.310): marketplace add and `claude plugin install logo-design@framecore-works-toolbox` succeeded; `installed_plugins.json` records gitCommitSha 734090317a2155c5bf1ae8bd4cc85c6848a0128f. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai (owner, 2026-10-26): toolbox synced at c607fff, every plugin synced. No warnings for this plugin. Versions after adding the plugin: not reported yet.
- Cowork: NOT_RUN

## Risks

1. The SVG reference library contains third-party trademarks (see upstream `TRADEMARKS.md`); use them as references, not in deliverables.
2. Large cache footprint (1,560 files).

## Verdict

Accept: local skill with no hooks, MCP or network.

## History

- 2026-10-26: added at 7340903 (version 1.4.5) under the owner's blanket approval for the shortlist.
