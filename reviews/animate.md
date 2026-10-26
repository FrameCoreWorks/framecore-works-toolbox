# Review: animate

## Entry

- Name: animate
- Status: active
- Upstream: https://github.com/cth9191/animate
- Author: cth9191 (GitHub user)
- License: MIT
- Commit: 7e5eb56feb2dd573f890e1b7b34748af43d58263
- Upstream version: 0.4.0 (`plugins/animate/.claude-plugin/plugin.json`)
- Kind: plugin
- Eligibility: upstream ships `plugins/animate/.claude-plugin/plugin.json` and its own `.claude-plugin/marketplace.json`
- Source: git-subdir (path `plugins/animate`)
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks, no MCP servers; the optional ElevenLabs voice goes through the user's own Claude connector)

GitHub metadata at review time: 983 stars, 136 forks, created 2026-10-04,
last commit 2026-10-05.

## What it is

One skill, `animate`, that makes short procedural animations (explainers,
histories, product reels, small stories) as single-file canvas videos with a
synthesized score, rendered to MP4. Seven built-in styles (cut paper,
crosshatch, riso, sketchbook, math, pixel, isometric) or a new style from the
user's references. Works through intake, then story, look and storyboard
check-ins, then a measured build. Ships Node and Python helper scripts under
`skills/animate/tools/`, templates, examples and style kits. No commands,
agents, hooks or MCP servers.

## Files reviewed

`.claude-plugin/marketplace.json`, `plugins/animate/.claude-plugin/plugin.json`,
`plugins/animate/skills/animate/SKILL.md` (header and requirements),
`README.md`, `LICENSE`, and a scan of every `.mjs`, `.js`, `.py` and `.html`
file under `plugins/animate/skills/animate/` for network calls, process
execution, environment variables and writes outside the project. Repo cloned
as data at the pinned commit; nothing was run.

## What it installs and writes

- Install: only `plugins/animate/` is copied into the plugin cache
  (git-subdir). No install scripts.
- At use: Claude runs the helper scripts with Node, which write the piece
  (sources, frames, renders, logs) into the piece folder in the user's
  project. No writes to the home directory found.
- The skill tells the user to install missing tools themselves
  (`npm i -g playwright && npx playwright install chromium`, ffmpeg,
  optionally `pip install faster-whisper`); it stops instead of installing.

## Hooks

None.

## Network traffic

- No URLs or HTTP calls in the scripts (scan found none besides SVG
  namespaces).
- Optional voice-over: the skill asks Claude to use the ElevenLabs connector
  if the user has connected it; that traffic goes through the user's
  connector, not through this plugin.
- Inference, not verified: `faster-whisper` (optional) downloads its speech
  model from Hugging Face on first use.

## Changes to prompts or tool results

None beyond the skill's own instructions when it is loaded.

## Data sent outside

Nothing by the plugin itself. Script text for a voice-over goes to
ElevenLabs only if the user chooses that connector.

## Requirements

Node 18+, Playwright with Chromium, ffmpeg and ffprobe on PATH; optionally
Python with `faster-whisper`. Local text-to-speech fallback uses `say`
(macOS), PowerShell (Windows) or `espeak` (Linux). Rendering needs a machine
that can run these: Claude Code or Cowork. In claude.ai chat the skill loads,
but rendering there is Unknown (depends on the code-execution sandbox having
Playwright and ffmpeg).

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR, Claude Code 2.1.310): PASS.
  `claude plugin validate .` passed; marketplace add and
  `claude plugin install animate@framecore-works-toolbox` succeeded;
  `claude plugin list` shows 0.4.0 enabled; `installed_plugins.json` records
  `gitCommitSha` 7e5eb56feb2dd573f890e1b7b34748af43d58263; the cache holds
  only `skills/` (git-subdir). Rendering a video was NOT_RUN. Temporary
  config dir deleted.
- claude.ai (owner, 2026-10-26): toolbox synced at c607fff, every plugin synced. No warnings for this plugin. Versions after adding the plugin: not reported yet.
- Cowork: NOT_RUN

## Risks

1. Runs local scripts through Claude's shell (Node, ffmpeg, headless
   Chromium) with the user's permissions; review prompts as usual.
2. Young project (created 2026-10-04, single author); pinned by commit, every
   update needs a new review.
3. Heavy prerequisites (Playwright Chromium, ffmpeg) the user installs
   globally.

## Verdict

Accept: a self-contained creative plugin with no hooks, no MCP and no
external service of its own.

## History

- 2026-10-26: reviewed at 7e5eb56 (version 0.4.0).
- 2026-10-26: added after the owner's "Tak, dodaj animate".
