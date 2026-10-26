# ponytail: install notes

- Upstream: https://github.com/DietrichGebert/ponytail
- Pinned commit: 09c434ab73ca43761c5d8b0c5d341926c2fba710 (version 5.3.2)
- Review: [reviews/ponytail.md](../reviews/ponytail.md)

## Install

See [install.md](install.md). Plugin id: `ponytail@framecore-works-toolbox`.

## Setup after install

- Plugin options (Claude Code: `/plugin configure ponytail@framecore-works-toolbox`):
  keep `webhookUrl` empty so nothing leaves the machine; set `ledger` to
  false if you do not want the local log in `~/.config/ponytail/band/`.
- In the first Claude Code or Cowork session the hook asks Claude to offer a
  statusline edit in `~/.claude/settings.json`. Decline unless you want it.

## What works where

| Component | Chat | Cowork | Claude Code |
| --------- | ---- | ------ | ----------- |
| 6 skills (`ponytail`, `-review`, `-audit`, `-debt`, `-gain`, `-help`) | yes | yes | yes |
| Hooks (ruleset in every session and subagent, codebase map) | no | yes | yes |
| Band mod (status band, task ledger, board) | no | no | yes |

In chat the mode is active only when a skill matches the task or you ask for
"ponytail mode"; there is no always-on injection.

## Use

- Always on in Cowork and Claude Code once enabled.
- Levels: `/ponytail lite|full|ultra|off`; default for new sessions:
  `/ponytail default <level>`.
- Reviews and reports: `/ponytail:ponytail-review`, `/ponytail:ponytail-audit`,
  `/ponytail:ponytail-debt`.
- Turn it off for creative or non-coding work: `/ponytail off`, or disable
  the plugin.

## Full removal

1. Remove the plugin in Customize > Plugins, or run
   `claude plugin uninstall ponytail@framecore-works-toolbox`.
2. Delete `~/.claude/.ponytail-*` and `~/.claude/ponytail-statusline.*`, and
   any `statusLine` entry pointing to them in `~/.claude/settings.json`.
3. Delete `~/.config/ponytail/`.
