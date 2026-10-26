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

claude.ai shows a sync warning that `types` in the upstream plugin.json is
stripped. It is expected: that field serves only the band mod in Claude Code.

In chat the mode is active only when a skill matches the task or you ask for
"ponytail mode"; there is no always-on injection.

## Use

- Always on in Cowork and Claude Code once enabled, unless the default is
  set to off (see below).
- Levels: `/ponytail lite|full|ultra|off`; default for new sessions:
  `/ponytail default <level>`.
- Reviews and reports: `/ponytail:ponytail-review`, `/ponytail:ponytail-audit`,
  `/ponytail:ponytail-debt`.
- Turn it off for creative or non-coding work: `/ponytail off`, or disable
  the plugin.

## Run it only where you want it

Ponytail picks its starting level from `PONYTAIL_DEFAULT_MODE` first, then
`~/.config/ponytail/config.json`, then `full`. Claude Code applies `env` from
settings files, and project settings override user settings. So:

- Off everywhere by default:
  - your computer (Claude Code CLI, desktop Code tab, VS Code): add
    `"env": {"PONYTAIL_DEFAULT_MODE": "off"}` to `~/.claude/settings.json`;
  - Claude Code cloud sessions: user settings do not persist there, so set the
    environment variable `PONYTAIL_DEFAULT_MODE=off` in the cloud
    environment's settings (environment menu in the session title bar, Edit).
    New sessions pick it up.
- On in this repo: `.claude/settings.json` here sets
  `PONYTAIL_DEFAULT_MODE=lite` (builds what was asked, names smaller options
  without cutting scope), which overrides the global `off`.
- On for one session anywhere: `/ponytail` (or `/ponytail lite|full|ultra`);
  off again with `/ponytail off` or "stop ponytail".

Tested 2026-10-26 in Claude Code: with `PONYTAIL_DEFAULT_MODE=off` in the
process environment, a repo without project settings started with ponytail
off, and a repo with the project setting above started in `full`. After the
switch to `lite`, a new session in this repo started in `lite`.

Not covered: Cowork (whether it reads `~/.claude/settings.json` is Unknown;
use `/ponytail off` there or disable the plugin) and claude.ai chat (no hooks;
skills load only when a task matches their description).

## Full removal

1. Remove the plugin in Customize > Plugins, or run
   `claude plugin uninstall ponytail@framecore-works-toolbox`.
2. Delete `~/.claude/.ponytail-*` and `~/.claude/ponytail-statusline.*`, and
   any `statusLine` entry pointing to them in `~/.claude/settings.json`.
3. Delete `~/.config/ponytail/`.
