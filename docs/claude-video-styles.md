# claude-video-styles

Reel style pack built into the Toolbox plugin since 1.14.0: MIT copy of
[ItsssssJack/claude-video-2](https://github.com/ItsssssJack/claude-video-2) at commit `18891e4996abb7ccc0085f2d43cef2fd7eff1dc8`, by Claude Video Studio contributors (ItsssssJack).

- Files: `plugins/toolbox/capabilities/reel-styles/claude-video-styles/` (`UPSTREAM.md`, `SHA256SUMS`, `upstream/`)
- Instructions: `plugins/toolbox/skills/toolbox/references/reel-styles.md`
- Review: [reviews/claude-video-styles.md](../reviews/claude-video-styles.md)

## Install

There is no separate plugin. Install or update Toolbox (see [install.md](install.md),
[CHATGPT_INSTALL.md](../CHATGPT_INSTALL.md), [CODEX_INSTALL.md](../CODEX_INSTALL.md));
the pack comes with it.

## Setup after install

None for the style files. Renders use the host's own HyperFrames or Remotion route.

## What works where

| Host | Status |
| --- | --- |
| Claude Code (desktop, cloud, phone) | files ship with Toolbox; style reading and render on the host route |
| Claude apps / Cowork | files ship with Toolbox; render Unknown in chat |
| ChatGPT Work | files ship in the Toolbox package; activation NOT_RUN |
| Codex | files ship in the Toolbox package; activation NOT_RUN |

## Use

Ask Toolbox or Creative Studio for a reel style ("swiss-grid", "karaoke captions",
"whiteboard explainer"); see the reference for the full list.

## Full removal

Remove or downgrade Toolbox below 1.14.0. Nothing is installed elsewhere, except
packages a user approved for the animation engines inside their own project.
