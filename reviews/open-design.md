# Review: open-design

## Entry

- Name: open-design
- Status: removed
- Upstream: https://github.com/nexu-io/open-design
- Author: nexu-io (GitHub org; latest commit by open-design-crew[bot])
- License: MIT
- Commit: 26d60298f8129e229a1c10aab4df7ca25b1e9ad3
- Upstream version: 1.0.0
- Kind: plugin
- Eligibility: upstream ships `plugins/open-design/.claude-plugin/plugin.json` and its own `.claude-plugin/marketplace.json`
- Source: git-subdir (path `plugins/open-design`)
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required for the plugin itself (one MCP server that talks to the user's own local app); installing the Open Design app is a separate decision

GitHub metadata at review time: 104052 stars, 11897 forks, created 2026-04-28, last commit 2026-10-26.

## What it is

A thin plugin: `plugins/open-design/` holds only `.claude-plugin/plugin.json` and `.mcp.json`. The MCP server runs `od mcp --daemon-url http://127.0.0.1:7456`, which connects Claude to the user's locally installed Open Design app (projects, files, previews; the app carries its own 139 skills and 150 design systems). Without the app, the plugin does nothing.

## Files reviewed

`plugins/open-design/.claude-plugin/plugin.json`, `plugins/open-design/.mcp.json`, the repo's `.claude-plugin/marketplace.json` and `README.md` (install part). The Open Design app itself (`od` CLI and daemon) was not reviewed.. Repo cloned as data at the pinned commit; nothing was run.

## What it installs and writes

- Install: only `plugins/open-design/` (2 files) is copied into the plugin cache (git-subdir).
- At use: whatever the local Open Design app does with its projects (not reviewed).

## Hooks

None.

## Network traffic

The MCP server talks to `127.0.0.1:7456` (the local daemon). What the app sends outside (for example model providers it is configured with) is Unknown: not reviewed.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions or MCP tools when they are used.

## Data sent outside

Nothing by the plugin. The app may send designs or prompts to the model providers you configure in it (Unknown).

## Requirements

The Open Design app with the `od` command on PATH and its daemon running. Works only where a local process can run: Claude Code and Cowork.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code 2.1.310): marketplace add and `claude plugin install open-design@framecore-works-toolbox` succeeded; `installed_plugins.json` records gitCommitSha 26d60298f8129e229a1c10aab4df7ca25b1e9ad3. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai (owner, 2026-10-26): toolbox synced at c607fff, every plugin synced. No warnings for this plugin. Versions after adding the plugin: not reported yet.
- Cowork: NOT_RUN

## Risks

1. Depends on a separate, large local app (13,658 files in the repo) that this review did not cover; review or trust it before installing.
2. Fast-moving upstream maintained partly by a bot; pinned by commit.

## Verdict

Accept with conditions: the plugin is two config files; install the Open Design app only if you trust it.

## History

- 2026-10-26: added at 26d6029 (version 1.0.0) under the owner's blanket approval for the shortlist.
- 2026-10-31: removed by owner decision: Toolbox keeps only entries that install without accounts, API keys or separate desktop apps; it needs the separate Open Design desktop app installed and running.
