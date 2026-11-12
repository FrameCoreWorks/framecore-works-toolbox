# claude-video-styles

Reel style pack built into FrameCore Works Toolbox. The files in `upstream/` are
byte-identical copies of the upstream repository at the reviewed commit; nothing in
them was edited. One rename: each upstream `SKILL.md` is stored as `SKILL.source.md`
so that no host registers these copies as extra skills of the Toolbox plugin (links
inside the copies that say `SKILL.md` mean that file). `SHA256SUMS` lists every copied file.

- Upstream: https://github.com/ItsssssJack/claude-video-2
- Author: Claude Video Studio contributors (ItsssssJack)
- Licence: MIT (`upstream/LICENSE`; keep it with any copy)
- Commit: 18891e4996abb7ccc0085f2d43cef2fd7eff1dc8 (2026-10-21, no version (single commit))
- Copied on: 2026-11-12, owner request in the Toolbox thread ("wgraj do toolboxa ... dodatkowe asety")
- Review: `reviews/claude-video-styles.md` in FrameCoreWorks/framecore-works-toolbox

## Copied

`LICENSE`, `README.md`, `styles/` (21 looks: `STYLE.md` plus a reference `index.html` and `studio.js` where upstream has them), `references/` and `templates/motion/`.

## Left out

`gallery/` (61 MB of preview videos), `scripts/` (including the optional paid Higgsfield client), `examples/`, `SKILL.md`, `questions.md`, `NOTION-PAGE.md` and `config.json`. Reference pieces load GSAP 3.14.2 from jsDelivr and fonts from Google Fonts at render time.

## Attribution

When a delivered piece uses a template or preset from this pack, keep the MIT notice
with any copied code and credit "Claude Video Studio contributors (ItsssssJack), ItsssssJack/claude-video-2" in the project notes.
