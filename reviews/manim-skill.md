# Review: manim-skill

## Entry

- Name: manim-skill
- Status: active
- Upstream: https://github.com/Yusuke710/manim-skill
- Author: Yusuke710
- License: MIT
- Commit: a0048d9e265499038f34a9aa58ff16d306b5034c
- Upstream version: 1.0.0
- Kind: plugin
- Eligibility: upstream ships .claude-plugin/plugin.json and its own .claude-plugin/marketplace.json
- Source: github (the full upstream plugin)
- Reviewed on: 2026-11-06
- Reviewer: Claude (cloud project thread)
- Owner approval: "yes" from Kamil on 2026-11-06, quote: "Dodaj oaoercut, manim, kimeur i gsap. I daj mi też to jako listę dla wątku gdzie robię i found the repo" (after the A-to-Z review of the Gemini Deep Research report on motion graphics repositories), an explicit exception to the stabilisation stage

## What it is

One skill, `manim-skill`, for math and science explainer videos in Manim Community (3Blue1Brown style): scene planning, LaTeX formulas, graphs and geometry, pacing, subtitles and narration. Tools: `lint-subtitles.py`, `tts-generate.py` (local Kokoro voice with a cache) and `video_viewer.py` with `ui.html` (a local preview server that opens the browser). `pyproject.toml` lists manim>=0.18, kokoro>=0.9.4 and soundfile. Voiceover is on by default when Kokoro is installed. Last commit 2026-10-07.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, educational and explainer pieces with formulas, graphs or algorithms | Exact animated formulas (LaTeX), plots and geometric constructions that Studio's Remotion and HyperFrames routes do not draw | Source read; isolated Claude Code install PASS and the skill listed; renders and an A/B NOT_RUN |

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: .claude-plugin/plugin.json and marketplace.json, README.md, LICENSE, pyproject.toml, skills/manim-skill/SKILL.md and its references, the three Python tools and ui.html (scan for network calls and installs).

## What it installs and writes

The plugin cache (about 1.3 MB). At use: the scene files, narration, subtitles, `.tts-cache/` and renders in the user's project.

## Hooks

None.

## Network traffic

None by the tools except the local preview server on localhost. Installing Manim, LaTeX and Kokoro (and Kokoro's first model download) is the user's step.

## Changes to prompts or tool results

None. Skills load by their descriptions.

## Data sent outside

None found.

## Requirements

Python with Manim Community (`uv sync` or pip), a LaTeX install for MathTex, ffmpeg; Kokoro and soundfile optional for voice. No account, no API key, no desktop app.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-11-06 with Claude Code 2.1.318: `claude plugin marketplace add` of this repository, `claude plugin install manim-skill@framecore-works-toolbox` succeeded, `claude plugin list` showed 1.0.0 enabled, cache about 1.3 MB; a headless `claude -p` session listed `manim-skill:manim-skill`.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. The pyproject uses lower bounds (`>=`), not exact versions; pin them in the user's project.
2. LaTeX is a large install on some systems.
3. Voice is on by default when Kokoro is installed; ask for a silent video when needed.

## Verdict

accept: full upstream plugin, pinned.

## History

- 2026-11-06: added at a0048d9 (Toolbox 1.9.0).
