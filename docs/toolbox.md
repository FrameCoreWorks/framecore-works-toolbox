# toolbox: install notes

First-party plugin written in this repo (`plugins/toolbox/`). No upstream, no
hooks, no scripts, no network. One skill, `toolbox`, that lists the plugins in
this marketplace.

## Install

See [install.md](install.md). Plugin id: `toolbox@framecore-works-toolbox`.

## What works where

| Component | Chat | Cowork | Claude Code |
| --------- | ---- | ------ | ----------- |
| Skill `toolbox` | yes | yes | yes |

## Use

Type `toolbox` (or `/toolbox:toolbox`). It shows every plugin in the
toolbox grouped by category (Creative, Dev tools, Marketing & growth), with a one-line purpose,
where it works, and how to add and use it. `toolbox creative` shows one
category. It does not say which
plugins you have installed (Claude cannot see that reliably); check
Customize > Plugins, "From marketplaces you added".

Tested 2026-10-26 in Claude Code with another studio plugin installed:
`toolbox` and `co jest w toolboxie?` both opened this skill.
claude.ai (owner, 2026-10-26, synced at bc04b13): works once the toolbox
plugin itself is added in Customize > Plugins; adding the marketplace alone
does not add it, and without it Claude lists its own tools instead.

If another plugin answers instead (for example a studio menu), call it
explicitly with `/toolbox:toolbox`.

## Maintenance

Every entry added to or removed from `.claude-plugin/marketplace.json` must be
added to or removed from the catalog table in
`plugins/toolbox/skills/toolbox/SKILL.md` in the same commit.
`scripts/check_marketplace.py` fails when they differ. The plugin sets no
`version`, so no stale version string holds back updates; after a toolbox
change, use Check for updates in claude.ai or
`claude plugin update toolbox@framecore-works-toolbox`.

## Full removal

Remove it in Customize > Plugins, or run
`claude plugin uninstall toolbox@framecore-works-toolbox`. It leaves no files.
