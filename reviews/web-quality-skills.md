# Review: web-quality-skills

## Entry

- Name: web-quality-skills
- Status: active
- Upstream: https://github.com/addyosmani/web-quality-skills
- Author: GitHub owner `addyosmani`
- License: MIT
- Commit: afa8da942115f2961fdbfa80807ea0b232ff6c00
- Upstream version: 2.0.0
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own marketplace
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks, no external services of its own); covered anyway by: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 2991 stars, created 2026-01-18, last commit 2026-08-24.

## What it is

Six skills for web quality based on Lighthouse and Core Web Vitals: performance, accessibility, SEO basics, best practices.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Nothing outside your project.

## Hooks

None.

## Network traffic

None found.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

Nothing.

## Requirements

A local site; Lighthouse when you run audits.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. None specific.

## Verdict

Accept: Web quality checks from Lighthouse and Core Web Vitals: speed, accessibility, best practices.

## History

- 2026-10-26: added at afa8da9 (version 2.0.0) from the researched shortlist.
