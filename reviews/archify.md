# Review: archify

## Entry

- Name: archify
- Status: active
- Upstream: https://github.com/tt-a1i/archify
- Author: GitHub owner `tt-a1i`
- License: Apache-2.0
- Commit: 81c6be8d87090670c45d08a8f97f9d29c5af0bec
- Upstream version: 3.2
- Kind: skills
- Eligibility: upstream documents `archify/SKILL.md` as an installable skill (`npx skills add tt-a1i/archify`); entry declares `skills: ["./archify"]`
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks, no external services of its own); covered anyway by: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 89577 stars, created 2026-04-15, last commit 2026-10-25.

## What it is

Turns an idea, plan or codebase into validated interactive diagrams (architecture, workflow, sequence, ERD, timeline...) as standalone HTML with export to image, SVG or WebM.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Diagram HTML files in your project.

## Hooks

None.

## Network traffic

`scripts/check-update.mjs` fetches an update manifest when the skill runs its update check.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

An update-check request; nothing about your project.

## Requirements

Node for its scripts; a browser to view the HTML.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Whole repo (incl. a 'archify.zip' and site files) is copied into the plugin cache; only `archify/` is loaded as a skill.

## Verdict

Accept: Interactive architecture, flow, sequence and ERD diagrams from an idea or a codebase, as standalone HTML.

## History

- 2026-10-26: added at 81c6be8 (version 3.2) from the researched shortlist.
