# pixelfx: install notes

- Upstream: https://github.com/patch-gg/pixelfx
- Pinned commit: a84159688af3ca37a4be05a0d422b94451b2e24e (version 0.3.0)
- Wrapper: [plugins/pixelfx](../plugins/pixelfx/) (our own skill; checks out the upstream at the pinned commit)
- Review: [reviews/pixelfx.md](../reviews/pixelfx.md)

## Install

See [install.md](install.md). Plugin id: `pixelfx@framecore-works-toolbox`.

## Setup after install

None up front. On first use the skill asks once, then clones pixelfx (about 40 MB) into `pixelfx/` in the project at the pinned commit. It needs git and Node.js 18+; ffmpeg only for GIF and MP4.

## What works where

Chat: skill only (no code execution, so no renders). Cowork and Claude Code: skill plus renders, sprite sheets and checks. Codex and ChatGPT Work: the wrapper has a skill folder, so it can be saved as a private plugin; renders need code execution with access to github.com (NOT_RUN).

## Use

Ask for a pixel effect ("a frost nova for my mage", "a coin pickup sparkle"), a recolor, a sprite sheet for Godot, Unity or Phaser, or a GIF/MP4 of an effect for a video.

## Watch out

The Patch Pixel font in `gallery/fonts` is not MIT; never ship it. Never move the checkout off the pinned commit without a new review.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall pixelfx@framecore-works-toolbox`, and delete the project's `pixelfx/` folder.
