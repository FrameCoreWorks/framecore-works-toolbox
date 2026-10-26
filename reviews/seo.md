# Review: seo

## Entry

- Name: seo
- Status: active
- Upstream: https://github.com/AgriciDaniel/claude-seo
- Author: GitHub owner `AgriciDaniel`
- License: MIT
- Commit: 6be93f45064ffbadced572b5d5c95f55fd263af0
- Upstream version: 2.5.0
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` (plugin name `claude-seo`; entry renamed because `claude-` names are reserved)
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 21784 stars, created 2026-02-07, last commit 2026-10-22.

## What it is

Full SEO suite: 26 sub-skills and 19 sub-agents for technical SEO, schema, E-E-A-T, GEO/AEO, local, international and e-commerce SEO, reports. The upstream marketplace also lists an optional `seo-cockpit` mod plugin, not added.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Reports in your project.

## Hooks

PostToolUse on Edit|Write: runs `hooks/validate-schema.py` locally on the edited file to check structured data.

## Network traffic

Optional Google APIs (Search Console, PageSpeed, Gemini), Bing, Moz, Matomo and other data sources with your keys; optional extensions install their own MCPs through `curl | bash` scripts you run by hand.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

Only to the services whose keys you set.

## Requirements

Python for scripts and the hook; optional API keys.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. A PostToolUse hook runs after every file edit (local validation; approved).
2. Optional extension installers use `curl | bash`; run only if needed.

## Verdict

Accept with conditions: Complete SEO toolkit: technical SEO, schema, GEO/AEO, local and e-commerce audits and reports.

## History

- 2026-10-26: added at 6be93f4 (version 2.5.0) from the researched shortlist.
