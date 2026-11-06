# motion-launch-videos: install notes

- Upstream: https://github.com/Kimeur/motion-launch-videos
- Pinned commit: 5092579bc9aaeb0e3547ded0980a93404d2dc906 (version 2.3.0)
- Review: [reviews/motion-launch-videos.md](../reviews/motion-launch-videos.md)

## Install

See [install.md](install.md). Plugin id: `motion-launch-videos@framecore-works-toolbox`.

## Setup after install

On first render the skill runs `render.mjs doctor` and shows what is missing: usually `npm install --prefix` in the skill folder (playwright-core 1.63.0) and a Chromium download. Needs Node 20+ and ffmpeg.

## What works where

Chat: skills only (no renders). Cowork and Claude Code: skills plus renders. Codex and ChatGPT Work: NOT_RUN.

## Use

Ask for a product launch video, a promo, an animated chart, captions, or a 3D, globe or particle shot rendered to MP4.

## Watch out

`motion-story` calls unpinned `npx hyperframes` for voice and transcripts; pin a version or skip it.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall motion-launch-videos@framecore-works-toolbox`; delete the Playwright Chromium cache if nothing else uses it.
