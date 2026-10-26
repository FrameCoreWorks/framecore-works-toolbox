# Review: compound-engineering

## Entry

- Name: compound-engineering
- Status: removed
- Upstream: https://github.com/EveryInc/compound-engineering-plugin
- Author: GitHub owner `EveryInc`
- License: MIT
- Commit: 9f5b16fc617fb5bf4817c8f42537b626c17abd05
- Upstream version: 3.32.2
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own marketplace
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 25721 stars, created 2025-10-09, last commit 2026-10-25.

## What it is

Every's compound engineering method: 43 skills and agents for planning, working, reviewing and compounding lessons into the codebase.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Plans, reviews and learnings in your project.

## Hooks

None at plugin level (hook files only in test fixtures).

## Network traffic

Optional cross-model review through OpenAI (`OPENAI_API_KEY`); references the Context7 MCP; one setup skill can install Bun with `curl | bash`.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

With `OPENAI_API_KEY` and cross-model review: documents or code under review go to OpenAI.

## Requirements

Git; optional Bun, OpenAI key.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Large (1,558 files) and overlaps heavily with Superpowers.
2. Optional OpenAI review sends code outside (approved).

## Verdict

Accept with conditions: Every's compound engineering workflow: plan, build, review and turn lessons into reusable rules.

## History

- 2026-10-26: added at 9f5b16f (version 3.32.2) from the researched shortlist.
- 2026-10-26: removed; owner chose to drop it: overlaps Superpowers, which the owner already uses; large dev-team workflow with low fit for the studio.
