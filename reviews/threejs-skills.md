# Review: threejs-skills

## Entry

- Name: threejs-skills
- Status: active
- Upstream: https://github.com/CloudAI-X/threejs-skills
- Author: CloudAI-X
- License: MIT
- Commit: 0e181866f095b5f06d005133876e926515390d95
- Upstream version: 0.0.0 (unreleased; pinned commit; targets three.js r186)
- Kind: skills
- Eligibility: upstream presents its 13 skills/threejs-* folders as installable Claude Code skills (README, `npx skills add` or a copy to .claude/skills)
- Source: github (inline manifest, 13 skills ./skills/threejs-*, strict false)
- Reviewed on: 2026-11-06
- Reviewer: Claude (cloud project thread)
- Owner approval: "yes" from Kamil on 2026-11-06, quote: "No to GL Transition dodajemy. Ten Cloud AIX też. No i myślę, że Bank Motion też będzie dodany, bo to przez tego, że dubluje, może być używany jako uzupełnienie"

## What it is

Thirteen reference skills for three.js r186, React Three Fiber 9.8 with drei 10.7 and gltf-transform 4.5: fundamentals, geometry, materials, lighting, textures, loaders, asset pipeline, shaders, post-processing, animation, interaction, performance and React Three Fiber. Each has current API examples, a WebGPU and TSL section and a Common Mistakes list of outdated patterns. Text only: no scripts, commands, agents, hooks or MCP servers.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, 3D scenes in Remotion (`@remotion/three`) and HyperFrames work | Current three.js API instead of a mix of releases from training data; Studio has only a `@remotion/three` example | Headless A/B 2026-11-06, one prompt each (HDR environment map plus delta-time loop for r186): without the skill the answer used `THREE.Clock`, which r186 replaced with `Timer`; with the skills it used `Timer` and `HDRLoader`. One case, 2 runs, about 26 s; a rendered scene NOT_RUN |

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; nothing was run. Read: README.md, LICENSE and all 13 SKILL.md files (15 tracked files, about 315 kB of skill text).

## What it installs and writes

The plugin cache (about 0.4 MB). Nothing else; code goes into the user's project only when the user builds with it.

## Hooks

None.

## Network traffic

None from the plugin. Examples load three.js add-ons and sample assets from cdn.jsdelivr.net when the user's page runs them.

## Changes to prompts or tool results

None. Skills load by their descriptions.

## Data sent outside

None found.

## Requirements

None for the skills; a project using three.js needs Node or a browser.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-11-06: `claude plugin install threejs-skills@framecore-works-toolbox` succeeded, `claude plugin list` showed it enabled, and a headless `claude -p` session listed all 13 `threejs-skills:threejs-*` skills.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Written for three.js r186; a project pinned to an older or newer release may need other APIs. 2. Thirteen descriptions add to the skill list a host shows the model.

## Verdict

accept.

## History

- 2026-11-06: added at 0e18186.
