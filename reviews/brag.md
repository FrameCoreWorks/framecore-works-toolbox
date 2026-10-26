# Review: brag

## Entry

- Name: brag
- Status: active
- Upstream: https://github.com/latent-spaces/brag
- Author: GitHub owner `latent-spaces`
- License: MIT
- Commit: 669ab9286aa28b6c3ee30e75f181ee74319d012a
- Upstream version: 0.5.0
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own marketplace
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks, no external services of its own); covered anyway by: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 18729 stars, created 2026-06-16, last commit 2026-10-24.

## What it is

Two skills that turn the project you just built into a short shareable launch video with one command (HyperFrames-based).

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Video files in your project.

## Hooks

None.

## Network traffic

None found in the scripts.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

Nothing found.

## Requirements

Node; HyperFrames tooling for rendering.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Overlaps with motion-designer and the official hyperframes plugin.

## Verdict

Accept: Turns the project you just built into a short launch video with one command.

## History

- 2026-10-26: added at 669ab92 (version 0.5.0) from the researched shortlist.
