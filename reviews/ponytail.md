# Review: ponytail

## Entry

- Name: ponytail
- Status: active
- Upstream: https://github.com/DietrichGebert/ponytail
- Author: Dietrich Gebert (GitHub user DietrichGebert); latest commit authored as "OhMyCode"
- License: MIT
- Commit: 09c434ab73ca43761c5d8b0c5d341926c2fba710
- Upstream version: 5.3.2 (`.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`)
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json` and its own Claude Code and Codex marketplaces
- Claude Code source: github
- Codex-Pin: sha
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: "yes" from Kamil on 2026-10-26. Offered two options (1: skills only, no hooks; 2: full plugin with always-on hooks, mod and local ledger); Kamil replied "2".

GitHub metadata at review time: 176,440 stars, 9,637 forks, 137 open issues,
created 2026-06-12, last push 2026-10-18 (GitHub API).

## What it is

A "lazy senior dev" mode: rules that push the agent to the smallest correct
change (YAGNI, standard library first, no unrequested abstractions, short
replies). Ships 6 skills (`ponytail`, `ponytail-review`, `ponytail-audit`,
`ponytail-debt`, `ponytail-gain`, `ponytail-help`), lifecycle hooks for Claude
Code and Codex, and a Claude Code mod ("band") that shows a status band and
keeps a per-task ledger. The repo also carries ports for Cursor, Copilot,
Gemini, OpenCode, Qoder, Windsurf and others; those are not used by this entry.

## Files reviewed

`.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`,
`.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `plugin.json`,
`package.json`, `skills/*/SKILL.md`, `skills/plugin.json`,
`hooks/claude-codex-hooks.json`, `hooks/claude-band.json`,
`hooks/ponytail-activate.js`, `hooks/ponytail-mode-tracker.js`,
`hooks/ponytail-subagent.js` (injection points), `hooks/ponytail-map.js`
(header), `hooks/ponytail-instructions.js` (header),
`hooks/ponytail-band-import.js` (I/O parts), `hooks/band/register.tsx` (I/O
parts), `hooks/band/metrics.ts` (`webhookRequest`). Repo cloned as data at the
pinned commit; nothing was run.

## What it installs and writes

- Install: the whole upstream repo is copied into the Claude Code plugin
  cache (github source). No install scripts (`package.json` has only `test`).
- At session start: `$CLAUDE_CONFIG_DIR/.ponytail-active` (mode flag),
  `.ponytail-statusline-nudged`, and a copy of `ponytail-statusline.sh` (or
  `.ps1`) in `$CLAUDE_CONFIG_DIR` (default `~/.claude`).
- `/ponytail default <mode>`: `~/.config/ponytail/config.json`.
- `/ponytail band off`: `$CLAUDE_CONFIG_DIR/.ponytail-band`.
- Band mod, after every turn, on by default (`ledger` option, default true):
  `~/.config/ponytail/band/<project>.csv` (task key, project, task name, cost,
  turns, agent time, tokens, reuse, tests, level, model) and `board.html`.
- `/ponytail band import` (manual): reads every transcript under
  `$CLAUDE_CONFIG_DIR/projects` and adds rows to the same CSVs.

## Hooks

From `hooks/claude-codex-hooks.json` (Claude Code and Codex), all run `node`
on files in the plugin cache:

- `SessionStart` (startup, resume, clear, compact) -> `ponytail-activate.js`:
  injects the ponytail ruleset (body of `skills/ponytail/SKILL.md`, about 600
  words, filtered by level) as hidden context, plus a codebase map (top-level
  functions/classes from `git ls-files` and regexes, up to 2,000 chars, 3 s
  limit; off with `PONYTAIL_MAP=0`). If no statusline is configured, it adds
  an instruction telling the agent to "proactively offer" to edit
  `settings.json` (once per config dir).
- `SubagentStart` -> `ponytail-subagent.js`: injects the ruleset into every
  subagent.
- `UserPromptSubmit` -> `ponytail-mode-tracker.js`: parses `/ponytail ...`
  commands and "stop ponytail", switches the level, writes flags.

From `hooks/claude-band.json` (Claude Code only): mod module
`hooks/band/register.tsx` runs inside Claude Code, reads session usage,
transcripts (via `grep`) and edited files, runs `git grep` in the project, and
writes the ledger described above. `openBoard` runs `xdg-open`/`open`/`start`
on the local `board.html`.

## Network traffic

- None by default.
- Optional webhook (`webhookUrl` user option, empty by default): POSTs the
  task row as JSON after every turn; HTTPS only (HTTP only to localhost);
  optional Bearer token stored as a sensitive option; `sendNames` controls
  whether the task name is included.
- No other network calls found in hooks or skills.

## Changes to prompts or tool results

Yes. The ruleset and codebase map are injected into every session and every
subagent while the plugin is enabled. They change how the agent writes code
and how long its replies are. Tool results are not modified.

## Data sent outside

Nothing unless the webhook is configured. With a webhook: project name, task
name (optional), cost, token counts, turns, timing, model, test counts.

## Requirements

Node.js on PATH (hooks). The band needs a Claude Code version with mod
support (Unknown which minimum; not checked). `git` for the codebase map.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR, Claude Code 2.1.310): PASS.
  `claude plugin validate .` passed; `claude plugin marketplace add <repo>`
  and `claude plugin install ponytail@framecore-works-toolbox` succeeded;
  `claude plugin list` shows version 5.3.2 enabled; `installed_plugins.json`
  records `gitCommitSha` 09c434ab73ca43761c5d8b0c5d341926c2fba710. Install
  reported "4 userConfig options not yet set". Hooks did not run during
  install (no `~/.config/ponytail` created). A live session with the hooks
  was NOT_RUN. Temporary config dir deleted.
- Codex CLI: NOT_RUN (Codex CLI not installed in the review environment).
  Upstream ships `.codex-plugin/plugin.json`, so the entry is pinned by `sha`.
  Per Codex docs, plugin-bundled hooks are skipped until the user trusts them.
- Claude app / ChatGPT / ChatGPT Work: NOT_RUN (manual upload, see
  docs/ponytail.md).

## Risks

1. Always-on context injection in every session and subagent, including
   non-coding and creative work. It can conflict with other workflow rules
   (Superpowers, project CLAUDE.md) by pushing toward minimal changes and
   terse replies. Mitigation: `/ponytail off`, `/ponytail default off`, or
   disable the plugin per project.
2. The SessionStart hook tells the agent to offer an edit of the global
   `settings.json` (statusline). Decline unless wanted.
3. Local ledger on by default records project and task names, cost and
   tokens under `~/.config/ponytail/band/`. Turn off with the `ledger` option.
4. Large, fast-moving upstream (many ports and frequent releases). Pinned by
   commit; every update needs a new review.

## Verdict

Accept with conditions: added as a full plugin at the pinned commit with the
owner's explicit approval of the hooks. Leave `webhookUrl` empty; set
`ledger` to false if the local log is not wanted.

## History

- 2026-10-26: added at 09c434a (version 5.3.2).
