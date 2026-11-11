# Review: cinecode

## Entry

- Name: cinecode
- Status: rejected
- Upstream: https://github.com/sarpstar/cinecode
- Author: sarpstar
- License: MIT
- Commit: 67f9807112b97ae253d4a5f0eccaccc46c3b2633
- Upstream version: none
- Kind: skills
- Eligibility: a root SKILL.md presented as an installable skill, without a Claude plugin manifest
- Source: none (not listed)
- Reviewed on: 2026-11-11
- Reviewer: Claude (thread "Opieka nad repo FrameCore", research intake Phase C)
- Owner approval: not required (rejected at the reject gate)

## What it is

A film-making skill for coding agents: one root SKILL.md with about twenty references (camera, looks, motion, music video, footage editing, finish, jury review), a context protocol and QA scripts. Its 58 film looks largely come from the same LemoLab source that Creative Studio already adapted as its 66-look film-style library.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, motion and film styles | None shown beyond the existing film-style library and motion review | Not admitted; comparison of its qc.py and words_check.py with Studio's motion-review stays optional (NOT_RUN) |

## Files reviewed

README.md (install section), SKILL.md front matter (hooks), the top-level tree, LICENSE; read through raw GitHub at the commit above. Nothing was cloned or run.

## What it installs and writes

The README installs with `git clone https://github.com/sarpstar/cinecode.git ~/.claude/skills/cinecode` (a moving branch into the user's home folder) and updates by pulling the latest version on request.

## Hooks

SKILL.md declares three hooks: UserPromptSubmit, Stop and PreToolUse (matcher `*`), each an inline `node -e` script that searches `~/.claude/skills` and the project's `.claude/skills` for a cinecode folder and runs a script from it. Not executed in this review.

## Network traffic

Install and update clone from GitHub at a branch, not a pinned commit. Script traffic: NOT_RUN.

## Changes to prompts or tool results

The UserPromptSubmit and PreToolUse hooks run on every prompt and tool call while the skill is installed (content of their output: NOT_RUN).

## Data sent outside

None found in the reviewed files; scripts NOT_RUN.

## Requirements

Node; git for the documented install.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): NOT_RUN (rejected at the gate)
- claude.ai / Cowork (Customize > Plugins): NOT_RUN

## Risks

1. Unpinned install and update by git clone of a branch into ~/.claude/skills.
2. Hooks on every prompt and tool call.

## Verdict

reject: installs and updates unpinned code outside the project (reject gate), with hooks on every prompt and tool call.

## History

- 2026-11-11: reviewed at 67f9807; rejected.
