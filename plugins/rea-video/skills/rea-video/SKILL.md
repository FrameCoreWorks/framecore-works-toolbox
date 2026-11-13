---
name: rea-video
description: "Reverse engineer a reference video with rea-video by JuneYaooo (Apache-2.0), checked out at the reviewed commit: shot by shot, how the picture was made (live action, film clip, AI video, avatar, 3D, 2D or stop-motion animation, code or template render, screen recording, pan-and-zoom still), AI edits on live footage, the editing package (subtitle timing and style, titles, labels, stickers, picture in picture), voice, music and sound effects tied to picture events, cutting rhythm, lighting and grade, the real footage to collect, and a remake plan per shot, delivered as VIDEO.md, an HTML report, a storyboard and audio stems. Local Python and ffmpeg, no account or key. Use when the user gives a reference reel or ad and asks how it was made, whether it is AI, what footage it uses, or how to remake it or make one like it. Not for making the new video itself."
---

# rea-video (pinned)

rea-video is JuneYaooo's Apache-2.0 tool that takes a finished video apart: it splits it into
shots, measures each one (frame rate, motion, faces, overlays, OCR, audio stems) and writes a
breakdown an agent then checks by looking at the frames. This wrapper fetches it at the
reviewed commit, installs exact package versions in its own environment inside the project,
keeps its files in the project, and hands over to the upstream method.

Reviewed commit: `ab8580e38a1255425b0d3b481866590766932079` (rea-video 0.1.0, 2026-11-13).

## 1. Get the pinned checkout

1. Look for a folder `rea-video/` in the project holding `skills/rea-video/SKILL.md` and
   `.venv/bin/rea-video`. If one exists, run `git -C rea-video rev-parse HEAD`. The reviewed
   commit means it is ready. Another commit: tell the user which one and ask before checking
   out the reviewed one.
2. Needs git, ffmpeg with ffprobe, and Python 3.13 or 3.14 (the exact package set below was
   resolved for 3.13; 3.14 has the same wheels on a Mac). Name a missing one instead of
   installing it unasked; on a Mac, `brew install python@3.13 ffmpeg` after the user's yes.
3. No checkout: say in one line what will be written, then ask once. "I will download the
   rea-video repository at the commit FrameCore Works reviewed into `rea-video/` in this
   project (about 4 MB of code; its 70 MB of sample videos are skipped), create a Python
   environment there with exact package versions (about 410 MB), and on the first analysis it
   downloads about 220 MB of checked model files into `rea-video/.models/`. Nothing is
   installed elsewhere." On yes, from the project folder:

   ```bash
   git clone --filter=blob:none --no-checkout https://github.com/JuneYaooo/rea-video rea-video
   git -C rea-video sparse-checkout set --no-cone '/*' '!/docs/cases/'
   git -C rea-video checkout --detach ab8580e38a1255425b0d3b481866590766932079
   cat > rea-video/.framecore-constraints.txt <<'PINS'
   setuptools==84.2.1
   attrs==26.1.0
   certifi==2026.10.23
   charset-normalizer==3.5.2
   colorlog==6.12.0
   flatbuffers==25.12.19
   idna==3.20
   jsonschema==4.26.0
   jsonschema-specifications==2025.9.1
   numpy==2.5.4
   omegaconf==2.4.0
   onnxruntime==1.32.0
   opencv-python-headless==4.14.0.94
   packaging==26.3
   pillow==13.0.0
   protobuf==7.36.2
   pyclipper==1.4.0
   PyYAML==6.0.3
   rapidocr==3.10.0
   referencing==0.37.0
   requests==2.34.2
   rpds-py==2026.9.1
   shapely==2.2.0
   six==1.17.0
   tqdm==4.70.1
   typing_extensions==4.16.0
   urllib3==2.8.0
   videomd==1.2.0
   PINS
   python3.13 -m venv rea-video/.venv
   rea-video/.venv/bin/pip install -c rea-video/.framecore-constraints.txt setuptools
   rea-video/.venv/bin/pip install --no-build-isolation --only-binary :all: \
     -c rea-video/.framecore-constraints.txt -e "./rea-video[ocr]"
   ```

   Use `python3.14` instead when only 3.14 is installed.
4. Run every rea-video command with these variables, so its preferences and models stay in the
   project instead of the home folder:

   ```bash
   export REA_VIDEO_HOME="$PWD/rea-video/.home" REA_VIDEO_MODELS="$PWD/rea-video/.models"
   export PATH="$PWD/rea-video/.venv/bin:$PATH"
   ```

5. Never run the upstream `scripts/install_skill.sh` (it links the skill into `~/.claude`,
   `~/.codex` and `~/.agents`), `pip install "rea-video @ git+..."` without the commit,
   `git pull`, or the `[asr]` extra: they take unpinned code or write outside the project.
   Speech recognition is therefore off; dialogue comes from burned-in subtitles (OCR), the
   user's transcript, or the agent listening to `stems/vocals.wav` when it can.

## 2. Follow the upstream method

Read `rea-video/skills/rea-video/SKILL.md` and the files in `rea-video/skills/rea-video/references/`
that it points to, and follow them. They are written in Chinese; answer the user in their own
language and pass `--lang en` to `decompose` unless they want Chinese. Write outputs to
`rea-video-out/<name>/` in the project.

- Run `decompose` without `--vlm` and `--env-file`. As an agent that can see images, do the
  upstream's visual review (`review`, fill `review_answers.json`, `apply-review`): the
  upstream's own evaluation found that more accurate than an external vision model alone.
- Read the breakdown package the upstream way (`VIDEO.md`, then `video/timeline.md`, then single
  shots), never `breakdown.json` whole.
- Uncertain verdicts stay marked as uncertain with what is missing, as the upstream asks.

## 3. External vision model (optional, the user's own key)

The upstream can send each shot's frames and short clips to an OpenAI-compatible vision model
(Gemini, GPT-4o, Qwen-VL and others). Offer it only when the user asks for it or the result
needs it (motion and sound the agent cannot judge from stills). Say that the video's frames and
clips go to that provider and may cost money on their account, then ask. The user puts
`REA_VLM_BASE_URL`, `REA_VLM_API_KEY` and `REA_VLM_MODEL` in a `.env` file they own; pass it
with `--env-file` and `--vlm`. Never open or print that file or the key.

## 4. Remakes and paid tools

The upstream's remake route (`remake-plan`, `remake-run`) calls capsule-cinema, a separate
local project with its own model keys that charges per generation; `references/remake-tools.md`
also lists ChatCut, a hosted paid service, with a referral link. Do not recommend either by
default. Give the remake plan per shot, then hand it to the user's own route: when FrameCore
Works Creative Studio leads, its brief, prompt and review skills; FrameMotion for code-rendered
shots (titles, kinetic type, UI and data animation); FrameCut for the edit, captions and
assembly; Toolbox's Earshot for loudness and sound effects. Run `remake-run` only on the user's
explicit request, after `--dry-run` and their yes to the cost.

## 5. Rights and handoff

- rea-video is Apache-2.0 (NOTICE: Copyright 2026 JuneYaooo). Its models come from their
  own projects (UVR MDX-Net, BandIt v2, OpenCV YuNet, RapidOCR), each downloaded once and
  checked by SHA-256.
- The analysed video belongs to its owner. The breakdown is study material: a remake takes the
  structure and methods, not the footage, music, characters or brand of the original.
- Report what was checked: shots reviewed by eye, stems listened to or NOT_RUN, which
  verdicts stay uncertain, and that no external model was used unless the user chose one.
