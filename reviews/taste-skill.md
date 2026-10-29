# Review: taste-skill

## Entry

- Name: taste-skill
- Status: active
- Upstream: https://github.com/Leonxlnx/taste-skill
- Author: Leonxlnx
- License: MIT
- Commit: 12af471f627f866411b4bd785b19646d3672784c
- Upstream version: 2.1.5
- Kind: skills
- Eligibility: upstream presents skills/taste-skill as an installable skill and ships its own marketplace.json (unpinned, default branch)
- Source: github (inline manifest, skills ./skills/taste-skill, strict false)
- Reviewed on: 2026-10-29
- Reviewer: Claude (cloud orchestration thread), carrying over the Creative Studio registry review at the same commit
- Owner approval: "yes" from Kamil on 2026-10-29 (decision card "Przenieść wszystko do Toolboxa", then "decyzje są już podjęte" accepting the move list)

## What it is

One skill, `design-taste-frontend`, that art-directs landing pages, product pages, dashboards and app screens: a library of researched directions from 247 gallery sites, a found-image search in open collections with per-image credits and a headless-browser inspector.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, landing pages and app screens (previously Studio's recommended extension `taste-skill`) | Researched art direction and a real-browser check beyond Studio's restated craft rules | Studio review 2026-10-26 at 12af471; Toolbox install PASS; invocation on a real page NOT_RUN |

Moved from Creative Studio's recommended-extension registry to Toolbox by owner decision 2026-10-29: Toolbox becomes the single source of installable recommendations and Studio points here.

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: README.md, .claude-plugin/marketplace.json, install.sh (read, not run), skills/taste-skill/** (SKILL.md, references, scripts), LICENSE.

## What it installs and writes

The plugin cache (about 3 MB). Pages and images the user asks for, in the project.

## Hooks

None.

## Network traffic

Only when the skill searches pictures: archive.org, Art Institute of Chicago, Metropolitan Museum, NASA images, Openverse-style CC sources and Lorem Picsum; fonts from Google Fonts and scripts from jsDelivr in generated pages.

## Changes to prompts or tool results

The skill loads by description on front-end design tasks.

## Data sent outside

Image search queries go to the open collections above when the skill searches; no telemetry found.

## Requirements

A browser for its inspector (Node or Python per its scripts).

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-10-29 in an isolated CLAUDE_CONFIG_DIR: `claude plugin marketplace add` of this repository, `claude plugin install taste-skill@framecore-works-toolbox` succeeded, `claude plugin list` showed it enabled, and a headless `claude -p` session listed its skills (`taste-skill:taste-skill`).
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Found images keep their own licences (CC BY-SA adaptations stay BY-SA). 2. Its site records describe real sites: never rebuild a named site for a client.

## Verdict

accept.

## History

- 2026-10-29: added at 12af471, moved from Creative Studio's recommended extensions.
