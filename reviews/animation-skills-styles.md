# Review: animation-skills-styles

## Entry

- Name: animation-skills-styles
- Status: active
- Upstream: https://github.com/artemnovitckii/claude-animation-skills
- Author: Artem Novitckii
- License: MIT
- Commit: 5dbea55c23aa6a5c93dc3cfb5583840513b56b94
- Upstream version: 1.0.0
- Kind: built-in
- Eligibility: built-in reel style pack of the toolbox plugin: byte-identical MIT copy of selected upstream files, explicitly requested by the owner
- Source: built-in ./plugins/toolbox/capabilities/reel-styles/animation-skills-styles (instructions ./plugins/toolbox/skills/toolbox/references/reel-styles.md)
- Reviewed on: 2026-11-12
- Reviewer: Claude Code (cloud) for Kamil (FrameCore Works)
- Owner approval: Kamil on 2026-11-12: "To weź się wgraj jako do toolboxa. To będą takie już dodatkowe asety." (after the research "FrameMotion – research gotowych stylów rolek")

GitHub metadata at review time: 660 stars, 2 commits, 2026-11-01.

## What it is

A Claude plugin with six skills that make 9:16 reels with no footage. Toolbox copies five (graph, minimalistic-graphics, map-route, breakdown, zach-d-films) with the shared `kit/` (Python helpers, locked npm manifest, setup script, OFL fonts). `stick-figure` is left out (2.3 MB with audio, `stickman-kino` covers it).

This is an owner-requested exception to the no-upstream-copy rule (see CLAUDE.md,
"Reel style packs"): the files ship inside the Toolbox package so they work in
ChatGPT Work and Codex without a download from GitHub. `UPSTREAM.md` in the pack
lists what was copied and left out; `SHA256SUMS` lists every copied file. Upstream
`SKILL.md` files are stored as `SKILL.source.md` (the only change) so hosts do not
register them as extra skills.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| framecore-works-creative-studio / motion reels | Five ready reel engines driven by a JSON spec (stat graph, route map, exploded phone, line art, 3D cartoon explainer) that Studio's HyperFrames route would otherwise build from scratch. | Render NOT_RUN: running the upstream build script in the cloud session was blocked by the session's safety check for downloaded code; GSAP download and `hyperframes@0.8.34 --version` PASS. |

## Files reviewed

Whole tree, `.claude-plugin/*.json`, `install.sh`, `kit/setup.sh`, `kit/anim.py`, `kit/package.json`, each copied SKILL.md and grep of scripts and templates for URLs. `install.sh` symlinks skills into `~/.claude/skills` (not copied into use; never run). `kit/setup.sh` runs `npm install` from the lockfile (three 0.169.0, Playwright 1.49.1, @fontsource/montserrat 5.1.0), installs Playwright's Chromium, downloads GSAP 3.12.5 from cdnjs and warms up `hyperframes@0.8.34`; `--voice` adds unpinned-by-hash Kokoro and Parakeet models (about 1 GB) from GitHub release tags. Every version is pinned. Cloned as data into a temporary folder at the pinned commit; no upstream script, installer, hook or test was executed.

## What it installs and writes

Nothing at install beyond the copied files inside the Toolbox plugin. At use, the model
builds a new composition in the user's project; copied template files go into the
project together with the upstream LICENSE.

## Hooks

None.

## Network traffic

None until setup. Setup reaches the npm registry, Playwright's CDN, cdnjs and (voice only) GitHub releases. `stick-figure`'s ElevenLabs client is not copied.

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

The upstream skill runs `kit/setup.sh` on first use without asking; Toolbox's reference requires the user's yes and a copy in the project. Voice models are fetched by tag, not hash. `zach-d-films` imitates a known creator's genre; never use the creator's name or branding.

## Verdict

Accepted as a built-in style pack (MIT, pinned, no account or API key).

## History

- 2026-11-12: added to Toolbox 1.14.0 at `5dbea55`.
