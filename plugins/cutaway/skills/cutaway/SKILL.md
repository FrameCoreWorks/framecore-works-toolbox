---
name: cutaway
description: "Robotic cutaway films from one reference picture with cutaway by Nyxera0x (MIT), checked out at the reviewed commit: a robotic animal, machine or device rebuilt as a three.js object written in code, matched to the picture with a graded checklist and measured proportions, a page with a button for every part, and a 60 fps film where each part comes apart under its own camera, then the whole object explodes and snaps back, with a synced procedural score at -14 LUFS. Reference pictures can come from the user's own image connector (for example GPT Image 2.5); an optional local Kokoro narrator. Works best with Claude Opus 5.5. Use for a cutaway, an exploded view, a robot animal or machine that takes itself apart, or a product teardown film from an image. Not for flat diagrams or isometric explainers."
---

# cutaway (pinned)

cutaway is Nyxera0x's MIT skill, built on whaleyxbt/claude-motion (MIT), that turns one
picture into a three.js object that takes itself apart on camera. This wrapper only fetches
it at the reviewed commit, keeps its setup to pinned steps, adds the optional narrator, and
hands over to the upstream method.

Reviewed commit: `5d8f1c6efe0ed65a8fc7647a7a2a3ee9fbb4d20a` (cutaway 1.0.0, 2026-11-06).

## Model

The method needs long visual review loops (stills against the reference, sheets of frames).
It works best with Claude Opus 5.5. On a smaller model, say once that results and the number
of rounds may suffer. The upstream's own notes report about 430,000 to 450,000 tokens for one
object that failed, so stop after round 2 for the user's review, as the upstream asks.

## 1. Get the pinned checkout

1. Look for a folder `cutaway/` in the project holding `SKILL.md` and `sims/build.mjs`. If one
   exists, run `git -C cutaway rev-parse HEAD`. The reviewed commit means it is ready. Another
   commit: tell the user which one and ask before checking out the reviewed one.
2. No checkout: say in one line what will be written, then ask once. "I will download the
   cutaway repository (about 16 MB) into `cutaway/` in this project, at the commit FrameCore
   Works reviewed, and install its locked Node packages there (three.js, esbuild, Playwright,
   two fonts). Nothing is installed elsewhere." On yes:

   ```bash
   git clone https://github.com/Nyxera0x/cutaway cutaway
   git -C cutaway checkout --detach 5d8f1c6efe0ed65a8fc7647a7a2a3ee9fbb4d20a
   (cd cutaway && npm ci --no-fund --no-audit)
   ```

3. Browser: prefer an installed Chrome or Chromium through the `CHROMIUM` variable (on a Mac
   `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`). If there is none, say that
   Playwright will download its own Chromium (about 170 MB, into the user's Playwright cache)
   and ask before `(cd cutaway && npx playwright install chromium)`.
4. Films also need `ffmpeg` on PATH and Python 3 (standard library only). Name a missing one
   instead of installing it unasked.
5. Never run `npx skills add`, `npm install`, `git pull` or switch to `main`: they take
   unpinned code.

## 2. Follow the upstream method

Read `cutaway/SKILL.md`, then the four files in `cutaway/docs/` (`JOB_DESCRIPTION.md`,
`CHECKLIST.md`, `PROMPTS.md`, `LESSONS.md`), and follow them. Where the upstream writes
`$SKILL_DIR`, use the `cutaway/` folder. Builds and renders go to `./cutaway-out` of the
folder you run from; keep that in the project.

- Start a new object from the example with the closest body (tarantula, piranha, wasp) and
  keep its choreography; flag an object with no close body before starting.
- Stop after still round 2 and show the user the stack and the grades. Film nothing before
  their yes.
- Never report a film as done without reading the frame sheets of the current render.

## 3. Reference pictures and extra graphics

The upstream rebuilds one reference picture and never imports it.

- The user's own picture is the default.
- With no picture, or for extra graphics (a poster, a thumbnail, part close-ups), use an image
  generator the user already has as a connector, for example GPT Image 2.5 or another
  model, with the prompt in `cutaway/docs/PROMPTS.md`. Say which connector and model will be
  used, and that generations may cost credits on the user's account, before the first call.
- No connector: give the user the prompt to paste into the image tool they use. cutaway itself
  needs no account and no API key.

## 4. Narrator (optional, local Kokoro)

The upstream film has a score but no voice. Ask before adding one:

- the user's own recording, or a voice made with Studio's voice and narration route, saved as
  files;
- no voice (the default: the score carries the film);
- the local Kokoro voice. Kokoro speaks English, Spanish, French, Italian, Portuguese, Hindi,
  Japanese and Mandarin, not Polish. State that it creates a Python environment of about
  250 MB in `cutaway/.narrator/venv` and downloads about 355 MB of model files, then ask. On
  yes, from inside `cutaway/`:

  ```bash
  python3 -m venv .narrator/venv
  .narrator/venv/bin/pip install "kokoro-onnx==0.6.1" "soundfile==0.14.0"
  mkdir -p .narrator/models
  curl -L -o .narrator/models/kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
  curl -L -o .narrator/models/voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
  ```

  Check the files before first use and delete them on a mismatch:
  `kokoro-v1.0.onnx` sha256 `7d5df8ecf7d4b1878015a32686053fd0eebe2bc377234608764cc0ef3636a6c5`,
  `voices-v1.0.bin` sha256 `bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d`.

  Write one line per beat of the film's `timeline.json`, render each with
  `Kokoro(".narrator/models/kokoro-v1.0.onnx", ".narrator/models/voices-v1.0.bin").create(text, voice=..., speed=1.0, lang=...)`
  into WAV files in `cutaway-out/`, and place each at its beat time. Keep the line shorter than
  its beat; lengthen the beat in the timeline rather than rushing the voice. Duck the score
  under the voice, mix with ffmpeg and master the result to -14 LUFS with true peak at most
  -1 dBTP (Toolbox's Earshot can measure it).

## 5. Rights and handoff

- Code is MIT (Nyxera0x, whaleyxbt); recorded samples are CC0 (sources in
  `cutaway/sfx/samples/SOURCES.md`); fonts Inter and JetBrains Mono are SIL OFL 1.1. The
  example creatures and product names (Theraphos TH-8, Serrasal PX-7, Vespion VX-9) are
  the upstream's inventions: do not present them as a client's products.
- A reference picture of a real product or brand needs the user's right to use it.
- When FrameCore Works Creative Studio leads the project, it keeps the brief, copy locks and
  review; this skill builds the object and film and reports the files, length, format, voice
  route and what was checked (still rounds and grades, frame sheets read, render watched or
  NOT_RUN).
