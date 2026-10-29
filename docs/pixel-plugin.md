# pixel-plugin: install notes

- Upstream: https://github.com/willibrandon/pixel-plugin
- Pinned commit: dee350645b705916655c013f208bf5580ecb9317 (version 0.5.0)
- Review: [reviews/pixel-plugin.md](../reviews/pixel-plugin.md)

## Install

See [install.md](install.md). Plugin id: `pixel-plugin@framecore-works-toolbox`.

## Setup after install

Aseprite 1.3.0 or later installed and licensed by the user (commercial, not bundled). Claude Code with local MCP (Cowork and claude.ai refuse plugins with a top-level `bin/`). `bin/pixel-mcp` is a bash launcher, so native Windows needs a bash shell (Git Bash or WSL).

## What works where

Claude Code with Aseprite; not chat or Cowork (top-level `bin/`).

## Use

Ask for a sprite, a character or a pixel animation, or run `/pixel-setup` first and then `/pixel-new`.

## Watch out

Needs Aseprite 1.3+; Claude Code only (top-level `bin/`); its MCP binaries are prebuilt and unverified.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall pixel-plugin@framecore-works-toolbox`.
