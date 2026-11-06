# Review: papercut-explainer

## Entry

- Name: papercut-explainer
- Status: active
- Upstream: https://github.com/0xS4N4TG/papercut-explainer
- Author: 0xS4N4TG
- License: MIT (code, sound effects, music beds, textures); fonts SIL OFL 1.1; Remotion source-available under its own licence
- Commit: ff8223abc8136cc09e8d7e9b62ecb5d080c389e1
- Upstream version: 0.1.0 (library)
- Kind: adapted
- Eligibility: adapted: our own wrapper plugin `plugins/papercut-explainer` with its own skill that checks out the upstream at the reviewed commit inside the project after the user's yes and then follows the upstream stage skills; the upstream skills are not listed directly because `papercut-setup` clones the unpinned default branch and `install.sh` runs `npx -y skills@latest add remotion-dev/skills` and links skills into home folders
- Source: local wrapper ./plugins/papercut-explainer (UPSTREAM.md names the reviewed commit)
- Reviewed on: 2026-11-06
- Reviewer: Claude (cloud project thread)
- Owner approval: "yes" from Kamil on 2026-11-06, quote: "Dodaj oaoercut, manim, kimeur i gsap. I daj mi też to jako listę dla wątku gdzie robię i found the repo" (after the A-to-Z review of the Gemini Deep Research report on motion graphics repositories), an explicit exception to the stabilisation stage

## What it is

A pipeline for short vertical (9:16) cut-paper explainer reels: nine skills (`papercut-explainer` router, strategy, hook, script, storyboard, build, voice, qa, setup), a scene subagent (`agents/papercut-scene.md`), and a library with a Remotion 4.0.530 template (lockfile), paper props, 24 backdrops, sound effects, music beds, four fonts, `env.sh`, `new_episode.sh`, Python tools and an optional local Qwen3-TTS voice. `install.sh` sets up the parts. Last commit 2026-10-17.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, short explainer reels for clients and the owner's "I found the repo" series | A ready cut-paper style with its own nine-stage pipeline from a link to an MP4 (hook, script, storyboard, build, QA) | Source read; isolated Claude Code install of the wrapper PASS and its skill listed; the clone, `npm install` and renders NOT_RUN |

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: README.md, LICENSE, THIRD_PARTY.md, install.sh, harnesses.sh, library/env.sh, library/new_episode.sh, the router and eight stage SKILL.md files, agents/papercut-scene.md, library/papercut/template/package.json and the lockfile list, and a scan of library/tools for network calls.

## What it installs and writes

The wrapper is four small files in the plugin cache. After the user's yes, its skill clones the upstream (about 35 MB with history) into `papercut-explainer/` in the project at the reviewed commit; `new_episode.sh` creates an episode folder and runs `npm install` from the template lockfile. Only on a second yes: the Qwen3-TTS environment in `~/.local/share/papercut-explainer` and its model in the Hugging Face cache (several GB). The wrapper never runs `install.sh` modes that install skills or write `~/.config` links.

## Hooks

None (neither the wrapper nor the upstream).

## Network traffic

The one clone from github.com and npm during `npm install`, after the user's yes; the optional voice downloads Python packages and a Hugging Face model, after a separate yes.

## Changes to prompts or tool results

None. Skills load by their descriptions.

## Data sent outside

None found.

## Requirements

git, Node.js 20+, ffmpeg, python3 with numpy and Pillow; optional local voice (several GB). No account, no API key, no desktop app.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-11-06 with Claude Code 2.1.318: `claude plugin marketplace add` of this repository, `claude plugin install papercut-explainer@framecore-works-toolbox` succeeded, `claude plugin list` showed 0.1.0 enabled, cache about 48 KB (wrapper); a headless `claude -p` session listed `papercut-explainer:papercut-explainer`.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result
- The wrapper's clone, `npm install` and renders: NOT_RUN

## Risks

1. The upstream setup clones the unpinned default branch and installs unpinned Remotion skills; the wrapper replaces both, but a user who installs the upstream directly gets that behaviour.
2. Remotion needs a paid company licence above its size threshold.
3. Sixteen of the 24 backdrops are AI-generated and may carry no enforceable copyright; all upstream example products and numbers are invented.
4. Young project (one release, 2026-10-17); later commits need a new review before the pin moves.

## Verdict

accept with conditions: listed only through our pinned wrapper; renders NOT_RUN.

## History

- 2026-11-06: added at ff8223a (Toolbox 1.9.0).
