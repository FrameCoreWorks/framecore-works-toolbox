# rife-interpolate: install notes

- Upstream: https://github.com/TNTwise/rife-ncnn-vulkan (fork of nihui/rife-ncnn-vulkan)
- Pinned commit: 5eea93c6e7079dda69d7a0ce9c1106ff5e641143 (release 20250112)
- Review: [reviews/rife-interpolate.md](../reviews/rife-interpolate.md)

## Install

See [install.md](install.md). Plugin id: `rife-interpolate@framecore-works-toolbox`.
Installing the plugin installs only the skill and launcher. The program
(about 830 MB download, about 45 MB kept) downloads when you first use it,
after your yes.

## Codex

`plugins/rife-interpolate/` carries `.codex-plugin/plugin.json`. Install that
directory through the Codex host's local plugin route on the user's request.
Codex activation and a Codex run remain NOT_RUN.

## Setup after install

Python 3, ffmpeg and ffprobe. macOS (Apple Silicon or Intel) or Linux x86_64.

## What works where

Claude Code on a Mac (graphics card through Metal) and Linux; Claude Code
cloud after installing Mesa's software Vulkan driver (`mesa-vulkan-drivers`,
`libvulkan1`, after your yes), on the CPU: about 1.4 s (rife-v4.6) to 1.9 s
(rife-v4.26) per output frame at 540x960 on 4 cores, four times that at full
HD. Cowork Unknown; chat: skill only, no run.

## Use

Ask to smooth a clip, raise its frame rate or make slow motion. The skill
checks status, shows the download plan, installs after your yes, runs
`scripts/rife.py run` and checks the frames with `scripts/rife.py sheet`.

## Watch out

Interpolation invents frames: check fast motion, text and edges. Cut to one
shot per run; captions and watermarks go on after it; the sound stays the
original's. Never use the program's `-g -1` CPU switch (garbage frames in our
test); the launcher does not. Motion rendered from code is better rendered again at the
target frame rate.

## Full removal

Remove it in Customize > Plugins or with
`claude plugin uninstall rife-interpolate@framecore-works-toolbox`, then
delete `~/.cache/framecore/rife`.
