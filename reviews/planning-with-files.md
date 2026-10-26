# Review: planning-with-files

## Entry

- Name: planning-with-files
- Status: active
- Upstream: https://github.com/OthmanAdi/planning-with-files
- Author: GitHub owner `OthmanAdi`
- License: MIT
- Commit: dcdfb278de53fdb69b2067ea173dbb1de45345a3
- Upstream version: 3.25.2
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own marketplace
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 27662 stars, created 2026-01-03, last commit 2026-10-24.

## What it is

Persistent file-based planning for long tasks: markdown plans that survive /clear and compaction, re-injected each turn, with a completion gate. 18 skills incl. translations.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Plan files in your project; session catch-up scripts read your Claude transcripts.

## Hooks

Six plugin hooks, all running `hooks/claude-hook.sh <event>` (10 s timeout; `PLANNING_DISABLED=1` turns them off): SessionStart (startup, resume, clear, compact) and UserPromptSubmit re-inject the current plan into context; PreToolUse (Write, Edit, Bash, Read, Glob, Grep) and PostToolUse (Write, Edit) remind about the plan around tool calls; PreCompact saves state before compaction; Stop runs a completion gate (`scripts/gate-stop.sh`) that can block stopping while the plan has open steps.

## Network traffic

None found.

## Changes to prompts or tool results

Yes: see Hooks.

## Data sent outside

Nothing.

## Requirements

sh, Python for helper scripts.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Six hooks change what Claude sees every turn and around tool calls, and the Stop gate can keep Claude working until the plan is done (approved). `PLANNING_DISABLED=1` turns them off.
2. Overlaps with Superpowers planning; do not run both on the same task.

## Verdict

Accept with conditions: File-based plans that survive /clear and compaction, re-injected every turn.

## History

- 2026-10-26: added at dcdfb27 (version 3.25.2) from the researched shortlist.
