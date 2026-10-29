# pixel-plugin: app note

- Upstream: https://github.com/willibrandon/pixel-plugin
- Pinned commit: dee350645b705916655c013f208bf5580ecb9317 (version 0.5.0)
- Review: [reviews/pixel-plugin.md](../reviews/pixel-plugin.md)

## Install in Claude Code (by hand)

claude.ai and Cowork refuse plugins with a top-level `bin/`, and this upstream
ships one, so it is an app note, not a marketplace entry: the Toolbox
marketplace does not install it. In Claude Code, clone it at the pinned commit
and add the clone as its own marketplace:

```bash
git clone https://github.com/willibrandon/pixel-plugin ~/.claude/framecore-apps/pixel-plugin
git -C ~/.claude/framecore-apps/pixel-plugin checkout dee350645b705916655c013f208bf5580ecb9317
claude plugin marketplace add ~/.claude/framecore-apps/pixel-plugin
claude plugin install pixel-plugin@pixel-plugin
```

Tested 2026-10-29 in an isolated Claude Code 2.1.312 config: the plugin
installed and was enabled at the pinned version. A newer upstream commit needs
a new review before you move the checkout.

## Setup after install

Aseprite 1.3.0 or later installed and licensed by the user (commercial, not bundled). Claude Code with local MCP (Cowork and claude.ai refuse plugins with a top-level `bin/`). `bin/pixel-mcp` is a bash launcher, so native Windows needs a bash shell (Git Bash or WSL).

## What works where

Claude Code with Aseprite; not chat or Cowork (top-level `bin/`).

## Use

Ask for a sprite, a character or a pixel animation, or run `/pixel-setup` first and then `/pixel-new`.

## Watch out

Needs Aseprite 1.3+; Claude Code only (top-level `bin/`); its MCP binaries are prebuilt and unverified.

## Full removal

`claude plugin uninstall pixel-plugin@pixel-plugin`, then `claude plugin marketplace remove pixel-plugin` and delete `~/.claude/framecore-apps/pixel-plugin`.
