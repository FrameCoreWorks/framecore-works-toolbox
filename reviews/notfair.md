# Review: notfair

## Entry

- Name: notfair
- Status: active
- Upstream: https://github.com/nowork-studio/notfair-plugin
- Author: GitHub owner `nowork-studio`
- License: MIT
- Commit: ed835f273dce03a451c13fa0cb67305ae58ecb05
- Upstream version: 0.27.17
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own marketplace
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 4063 stars, created 2026-03-27, last commit 2026-10-19.

## What it is

SEO, GEO and paid-ads skills (Google Ads, Meta Ads) backed by the NotFair remote MCP server.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Config under its own folder via `scripts/notfair-config.sh`; reports in your project.

## Hooks

None.

## Network traffic

Remote MCP `https://notfair.co/api/mcp/notfair` (loaded by default); optional Google Cloud/Search Console, PageSpeed and Gemini APIs; an update-check script.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

Requests and ad-account data you use through the NotFair MCP go to notfair.co (approved).

## Requirements

A NotFair account for the MCP; optional Google credentials.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai (owner, 2026-10-26): synced at 03fa287 with a warning: unrecognized plugin.json keys `documentationUrl`, `icon`, `privacyPolicyUrl`, `supportUrl`, `termsOfServiceUrl` stripped (metadata only; skills and MCP unaffected).
- Cowork: NOT_RUN

## Risks

1. Remote MCP: data goes to a third-party service (approved).
2. Young company service; check its terms before connecting ad accounts.

## Verdict

Accept with conditions: SEO, GEO and Google/Meta Ads work through the NotFair service (remote MCP).

## History

- 2026-10-26: added at ed835f2 (version 0.27.17) from the researched shortlist.
