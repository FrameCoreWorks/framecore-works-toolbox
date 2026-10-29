# Review: hairline

## Entry

- Name: hairline
- Status: active
- Upstream: https://github.com/lucasmarkes/hairline
- Author: Lucas Marques (lucasmarkes)
- License: MIT
- Commit: 37d2e78dcb333ab30c3338e28ed4a690364ea014
- Upstream version: 0.5.1
- Kind: skills
- Eligibility: upstream presents skills/hairline-create and skills/hairline-adopt as coding-agent skills
- Source: github (inline manifest, skills ./skills/hairline-create and ./skills/hairline-adopt, strict false)
- Reviewed on: 2026-10-29
- Reviewer: Claude (cloud orchestration thread), carrying over the Creative Studio registry review at the same commit
- Owner approval: "yes" from Kamil on 2026-10-29 (decision card "Przenieść wszystko do Toolboxa", then "decyzje są już podjęte" accepting the move list)

## What it is

Two skills around the Hairline library of isometric line figures that answer the mouse pointer: `hairline-create` draws a new figure to ten drawing rules as one HTML file and checks it in a browser; `hairline-adopt` adds the npm package `@lucasmarkes/hairline` 0.5.1 to a project.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, isometric line figures for pages (previously Studio's recommended extension `hairline`) | The original interactive web figures next to Studio's seekable video kit | Studio review 2026-10-26 at 37d2e78; Toolbox install PASS; invocation NOT_RUN |

Moved from Creative Studio's recommended-extension registry to Toolbox by owner decision 2026-10-29: Toolbox becomes the single source of installable recommendations and Studio points here.

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: README.md, skills/hairline-create/SKILL.md, skills/hairline-adopt/SKILL.md, packages/hairline/package.json, LICENSE (repository of 216 files read as data).

## What it installs and writes

The plugin cache (about 7 MB). The HTML figure or, with adopt, the npm dependency in the user's project.

## Hooks

None.

## Network traffic

Generated pages load modules from esm.sh; `hairline-adopt` installs the npm package into the project when the user asks.

## Changes to prompts or tool results

Skills load by description or `/hairline-create`.

## Data sent outside

None found.

## Requirements

A browser for the check; Node and a package manager for adopt.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-10-29 in an isolated CLAUDE_CONFIG_DIR: `claude plugin marketplace add` of this repository, `claude plugin install hairline@framecore-works-toolbox` succeeded, `claude plugin list` showed it enabled, and a headless `claude -p` session listed its skills (`hairline:hairline-create`, `hairline:hairline-adopt`).
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Figures run on the browser frame loop and do not seek, so they are not video renders. 2. A figure from a supplied logo shows that owner's mark.

## Verdict

accept.

## History

- 2026-10-29: added at 37d2e78, moved from Creative Studio's recommended extensions.
