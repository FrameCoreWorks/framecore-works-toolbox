---
name: toolbox
description: >
  Lists the plugins in the FrameCore Works toolbox (Kamil's private Claude
  marketplace FrameCoreWorks/framecore-works-toolbox), grouped by category
  (Creative, Dev tools) with a one-line description of each. Use when the user
  types "toolbox", "/toolbox", "show toolbox", "co jest w toolboxie", "lista
  toolbox", or asks which extra plugins or skills the toolbox has. Not for
  creative production work.
---

# Toolbox

Show the catalog below. Do not start any other workflow or menu.

## Reply format

1. One line: "FrameCore Works Toolbox: <N> plugins in <M> categories."
2. For each category in the catalog, in order: its heading, then its table
   as it is. For a category with no rows, write "No plugins yet."
   Translate the "What it is for" text into the user's language; keep plugin
   names as they are.
3. Do not claim whether a plugin is installed; you cannot see that reliably.
4. One line on how to add a plugin: claude.ai, desktop and Cowork:
   Customize > Plugins > Discover, search the name, Add; Claude Code:
   `claude plugin install <name>@framecore-works-toolbox`. Installed plugins
   are listed in Customize > Plugins under "From marketplaces you added".
5. One line on how to use a plugin: describe the task, or type `/` and pick
   `<plugin>:<skill>`.
6. Stop there. Only if the user asks about one plugin, give its "Use" and
   "Watch out" notes from the details below and its review link.

If the user asks for one category only ("toolbox creative"), show just that
category. Answer in the user's language. Keep it short.

## Catalog

### Creative

| Plugin | What it is for | Works in |
| ------ | -------------- | -------- |

### Dev tools

| Plugin | What it is for | Works in |
| ------ | -------------- | -------- |
| `ponytail` | Keeps code changes minimal (YAGNI, stdlib first); also code review, repo audit and a list of deferred shortcuts. Use for coding work, not creative work. | Chat: skills. Cowork and Claude Code: skills plus always-on hooks. Claude Code: plus band mod |

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
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/ponytail.md
