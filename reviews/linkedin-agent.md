# Review: linkedin-agent

## Entry

- Name: linkedin-agent
- Status: active
- Upstream: https://github.com/Jakeschincariol/linkedin-agent-skill
- Author: GitHub owner `Jakeschincariol`
- License: MIT
- Commit: add2c23882fe79180737d242ff80a5da205eda6a
- Upstream version: 1.0.0
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own marketplace
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks, no external services of its own); covered anyway by: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 2706 stars, created 2026-09-07, last commit 2026-09-07.

## What it is

Eleven skills for running a LinkedIn account: posts from hook formulas, comments, replies, profile score, weekly plan and a humanizer.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Drafts in your project.

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

1. No updates since creation.

## Verdict

Accept: LinkedIn content: posts, comments, replies, profile score and a weekly plan.

## History

- 2026-10-26: added at add2c23 (version 1.0.0) from the researched shortlist.
