# Review: gsap-skills

## Entry

- Name: gsap-skills
- Status: active
- Upstream: https://github.com/greensock/gsap-skills
- Author: GreenSock (Webflow)
- License: MIT (the skills); GSAP itself is free under Webflow's own "no charge" licence, not MIT
- Commit: aed9cfd3277740755f6bfc1155c7aa645403b760
- Upstream version: 1.0.0
- Kind: plugin
- Eligibility: upstream ships .claude-plugin/plugin.json and its own .claude-plugin/marketplace.json
- Source: github (the full upstream plugin)
- Reviewed on: 2026-11-06
- Reviewer: Claude (cloud project thread)
- Owner approval: "yes" from Kamil on 2026-11-06, quote: "Dodaj oaoercut, manim, kimeur i gsap. I daj mi też to jako listę dla wątku gdzie robię i found the repo" (after the A-to-Z review of the Gemini Deep Research report on motion graphics repositories), an explicit exception to the stabilisation stage

## What it is

GreenSock's official agent skills for GSAP: eight skills (`gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-plugins`, `gsap-react`, `gsap-frameworks`, `gsap-utils`, `gsap-performance`) plus `skills/llms.txt`. They cover tweens and easing, timelines and labels, ScrollTrigger, the plugins made free in 2025 (SplitText, MorphSVG, DrawSVG, Flip and others), React `useGSAP` and other frameworks, utilities and performance. The repository also has examples and a Cursor plugin manifest. No commands, agents, hooks, MCP servers or scripts. Last commit 2026-04-21.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, HyperFrames compositions and web animation (GSAP is HyperFrames' animation engine) | Current GSAP API and plugin options from the vendor: in a text A/B (1 case, the skill text appended to the system prompt, no tools) on a SplitText reveal with a morph, the run with the skill used `mask: "chars"` as asked (without it: `"lines"`) and MorphSVG `shapeIndex: "log"` with `convertToPath`; the run without it already knew `SplitText.create`, `autoSplit` and `onSplit` | Small improvement, 1 case; renders NOT_RUN. Isolated Claude Code install PASS and all 8 skills listed |

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: .claude-plugin/plugin.json and marketplace.json, README.md, LICENSE, all eight SKILL.md files, skills/llms.txt, the examples list and .cursor-plugin manifest (full shallow clone; a scan for scripts, hooks, network calls and package installs found none; the only links are gsap.com).

## What it installs and writes

The plugin cache (about 360 KB). At use: the GSAP code Claude writes in the user's project.

## Hooks

None.

## Network traffic

None by the plugin. Code it helps write may load GSAP from npm or a CDN, which is the user's choice.

## Changes to prompts or tool results

None. Skills load by their descriptions.

## Data sent outside

None found.

## Requirements

None for the skills. Running the code needs the `gsap` package (npm, free licence). No account, no API key, no desktop app.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-11-06 with Claude Code 2.1.318: `claude plugin marketplace add` of this repository, `claude plugin install gsap-skills@framecore-works-toolbox` succeeded, `claude plugin list` showed 1.0.0 enabled, cache about 360 KB; a headless `claude -p` session listed all eight `gsap-skills:gsap-*` skills.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. GSAP is not MIT: its free licence forbids use in a tool that competes with Webflow; client animation work is allowed.
2. Last upstream commit 2026-04-21; plugin options that change later need a new review.

## Verdict

accept: full upstream plugin, pinned.

## History

- 2026-11-06: added at aed9cfd (Toolbox 1.9.0).
