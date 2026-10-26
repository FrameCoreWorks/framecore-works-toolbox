# ponytail: install notes

- Upstream: https://github.com/DietrichGebert/ponytail
- Pinned commit: 09c434ab73ca43761c5d8b0c5d341926c2fba710 (version 5.3.2)
- Skill folders: `skills/ponytail`, `skills/ponytail-review`,
  `skills/ponytail-audit`, `skills/ponytail-debt`, `skills/ponytail-gain`,
  `skills/ponytail-help`
- Review: [reviews/ponytail.md](../reviews/ponytail.md)

## Claude Code and Codex

Install from the toolbox marketplace (see the README). In Claude Code, after
install, check the plugin options with
`/plugin configure ponytail@framecore-works-toolbox`: keep `webhookUrl` empty,
set `ledger` to false if you do not want the local log in
`~/.config/ponytail/band/`. Turn the mode off for a session with
`/ponytail off`, or by default with `/ponytail default off`.

Remove: `claude plugin uninstall ponytail@framecore-works-toolbox`, then
delete `~/.claude/.ponytail-*`, `~/.claude/ponytail-statusline.*`, any
`statusLine` entry pointing to them in `~/.claude/settings.json`, and
`~/.config/ponytail/`.

## Get the files at the pinned commit

Every skill is a single `SKILL.md` with no scripts.

```bash
python3 scripts/pack_skill.py DietrichGebert/ponytail 09c434ab73ca43761c5d8b0c5d341926c2fba710 skills/ponytail
python3 scripts/pack_skill.py DietrichGebert/ponytail 09c434ab73ca43761c5d8b0c5d341926c2fba710 skills/ponytail-review
# repeat for ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help as needed
```

## Claude apps (claude.ai, desktop, mobile)

General steps and caveats: [apps.md](apps.md).

1. Upload `ponytail-<short-sha>.zip` (and optionally the review and audit ZIPs)
   in the Skills section of settings.
2. There are no hooks in the apps: the mode is active only when the skill
   triggers from its description or you ask for "ponytail mode". The band,
   statusline and codebase map do not exist here.
3. Remove: delete each skill in the Skills section.

## ChatGPT (Project or custom GPT)

1. Upload `skills/ponytail/SKILL.md` (and optionally the review and audit
   `SKILL.md` files, renamed, for example `ponytail-review.md`) as knowledge
   files.
2. Add to the instructions: "For coding tasks, follow ponytail SKILL.md."
3. No scripts are involved, so nothing is lost beyond the hooks, band and
   codebase map.
4. Remove: delete the knowledge files and the instruction line.

## ChatGPT Work

Same as ChatGPT. Code execution is not needed.

## Notes

`ponytail-gain` cites `benchmarks/results/...` from the upstream repo, which is
not inside the skill folder; it reads as a display of numbers and still works
without it. `ponytail-help` lists slash commands that exist only with the full
plugin.
