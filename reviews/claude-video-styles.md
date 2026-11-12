# Review: claude-video-styles

## Entry

- Name: claude-video-styles
- Status: active
- Upstream: https://github.com/ItsssssJack/claude-video-2
- Author: Claude Video Studio contributors (ItsssssJack)
- License: MIT
- Commit: 18891e4996abb7ccc0085f2d43cef2fd7eff1dc8
- Upstream version: none (single commit)
- Kind: built-in
- Eligibility: built-in reel style pack of the toolbox plugin: byte-identical MIT copy of selected upstream files, explicitly requested by the owner
- Source: built-in ./plugins/toolbox/capabilities/reel-styles/claude-video-styles (instructions ./plugins/toolbox/skills/toolbox/references/reel-styles.md)
- Reviewed on: 2026-11-12
- Reviewer: Claude Code (cloud) for Kamil (FrameCore Works)
- Owner approval: Kamil on 2026-11-12: "To weź się wgraj jako do toolboxa. To będą takie już dodatkowe asety." (after the research "FrameMotion – research gotowych stylów rolek")

GitHub metadata at review time: 166 stars, 1 commit, 2026-10-21.

## What it is

A root-level skill (`SKILL.md`, not a plugin manifest) for motion videos in HyperFrames with a gallery of 21 looks. Each look has a `STYLE.md` (palette in hex, type, easing in seconds and frames, motion rules, signature moves, composition, media rules, ban list) and most have a 16:9 reference `index.html`. Toolbox copies `styles/`, `references/`, `templates/motion/`, README and LICENSE; not the 61 MB gallery videos or scripts.

This is an owner-requested exception to the no-upstream-copy rule (see CLAUDE.md,
"Reel style packs"): the files ship inside the Toolbox package so they work in
ChatGPT Work and Codex without a download from GitHub. `UPSTREAM.md` in the pack
lists what was copied and left out; `SHA256SUMS` lists every copied file. Upstream
`SKILL.md` files are stored as `SKILL.source.md` (the only change) so hosts do not
register them as extra skills.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| framecore-works-creative-studio / motion reels | A named look with exact palette, type, easing and ban list before the build, so a reel does not fall back to a generic look. | PASS 2026-11-12 (cloud): a new 8 s 9:16 composition built from `swiss-grid/STYLE.md` with the copied `templates/motion/studio.js` rendered with `hyperframes@0.8.34` (240 frames, 14.8 s); frames checked every 0.5 s: text readable, inside the 9:16 safe area, holds over 1 s. No client material or sound. |

## Files reviewed

Whole tree, `SKILL.md`, `scripts/` (render, doctor, the optional Higgsfield client), `config.json`, every `STYLE.md`; grep of `styles/` and `templates/` for network calls (`fetch`, XHR, WebSocket, storage, eval): none. Reference pieces load GSAP 3.14.2 from jsDelivr and fonts from Google Fonts. Cloned as data into a temporary folder at the pinned commit; no upstream script, installer, hook or test was executed.

## What it installs and writes

Nothing at install beyond the copied files inside the Toolbox plugin. At use, the model
builds a new composition in the user's project; copied template files go into the
project together with the upstream LICENSE.

## Hooks

None.

## Network traffic

Reference pieces load pinned GSAP 3.14.2 from jsDelivr and fonts from Google Fonts when rendered. The paid Higgsfield client (`scripts/higgsfield.py`) is not copied.

## Changes to prompts or tool results

None. The files are read only when the Toolbox skill points to them for a style request.

## Data sent outside

Nothing by the pack itself.

## Requirements

None for reading. Renders use the host's own HyperFrames or Remotion route (Node, ffmpeg, Chromium).

## Install tests

Package check (`scripts/package_plugins.py --check`) and the full repository checks: see
CHANGELOG 1.14.0 and docs/verification.md. Fresh host activation (claude.ai, Cowork,
Codex, ChatGPT Work): NOT_RUN.

## Risks

Only one commit; no releases. Reference pieces are 16:9.

## Verdict

Accepted as a built-in style pack (MIT, pinned, no account or API key).

## History

- 2026-11-12: added to Toolbox 1.14.0 at `18891e4`.
