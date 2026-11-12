# animation-skills-styles

Reel style pack built into FrameCore Works Toolbox. The files in `upstream/` are
byte-identical copies of the upstream repository at the reviewed commit; nothing in
them was edited. One rename: each upstream `SKILL.md` is stored as `SKILL.source.md`
so that no host registers these copies as extra skills of the Toolbox plugin (links
inside the copies that say `SKILL.md` mean that file). `SHA256SUMS` lists every copied file.

- Upstream: https://github.com/artemnovitckii/claude-animation-skills
- Author: Artem Novitckii
- Licence: MIT (`upstream/LICENSE`; keep it with any copy)
- Commit: 5dbea55c23aa6a5c93dc3cfb5583840513b56b94 (2026-11-01, plugin 1.0.0)
- Copied on: 2026-11-12, owner request in the Toolbox thread ("wgraj do toolboxa ... dodatkowe asety")
- Review: `reviews/animation-skills-styles.md` in FrameCoreWorks/framecore-works-toolbox

## Copied

`LICENSE`, `README.md`, `kit/` (`anim.py`, `words.py`, `package.json`, `package-lock.json`, `setup.sh`, `fonts/` with their OFL licences) and the skills `graph`, `minimalistic-graphics`, `map-route`, `breakdown` and `zach-d-films` (SKILL.md, build scripts, templates, engine).

## Left out

`stick-figure` (2.3 MB with audio; `stickman-kino` covers stick figures), `install.sh` (links skills into `~/.claude/skills`) and `docs/`. Do not run `kit/setup.sh` or `install.sh` on the user's behalf: copy the pack into the project and install with the user's yes (see the reel-styles reference). `zach-d-films` is a generic 3D cartoon explainer look; never present a piece as made by or for Zack D. Films.

## Attribution

When a delivered piece uses a template or preset from this pack, keep the MIT notice
with any copied code and credit "Artem Novitckii, artemnovitckii/claude-animation-skills" in the project notes.
