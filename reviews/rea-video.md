# Review: rea-video

## Entry

- Name: rea-video
- Status: active
- Upstream: https://github.com/JuneYaooo/rea-video
- Author: JuneYaooo (June)
- License: Apache-2.0 (code, skill and docs; NOTICE: Copyright 2026 JuneYaooo). Downloaded models keep their own projects' licences (UVR MDX-Net, BandIt v2, OpenCV YuNet, RapidOCR); the sample videos in `docs/cases/` are third-party clips (TikTok, Douyin and AI remakes) not covered by the repository licence
- Commit: ab8580e38a1255425b0d3b481866590766932079
- Upstream version: 0.1.0 (pyproject.toml, .claude-plugin/plugin.json)
- Kind: adapted
- Eligibility: adapted: our own wrapper plugin `plugins/rea-video` with its own skill that checks out the upstream at the reviewed commit inside the project after the user's yes, installs exact package versions in `rea-video/.venv` and follows the upstream method; the upstream plugin (it ships `.claude-plugin/plugin.json` and `marketplace.json`) is not listed directly because its documented install takes the current default branch with open version ranges, `scripts/install_skill.sh` links the skill into `~/.claude`, `~/.codex` and `~/.agents`, and its first run writes to `~/.rea-video` and `~/.cache/rea-video`
- Source: local wrapper ./plugins/rea-video (UPSTREAM.md names the reviewed commit)
- Reviewed on: 2026-11-13
- Reviewer: Claude (cloud project thread)
- Owner approval: "yes" from Kamil on 2026-11-13, quote: "Dodaj też to jako dodatek do toolboxa. No i też do motion video." Given with the request, before the verdict; the optional external vision model (frames and clips sent to a provider) stays off unless the user brings their own key and says yes

## What it is

One skill (`skills/rea-video/SKILL.md`, 16 KB, Chinese, with nine reference files) plus a Python CLI package `rea_video` (about 60 modules). From a video it detects shots, then per shot measures frame rate, motion, faces (YuNet), overlays and subtitles (RapidOCR), colour, lighting and framing, separates voice, music and effects (UVR MDX-Net, BandIt v2 through onnxruntime), and writes `VIDEO.md` with a per-shot timeline, `report.html` and `report.md`, `breakdown.json`, a storyboard, an audio picture, shot contact sheets and stems. The agent then reviews shots by eye (`review`, `apply-review`), which the upstream's own evaluation (`eval/RESULTS.md`) found more accurate than an external vision model alone. A remake planner maps shots to generation units, shoots or code renders. Very active: the reviewed commit is from the day of the review.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio and FrameMotion, reels made "like this reference" (owner request 2026-11-13) | A measured shot list of a reference reel (shot types, cut rhythm, subtitle timing and style, sound effect placement, footage to collect) that a brief and a FrameMotion or FrameCut build can start from, instead of an agent watching the reel frame by frame without tools | Source read; the pinned install procedure ran in a Linux sandbox with Python 3.13 (exact versions, nothing extra installed); Mac arm64 wheels for Python 3.13 and 3.14 confirmed on PyPI; the analysis itself NOT_RUN. Owner added it before a breakdown was shown |

## Files reviewed

Upstream cloned as data into a temporary folder at the pinned commit; no upstream scripts, installers, CLI commands or tests were run. Read: README.md, LICENSE, NOTICE, `.claude-plugin/plugin.json` and `marketplace.json`, pyproject.toml, `scripts/install_skill.sh`, SKILL.md, `references/setup.md` and `remake-tools.md`, `rea_video/memory.py`, `vlm.py`, `util.py`, the model loaders (`stems.py`, `effects.py`, `faces.py`, `overlay.py`, `speech.py`, `speakers.py`) and `integrations/run_remake.py`, plus a scan of every module for URLs, network calls, child processes, environment variables and home-directory paths. The wheels of `videomd` 1.2.0 and `rapidocr` 3.10.0 were unpacked to check their licences and model downloads. The wrapper's install (sparse clone, venv, constrained pip install) was run once in a sandbox; it builds the package with setuptools from `pyproject.toml` only and runs no upstream code.

## What it installs and writes

The wrapper is six small files in the plugin cache. After the user's yes, its skill clones the upstream into `rea-video/` in the project at the reviewed commit with `docs/cases/` (about 70 MB of sample videos) left out (about 4 MB), writes our constraints list to `rea-video/.framecore-constraints.txt`, creates `rea-video/.venv` (Python 3.13 or 3.14) and installs the package with the OCR extra and 27 exact dependency versions (numpy 2.5.4, opencv-python-headless 4.14.0.94, onnxruntime 1.32.0, rapidocr 3.10.0, videomd 1.2.0 and their dependencies; about 410 MB), build isolation off and wheels only. `REA_VIDEO_HOME` and `REA_VIDEO_MODELS` point at `rea-video/.home` and `rea-video/.models`. On the first analysis the tool downloads its models into `rea-video/.models` (UVR MDX-Net about 67 MB, BandIt v2 about 149 MB, YuNet) and RapidOCR's models into the venv, each checked by a SHA-256 written in the code. Outputs go to `rea-video-out/` in the project.

## Hooks

None (neither the wrapper nor the upstream).

## Network traffic

The clone from github.com and the package downloads from PyPI, after the user's yes. Model files on first use: GitHub releases (TRvlvr/model_repo, xuankhanh/MediaDownloader, opencv/opencv_zoo at a fixed commit) and modelscope.cn (RapidOCR), all hash-checked. The optional vision model: frames and short clips of each shot (up to 60 calls by default) to the OpenAI-compatible endpoint the user configures, only with `--vlm` and their own key. No telemetry or analytics found.

## Changes to prompts or tool results

None. The skill loads by its description.

## Data sent outside

None by default. With the optional vision model, the analysed video's frames, clips and audio go to the user's chosen provider. The upstream remake route (`remake-run`) sends prompts and reference images to video models through capsule-cinema with the user's keys; the wrapper never runs it unasked.

## Requirements

git, ffmpeg with ffprobe, Python 3.13 or 3.14. No account and no API key are required. Optional: an OpenAI-compatible vision model with the user's own key; Chrome or Chromium for `rea-video pdf`.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): see `docs/verification.md`, Toolbox 1.15.0
- The wrapper's pinned install procedure: PASS 2026-11-13 in a Linux cloud sandbox with Python 3.13.x (clone and install took 17 s; `pip freeze` equals the constraints list plus the package); on a Mac NOT_RUN
- Analysis of a video, model downloads, visual review, vision model, remake: NOT_RUN
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Very young and fast-moving project (created in November 2026, new commits daily); later commits need a new review before the pin moves.
2. The upstream skill and reports default to Chinese; the wrapper asks for `--lang en` and answers in the user's language.
3. The upstream skill tells agents to list capsule-cinema and ChatCut (a paid hosted service, through a referral link) at the end of replies about remakes; the wrapper overrides that and routes remakes to the user's own tools.
4. Speech recognition (`[asr]`, sherpa-onnx with an open version range) is left out; dialogue without subtitles depends on the agent listening to the vocal stem or the user's transcript.
5. The `docs/cases/` sample videos are third-party clips; they are not downloaded and must not be reused.
6. Overlaps nothing in Toolbox; Studio's cinematography and storyboard skills describe shots in words, this tool measures them.

## Verdict

accept with conditions: listed only through our pinned wrapper with exact package versions; analysis NOT_RUN.

## History

- 2026-11-13: added at ab8580e (Toolbox 1.15.0).
