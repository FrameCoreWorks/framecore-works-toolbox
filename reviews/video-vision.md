# Review: video-vision

## Entry

- Name: video-vision
- Status: removed
- Upstream: https://github.com/jordanrendric/claude-video-vision
- Author: GitHub owner `jordanrendric`
- License: MIT
- Commit: 4a4f99016f249a24018cd19b66531ebbcd58024b
- Upstream version: 1.4.0
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` (plugin name `claude-video-vision`; entry renamed because `claude-` names are reserved)
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: yes from Kamil on 2026-10-26: "wprowadź wszystko" for the researched shortlist

GitHub metadata at review time: 1424 stars, created 2026-03-31, last commit 2026-10-06.

## What it is

Lets Claude watch videos: an MCP server extracts frames with ffmpeg and transcribes audio, so Claude gets frames plus a timed transcript. Useful to review renders.

## Files reviewed

Manifests (`.claude-plugin/`), README, `hooks/hooks.json` and `.mcp.json` where present, the main SKILL.md files, and a scan of all `.js`, `.mjs`, `.cjs`, `.ts`, `.py` and `.sh` files for URLs, API-key variables, install commands and home-directory writes. Repo cloned as data at the pinned commit; nothing was run. A full line-by-line code review was NOT_RUN.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache.
- Frame and audio extracts in a temporary or configured folder; backend settings saved by its configure tool.

## Hooks

None.

## Network traffic

The MCP server is started with `npx -y claude-video-vision@latest` (not pinned: the npm package can change without a new review). Audio backends: local Whisper (model download from Hugging Face), Gemini API (`GEMINI_API_KEY`) or OpenAI API (`OPENAI_API_KEY`).

## Changes to prompts or tool results

None beyond the plugin's own skill instructions, agents or MCP tools when used.

## Data sent outside

With a cloud backend: the video's audio goes to Google or OpenAI. With local Whisper: nothing.

## Requirements

Node (npx), ffmpeg; local Whisper or a Gemini/OpenAI key.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code, 2026-10-26): marketplace add and `claude plugin install` succeeded; `installed_plugins.json` gitCommitSha equals the pinned commit; `claude plugin details` lists the components described above. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. The MCP server runs the latest npm release, not the reviewed commit (approved).
2. Cloud audio backends send audio outside (approved); prefer local Whisper.

## Verdict

Accept with conditions: Lets Claude watch a video (frames plus timed transcript) to review renders and footage.

## History

- 2026-10-26: added at 4a4f990 (version 1.4.0) from the researched shortlist.
- 2026-10-26: removed. Its MCP server starts `npx -y claude-video-vision@latest` (unpinned npm code at every start), which the owner's reject gate rules out.
