# Review: huashu-art-motion

## Entry

- Name: huashu-art-motion
- Status: active
- Upstream: https://github.com/alchaincyf/huashu-art-motion
- Author: alchaincyf (花叔)
- License: MIT
- Commit: 8a0d7d72ca65fcce6f8ba82c4a6c8dfe35b8422c
- Upstream version: 1.2.0
- Kind: skills
- Eligibility: upstream presents its root SKILL.md as an installable skill
- Source: github (inline manifest, skills ./, strict false)
- Reviewed on: 2026-10-29
- Reviewer: Claude (cloud orchestration thread), carrying over the Creative Studio registry review at the same commit
- Owner approval: "yes" from Kamil on 2026-10-29 (decision card "Przenieść wszystko do Toolboxa", then "decyzje są już podjęte" accepting the move list)

## What it is

One skill (written in Chinese) for art-style animation: 36 implemented style scenes from cave painting to Monet, Van Gogh, Bauhaus, 8-bit and Ghibli, 17 research cards, 9 explainer grammars, reference breakdown and shot-list gates, with a clip renderer.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, art-style motion (previously Studio's recommended extension `huashu-art-motion`) | The original 36 style scenes and clip renderer next to Studio's English restatement of its method | Studio review 2026-10-18; breakdown tool adapted and tested in Studio; Toolbox install PASS; invocation NOT_RUN |

Moved from Creative Studio's recommended-extension registry to Toolbox by owner decision 2026-10-29: Toolbox becomes the single source of installable recommendations and Studio points here.

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: SKILL.md, README.en.md, references/, scripts/ (read, not run), release-manifest.json, LICENSE.

## What it installs and writes

The plugin cache (about 74 MB with its assets). Its version check writes `.last-update-check` in the skill folder.

## Hooks

None.

## Network traffic

A version check with `git ls-remote` at most monthly, only when the skill folder is a git clone (the plugin cache is not, so it is skipped); optional voice through ByteDance OpenSpeech only with the user's own key; three.js from a CDN in some pages.

## Changes to prompts or tool results

The skill loads by description.

## Data sent outside

Only with the user's own voice-service key: text sent to ByteDance OpenSpeech. No telemetry found.

## Requirements

Node and a browser for rendering; optional voice-service key.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-10-29 in an isolated CLAUDE_CONFIG_DIR: `claude plugin marketplace add` of this repository, `claude plugin install huashu-art-motion@framecore-works-toolbox` succeeded, `claude plugin list` showed it enabled, and a headless `claude -p` session listed its skills (`huashu-art-motion:huashu-art-motion`).
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Showcase films include generated images of real people: never reuse them. 2. The skill text is Chinese; answers follow the user's language.

## Verdict

accept.

## History

- 2026-10-29: added at 8a0d7d7, moved from Creative Studio's recommended extensions.
