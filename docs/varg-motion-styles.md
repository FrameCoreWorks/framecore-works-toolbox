# varg-motion-styles

Reel style pack built into the Toolbox plugin since 1.14.0: MIT copy of
[vargHQ/skills](https://github.com/vargHQ/skills) at commit `ff940b67bc03a85d03f0fe33591ac59239eb8b84`, by vargai Inc. (vargHQ).

- Files: `plugins/toolbox/capabilities/reel-styles/varg-motion-styles/` (`UPSTREAM.md`, `SHA256SUMS`, `upstream/`)
- Instructions: `plugins/toolbox/skills/toolbox/references/reel-styles.md`
- Review: [reviews/varg-motion-styles.md](../reviews/varg-motion-styles.md)

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
