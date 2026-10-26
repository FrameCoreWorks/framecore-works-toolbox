# animate: install notes

- Upstream: https://github.com/cth9191/animate
- Pinned commit: 7e5eb56feb2dd573f890e1b7b34748af43d58263 (version 0.4.0)
- Review: [reviews/animate.md](../reviews/animate.md)

## Install

See [install.md](install.md). Plugin id: `animate@framecore-works-toolbox`.

## Setup after install

On the computer that renders (Claude Code or Cowork):

```bash
npm i -g playwright && npx playwright install chromium
# ffmpeg and ffprobe on PATH (for example: brew install ffmpeg)
pip install faster-whisper   # optional, times each word of a voice-over
```

For a voice-over, connect ElevenLabs in Claude (Settings > Connectors), or the
system voice is used (`say`, PowerShell or `espeak`).

## What works where

| Component | Chat | Cowork | Claude Code |
| --------- | ---- | ------ | ----------- |
| Skill `animate` (plan, story, look, storyboard) | yes | yes | yes |
| Rendering to MP4 (Node, Playwright, ffmpeg) | Unknown | yes, if the tools are installed | yes, if the tools are installed |

## Use

Describe the video, for example "a narrated 45s explainer of how DNS works,
math style, 16:9", or call `/animate:animate`. It asks intake questions, then
shows story, look and storyboard for approval before it renders. Output goes
to the piece folder in your project.

## Full removal

Remove it in Customize > Plugins, or run
`claude plugin uninstall animate@framecore-works-toolbox`. Delete the piece
folders it created in your projects if you no longer need them.
