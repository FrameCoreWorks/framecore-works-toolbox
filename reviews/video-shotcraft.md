# Review: video-shotcraft

## Entry

- Name: video-shotcraft
- Status: active
- Upstream: https://github.com/Vincentwei1021/video-shotcraft
- Author: GitHub owner `Vincentwei1021`
- License: Apache-2.0
- Commit: 43bd349a136651865ecfa6ea1cf012f6e957d304
- Upstream version: 1.0.0
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json`
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks, no external services of its own); covered anyway by: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 13729 stars, created 2026-07-19, last commit 2026-10-18.

## What it is

One skill for cinematic product videos built with Remotion: 152 shot recipe cards, 209 motion previews and a production template. The repo also has JianYing/CapCut draft export scripts and a promo site.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Video projects in your project folder; the JianYing export scripts write drafts into the JianYing/CapCut draft folder in your home directory when run.

## Hooks

None.

## Network traffic

Optional: posting helpers reference `api.upload-post.com` (social posting service) and the skill links to YouTube/TikTok examples. Rendering is local (Remotion).

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

Nothing by default; only if you use the upload-post helper with your own key.

## Requirements

Node and Remotion for rendering; Python with Pillow for some helpers.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Large repo (1,360 files) copied into the plugin cache.
2. Overlaps with the Remotion skill in the FrameCore Creative Studio.

## Verdict

Accept: Cinematic product and promo videos in Remotion from 152 shot recipes and a production template.

## History

- 2026-10-26: added at 43bd349 (version 1.0.0) from the researched shortlist.
