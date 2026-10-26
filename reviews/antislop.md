# Review: antislop

## Entry

- Name: antislop
- Status: active
- Upstream: https://github.com/miqdadbadjuber/anti-slop
- Author: miqdadbadjuber (GitHub user)
- License: MIT
- Commit: 5ca57fe37c60670064abf3beae775e3dad6687a1
- Upstream version: 3.2.23
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own `.claude-plugin/marketplace.json`
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (the MCP server is local: Python standard library only, no network)

GitHub metadata at review time: 7210 stars, 490 forks, created 2026-08-07, last commit 2026-10-26.

## What it is

Six skills (`antislop`, `antislop-ui`, `antislop-copywriting`, `antislop-code`, `antislop-layoutmobile`, `antislop-human`) with rules that stop generic AI output in UI, copy and code, plus one local MCP server, `antislop-contrast`, for colour-contrast checks. The repo also ships ports for other agents and a CLI installer, not used by this entry.

## Files reviewed

`.claude-plugin/plugin.json`, `.claude-plugin/contrast-mcp-launcher.mjs`, `skills/antislop-human/contrast-mcp.py` (imports), `README.md`, and a scan of all code for URLs, process execution, environment variables and home-directory writes. Repo cloned as data at the pinned commit; nothing was run.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- At use: nothing outside the conversation; the MCP server answers contrast queries over stdio.
- The CLI under `cli/` writes skills into other agents' folders, but only when run by hand; Claude does not run it as part of the plugin.

## Hooks

None.

## Network traffic

None found. The MCP launcher starts `contrast-mcp.py` with the local Python; that script imports only `json` and `sys`.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions or MCP tools when they are used.

## Data sent outside

Nothing.

## Requirements

Python 3 for the contrast MCP server (the skills work without it). Node for the launcher.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code 2.1.310): marketplace add and `claude plugin install antislop@framecore-works-toolbox` succeeded; `installed_plugins.json` records gitCommitSha 5ca57fe37c60670064abf3beae775e3dad6687a1. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai (owner, 2026-10-26): toolbox synced at c607fff, every plugin synced. No warnings for this plugin. Versions after adding the plugin: not reported yet.
- Cowork: NOT_RUN

## Risks

1. Six rule skills can trigger on many UI, copy and code tasks; disable the plugin where they get in the way.
2. Starts a local MCP server process in Claude Code and Cowork.

## Verdict

Accept: rule skills plus a local, offline MCP server.

## History

- 2026-10-26: added at 5ca57fe (version 3.2.23) under the owner's blanket approval for the shortlist.
