# antislop: install notes

- Upstream: https://github.com/miqdadbadjuber/anti-slop
- Pinned commit: 5ca57fe37c60670064abf3beae775e3dad6687a1 (version 3.2.23)
- Review: [reviews/antislop.md](../reviews/antislop.md)

## Install

See [install.md](install.md). Plugin id: `antislop@framecore-works-toolbox`.

## Setup after install

Python 3 on PATH for the contrast tool.

## What works where

| Component | Chat | Cowork | Claude Code |
| --------- | ---- | ------ | ----------- |
| 6 skills | yes | yes | yes |
| MCP `antislop-contrast` (local Python) | no | yes | yes |

## Use

Loads by description on UI, copy and code work; `/antislop:antislop` for the full rule set.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall antislop@framecore-works-toolbox`. It leaves no files.
