# Review: blender-agent-skills

## Entry

- Name: blender-agent-skills
- Status: removed
- Upstream: https://github.com/EL4CTEO/blender-skills
- Author: GitHub owner `EL4CTEO`
- License: MIT
- Commit: 71d031dab8bc6729504d11a78cbe91945401045f
- Upstream version: 1.1.0
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own marketplace
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks, no external services of its own); covered anyway by: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 520 stars, created 2026-10-14, last commit 2026-10-16.

## What it is

22 Blender 5.2 workflow skills: modeling, UVs, PBR, baking, rigging, animation, export and QA, with a helper that runs Python inside Blender.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Blender files and exports in your project; `install/install.sh` (manual) copies skills into agent folders, not needed with the plugin.

## Hooks

None.

## Network traffic

None found.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

Nothing.

## Requirements

Blender 5.2 installed locally.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Very young repo (created 2026-10-14).
2. Runs Python inside Blender with your permissions.

## Verdict

Accept: Blender 5.2 workflows for 3D: modeling, UVs, PBR, rigging, animation and export.

## History

- 2026-10-26: added at 71d031d (version 1.1.0) from the researched shortlist.
- 2026-10-31: removed by owner decision: Toolbox keeps only entries that install without accounts, API keys or separate desktop apps; it needs the Blender desktop app installed.
