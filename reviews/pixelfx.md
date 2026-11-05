# Review: pixelfx

## Entry

- Name: pixelfx
- Status: active
- Upstream: https://github.com/patch-gg/pixelfx
- Author: Patch (patch-gg; commits by rehan-remade), with parts adapted from Hugo Duprez (Sprite Fusion) and Hollow Crown
- License: MIT
- Commit: a84159688af3ca37a4be05a0d422b94451b2e24e
- Upstream version: 0.3.0
- Kind: adapted
- Eligibility: adapted: our own wrapper plugin `plugins/pixelfx` with its own skill that checks out the upstream at the reviewed commit inside the project after the user's yes and then follows the upstream skill; the upstream plugin is not listed directly because its skill first clones the unpinned default branch next to the project
- Source: local wrapper ./plugins/pixelfx (UPSTREAM.md names the reviewed commit)
- Reviewed on: 2026-11-05
- Reviewer: Claude (cloud thread "Wyciągnij wiedzę z pixelfx do Studia i Toolboxa")
- Owner approval: "yes" from Kamil on 2026-11-05 ("do listy, do toolboxa jako polecane repo"), as an explicit exception to the stabilisation stage

## What it is

A library of 244 pixel art effects in 21 categories (fire, explosions, water, ice, lightning, sci-fi, melee, impacts, projectiles, spawn and death, arcane, holy, shadow, status, nature, weather, UI, pickups, transitions, critters, moves), each one JavaScript file that draws into a colour buffer and an additive light buffer. Effects with a character carry an "act" (wind-up, hit-stop, target reaction, recovery). Node tools render contact sheets, GIF/MP4 (through ffmpeg), sprite sheets with Aseprite-style JSON, and check effects for spills, seams, unseeded randomness and slow frames. The upstream ships a Claude plugin (`.claude-plugin/plugin.json`, `marketplace.json`) with one skill, `skills/pixelfx/SKILL.md`, and a gallery on GitHub Pages. Activity: 8 commits from 2026-10-29 to 2026-10-31, about 5.1k stars and 674 forks on 2026-11-05 (GitHub page), 2 contributors.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, pixel-art looks and game-style hits in motion pieces (Motion Graphics, Animate engine pixel style) | Ready, seeded pixel effects and sprite sheets, plus a written quality bar (lines and light, translucent smoke, phased choreography, hit-stop) that Studio's pixel style lacked; Studio 1.171.0 adds its own-words craft reference from this review | Source read at the pinned commit; Toolbox isolated install see below; rendering an effect NOT_RUN (upstream tools not run during review) |
| Studio users making games or game trailers | Sprite sheets with pivot, FPS and act timing for Godot, Unity and Phaser, which Studio cannot produce itself | NOT_RUN in any engine |

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: README.md, LICENSE, NOTICE.md, package.json, .claude-plugin/plugin.json and marketplace.json, skills/pixelfx/SKILL.md, docs/AUTHORING.md, gallery/fonts/NOTICE.md, .github/workflows/gallery.yml, and a scan of tools/*.mjs and tools/lib/*.mjs for network and process calls (313 files).

## What it installs and writes

The wrapper plugin itself is four small files in the plugin cache. After the user's yes, its skill clones the upstream (about 40 MB with history) into `pixelfx/` in the project at the reviewed commit. Upstream tools write renders to `pixelfx/records/` (or `--out`) and new effects to `pixelfx/src/fx/`.

## Hooks

None (neither the wrapper nor the upstream plugin).

## Network traffic

The one clone from github.com, after the user's yes. The tools make no requests; `tools/build-gallery.mjs` (not used by the wrapper) adds a Google Fonts link to the generated gallery page and needs the npm package esbuild.

## Changes to prompts or tool results

None. The skill loads by its description or `/pixelfx:pixelfx`.

## Data sent outside

None found.

## Requirements

git, Node.js 18 or newer; ffmpeg optional (GIF and MP4 previews, spawned by `tools/lib/fxlib.mjs`). No account, no API key, no desktop app.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-11-05 with Claude Code 2.1.318: `claude plugin marketplace add` of this repository, `claude plugin install pixelfx@framecore-works-toolbox` succeeded, `claude plugin list` showed 0.3.0 enabled and the cache held `skills/pixelfx/SKILL.md`. The skill's clone and the upstream tools were not run (NOT_RUN).
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. The upstream skill's first step clones the unpinned default branch; the wrapper replaces that step, but a user who installs the upstream marketplace directly gets the unpinned behaviour.
2. The Patch Pixel font in `gallery/fonts` is not MIT (all rights reserved); it must not be shipped.
3. Young project (three days of history at review); later commits need a new review before the pin moves.
4. Effects drawn on the body paint the stock dummy character; a user's own character needs its own animation timed from the act data.

## Verdict

accept with conditions: listed only through our pinned wrapper; renders and engine imports NOT_RUN.

## History

- 2026-11-05: added at a841596 as wrapper `plugins/pixelfx` (Toolbox 1.7.0).
