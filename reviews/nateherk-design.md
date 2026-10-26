# Review: nateherk-design

## Entry

- Name: nateherk-design
- Status: active
- Upstream: https://github.com/nateherkai/scroll-craft
- Author: GitHub owner `nateherkai`
- License: MIT
- Commit: 75d81f74e83692add18cd7a8a8e078b8a887a579
- Upstream version: 0.3.1
- Kind: plugin
- Eligibility: upstream ships `plugins/nateherk-design/.claude-plugin/plugin.json` listed in its own marketplace
- Source: git-subdir (path `plugins/nateherk-design`)
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 4061 stars, created 2026-08-22, last commit 2026-09-30.

## What it is

The scroll-craft skill (published as plugin `nateherk-design`) for premium, immersive scroll-driven websites: scrollytelling, typography, motion, accessibility.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: only `plugins/nateherk-design/` is copied into the plugin cache.
- Site files in your project.

## Hooks

None.

## Network traffic

Optional image generation through kie.ai (`api.kie.ai`) when `KIE_AI_API_KEY` is set.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

With `KIE_AI_API_KEY` set: image prompts go to kie.ai.

## Requirements

A web stack in your project; optional kie.ai key.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Optional external image generation (approved).

## Verdict

Accept with conditions: Builds premium scroll-driven websites (scrollytelling, motion, typography), optional kie.ai images.

## History

- 2026-10-26: added at 75d81f7 (version 0.3.1) from the researched shortlist.
