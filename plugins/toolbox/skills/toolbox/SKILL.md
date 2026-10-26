---
name: toolbox
description: >
  Lists the plugins in the FrameCore Works toolbox (Kamil's private Claude
  marketplace FrameCoreWorks/framecore-works-toolbox). Use when the user types
  "toolbox", "/toolbox", "show toolbox", "co jest w toolboxie", "lista
  toolbox", or asks which extra plugins or skills the toolbox has. Not for
  creative production work.
---

# Toolbox

Show the catalog below. Do not start any other workflow or menu.

## Reply format

1. One line: "FrameCore Works Toolbox: <N> plugins."
2. The catalog table below, as it is. Do not claim whether a plugin is
   installed; you cannot see that reliably.
3. One line on how to add a plugin: claude.ai, desktop and Cowork:
   Customize > Plugins > Discover, search the name, Add; Claude Code:
   `claude plugin install <name>@framecore-works-toolbox`. Installed plugins
   are listed in Customize > Plugins under "From marketplaces you added".
4. One line on how to use a plugin: describe the task, or type `/` and pick
   `<plugin>:<skill>`.
5. Stop there. Only if the user asks about one plugin, give its "Use" and
   "Watch out" notes from the details below and the link to its review.

Answer in the user's language. Keep it short.

## Catalog

| Plugin | What it does | Works in | Review |
| ------ | ------------ | -------- | ------ |
| `ponytail` | Lazy senior dev mode: smallest correct change, YAGNI, stdlib first; code review, repo audit, shortcut ledger | Chat: skills. Cowork and Claude Code: skills plus always-on hooks. Claude Code: plus band mod | https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/ponytail.md |

## Details

### ponytail

- Use: coding tasks pick it up by description; `/ponytail:ponytail-review`,
  `/ponytail:ponytail-audit`, `/ponytail:ponytail-debt`; levels with
  `/ponytail lite|full|ultra|off`.
- Watch out: in Cowork and Claude Code its hooks inject the ruleset into
  every session and subagent, also in creative work; turn it off there with
  `/ponytail off`, or make it on-demand with `PONYTAIL_DEFAULT_MODE=off`
  (see the plugin's docs in the toolbox repo). Keep the `webhookUrl` option
  empty.
