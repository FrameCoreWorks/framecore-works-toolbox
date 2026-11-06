# gsap-skills: install notes

- Upstream: https://github.com/greensock/gsap-skills
- Pinned commit: aed9cfd3277740755f6bfc1155c7aa645403b760 (version 1.0.0)
- Review: [reviews/gsap-skills.md](../reviews/gsap-skills.md)

## Install

See [install.md](install.md). Plugin id: `gsap-skills@framecore-works-toolbox`.

## Setup after install

None. Code it writes needs the `gsap` npm package or the GSAP CDN script.

## What works where

Chat, Cowork and Claude Code: skills (instructions only). Codex and ChatGPT Work: NOT_RUN.

## Use

Ask a GSAP task: a timeline, ScrollTrigger, a SplitText reveal, a MorphSVG shape change, a React animation. The matching `gsap-*` skill loads.

## Watch out

GSAP itself is free under Webflow's licence, not MIT; the skills are MIT.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall gsap-skills@framecore-works-toolbox`.
