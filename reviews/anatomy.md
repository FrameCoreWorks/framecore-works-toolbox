# Review: anatomy

## Entry

- Name: anatomy
- Status: active
- Upstream: https://github.com/wheresryan22/anatomy
- Author: Ryan (wheresryan22)
- License: MIT
- Commit: e9488296a44211c42701ff71705b7901470ec78f
- Upstream version: 0.0.0 (unreleased; pinned commit)
- Kind: skills
- Eligibility: upstream presents its root SKILL.md as an installable skill (README documents `npx skills add`)
- Source: github (inline manifest, skills ./, strict false)
- Reviewed on: 2026-10-29
- Reviewer: Claude (cloud orchestration thread), carrying over the Creative Studio registry review at the same commit
- Owner approval: "yes" from Kamil on 2026-10-29 (decision card "Przenieść wszystko do Toolboxa", then "decyzje są już podjęte" accepting the move list)

## What it is

One skill that builds detailed interactive isometric SVG figures explaining a technical idea as a physical object, with optional WebGL shader layers, React adapters and geometry and browser audits.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, technical explainers (previously Studio's recommended extension `anatomy`) | The original skill with its audits, next to Studio's bundled graphics kit | Studio review 2026-10-17: 62 upstream geometry and browser tests passed locally; Toolbox install PASS; invocation NOT_RUN |

Moved from Creative Studio's recommended-extension registry to Toolbox by owner decision 2026-10-29: Toolbox becomes the single source of installable recommendations and Studio points here.

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: SKILL.md, README.md, SECURITY.md, kit/, references/, scripts/*.mjs (read, not run), LICENSE.

## What it installs and writes

The plugin cache (about 13 MB). Figures in the user's project.

## Hooks

None.

## Network traffic

Only `scripts/publish.mjs`, which shares a figure in the community gallery through the GitHub CLI when the user asks.

## Changes to prompts or tool results

The skill loads by description.

## Data sent outside

Only on an explicit publish request: the figure goes to the public Anatomy gallery.

## Requirements

Node 20.10+, Chrome or Chromium for the checks; WebGL for shaders.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-10-29 in an isolated CLAUDE_CONFIG_DIR: `claude plugin marketplace add` of this repository, `claude plugin install anatomy@framecore-works-toolbox` succeeded, `claude plugin list` showed it enabled, and a headless `claude -p` session listed its skills (`anatomy:anatomy`).
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Never publish to the gallery without the user asking. 2. Large figures take hours; the skill estimates first.

## Verdict

accept.

## History

- 2026-10-29: added at e948829, moved from Creative Studio's recommended extensions.
