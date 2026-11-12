# Reel styles built into Toolbox

Four style packs ship inside the Toolbox plugin, so they work as soon as Toolbox is
installed, also in ChatGPT Work and Codex, with nothing downloaded from GitHub. Each
pack is a byte-identical MIT copy of an upstream repository at a reviewed commit,
under `capabilities/reel-styles/<pack>/upstream/`, with `UPSTREAM.md` (source,
author, commit, what was copied and left out) and `SHA256SUMS`. Each upstream
`SKILL.md` is stored as `SKILL.source.md`, so these copies never register as extra
skills; a link to `SKILL.md` inside a pack means that file.

They are knowledge and templates, not a separate pipeline: Creative Studio (or the
user) picks a style here and builds the piece on its own HyperFrames or Remotion
route. Toolbox never starts a production on its own.

## How to use a style

1. Pick the style from the tables below by the user's brief (format, mood, content).
   Offer two or three that fit when the user has none in mind.
2. Read the style's file in full before building: `STYLE.md` (claude-video-styles),
   the reference file plus its preset JSON (varg-motion-styles), or the `SKILL.source.md`
   and its references (animation-skills-styles, iart-explainer-styles). Paths are
   relative to `capabilities/reel-styles/`.
3. Build a new composition in the user's project with those numbers (palette, type,
   easing, timing, motion rules, ban list). Rework sizes for 9:16 when the source is
   16:9, and keep text inside the safe area (9:16: top 10%, bottom 20%).
4. Copy a template file (for example `templates/motion/studio.js` or an
   `index.html` reference piece) into the project only together with the pack's
   `upstream/LICENSE`; never edit the files inside the plugin.
5. Render on the host's own route and check frames across the whole timeline before
   delivery. Note the pack and upstream in the project notes (see "Attribution" in
   the pack's `UPSTREAM.md`).

Runnable engines (animation-skills-styles): copy the whole pack folder
(`upstream/kit` and `upstream/skills/<style>`) into the project first, because the
scripts write `node_modules`, renders and frames next to themselves. Then, after the
user's yes, run `bash kit/setup.sh` in the copy: it installs the locked npm packages
(three 0.169.0, Playwright 1.49.1, Montserrat 5.1.0), Playwright's Chromium, GSAP
3.12.5 from cdnjs, and warms up `hyperframes@0.8.34`. `--voice` adds about 1 GB of
voice models; ask separately. In ChatGPT Work this needs public internet access on.

No pack needs an account or API key. Never call varg.ai, iart.ai or Higgsfield from
these packs; their paid services are not part of Toolbox.

## varg-motion-styles (vargHQ/skills, `ff940b6`)

Presets in exact numbers (beats, frames, tracking, hex palettes, OFL/Apache font
pairings), each with cited sources. Folder `varg-motion-styles/upstream/<skill>/`:
`references/<style>.md` and `assets/presets/<style>.json`; read
`references/shared-*.md` or `title-craft-basics.md` first where present.

| Skill | Styles |
| --- | --- |
| `kinetic-type-art` | typeface-strobe, red-beat-words (one word per beat), word-corridor, perspective-photo-wall, type-specimen-grid, justified-manifesto, didone-city-title, scan-glitch-wordmark, hyphen-bridge-wordmark, crt-decrypt-title, particle-burst-title, anime-command-screen, photocopy-explainer, echo-halftone-portrait, glyph-tracking-terminal, bitten-word-title, liquid-art-reveal |
| `motion-formats` | found-footage-website-trailer (analog horror), vhs-bouncing-logo, pixel-runner-crt, wave-wordmark, daw-timeline-one-shot, import-launch-trailer, kinetic-lyric-video |
| `title-design` | name-lower-third, place-lower-third, speaker-plates, show-open-title, headline-write-on, stepped-channel-bumper, crt-scanline-title, chrome-echo-melt, block-glitch-title |
| `transition-craft` | photo-collage-burst, droste-recursive-zoom, tile-flip-mosaic, bokeh-light-spot, photo-cloud-gallery, shake-distort-cut |
| `caption-styles` | karaoke-fill, active-word-pop, active-word-color, sliding-pill, word-tile, frosted-panel, neon-tube, serif-italic, white-card, bounce-word-pill, tilted-card-word-pop, gradient-word, grow-highlight, line-hug-box, outline-spring, shadow-minimal, translucent-box subtitles |

## claude-video-styles (ItsssssJack/claude-video-2, `18891e4`)

21 looks, each `claude-video-styles/upstream/styles/<look>/STYLE.md` with palette,
type, easing in seconds and frames, motion rules, signature moves, composition and a
ban list; most have a 16:9 reference `index.html`. Shared craft:
`upstream/references/` (motion-craft, loops, hacks, hyperframes, style-format);
starter `upstream/templates/motion/` (one clock in `studio.js`, seek-safe).

| Look | Best for |
| --- | --- |
| swiss-grid | titles, product facts, launch cards, kinetic type |
| swiss-kinetic | kinetic type, music promos, title sequences, slogans |
| poster-pop | hooks, Shorts, big claims, countdowns, "3 things" lists |
| risograph | playful promos, events, music, culture |
| editorial-paper | data, charts, "what the numbers say" |
| data-story | retention and growth stats, before and after |
| explainer-diagram | how something works, pipelines, product flows |
| blueprint | how things work, product parts, step by step |
| midnight-grid | tech and AI explainers, diagrams |
| particle-field | AI and data openers, abstract intros, logo builds |
| ink-line | brand stings, calm intros, logo reveals |
| paper-cut | stories, travel, nature, gentle brand moments |
| paper-world | story openers, place pieces, calm brand films |
| growing-city | growth over time, yearly recaps, milestones |
| time-travel | history of an idea, then vs now, timelines |
| graphite-ui | software launches, app demos, feature reveals |
| weather-widget | app UI promos, state changes, dashboards |
| editor-ui | "AI edits my video" demos, tool launches |
| design-app-ui | design tool demos, layout explainers |
| motion-app-ui | motion tool demos, keyframe and easing explainers |
| audio-app-ui | music and audio tool launches, beat-sync explainers |

## animation-skills-styles (artemnovitckii/claude-animation-skills, `5dbea55`)

Ready 9:16 reel engines driven by a small JSON spec; see each `SKILL.source.md`.

| Style | Look |
| --- | --- |
| `graph` | one black line draws itself while one big number counts up |
| `minimalistic-graphics` | black-and-white line art, steps and orbit, one lowercase line |
| `map-route` | 3D white city, route draws itself, pin drop, ETA card |
| `breakdown` | phone exploded view with leader lines and labels (`cutaway` covers other objects) |
| `zach-d-films` | 3D cartoon "what if" explainer in three.js (generic look; never claim the creator's name) |

## iart-explainer-styles (iart-ai/explainer-video-skills, `3c13a1b`)

Method and recipes, `iart-explainer-styles/upstream/skills/<skill>/`.

| Skill | Look |
| --- | --- |
| `explainer-video` | script to storyboard to narrated explainer, VO-first timing |
| `whiteboard-animation` | hand draws strokes on a whiteboard (draw-on order, nib on the tip) |
| `isometric-animation` | 2.5D isometric scenes, stacked layers, city builds |
| `diagram-animation` | flowcharts and charts revealed node, edge, label |
| `wrapped-video` | year-in-review and personal data recaps (Remotion) |

Some iart recipes import `gsap/+esm` unversioned: use `gsap@3.14.2` instead.
