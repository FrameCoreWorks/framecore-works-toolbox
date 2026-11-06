---
name: papercut-explainer
description: "Short vertical (9:16) cut-paper explainer reels with papercut-explainer by 0xS4N4TG (MIT), checked out at the reviewed commit: layered construction-paper props with drop shadows, rigid cut-out motion, stop-motion paper boil, a taped headline banner per beat and torn-paper captions, built in Remotion from a link (repo, product page, announcement) through strategy, hook, script, storyboard, build, voice and QA. Use for a papercut or cut-paper explainer, reel or short, or for that style prompt for another tool. Not for other motion styles."
---

# papercut-explainer (pinned)

papercut-explainer is 0xS4N4TG's MIT pipeline for cut-paper explainer reels, with nine
stage skills and a Remotion library. This wrapper only fetches it at the reviewed commit and
hands over to those skills.

Reviewed commit: `ff8223abc8136cc09e8d7e9b62ecb5d080c389e1` (library 0.1.0).

## 1. Get the pinned checkout

1. Look for an existing checkout: a folder `papercut-explainer/` in the project holding
   `library/env.sh`. If one exists, run `git -C papercut-explainer rev-parse HEAD`. The
   reviewed commit means it is ready. Another commit: tell the user which one it is and ask
   before checking out the reviewed one.
2. No checkout: say in one line what will be written, then ask once. "I will download the
   papercut-explainer repository (about 35 MB) into `papercut-explainer/` in this project,
   at the commit FrameCore Works reviewed. Script, storyboard and style prompts need nothing
   else; rendering needs Node.js 20+, ffmpeg and python3 with numpy and Pillow." On yes:

   ```bash
   git clone https://github.com/0xS4N4TG/papercut-explainer papercut-explainer
   git -C papercut-explainer checkout --detach ff8223abc8136cc09e8d7e9b62ecb5d080c389e1
   ```

3. In every shell command that uses the library, set
   `export PAPERCUT_LIB="$PWD/papercut-explainer/library"` first (an environment value wins
   over any config file).
4. Never `git pull`, switch to `main`, or run `install.sh` in any mode that installs skills,
   the Remotion agent skills (`npx skills@latest add remotion-dev/skills`, unpinned) or links
   into home folders. Do not run `papercut-setup`. For Remotion craft use Creative Studio's
   Remotion skill when it is installed.

## 2. Follow the upstream skills

Read `papercut-explainer/skills/papercut-explainer/SKILL.md` and follow it. Whenever it
names a stage skill (`papercut-strategy`, `papercut-hook`, `papercut-script`,
`papercut-storyboard`, `papercut-build`, `papercut-voice`, `papercut-qa`), read
`papercut-explainer/skills/<name>/SKILL.md` from the checkout and follow it. Skip any step
that clones the repository or runs the installer: the pinned checkout replaces it.

- Rendering: `library/new_episode.sh` runs `npm install` from the template's lockfile (Remotion
  4.0.530) inside the new episode folder. Check `node --version` (20 or newer), `ffmpeg` and
  `python3 -c "import numpy, PIL"` first; name anything missing and stop.
- Scene agents: where the upstream hands scenes to the `papercut-scene` agent, build the
  scenes yourself, or give a subagent `papercut-explainer/agents/papercut-scene.md` as its
  instructions.
- Voice: the placeholder voice or the user's own recording needs no install. The local
  Qwen3-TTS voice is a separate download of several GB (a Python environment in
  `~/.local/share/papercut-explainer` and a model in the Hugging Face cache): state the size
  and ask before running
  `./install.sh --mode custom --components tts --target claude --project "$PWD" --yes`
  from inside `papercut-explainer/`.

## 3. Rights and handoff

- Code, sound effects, music beds and textures are MIT. Remotion is source-available under
  its own licence: companies above its size threshold need a paid Remotion licence.
- Sixteen bundled backdrops were made with an AI image model; they may not carry enforceable
  copyright. The four fonts are SIL OFL 1.1.
- Every product, company and number in the upstream examples is invented: never reuse them.
- When FrameCore Works Creative Studio leads the project, it keeps the brief, copy locks and
  review; this skill builds the reel and reports the files, length, voice route and what was
  checked (stills looked at, render watched or NOT_RUN).
