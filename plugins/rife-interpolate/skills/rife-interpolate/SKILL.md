---
name: rife-interpolate
description: "Smooth or slow down video with RIFE frame interpolation (TNTwise/rife-ncnn-vulkan, pinned release 20250112, model rife-v4.26 by default): raise the frame rate of footage (24 or 30 to 60 fps), make slow motion from normal footage, or fill in a low-frame-rate render such as a Blender preview. Runs locally on the graphics card through Vulkan (Apple Silicon and Intel Macs, Linux), no account or key. Use when the user asks to smooth, interpolate, upscale the frame rate, make slow motion or remove judder. Not for animation rendered from code that can simply be rendered at the target frame rate, and not for upscaling resolution."
---

# RIFE frame interpolation (pinned)

This plugin is a FrameCore Works wrapper. The program is
[TNTwise/rife-ncnn-vulkan](https://github.com/TNTwise/rife-ncnn-vulkan)
(MIT, release `20250112`, commit `5eea93c`), a fork of nihui/rife-ncnn-vulkan
with RIFE models up to v4.26. Nothing from upstream is stored in this plugin:
the launcher downloads the pinned release on request.

Launcher: `scripts/rife.py` next to this file (Python 3 standard library,
plus ffmpeg and ffprobe for video). Every command prints one JSON object.

## 1. Decide whether RIFE is the right tool

- Footage, screen recordings and renders that are expensive to redo: yes.
- Motion graphics rendered from code (HyperFrames, Remotion, canvas): render
  again at the target frame rate instead; that is exact and has no artifacts.
- Resolution upscaling is a different job; say so.
- Hard cases for any interpolator: fast motion, motion blur, small text,
  UI elements, hands and crossing objects, scene cuts. Warn the user before
  the run when the clip has them.

## 2. Check and install (only after a yes)

1. `python3 scripts/rife.py status`. If `installed`, go to step 3.
2. `python3 scripts/rife.py plan` and tell the user, in their language: the
   download size (about 830 MB, once), where it goes (outside the project,
   `~/.cache/framecore/rife/20250112`, about 45 MB kept), the SHA-256 check,
   and that the archive is deleted after unpacking.
3. Only after the user's yes: `python3 scripts/rife.py install --yes`.
   Another model: `--models rife-v4.26,rife-v4.6`.

Supported hosts: macOS (universal binary) and Linux x86_64. Other hosts get
`unsupported_host`; say so and offer ffmpeg's `minterpolate` as a weaker
fallback (faster, but edges tear on fast motion).

**Cloud or Linux without a graphics card.** `status` shows `vulkan`. When it
is `missing`, RIFE cannot start: ask the user, then install Mesa's software
Vulkan driver, `apt-get install -y mesa-vulkan-drivers libvulkan1` (with
`sudo` when not root; in a cloud session it lasts for that session). Vulkan
then runs on the CPU (llvmpipe). Never use the program's own CPU switch
`-g -1`: in our test it wrote garbage in-between frames. CPU time, 4 cores,
540x960: about 1.4 s per output frame with `rife-v4.6`, about 1.9 s with
`rife-v4.26`; 1080x1920 about four times that, so a 23 s clip at 60 fps takes
about 35 minutes at 540x960 and about 2 hours at full HD. Before a long cloud
run, say how long it will take and offer the Mac (much faster on Apple
Silicon), a preview at `--max-height 960`, or `rife-v4.6`.

## 3. Run

- Smoother playback, same duration:
  `python3 scripts/rife.py run IN.mp4 OUT.mp4 --fps 60` (or `--factor 2`).
  The original sound is copied.
- Slow motion: `python3 scripts/rife.py run IN.mp4 OUT.mp4 --factor 4 --slowmo`
  keeps the frame rate, so the clip plays four times slower. The original
  sound is dropped; plan new sound.
- 24 or 25 to 60 fps is not a whole multiple: only `rife-v4*` models make
  frames at any time step; the launcher refuses an older model there.
- Options: `--model rife-v4.6` (lighter, faster), `--max-height 960`
  (preview), `--uhd` (forced on above 2000 px), `--keep-frames`, `--crf 16`.

Cut the clip to the shot first: interpolation across a scene cut mixes the
two pictures. One shot per run, never a whole edit; put the shots back
together afterwards. Add captions, titles and watermarks after
interpolation, never before. The sound stays the original's, unchanged.
When you script several shots, give every ffmpeg call `-nostdin`: in a
`while read` loop ffmpeg otherwise reads the list and every second shot
breaks.

## 4. Check the frames before you hand it over

Make a strip with
`python3 scripts/rife.py sheet OUT.mp4 SHEET.png --at SECONDS` (three
consecutive output frames; in a 2x run source, new, source) at the fastest moment, at text and at edges. Look at it.
Report what you checked and any warping, ghosting or broken text. If a
part is bad, use the original frames there or a lower factor.

## Report

State the model, source and output frame rates, frames in and out, what
happened to the sound, where the file is and what the frame check showed.
Never call a run checked when you did not look at the frames.
