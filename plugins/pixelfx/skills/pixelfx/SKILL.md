---
name: pixelfx
description: "Pixel art effects and sprite animations with pixelfx by Patch (MIT), checked out at the reviewed commit: 244 ready effects (fire, explosions, water, ice, lightning, magic, melee hits, projectiles, UI, pickups, transitions, critters) to recolor, mirror, export as sprite sheets for Godot, Unity or Phaser, or render as GIF/MP4, and the draft, render, look, refine loop for new ones with a body that winds up, freezes on contact and recovers. Use for pixel VFX, game juice, sprite sheets or a pixel effect inside a video. Not for non-pixel motion graphics."
---

# pixelfx (pinned)

pixelfx is Patch's MIT library of pixel art effects written as code, with its own skill.
This wrapper only fetches it at the reviewed commit and hands over to that skill.

Reviewed commit: `a84159688af3ca37a4be05a0d422b94451b2e24e` (pixelfx 0.3.0).

## 1. Get the pinned checkout

1. Look for an existing checkout: a folder `pixelfx/` in the project, or the working
   directory itself, holding `tools/render.mjs`. If one exists, run
   `git -C <folder> rev-parse HEAD`. The reviewed commit means it is ready. Another commit:
   tell the user which one it is and ask before checking out the reviewed one.
2. No checkout: say in one line what will be written, then ask once. "I will download the
   pixelfx repository (about 40 MB with its history) into `pixelfx/` in this project, at
   the commit FrameCore Works reviewed. It runs on Node.js only; nothing is installed
   elsewhere." On yes:

   ```bash
   git clone https://github.com/patch-gg/pixelfx pixelfx
   git -C pixelfx checkout --detach a84159688af3ca37a4be05a0d422b94451b2e24e
   ```

3. Check the tools: `node --version` must be 18 or newer. ffmpeg is needed only for
   `--gif` and `--mp4`. If git, Node or the network is missing, say which and stop.
4. Never `git pull`, switch to `main`, run `npm install`, `npm ci` or
   `tools/build-gallery.mjs` (the gallery build is the only part with npm dependencies).
   The render, check, list, act and new tools need nothing but Node.

## 2. Follow the upstream skill

Read `pixelfx/skills/pixelfx/SKILL.md` and, before making a new effect,
`pixelfx/docs/AUTHORING.md` from the checkout, then follow them. Skip their first step
(cloning the repository): the pinned checkout above replaces it. Run every command from
inside `pixelfx/`. Rendered files land in `pixelfx/records/`; copy what the user asked for
into the project's own output folder.

## 3. Rights and handoff

- Code and effects are MIT: keep the upstream `LICENSE` and `NOTICE.md` with any code
  copied into a game. Rendered sprite sheets, GIFs and MP4s may be used commercially.
- The Patch Pixel font in `gallery/fonts` is Patch's own, all rights reserved: never put it
  in a deliverable.
- New effects stay original: no specific game's sprite, character or logo.
- When FrameCore Works Creative Studio leads the project, it keeps the brief, the plan and
  the review; this skill makes the effect and reports the files, frame size, FPS and what was
  checked (`tools/check.mjs` result, contact sheet looked at, motion watched or NOT_RUN).
