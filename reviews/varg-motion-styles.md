# Review: varg-motion-styles

## Entry

- Name: varg-motion-styles
- Status: active
- Upstream: https://github.com/vargHQ/skills
- Author: vargai Inc. (vargHQ)
- License: MIT
- Commit: ff940b67bc03a85d03f0fe33591ac59239eb8b84
- Upstream version: 2.17.0 (plugin), skills 0.1.0
- Kind: built-in
- Eligibility: built-in reel style pack of the toolbox plugin: byte-identical MIT copy of selected upstream files, explicitly requested by the owner
- Source: built-in ./plugins/toolbox/capabilities/reel-styles/varg-motion-styles (instructions ./plugins/toolbox/skills/toolbox/references/reel-styles.md)
- Reviewed on: 2026-11-12
- Reviewer: Claude Code (cloud) for Kamil (FrameCore Works)
- Owner approval: Kamil on 2026-11-12: "To weź się wgraj jako do toolboxa. To będą takie już dodatkowe asety." (after the research "FrameMotion – research gotowych stylów rolek")

GitHub metadata at review time: 30 stars, 151 commits, last commit 2026-11-11.

## What it is

Upstream is a 78-skill Claude plugin for the paid varg.ai generation service, with two hosted MCP servers (`api.varg.ai`, `mcp.varg.ai`). Five of its skills are local craft packs that need no key (their frontmatter says "0 credits; renders locally"): `kinetic-type-art` (17 templates, 54 presets), `motion-formats` (7 formats), `title-design` (9 templates), `transition-craft` (6 transitions) and `caption-styles` (17 caption looks). Toolbox copies only these five (SKILL.md, README, references, preset JSON).

This is an owner-requested exception to the no-upstream-copy rule (see CLAUDE.md,
"Reel style packs"): the files ship inside the Toolbox package so they work in
ChatGPT Work and Codex without a download from GitHub. `UPSTREAM.md` in the pack
lists what was copied and left out; `SHA256SUMS` lists every copied file. Upstream
`SKILL.md` files are stored as `SKILL.source.md` (the only change) so hosts do not
register them as extra skills.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| framecore-works-creative-studio / motion reels | Exact numbers per style (frames per beat, tracking, hex palettes, safe areas, easing) for titles, captions, transitions and kinetic type, which Studio's motion references describe only in general terms. | Content checked in source. Renders from these presets NOT_RUN; the test reel used claude-video-styles. |

## Files reviewed

Tree of the whole repository, `.claude-plugin/plugin.json`, `.mcp.json`, `LICENSE`, the five SKILL.md files and their reference and preset folders; grep of the copied files for URLs, varg service calls and tool names. The full plugin was not added: its hosted MCP servers connect to varg.ai and most skills need a varg account, which the self-contained rule rejects. Cloned as data into a temporary folder at the pinned commit; no upstream script, installer, hook or test was executed.

## What it installs and writes

Nothing at install beyond the copied files inside the Toolbox plugin. At use, the model
builds a new composition in the user's project; copied template files go into the
project together with the upstream LICENSE.

## Hooks

None.

## Network traffic

None from the copied files. They are Markdown and JSON. They mention the `varg-ai` skill for paid generation; the reel-styles reference forbids calling varg.ai.

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

Links inside the copied SKILL.md files point to upstream `examples/` and paid varg skills that are not copied. Low stars (new repository).

## Verdict

Accepted as a built-in style pack (MIT, pinned, no account or API key).

## History

- 2026-11-12: added to Toolbox 1.14.0 at `ff940b6`.
