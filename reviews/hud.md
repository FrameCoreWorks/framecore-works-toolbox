# Review: hud

## Entry

- Name: hud
- Status: active
- Upstream: https://github.com/jarrodwatts/claude-hud
- Author: GitHub owner `jarrodwatts`
- License: MIT
- Commit: cf95a322afd18db045175d28962650ae7392ed77
- Upstream version: 0.13.1
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` (plugin name `claude-hud`; entry renamed because `claude-` names are reserved)
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks, no external services of its own); covered anyway by: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 28892 stars, created 2026-01-02, last commit 2026-10-26.

## What it is

A status line for Claude Code: context usage, active tools, running agents, todo progress and daily cost. Two commands (`setup`, `configure`), no skills.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Its setup command writes a `statusLine` entry into your Claude settings.

## Hooks

None (a status line command, configured by its setup command in `~/.claude/settings.json`).

## Network traffic

None found: the provider URLs in `src/stdin.ts` are only compared to detect the API provider. It reads the account block in `~/.claude.json` locally to show plan information.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

Nothing.

## Requirements

Node; Claude Code (status line).

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Edits your Claude settings when you run its setup command.

## Verdict

Accept: Status line for Claude Code: context use, active tools, agents, todos and cost.

## History

- 2026-10-26: added at cf95a32 (version 0.13.1) from the researched shortlist.
