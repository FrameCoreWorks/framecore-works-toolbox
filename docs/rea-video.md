# rea-video: install notes

- Upstream: https://github.com/JuneYaooo/rea-video
- Pinned commit: ab8580e38a1255425b0d3b481866590766932079 (version 0.1.0)
- Wrapper: [plugins/rea-video](../plugins/rea-video/) (our own skill; checks out the upstream at the pinned commit)
- Review: [reviews/rea-video.md](../reviews/rea-video.md)

## Install

See [install.md](install.md). Plugin id: `rea-video@framecore-works-toolbox`.

## Setup after install

None up front. On first use the skill asks once, then clones rea-video into `rea-video/` in the project at the pinned commit without its sample videos, and installs exact Python package versions in `rea-video/.venv` (about 410 MB). The first analysis downloads about 220 MB of hash-checked models into `rea-video/.models/`. Needs git, ffmpeg and Python 3.13 or 3.14.

## What you get

For each shot of a reference video: how the picture was made (live action, film clip, AI video, avatar, 3D, 2D or stop-motion animation, code or template render, screen recording, pan-and-zoom still), AI edits on live footage, subtitles and titles with timing and style, stickers, voice, music and sound effects tied to picture events, cutting rhythm, framing, lighting and grade, the real footage you would need, and a remake plan. Files: `VIDEO.md` with a shot timeline, `report.html`, a storyboard, an audio picture and separated stems, in `rea-video-out/` in the project.

## Vision model

Optional. Claude reviews the shots by eye by default. An external vision model (OpenAI-compatible: Gemini, GPT-4o, Qwen-VL and others) can add motion and sound judgements; it needs your own key in a `.env` file you keep, sends the video's frames and clips to that provider and may cost money there. The skill asks first.

## What works where

Chat: skill only (method and checklist, no analysis). Cowork and Claude Code: skill plus analysis. Codex and ChatGPT Work: the wrapper has a skill folder, so it can be saved as a private plugin; analysis NOT_RUN.

## Use

Give a reference reel, ad or clip and ask how it was made, whether it is AI, what footage it uses, or how to make one like it. Studio can take the shot list into a brief; FrameMotion builds the code-rendered shots and FrameCut the edit and captions.

## Watch out

Never run the upstream `scripts/install_skill.sh`, an unpinned `pip install ... @ git+...`, `git pull` or the `[asr]` extra without a new review. The upstream skill text is in Chinese. Remakes through capsule-cinema or ChatCut cost money and are not the default. The analysed video belongs to its owner: take its structure and methods, not its footage, music or brand.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall rea-video@framecore-works-toolbox`, then delete the project's `rea-video/` folder (it holds the environment, models and preferences) and `rea-video-out/`. Nothing is written outside the project.
