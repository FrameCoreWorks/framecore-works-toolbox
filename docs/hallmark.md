# hallmark: install notes

- Upstream: https://github.com/Nutlope/hallmark
- Pinned commit: 7ec868225c6caa040558c321ee0fefa0e73f83a8 (version 2.0.0)
- Review: [reviews/hallmark.md](../reviews/hallmark.md)

## Install

See [install.md](install.md). Plugin id: `hallmark@framecore-works-toolbox`.

## Setup after install

Optional: a local Chrome for screenshot checks; `TOGETHER_API_KEY` only for generated images.

## What works where

| Component | Chat | Cowork | Claude Code |
| --------- | ---- | ------ | ----------- |
| Skill `hallmark` | yes | yes | yes |
| Scripts (lint, screenshots, Together images) | Unknown | yes | yes |

## Use

claude.ai warns that the skill description contains angle brackets and stores it without them; only the example `<path>` is lost, so it still loads the same way.


Describe the page or redesign, or `/hallmark:hallmark`.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall hallmark@framecore-works-toolbox`. If you ran `install-hook.mjs`, remove its PostToolUse entry from `.claude/settings.json` (or `~/.claude/settings.json`).
