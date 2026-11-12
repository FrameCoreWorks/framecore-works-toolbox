# Review: iart-explainer-styles

## Entry

- Name: iart-explainer-styles
- Status: active
- Upstream: https://github.com/iart-ai/explainer-video-skills
- Author: iart.ai
- License: MIT
- Commit: 3c13a1bc360c08503f24f9c9a99fda6d3d35de56
- Upstream version: 0.1.0
- Kind: built-in
- Eligibility: built-in reel style pack of the toolbox plugin: byte-identical MIT copy of selected upstream files, explicitly requested by the owner
- Source: built-in ./plugins/toolbox/capabilities/reel-styles/iart-explainer-styles (instructions ./plugins/toolbox/skills/toolbox/references/reel-styles.md)
- Reviewed on: 2026-11-12
- Reviewer: Claude Code (cloud) for Kamil (FrameCore Works)
- Owner approval: Kamil on 2026-11-12: "To weź się wgraj jako do toolboxa. To będą takie już dodatkowe asety." (after the research "FrameMotion – research gotowych stylów rolek")

GitHub metadata at review time: 97 stars, 19 commits, last commit 2026-11-11.

## What it is

A Claude plugin with five method skills for explainers: explainer-video (script to storyboard to narrated explainer), whiteboard-animation, isometric-animation, diagram-animation and wrapped-video (year-in-review, Remotion), with recipe references. Toolbox copies `skills/`, README and LICENSE.

This is an owner-requested exception to the no-upstream-copy rule (see CLAUDE.md,
"Reel style packs"): the files ship inside the Toolbox package so they work in
ChatGPT Work and Codex without a download from GitHub. `UPSTREAM.md` in the pack
lists what was copied and left out; `SHA256SUMS` lists every copied file. Upstream
`SKILL.md` files are stored as `SKILL.source.md` (the only change) so hosts do not
register them as extra skills.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| framecore-works-creative-studio / explainers | Whiteboard draw-on order, isometric shading and diagram reveal recipes that Studio's explainer references lack in this detail. | Content checked in source. Renders NOT_RUN. |

## Files reviewed

Whole tree, `.claude-plugin/*.json`, every SKILL.md and reference, `scripts/` (contact sheet, probe, seek helpers; not copied); grep for URLs, keys and service calls. Recipes import GSAP (unversioned `gsap/+esm`) and three@0.160 from jsDelivr; closing lines link to iart.ai. Cloned as data into a temporary folder at the pinned commit; no upstream script, installer, hook or test was executed.

## What it installs and writes

Nothing at install beyond the copied files inside the Toolbox plugin. At use, the model
builds a new composition in the user's project; copied template files go into the
project together with the upstream LICENSE.

## Hooks

None.

## Network traffic

None from the copied Markdown. Recipes, if used as written, load GSAP unversioned from jsDelivr; the reference tells the model to pin `gsap@3.14.2`.

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

Promotional links to the paid iart.ai product stay in the copied text. Unversioned GSAP import in recipes.

## Verdict

Accepted as a built-in style pack (MIT, pinned, no account or API key).

## History

- 2026-11-12: added to Toolbox 1.14.0 at `3c13a1b`.
