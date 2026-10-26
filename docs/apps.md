# Manual install in the Claude apps, ChatGPT and ChatGPT Work

None of these apps install skills from GitHub. Upload the files of one skill
folder at the pinned commit listed in `docs/<name>.md`. App menu names change
over time; the paths below were not verified in the apps (NOT_RUN).

## Get the files

```bash
python3 scripts/pack_skill.py <owner>/<repo> <sha> <path/to/skill>
# -> dist/<skill>-<short-sha>.zip, one top-level folder with SKILL.md inside
```

`dist/` is ignored by git. Never commit ZIPs.

## Claude apps (claude.ai, desktop, mobile)

- Requires code execution / file creation and Skills to be enabled in settings.
- Upload the ZIP in the Skills section of settings. The ZIP must contain one
  skill folder with `SKILL.md` at its top.
- Remove: delete the skill in the same Skills section.

## ChatGPT (Project or custom GPT)

- Upload `SKILL.md` and the files under `references/` (if any) as knowledge
  files.
- Add one instruction line: "When a task matches the description in SKILL.md,
  follow SKILL.md."
- Scripts in the skill do not run as part of the skill. Each `docs/<name>.md`
  says what is lost.
- Remove: delete the knowledge files and the instruction line.

## ChatGPT Work

- Same as ChatGPT. Scripts can run only where code execution is enabled for
  the workspace, and only if you upload them as files and ask for them to be
  run.
- Remove: same as ChatGPT.
