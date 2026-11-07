# cutaway: install notes

- Upstream: https://github.com/Nyxera0x/cutaway
- Pinned commit: 5d8f1c6efe0ed65a8fc7647a7a2a3ee9fbb4d20a (version 1.0.0)
- Wrapper: [plugins/cutaway](../plugins/cutaway/) (our own skill; checks out the upstream at the pinned commit)
- Review: [reviews/cutaway.md](../reviews/cutaway.md)

## Install

See [install.md](install.md). Plugin id: `cutaway@framecore-works-toolbox`.

## Setup after install

None up front. On first use the skill asks once, then clones cutaway (about 16 MB) into `cutaway/` in the project at the pinned commit and runs `npm ci` there. Films need git, Node.js 20+, ffmpeg, Python 3 and Chrome or Chromium (or Playwright's own Chromium, about 170 MB, after a yes). A real GPU makes capture much faster; a cloud container renders in software.

## Best model

Works best with Claude Opus 5.5: the method runs long visual review loops, and the upstream reports about 450,000 tokens for one failed object. Review after still round 2.

## Reference pictures and extra graphics

Your own picture is the default. To generate one, or extra graphics such as a poster or thumbnail, the skill uses an image connector you already have, for example GPT Image 2.5 or another model, and says so before the first call (it may cost credits on your account). cutaway itself needs no account or API key.

## Narrator

Optional. Your own recording, a voice from Studio, or the local Kokoro engine: about 250 MB of Python packages (`kokoro-onnx==0.6.1`, `soundfile==0.14.0`) and about 355 MB of hash-checked model files in `cutaway/.narrator/`, asked separately. Kokoro does not speak Polish.

## What works where

Chat: skill only (reference prompt, checklist, plan). Cowork and Claude Code: skill plus builds and films. Codex and ChatGPT Work: the wrapper has a skill folder, so it can be saved as a private plugin; builds NOT_RUN.

## Use

Give a picture of a robotic animal, machine or device and ask for a 3D object that takes itself apart, an exploded view or a 20-second cutaway film.

## Watch out

Never run `npx skills add` or move the checkout off the pinned commit without a new review. The example creatures and product names are invented. Capture without a GPU is slow.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall cutaway@framecore-works-toolbox`, then delete the project's `cutaway/` folder (it also holds the optional narrator in `.narrator/`) and `cutaway-out/`. Playwright's Chromium, if downloaded, is in the Playwright cache (`~/Library/Caches/ms-playwright` on a Mac).
