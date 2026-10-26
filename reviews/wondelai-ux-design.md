# Review: wondelai-ux-design

## Entry

- Name: wondelai-ux-design
- Status: active
- Upstream: https://github.com/wondelai/skills
- Author: GitHub owner `wondelai`
- License: MIT
- Commit: c172996495bed0fcd26896a9416b2093fd7073f0
- Upstream version: 1.8.0
- Kind: skills
- Eligibility: upstream marketplace `wondelai-skills` publishes plugin `ux-design` as a skills list at the repo root; this entry reproduces it (`skills` list copied from the upstream entry)
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks, no external services of its own); covered anyway by: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 2508 stars, created 2026-01-29, last commit 2026-09-10.

## What it is

Wondel.ai plugin `ux-design`: UX and UI design skills including Refactoring UI, iOS HIG design, usability heuristics, habit-forming product design, behavior design for retention, web typography, award-winning top-design, Steve Jobs-style design reviews, and Don Norman's foundational design principles Skills: refactoring-ui, ios-hig-design, ux-heuristics, hooked-ux, improve-retention, web-typography, top-design, design-everyday-things, lean-ux, microinteractions, steve-jobs-design-review.

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

None.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai (owner, 2026-10-26): skipped at sync of 03fa287 ("requires .claude-plugin/plugin.json ... set strict: false"). Fixed by adding `"strict": false` to the entry; re-sync result NOT_RUN. Claude Code re-install with strict false: PASS, skill count matches the `skills` list.
- Cowork: NOT_RUN

## Risks

1. Book-based frameworks; paraphrased guidance, not the books themselves.

## Verdict

Accept: UX and UI design skills.

## History

- 2026-10-26: added at c172996 (version 1.8.0) from the researched shortlist.
