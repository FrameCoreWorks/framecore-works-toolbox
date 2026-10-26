# video-shotcraft: install notes

- Upstream: https://github.com/Vincentwei1021/video-shotcraft
- Pinned commit: 43bd349a136651865ecfa6ea1cf012f6e957d304 (version 1.0.0)
- Review: [reviews/video-shotcraft.md](../reviews/video-shotcraft.md)

## Install

See [install.md](install.md). Plugin id: `video-shotcraft@framecore-works-toolbox`.

## Setup after install

Node and Remotion for rendering; Python with Pillow for some helpers.

## What works where

Claude Code and Cowork (Node, Remotion); chat: skill loads, rendering Unknown.

## Use

Describe the product video, or `/video-shotcraft:video-shotcraft`.

Watch out: needs Node and Remotion; overlaps with Studio's Remotion skill.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall video-shotcraft@framecore-works-toolbox`. Delete files it created in your projects if you no longer need them.
