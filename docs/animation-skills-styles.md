# animation-skills-styles

Reel style pack built into the Toolbox plugin since 1.14.0: MIT copy of
[artemnovitckii/claude-animation-skills](https://github.com/artemnovitckii/claude-animation-skills) at commit `5dbea55c23aa6a5c93dc3cfb5583840513b56b94`, by Artem Novitckii.

- Files: `plugins/toolbox/capabilities/reel-styles/animation-skills-styles/` (`UPSTREAM.md`, `SHA256SUMS`, `upstream/`)
- Instructions: `plugins/toolbox/skills/toolbox/references/reel-styles.md`
- Review: [reviews/animation-skills-styles.md](../reviews/animation-skills-styles.md)

## Install

There is no separate plugin. Install or update Toolbox (see [install.md](install.md),
[CHATGPT_INSTALL.md](../CHATGPT_INSTALL.md), [CODEX_INSTALL.md](../CODEX_INSTALL.md));
the pack comes with it.

## Setup after install

None for the style files. Engines: copy the pack folder into the project and run `bash kit/setup.sh` there only after the user's yes (locked npm packages, Chromium, GSAP 3.12.5, HyperFrames 0.8.34).

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
