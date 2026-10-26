# video-vision: install notes

- Upstream: https://github.com/jordanrendric/claude-video-vision
- Pinned commit: 4a4f99016f249a24018cd19b66531ebbcd58024b (version 1.4.0)
- Review: [reviews/video-vision.md](../reviews/video-vision.md)

## Install

See [install.md](install.md). Plugin id: `video-vision@framecore-works-toolbox`.

## Setup after install

Node (npx), ffmpeg; local Whisper or a Gemini/OpenAI key.

## What works where

Cowork and Claude Code (MCP, ffmpeg); chat: no.

## Use

Ask Claude to watch a video file; run its configure step first and pick the local Whisper backend.

Watch out: its MCP runs `claude-video-vision@latest` from npm; cloud audio backends send audio to Google or OpenAI.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall video-vision@framecore-works-toolbox`. Delete files it created in your projects if you no longer need them.
