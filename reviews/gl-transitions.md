# Review: gl-transitions

## Entry

- Name: gl-transitions
- Status: active
- Upstream: https://github.com/gl-transitions/gl-transitions
- Author: gl-transitions contributors (organization gl-transitions, maintainer Gaëtan Renaudeau, gre)
- License: MIT
- Commit: c040bddd7abf5195c0c61942982508ca9ee39287
- Upstream version: 3.0.0 (npm package `gl-transitions` in the repository at this commit; the skill itself is unversioned)
- Kind: skills
- Eligibility: upstream presents skills/gl-transitions/SKILL.md as an installable agent skill
- Source: github (inline manifest, skills ./skills/gl-transitions, strict false)
- Reviewed on: 2026-11-06
- Reviewer: Claude (cloud project thread)
- Owner approval: "yes" from Kamil on 2026-11-06, quote: "No to GL Transition dodajemy. Ten Cloud AIX też. No i myślę, że Bank Motion też będzie dodany, bo to przez tego, że dubluje, może być używany jako uzupełnienie"

## What it is

One skill, `gl-transitions`, with four references (WebGL, Skia, video hosts, native hosts). It picks a transition from the open collection of GLSL transition shaders (fades, wipes, zooms, glitches, page curls), gets its source from the npm package or the jsDelivr CDN, and wires it into WebGL, Remotion (`@gl-transitions/remotion`), editly, React Native Skia, CanvasKit, FFmpeg (third-party filter), WebGPU, Rust, Swift or Android, with a check of both ends and one middle frame. No commands, agents, hooks or MCP servers.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, transitions between clips and scenes in Remotion and HyperFrames work | A catalogue of ready, licensed shader transitions with exact wiring per host, where Studio has no transition library | Owner test 2026-11-06: PASS_REPORTED. Isolated Claude Code install PASS and the skill is listed (`gl-transitions:gl-transitions`); a render in this review NOT_RUN |

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: skills/gl-transitions/SKILL.md and references/native.md, skia.md, video.md, webgl.md, LICENSE, package.json, packages/gl-transitions/package.json and CHANGELOG.md (3.0.0). The repository has 409 tracked files (transitions, packages, examples, build scripts); only the skill folder is declared.

## What it installs and writes

The plugin cache (about 6 MB, the whole repository at the commit). At use, only what the user's project needs: an npm package (`gl-transitions` or a host package) or shader files in the project.

## Hooks

None.

## Network traffic

None at install beyond the plugin fetch. At use the skill may fetch `references/catalog.md` and shader files from cdn.jsdelivr.net (`gl-transitions@2`), link previews on gl-transitions.com, and install npm packages in the project when the user builds with them.

## Changes to prompts or tool results

None. The skill loads by its description.

## Data sent outside

None found.

## Requirements

None for the skill. The chosen host needs its own runtime (Node for Remotion and editly, a custom FFmpeg build for the FFmpeg filter, Xcode or Android tooling for native packages).

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-11-06: `claude plugin marketplace add` of this repository, `claude plugin install gl-transitions@framecore-works-toolbox` succeeded, `claude plugin list` showed it enabled at 3.0.0, and a headless `claude -p` session listed `gl-transitions:gl-transitions`.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Version drift: the skill at this commit points its CDN links and catalogue fallback at `gl-transitions@2`, while npm `latest` is 3.0.0, which removed twelve duplicate transitions (for example `WipeLeft`, `Box`, `LinearBlur`). Pin one exact version in a project and take the names from that version's `gl-transitions.json`. 2. A few transitions carry licences other than MIT; credit the author and licence from the catalogue. 3. `catalog.md` is not in the repository; the skill fetches it from the CDN.

## Verdict

accept.

## History

- 2026-11-06: added at c040bdd.
