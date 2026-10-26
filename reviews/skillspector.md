# Review: skillspector

## Entry

- Name: skillspector
- Status: removed
- Upstream: https://github.com/NVIDIA/SkillSpector
- Author: GitHub owner `NVIDIA`
- License: Apache-2.0
- Commit: d7338f58200a9ae2a24810cee08911ab68b107a7
- Upstream version: 2.12.0
- Kind: adapted
- Eligibility: adapted: manifest-only entry exposing the upstream skill `skills/skill-inspector`; the `skillspector` CLI is installed by the user at the reviewed commit
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 21777 stars, created 2026-03-21, last commit 2026-10-22.

## What it is

NVIDIA's security scanner for agent skills. The upstream skill `skill-inspector` reviews a skill or plugin before install: static SkillSpector scan plus source-aware review, verdict APPROVE/CAUTION/REJECT. The upstream repo has no Claude manifest; this entry is itself the manifest and loads that skill.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Scan reports where you ask.

## Hooks

None.

## Network traffic

The CLI queries OSV.dev for known vulnerabilities (offline fallback). Optional LLM analysis only when asked (the skill keeps `--no-llm`).

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

Package names to OSV.dev when scanning; nothing else unless you enable LLM analysis.

## Requirements

The `skillspector` CLI: `uv tool install git+https://github.com/NVIDIA/SkillSpector@d7338f58200a9ae2a24810cee08911ab68b107a7` (Python 3). Without it the skill does a manual review.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. The CLI is a separate install; keep it at the reviewed commit.

## Verdict

Accept: Security review of a skill or plugin before you install it (NVIDIA SkillSpector scan plus source review).

## History

- 2026-10-26: added at d7338f5 (version 2.12.0) from the researched shortlist.
- 2026-10-26: removed; owner chose to drop it: the full scan needs a separate CLI install (fails the first-install rule) and toolbox reviews already cover pre-install checks.
