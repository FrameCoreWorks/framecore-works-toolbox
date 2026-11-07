# Review: cutaway

## Entry

- Name: cutaway
- Status: active
- Upstream: https://github.com/Nyxera0x/cutaway
- Author: Nyxera0x (with whaleyxbt, author of the claude-motion base)
- License: MIT (code); recorded samples CC0 1.0 (Freesound, via Barty-Bart/motion-graphics, MIT); fonts Inter and JetBrains Mono SIL OFL 1.1 (npm)
- Commit: 5d8f1c6efe0ed65a8fc7647a7a2a3ee9fbb4d20a
- Upstream version: 1.0.0 (package.json)
- Kind: adapted
- Eligibility: adapted: our own wrapper plugin `plugins/cutaway` with its own skill that checks out the upstream at the reviewed commit inside the project after the user's yes, runs `npm ci` from the upstream lockfile and follows the upstream method; the upstream skill is not listed directly because `npx skills add Nyxera0x/cutaway` takes the current `main` and its first run installs packages and a browser in the skill folder without asking
- Source: local wrapper ./plugins/cutaway (UPSTREAM.md names the reviewed commit)
- Reviewed on: 2026-11-07
- Reviewer: Claude (cloud project thread)
- Owner approval: "yes" from Kamil on 2026-11-07, quote: "Dodaj ten kataway do toolboxa, ale z zaznaczeniem, że to najlepiej działa z opusem 5,5 [...] generowanie dodatkowych asetów graficznych odbywa się poprzez [...] konektor przy użyciu np. GPT Image 2,5 lub innych, a także [...] żeby mieć lektora [...] instalowalny lokalnie silnik mowy Kokoro." Given after the verdict "not now"; an explicit exception to the stabilisation stage

## What it is

One Claude Code skill (`SKILL.md`, 13 KB, no plugin manifest) with a method in `docs/` (job description, checklist, prompts, lessons), a three.js kit (`sims/kit`), three complete objects (robotic tarantula, piranha, wasp; each with a 20 s film and a 10 s demo), a bundler (`sims/build.mjs`, esbuild), a frame capture to 60 fps MP4 and review sheets (`sims/capture.mjs`, Playwright and ffmpeg), review tools (camera track, part anchors, leftover-colour probe) and a procedural Python sound engine (`sfx/`, standard library, mastered to -14 LUFS) with 12 CC0 samples. From one reference picture Claude rebuilds the object in code, grades it against a 10-12 line checklist and measured proportions and dark share, stops after still round 2 for the user, then films each part opening under its own camera. Two commits, created 2026-11-06.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, product and mechanism films (owner request 2026-11-07) | A glossy three.js "product render" exploded-view film from one picture, with a page of part buttons and a synced score; Studio's Anatomy engine covers diagram-style cutaways (SVG, WebGL, isometric 3D) but not this rendered-product look or a picture-matching loop | Source read; isolated Claude Code install of the wrapper checked (see Install tests); the clone, `npm ci`, builds, films and Kokoro NOT_RUN. Owner added it before the improvement was shown in a render |

## Files reviewed

Upstream cloned as data into a temporary folder at the pinned commit; no scripts, installers or tests were run. Read: README.md, LICENSE, SKILL.md, package.json, package-lock.json (33 packages, all from registry.npmjs.org), paths.mjs, docs/PROMPTS.md, docs/LESSONS.md, sfx/samples/SOURCES.md, and a scan of every .js, .mjs and .py file for network calls, child processes and home-directory writes (only ffmpeg and Python are spawned; no fetch, HTTP or WebSocket calls). The Kokoro model files were downloaded once to record their SHA-256 and deleted.

## What it installs and writes

The wrapper is five small files in the plugin cache. After the user's yes, its skill clones the upstream (about 16 MB) into `cutaway/` in the project at the reviewed commit and runs `npm ci` there (three 0.186.1, esbuild 0.28.1, playwright 1.58.2, two fonts). Builds and renders go to `cutaway-out/` in the project. Only after a further yes: Playwright's Chromium (about 170 MB) in the user's Playwright cache, when no Chrome or Chromium is installed; and the optional Kokoro narrator, a Python environment in `cutaway/.narrator/venv` with `kokoro-onnx==0.6.1` and `soundfile==0.14.0` plus two model files (about 355 MB) checked against their SHA-256. Reference images or extra graphics come from an image connector the user already has, announced before the first call.

## Hooks

None (neither the wrapper nor the upstream).

## Network traffic

The one clone from github.com and npm during `npm ci`, after the user's yes; Playwright's Chromium and the Kokoro packages (PyPI) and model files (GitHub release `model-files-v1.0` of thewh1teagle/kokoro-onnx), each after a separate yes. Image connector calls only when the user asks for generated images. No other network calls found; no telemetry.

## Changes to prompts or tool results

None. The skill loads by its description.

## Data sent outside

None by cutaway. A reference prompt goes to the user's own image connector only when they ask for a generated picture.

## Requirements

git, Node.js 20+, ffmpeg, Python 3, Chrome or Chromium (or Playwright's after a yes); a real GPU for practical capture speed. Optional: an image connector, Python 3.10-3.13 for Kokoro. No account and no API key are required. Works best with Claude Opus 5.5 (owner note).

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-11-07 with Claude Code 2.1.319: marketplace add, `claude plugin install cutaway@framecore-works-toolbox` succeeded, `claude plugin list` showed 1.0.0 enabled, cache 48 KB (wrapper); a headless `claude -p` session listed `cutaway:cutaway`.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result
- The wrapper's clone, `npm ci`, builds, films and Kokoro narrator: NOT_RUN

## Risks

1. Very young project (two commits, one day old at review); later commits need a new review before the pin moves.
2. High token use: the upstream reports about 430,000 to 450,000 tokens for single failed objects.
3. Capture without a GPU falls back to a software renderer and is slow; cloud containers have no GPU.
4. Kokoro's transitive packages (onnxruntime, phonemizer, numpy, espeakng-loader) are not pinned by `kokoro-onnx`; Kokoro does not speak Polish.
5. Overlaps Studio's Anatomy engine for diagram-style cutaways; Studio chooses which route fits the brief.

## Verdict

accept with conditions: listed only through our pinned wrapper; renders NOT_RUN.

## History

- 2026-11-07: added at 5d8f1c6 (Toolbox 1.12.0).
