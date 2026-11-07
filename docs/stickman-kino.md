# stickman-kino: install notes

- Upstream: https://github.com/dsauce/stickman-kino
- Pinned commit: d3d665301c0b62f04c885785e6bd6044de0785c6 (version 1.0.0)
- Wrapper: [plugins/stickman-kino](../plugins/stickman-kino/) (our own skill; checks out the upstream at the pinned commit)
- Review: [reviews/stickman-kino.md](../reviews/stickman-kino.md)

## Install

See [install.md](install.md). Plugin id: `stickman-kino@framecore-works-toolbox`.

## Setup after install

None up front. On first use the skill asks once, then clones stickman-kino (about 85 MB) into `stickman-kino/` in the project at the pinned commit and runs `npm ci` there. Renders need git, Node.js 18+ and Chrome or Chromium. The Kokoro voice is optional and asked separately (about 200 MB plus model files); your own recording, macOS `say`, espeak or no voice need nothing more.

## What works where

Chat: skill only (script and storyboard). Cowork and Claude Code: skill plus renders. Codex and ChatGPT Work: the wrapper has a skill folder, so it can be saved as a private plugin; renders NOT_RUN.

## Use

Ask for a stickman or stick-figure video: an explainer, a short story, a faceless YouTube or Shorts clip, or a product promo in that style.

## Watch out

Never run the upstream `stickman setup` (unpinned voice install) and never move the checkout off the pinned commit without a new review. The sample films' apps and numbers are invented.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall stickman-kino@framecore-works-toolbox`, then delete the project's `stickman-kino/` folder (it also holds the optional voice environment in `.stickman/`) and any `stickman-films/` you no longer need.
