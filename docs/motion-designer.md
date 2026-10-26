# motion-designer: install notes

- Upstream: https://github.com/kaventro/motion-designer
- Pinned commit: 7d0b8bb78ddd2c91c57db9d1e83fcf711304bdb8 (version 1.2.0)
- Review: [reviews/motion-designer.md](../reviews/motion-designer.md)

## Install

See [install.md](install.md). Plugin id: `motion-designer@framecore-works-toolbox`.

## Setup after install

On the computer that renders, let the skill run `scripts/doctor.sh` and install only what you approve. Required: node 22+, Chrome, ffmpeg, python3.

## What works where

| Component | Chat | Cowork | Claude Code |
| --------- | ---- | ------ | ----------- |
| Skill `motion-designer` (plan, brief, materials) | yes | yes | yes |
| Rendering (node, Chrome, ffmpeg, python3) | Unknown | yes, with the tools | yes, with the tools |

## Use

Describe the film ("a 20s launch film of my app, upbeat") or `/motion-designer:motion-designer`; it plans, asks for music and materials, then builds and renders.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall motion-designer@framecore-works-toolbox`. Delete `~/.cache/motion-designer/` to remove the browser profile and any voice or music engines.
