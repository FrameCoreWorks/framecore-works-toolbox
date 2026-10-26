# Review: sepia

## Entry

- Name: sepia
- Status: active
- Upstream: https://github.com/Nanako0129/sepia
- Author: GitHub owner `Nanako0129`
- License: MIT
- Commit: fb06be76abeae7dd606960a32f2b10c1d1798e0d
- Upstream version: 0.12.4
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own marketplace
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks, no external services of its own); covered anyway by: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 3489 stars, created 2026-08-28, last commit 2026-10-15.

## What it is

Six writing skills that remove AI patterns from prose: narrative-architecture repair for fiction and venue-matched rules for professional text.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Nothing outside the edited text.

## Hooks

None.

## Network traffic

None found.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

Nothing.

## Requirements

None.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Overlaps with the Humanizer skill in the FrameCore Creative Studio.

## Verdict

Accept: Removes AI patterns from fiction and professional prose without changing what it says.

## History

- 2026-10-26: added at fb06be7 (version 0.12.4) from the researched shortlist.
