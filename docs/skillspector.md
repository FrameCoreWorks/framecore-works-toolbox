# skillspector: install notes

- Upstream: https://github.com/NVIDIA/SkillSpector
- Pinned commit: d7338f58200a9ae2a24810cee08911ab68b107a7 (version 2.12.0)
- Review: [reviews/skillspector.md](../reviews/skillspector.md)

## Install

See [install.md](install.md). Plugin id: `skillspector@framecore-works-toolbox`.

## Setup after install

The `skillspector` CLI: `uv tool install git+https://github.com/NVIDIA/SkillSpector@d7338f58200a9ae2a24810cee08911ab68b107a7` (Python 3). Without it the skill does a manual review.

## What works where

Claude Code and Cowork (CLI); chat: manual review only.

## Use

Ask whether a skill or repo is safe to install.

Watch out: install the `skillspector` CLI at the pinned commit (see docs).

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall skillspector@framecore-works-toolbox`. Delete files it created in your projects if you no longer need them.
