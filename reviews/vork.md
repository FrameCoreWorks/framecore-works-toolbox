# Review: vork

## Entry

- Name: vork
- Status: rejected
- Upstream: https://github.com/voyager-so/vork
- Author: voyager-so
- License: vork Preview License (not open source)
- Commit: 011e3f12e6c17696b3d854c173dca37a8159c6c4
- Upstream version: none
- Kind: app
- Eligibility: not eligible: no SKILL.md and no Claude plugin manifest
- Source: none (not listed)
- Reviewed on: 2026-11-11
- Reviewer: Claude (thread "Opieka nad repo FrameCore", research intake Phase C)
- Owner approval: not required (not eligible)

## What it is

A GPU video engine (rational clocks, structured warnings, render passes) driven from code. It needs a Vulkan or Metal GPU.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, motion rendering | None shown: Studio already has a master frame clock and deterministic renderers | Not admitted; nothing run |

## Files reviewed

LICENSE (first line "vork Preview License"), top-level tree, absence of .claude-plugin/plugin.json and .claude-plugin/marketplace.json (HTTP 404); read through raw GitHub at the commit above. Nothing was cloned or run.

## What it installs and writes

Not reviewed further (not eligible).

## Hooks

None found (no plugin manifest).

## Network traffic

NOT_RUN.

## Changes to prompts or tool results

None (no plugin).

## Data sent outside

NOT_RUN.

## Requirements

Vulkan or Metal GPU, its own runtime.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): NOT_RUN (not eligible)
- claude.ai / Cowork (Customize > Plugins): NOT_RUN

## Risks

1. Non-open licence: its text and code cannot be copied or adapted into FrameCore repositories.

## Verdict

reject: not eligible (no skill or plugin manifest), non-open licence, separate GPU runtime against the self-contained rule.

## History

- 2026-11-11: reviewed at 011e3f1; rejected.
