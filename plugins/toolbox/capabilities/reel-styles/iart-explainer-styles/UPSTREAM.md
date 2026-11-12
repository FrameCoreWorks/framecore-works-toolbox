# iart-explainer-styles

Reel style pack built into FrameCore Works Toolbox. The files in `upstream/` are
byte-identical copies of the upstream repository at the reviewed commit; nothing in
them was edited. One rename: each upstream `SKILL.md` is stored as `SKILL.source.md`
so that no host registers these copies as extra skills of the Toolbox plugin (links
inside the copies that say `SKILL.md` mean that file). `SHA256SUMS` lists every copied file.

- Upstream: https://github.com/iart-ai/explainer-video-skills
- Author: iart.ai
- Licence: MIT (`upstream/LICENSE`; keep it with any copy)
- Commit: 3c13a1bc360c08503f24f9c9a99fda6d3d35de56 (2026-11-11, plugin 0.1.0)
- Copied on: 2026-11-12, owner request in the Toolbox thread ("wgraj do toolboxa ... dodatkowe asety")
- Review: `reviews/iart-explainer-styles.md` in FrameCoreWorks/framecore-works-toolbox

## Copied

`LICENSE`, `README.md` and `skills/` (`explainer-video`, `whiteboard-animation`, `isometric-animation`, `diagram-animation`, `wrapped-video` with their references).

## Left out

`showcase.gif`, `showcase.html`, `scripts/` and the plugin manifests. Some recipes import `gsap/+esm` from jsDelivr without a version: pin `gsap@3.14.2` when you use them. Promotional links to iart.ai stay as upstream wrote them; the skills render locally and need no iart.ai account.

## Attribution

When a delivered piece uses a template or preset from this pack, keep the MIT notice
with any copied code and credit "iart.ai, iart-ai/explainer-video-skills" in the project notes.
