# Review: stickman-kino

## Entry

- Name: stickman-kino
- Status: active
- Upstream: https://github.com/dsauce/stickman-kino
- Author: Prerit Ahuja (dsauce)
- License: MIT (code, engine, generated music and effects); fonts SIL OFL 1.1; GSAP GreenSock no-charge standard licence; HyperFrames Apache-2.0
- Commit: d3d665301c0b62f04c885785e6bd6044de0785c6
- Upstream version: 1.0.0 (npm `stickman-kino`)
- Kind: adapted
- Eligibility: adapted: our own wrapper plugin `plugins/stickman-kino` with its own skill that checks out the upstream at the reviewed commit inside the project after the user's yes, runs `npm ci` from the upstream lockfile and follows the upstream skills; the upstream plugin is not listed directly because `stickman setup` pip-installs `kokoro-onnx` and `soundfile` without versions and runs `apt-get download`, and its top-level `bin/` blocks claude.ai and Cowork installs
- Source: local wrapper ./plugins/stickman-kino (UPSTREAM.md names the reviewed commit)
- Reviewed on: 2026-11-07
- Reviewer: Claude (cloud project thread)
- Owner approval: "yes" from Kamil on 2026-11-07, quote: "Podaj mi ten adres tego repo i wprowadzaj to repo do toolboxa." (after the research on stickman repositories for Remotion and HyperFrames), then "ale właśnie może połączyć te stickmankino z tym poprzednią wiedzą z tamtego repo i razem wprowadzić coś takiego, nie?"; an explicit exception to the stabilisation stage

## What it is

A pipeline for stickman explainer, story and promo films drawn by a local engine: a Claude plugin (`.claude-plugin/plugin.json`) with four skills (`stickman-kino` router, `stickman-director`, `stickman-animator`, `stickman-sound`), a CLI (`bin/stickman.mjs`), an engine (`engine/sm-*.js`: rigged figures with 58 poses and IK, about 190 props, charts, kinetic type, camera, effects, environments, themes, transitions), a JSON schema, samples and docs. Rendering uses HyperFrames 0.8.43 and GSAP 3.15.0 from a lockfile; voice through Kokoro (via `hyperframes tts`), macOS `say`, espeak or the user's files; music and sound effects are synthesised procedurally. It credits kaomei/stickman-video-director (MIT) for its five-stage narrative arc and prompt contract, re-expressed without copied text. Eight commits, last 2026-10-08.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, stickman and faceless explainer videos (owner request 2026-11-07) | A ready stick-figure rig, prop library and voice-led pipeline rendered locally through HyperFrames, the route Studio already uses, with no video model or API key; Studio's HyperFrames and Remotion routes had no stick-figure rig | Source read; isolated Claude Code install of the wrapper and its skill listing checked (see Install tests); the clone, `npm ci`, Kokoro and renders NOT_RUN |

## Files reviewed

Upstream cloned as data into a temporary folder and checked out at the pinned commit; no scripts, hooks, installers or tests were run. Read: README.md, LICENSE, THIRD_PARTY_NOTICES.md, package.json, package-lock.json entries for hyperframes and gsap, .gitignore, the four SKILL.md files, bin/stickman.mjs (help and commands), lib/setup.mjs, lib/env.mjs, lib/audio.mjs (voice providers), and a scan of lib/ and scripts/ for URLs, downloads and API keys. HyperFrames 0.8.43 was unpacked from npm as data to see how `tts` loads Kokoro.

## What it installs and writes

The wrapper is five small files in the plugin cache. After the user's yes, its skill clones the upstream (about 85 MB) into `stickman-kino/` in the project at the reviewed commit and runs `npm ci` there (lockfile with integrity hashes; `ffmpeg-static` downloads its pinned ffmpeg binary during install). Films go to `stickman-films/<slug>/` in the project. Only on a second yes: a Python environment of about 200 MB in `stickman-kino/.stickman/venv` with `kokoro-onnx==0.6.1` and `soundfile==0.14.0`; HyperFrames then downloads the Kokoro v1.0 model files from the kokoro-onnx GitHub release on first use. If no Chrome or Chromium is found, HyperFrames can download its own browser, only after the user is asked. The wrapper never runs `stickman setup`, `npm link`, `npm install -g` or `install-skills`.

## Hooks

None (neither the wrapper nor the upstream).

## Network traffic

The one clone from github.com and npm during `npm ci` (plus the pinned ffmpeg binary), after the user's yes; the optional Kokoro packages from PyPI and model files from GitHub, after a separate yes. The CLI sets `HYPERFRAMES_NO_TELEMETRY=1` and `DO_NOT_TRACK=1` for every HyperFrames call. No other network calls found.

## Changes to prompts or tool results

None. Skills load by their descriptions.

## Data sent outside

None found.

## Requirements

git, Node.js 18+, Chrome or Chromium (or HyperFrames' own browser after a yes); optional Python 3 for Kokoro. No account, no API key, no desktop app.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-11-07 with Claude Code 2.1.319: `claude plugin marketplace add` of this repository, `claude plugin install stickman-kino@framecore-works-toolbox` succeeded, `claude plugin list` showed 1.0.0 enabled, cache 48 KB (wrapper); a headless `claude -p` session listed `stickman-kino:stickman-kino`.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result
- The wrapper's clone, `npm ci`, Kokoro and renders: NOT_RUN

## Risks

1. The upstream `setup` installs unpinned Python packages and system libraries; the wrapper replaces it, but a user who installs the upstream directly gets that behaviour.
2. The pinned Kokoro versions (`kokoro-onnx` 0.6.1, `soundfile` 0.14.0) were chosen at review time and not run with HyperFrames 0.8.43 (NOT_RUN).
3. Young single-author project (eight commits, last 2026-10-08); later commits need a new review before the pin moves.
4. The sample films advertise invented apps and numbers.

## Verdict

accept with conditions: listed only through our pinned wrapper; renders NOT_RUN.

## History

- 2026-11-07: added at d3d6653 (Toolbox 1.11.0).
