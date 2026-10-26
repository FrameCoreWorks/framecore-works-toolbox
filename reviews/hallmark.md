# Review: hallmark

## Entry

- Name: hallmark
- Status: active
- Upstream: https://github.com/Nutlope/hallmark
- Author: Nutlope (Hassan El Mghari; latest commit by Youssef)
- License: MIT
- Commit: 7ec868225c6caa040558c321ee0fefa0e73f83a8
- Upstream version: 2.0.0
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own `.claude-plugin/marketplace.json`
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: yes from Kamil on 2026-10-26: "Działaj z Motion Designer i działaj z pozostałymi ... z tymi ustalonymi już je wprowadź" (blanket approval for the shortlist)

GitHub metadata at review time: 34981 stars, 1821 forks, created 2026-04-27, last commit 2026-10-22.

## What it is

One skill, `hallmark`, for designing web pages and apps that do not look AI-generated: themes, design references, a slop linter (`sloplint`), screenshot checks and optional generated images through Together AI. Ships Node scripts under `skills/hallmark/scripts/`. The plugin declares no hooks or MCP servers; `install-hook.mjs` can add an optional PostToolUse lint hook when run by hand.

## Files reviewed

`.claude-plugin/plugin.json`, `skills/hallmark/SKILL.md` (header), `references/flow.md`, `references/imagery.md`, `references/comp.md` (API use), `scripts/install-hook.mjs`, `README.md`, and a scan of all code for URLs, process execution, environment variables and home-directory writes. Repo cloned as data at the pinned commit; nothing was run.

## What it installs and writes

- Install: the whole repo (820 files incl. `site/` and `eval/`) is copied into the plugin cache.
- At use: pages, screenshots and images in the user's project.
- Optional, only if run: `install-hook.mjs` adds a PostToolUse hook (matcher `Write|Edit|MultiEdit`, runs `lint-hook.mjs`) to the project's `.claude/settings.json`, or to `~/.claude/settings.json` with `--global`. `install.mjs` copies the skill into agent folders; not needed with the plugin.

## Hooks

None in the plugin. Optional manual hook as described above: it reports lint findings after edits.

## Network traffic

- `scripts/imagegen.mjs` / `picture.mjs` call `api.together.xyz` only when `TOGETHER_API_KEY` is set and the user asked for generated images (per `references/imagery.md` and `comp.md`).
- `api.anthropic.com`, `api.z.ai` and `api.moonshot.ai` appear only under `eval/` (the author's benchmark), not in the skill.
- Screenshot checks use a local headless browser (Puppeteer or `CHROME_PATH`).

## Changes to prompts or tool results

None beyond the plugin's own skill instructions or MCP tools when they are used.

## Data sent outside

With `TOGETHER_API_KEY` set and images requested: image prompts go to Together AI.

## Requirements

Node; a local Chrome/Chromium for screenshots; a Together AI key only for generated images.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code 2.1.310): marketplace add and `claude plugin install hallmark@framecore-works-toolbox` succeeded; `installed_plugins.json` records gitCommitSha 7ec868225c6caa040558c321ee0fefa0e73f83a8. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Sends image prompts to Together AI when its key is set (owner approved).
2. The optional hook installer edits Claude settings; run it only if you want lint-on-edit.
3. Large cache footprint (820 files).

## Verdict

Accept with conditions: Together AI only with your key; the lint hook only if installed on purpose.

## History

- 2026-10-26: added at 7ec8682 (version 2.0.0) under the owner's blanket approval for the shortlist.
