# Review: marketing-skills

## Entry

- Name: marketing-skills
- Status: active
- Upstream: https://github.com/coreyhaines31/marketingskills
- Author: GitHub owner `coreyhaines31`
- License: MIT
- Commit: e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b
- Upstream version: 2.13.0
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own marketplace
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 56615 stars, created 2026-01-15, last commit 2026-10-19.

## What it is

52 marketing skills: CRO, copywriting, SEO, email, analytics, launch and growth engineering, with optional tool integrations.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Drafts and reports in your project.

## Hooks

None.

## Network traffic

Optional integrations call many marketing APIs (Ahrefs, Semrush, Google Ads, Meta, LinkedIn, Mailchimp, HubSpot-like CRMs and more) only when you set their keys.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

Only to the services whose API keys you set.

## Requirements

Optional API keys per integration.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Many optional external integrations (approved); set only the keys you need.

## Verdict

Accept with conditions: 52 marketing skills: CRO, copywriting, SEO, email, analytics and launch.

## History

- 2026-10-26: added at e85f3cb (version 2.13.0) from the researched shortlist.
