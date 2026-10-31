# toolbox: install notes

First-party plugin written in this repo (`plugins/toolbox/`). No upstream, no
hooks, no scripts, no network. One skill, `toolbox`, that lists the plugins in
this marketplace.

## Install

See the [three-host installation overview](../INSTALL.md). The same package at
`plugins/toolbox/` carries all three manifests. Claude plugin id:
`toolbox@framecore-works-toolbox`; portable/Codex name: `toolbox`.
ChatGPT Work uses a single-plugin ZIP through Plugin Creator. Codex can use its
observed plugin route or the complete-bundle native entry helper.

The catalog is portable; each listed third-party tool needs separate host
verification. See [verification](verification.md).

## What works where

| Component | Chat | Cowork | Claude Code |
| --------- | ---- | ------ | ----------- |
| Skill `toolbox` | yes (prior owner report) | prior package support | prior CLI test |

This historical table covers Claude. The current portable source and native
Codex installer have automated checks; fresh host activation remains NOT_RUN.

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

Current inventory: 17 listed items: 16 marketplace tools and Earshot (built in), plus this index; 17 marketplace entries; no app notes (`plugins/toolbox/apps.json` is empty since 1.4.0). The owner's
admission rule accepts only tools, assets and repositories with a fully demonstrated
improvement to FrameCore repositories. New admissions and future updates document
the affected repository/task, concrete benefit and verification using the
[review template](../reviews/TEMPLATE.md); see the [rules](../CLAUDE.md).

Every entry added to or removed from `.claude-plugin/marketplace.json` must be
added to or removed from the catalog table in
`plugins/toolbox/skills/toolbox/SKILL.md` in the same commit.
Built-in capabilities from `plugins/toolbox/capabilities.json` and app notes from `plugins/toolbox/apps.json` are listed there too. An app note is a desktop app, a skill archive or a plugin with a top-level `bin/` (claude.ai and Cowork skip those on marketplace sync): it has a review (`Kind: app`, `Pin:` a full commit or `sha256:` of the archive) and docs with manual install steps, and is never a marketplace entry.
`scripts/check_marketplace.py` fails when they differ. The current catalog version is `1.5.2` (portable releases started at `1.0.0`). Keep the version and identity
synchronized across the three plugin manifests and its marketplace entry. After
a package change, rebuild its ZIP and update the existing installation using
the selected host guide. In Claude use Check for updates or
`claude plugin update toolbox@framecore-works-toolbox`.

## Full removal

Remove it through the actual host plugin controls. For the native Codex entry,
inspect its installation receipt and remove only the catalog entry and bundle.
In Claude, remove it in Customize > Plugins, or run
`claude plugin uninstall toolbox@framecore-works-toolbox`. The plugin leaves no files; an Earshot
runtime folder the user set up is separate and stays until removed on request.
