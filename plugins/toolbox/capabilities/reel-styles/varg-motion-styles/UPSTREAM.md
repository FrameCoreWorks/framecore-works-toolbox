# varg-motion-styles

Reel style pack built into FrameCore Works Toolbox. The files in `upstream/` are
byte-identical copies of the upstream repository at the reviewed commit; nothing in
them was edited. One rename: each upstream `SKILL.md` is stored as `SKILL.source.md`
so that no host registers these copies as extra skills of the Toolbox plugin (links
inside the copies that say `SKILL.md` mean that file). `SHA256SUMS` lists every copied file.

- Upstream: https://github.com/vargHQ/skills
- Author: vargai Inc. (vargHQ)
- Licence: MIT (`upstream/LICENSE`; keep it with any copy)
- Commit: ff940b67bc03a85d03f0fe33591ac59239eb8b84 (2026-11-11, plugin 2.17.0)
- Copied on: 2026-11-12, owner request in the Toolbox thread ("wgraj do toolboxa ... dodatkowe asety")
- Review: `reviews/varg-motion-styles.md` in FrameCoreWorks/framecore-works-toolbox

## Copied

`LICENSE` and, for `kinetic-type-art`, `motion-formats`, `title-design`, `transition-craft` and `caption-styles`: `SKILL.md`, `README.md`, `references/` and `assets/presets/`.

## Left out

Every other upstream skill (most of them route to the paid varg.ai service), the two hosted MCP servers in `.mcp.json`, `examples/` (demo projects with bundled fonts) and `evals/`. Links in the copied SKILL.md files to `examples/`, `varg-ai` or other varg skills point at files that are not here; use the upstream repository at the commit above for them. Never call varg.ai from these packs.

## Attribution

When a delivered piece uses a template or preset from this pack, keep the MIT notice
with any copied code and credit "vargai Inc. (vargHQ), vargHQ/skills" in the project notes.
