# <entry-name>: manual install for Claude and ChatGPT apps

<!-- Copy to docs/<entry-name>.md. Keep the commit identical to the review. -->

- Upstream: https://github.com/<owner>/<repo>
- Pinned commit: <full 40-character commit SHA>
- Skill folders: `<path/to/skill>` (one line per skill)
- Review: [reviews/<entry-name>.md](../reviews/<entry-name>.md)

## Get the files at the pinned commit

```bash
python3 scripts/pack_skill.py <owner>/<repo> <commit> <path/to/skill>
# -> dist/<skill-name>-<short-sha>.zip (dist/ is ignored by git)
```

Or download https://github.com/<owner>/<repo>/archive/<commit>.zip and take the
skill folder from it.

## Claude apps (claude.ai, desktop, mobile)

General steps and caveats: [apps.md](apps.md).

1. Upload the ZIP in the Skills section of settings (one skill folder with
   `SKILL.md` at its top).
2. Remove: delete the skill in the same Skills section.

## ChatGPT (Project or custom GPT)

1. Upload `SKILL.md` and the files under `references/` as knowledge files.
2. Add to the instructions: "Follow SKILL.md when the task matches its
   description."
3. Scripts under `scripts/` do not run here. <Say what is lost.>
4. Remove: delete the files from the Project or GPT knowledge.

## ChatGPT Work

Same as ChatGPT. Scripts run only where code execution is available in the
workspace. <Say whether the skill needs them.>

## Notes

<Limits, required accounts, anything that does not work outside Claude Code or
Codex.>
