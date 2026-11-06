# gl-transitions: install notes

- Upstream: https://github.com/gl-transitions/gl-transitions
- Pinned commit: c040bddd7abf5195c0c61942982508ca9ee39287 (version 3.0.0)
- Review: [reviews/gl-transitions.md](../reviews/gl-transitions.md)

## Install

See [install.md](install.md). Plugin id: `gl-transitions@framecore-works-toolbox`.

## Setup after install

None.

## What works where

Chat: skill. Cowork and Claude Code: skill plus the user's own render tools (Node for Remotion and editly).

## Use

Ask for a transition between two images, clips or scenes, or name one (`CrossZoom`, `Cube`). The skill offers 2 or 3 candidates with preview links.

## Watch out

The skill links `gl-transitions@2` on the CDN, while npm `latest` is 3.0.0, which removed twelve duplicates; pin one exact version and take names from its `gl-transitions.json`. Credit each transition's author and licence.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall gl-transitions@framecore-works-toolbox`.
