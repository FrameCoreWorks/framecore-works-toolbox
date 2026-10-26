# Review: meta-ads-designer

## Entry

- Name: meta-ads-designer
- Status: active
- Upstream: https://github.com/aievolutionpl/meta-ads-designer
- Author: AI Evolution Labs / AI Evolution Polska (GitHub org aievolutionpl)
- License: MIT
- Commit: 656ce907380448389559958f055c8b43d71ab26e
- Upstream version: 6.5.0
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json`
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: yes from Kamil on 2026-10-26: "Działaj z Motion Designer i działaj z pozostałymi ... z tymi ustalonymi już je wprowadź" (blanket approval for the shortlist)

GitHub metadata at review time: 18 stars, 2 forks, created 2026-08-18, last commit 2026-09-24.

## What it is

One skill, `meta-ads-designer` (`SKILL.md` at the repo root), that researches, art-directs and generates Meta and social ads, posters and flyers with an AI image model, then analyses the result. Ships reference docs, examples and Python scripts, including `scripts/generate_fal.py` for fal.ai. No commands, agents, hooks or MCP servers.

## Files reviewed

`.claude-plugin/plugin.json`, `SKILL.md` (header and generation rules), `INSTALL.md`, `requirements.txt`, `scripts/generate_fal.py` (network part), and a scan of all code for URLs, process execution, environment variables and home-directory writes. Repo cloned as data at the pinned commit; nothing was run.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- At use: prompts and generated images in the user's project.

## Hooks

None.

## Network traffic

- `scripts/generate_fal.py` calls `https://queue.fal.run` when `FAL_KEY` is set.
- Otherwise the skill uses the host's own image tool or hands over ready prompts; with no image tool, nothing is rendered.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions or MCP tools when they are used.

## Data sent outside

With `FAL_KEY` set: ad prompts (and any reference images the script sends) go to fal.ai.

## Requirements

Python with Pillow and NumPy (`pip install -r requirements.txt`) for the scripts; a fal.ai key only for fal generation.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code 2.1.310): marketplace add and `claude plugin install meta-ads-designer@framecore-works-toolbox` succeeded; `installed_plugins.json` records gitCommitSha 656ce907380448389559958f055c8b43d71ab26e. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai (owner, 2026-10-26): toolbox synced at c607fff, every plugin synced. No warnings for this plugin. Versions after adding the plugin: not reported yet.
- Cowork: NOT_RUN

## Risks

1. Sends prompts to fal.ai when `FAL_KEY` is set (owner approved).
2. Very small project (18 stars, one org); pinned by commit.

## Verdict

Accept with conditions: external image generation only with your own fal.ai key, approved by the owner.

## History

- 2026-10-26: added at 656ce90 (version 6.5.0) under the owner's blanket approval for the shortlist.
