---
name: stickman-kino
description: "Stickman (stick-figure) explainer, story and promo films rendered locally as code with stickman-kino by Prerit Ahuja (MIT), checked out at the reviewed commit: script and storyboard, rigged figures with 58 poses and IK, about 190 props, charts, kinetic text, captions, camera moves and transitions in HyperFrames and GSAP, a local voice (your recording, macOS say, espeak or an optional Kokoro install), procedural music and sound effects, checked and rendered to MP4 in 16:9, 9:16 or 1:1. No video model, no API key. Use for a stickman or stick-figure video, a whiteboard-style explainer or a faceless YouTube, Shorts, Reels or TikTok clip in that style. Not for other animation styles."
---

# stickman-kino (pinned)

stickman-kino is Prerit Ahuja's MIT pipeline for stickman films drawn by a local engine
(HyperFrames + GSAP), with four skills of its own. This wrapper only fetches it at the
reviewed commit, keeps its setup to pinned steps, and hands over to those skills.

Reviewed commit: `d3d665301c0b62f04c885785e6bd6044de0785c6` (stickman-kino 1.0.0).

## 1. Get the pinned checkout

1. Look for an existing checkout: a folder `stickman-kino/` in the project holding
   `bin/stickman.mjs`. If one exists, run `git -C stickman-kino rev-parse HEAD`. The
   reviewed commit means it is ready. Another commit: tell the user which one it is and ask
   before checking out the reviewed one.
2. No checkout: say in one line what will be written, then ask once. "I will download the
   stickman-kino repository (about 85 MB) into `stickman-kino/` in this project, at the
   commit FrameCore Works reviewed, and install its locked Node packages there
   (HyperFrames 0.8.43, GSAP, a static ffmpeg). Nothing is installed elsewhere." On yes:

   ```bash
   git clone https://github.com/dsauce/stickman-kino stickman-kino
   git -C stickman-kino checkout --detach d3d665301c0b62f04c885785e6bd6044de0785c6
   (cd stickman-kino && npm ci --no-fund --no-audit)
   ```

3. Check the tools with `node stickman-kino/bin/stickman.mjs doctor`. Node.js 18 or newer
   and git are required. If it finds no browser, point it at an installed Chrome or
   Chromium with `HYPERFRAMES_BROWSER_PATH` (on a Mac:
   `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`). If there is none, name
   the gap and ask before letting HyperFrames download its own browser.
4. Never run `stickman setup`, `npm install`, `npm link`, `npm install -g`, `git pull` or
   switch to `main`. `setup` installs the voice engine without a pinned version and fetches
   system packages; step 3 and section 3 replace it.

## 2. Follow the upstream skills

Read `stickman-kino/skills/stickman-kino/SKILL.md` and follow its pipeline. Whenever it
names `stickman-director`, `stickman-animator` or `stickman-sound`, read
`stickman-kino/skills/<name>/SKILL.md` from the checkout and follow it. Engine API and
recipes are in `stickman-kino/docs/`, examples in `stickman-kino/samples/`.

- The upstream "Kino home" is the `stickman-kino/` folder; run its CLI as
  `node stickman-kino/bin/stickman.mjs <command>`.
- Put each film in the project, `stickman-films/<slug>/`, not inside the checkout, unless
  the user names another place. Skip the upstream's toolchain step that calls `setup`.
- The upstream's "never claim success without looking" rule stands: `check` passed,
  snapshots and contact sheets opened and looked at, render finished.

## 3. Voice

The default voice in `film.json` is Kokoro, which this wrapper does not install up front.
Ask which voice route the user wants before the first `stickman audio`:

- the user's own recording (`voice.provider: "files"`), or a voice made with Studio's voice
  and narration route and saved as files;
- `say` on a Mac or `espeak` (nothing to install on a Mac);
- `none` (captions and music carry the film);
- the local Kokoro voice: state that it creates a Python environment of about 200 MB in
  `stickman-kino/.stickman/venv` and downloads the Kokoro v1.0 model files on first use,
  then ask. On yes, from inside `stickman-kino/`:

  ```bash
  python3 -m venv .stickman/venv
  .stickman/venv/bin/pip install "kokoro-onnx==0.6.1" "soundfile==0.14.0"
  ```

Voice and music are generated per clip and cached; clip lengths follow the real voice.

## 4. Rights and handoff

- Code, engine and generated music and effects are MIT; the bundled fonts are SIL OFL 1.1;
  GSAP is under GreenSock's no-charge standard licence; HyperFrames is Apache-2.0. Music
  the user supplies must be cleared by them.
- The upstream sample films advertise invented apps and numbers: never reuse them as facts.
- Do not imitate a specific creator's or channel's character design for client work.
- When FrameCore Works Creative Studio leads the project, it keeps the brief, script and copy
  locks and the review; this skill builds the film and reports the files, length, format,
  voice route and what was checked (`check` result, contact sheets looked at, render watched
  or NOT_RUN).
