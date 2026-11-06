# Review: motion-launch-videos

## Entry

- Name: motion-launch-videos
- Status: active
- Upstream: https://github.com/Kimeur/motion-launch-videos
- Author: Marouane Gazouzi (Kimeur)
- License: MIT
- Commit: 5092579bc9aaeb0e3547ded0980a93404d2dc906
- Upstream version: 2.3.0
- Kind: plugin
- Eligibility: upstream ships its own .claude-plugin/marketplace.json with the plugin in plugins/motion-launch-videos (.claude-plugin/plugin.json)
- Source: git-subdir (`plugins/motion-launch-videos`, the full upstream plugin; the 100 MB examples folder stays out)
- Reviewed on: 2026-11-06
- Reviewer: Claude (cloud project thread)
- Owner approval: "yes" from Kamil on 2026-11-06, quote: "Dodaj oaoercut, manim, kimeur i gsap. I daj mi też to jako listę dla wątku gdzie robię i found the repo" (after the A-to-Z review of the Gemini Deep Research report on motion graphics repositories), an explicit exception to the stabilisation stage

## What it is

Thirteen skills that build launch and promo videos as HTML and render them frame by frame to MP4 (or video with alpha): `motion-launch-videos` (the main route), `motion-story`, `motion-charts`, `motion-captions`, `motion-3d`, `motion-globe`, `motion-particles`, `motion-overlays`, `motion-cartoon`, `motion-photo`, `motion-pixel`, `motion-shapes` and `motion-ui`. Each skill carries the same four scripts (`build.mjs`, `render.mjs`, `fonts.mjs`, `cmap.mjs`) and a `package.json` pinning `playwright-core` 1.63.0. The README states no analytics, no account and no keys. Last commit 2026-11-06.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, client launch and promo videos (motion graphics is Studio's main paid use) | A second launch-video method with its own deterministic frame renderer and thirteen specialised looks (charts, globes, 3D, captions, cartoon), next to Studio's HyperFrames and Remotion routes | Source read; isolated Claude Code install PASS and all 13 skills listed; renders and an A/B NOT_RUN |

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: root README.md, LICENSE and .claude-plugin/marketplace.json; plugins/motion-launch-videos/.claude-plugin/plugin.json; all thirteen SKILL.md files; the four scripts and package.json of each skill (identical across skills); a scan of the plugin folder for network calls, installs and hooks.

## What it installs and writes

The plugin cache (about 8.6 MB). At use: the HTML project and renders in the user's project. When the user follows `render.mjs doctor`, `npm install --prefix <skill folder>` puts playwright-core 1.63.0 in the plugin cache, and `npx playwright-core@1.63.0 install chromium` downloads a Chromium into the Playwright cache; `fonts.mjs` runs `npm pack @fontsource/<font>@5` for font files.

## Hooks

None.

## Network traffic

npm and the Playwright Chromium download during setup; npm for fonts. `motion-story` calls `npx hyperframes tts` and `transcribe` without a version (unpinned) and suggests `pip install kokoro-onnx soundfile` for a local voice.

## Changes to prompts or tool results

None. Skills load by their descriptions.

## Data sent outside

None found.

## Requirements

Node.js 20+, ffmpeg with libx264 (prores_ks or libvpx-vp9 for alpha), a Chromium. No account, no API key, no desktop app.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-11-06 with Claude Code 2.1.318: `claude plugin marketplace add` of this repository, `claude plugin install motion-launch-videos@framecore-works-toolbox` succeeded, `claude plugin list` showed 2.3.0 enabled, cache about 8.6 MB; a headless `claude -p` session listed all thirteen `motion-launch-videos:motion-*` skills.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. `motion-story` runs unpinned `npx hyperframes`; pin a HyperFrames version or skip that step.
2. The `fonts.mjs` range `@fontsource/<font>@5` is a major-version range, not an exact version.
3. Overlaps Studio's HyperFrames and Remotion routes and Toolbox's `animate` and `motion-designer`; pick one route per job.

## Verdict

accept with conditions: full upstream plugin, pinned; the unpinned `motion-story` voice step is named in the docs and index.

## History

- 2026-11-06: added at 5092579 (Toolbox 1.9.0).
