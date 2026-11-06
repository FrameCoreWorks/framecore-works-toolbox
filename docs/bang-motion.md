# bang-motion: install notes

- Upstream: https://github.com/bangtutorial/bang-motion
- Pinned commit: c1aa65e921c970d858705fcb4a53a8294d1a4131 (version 1.19.0)
- Review: [reviews/bang-motion.md](../reviews/bang-motion.md)

## Install

See [install.md](install.md). Plugin id: `bang-motion@framecore-works-toolbox`.

## Setup after install

None. Optional: Node with an exact puppeteer version for screenshots and MP4 export, Python 3 for the local server.

## What works where

Chat: skill. Cowork and Claude Code: skill plus optional preview and MP4 export scripts.

## Use

Ask for an opener, promo, bumper, kinetic typography or an explainer in one of its five styles; the result is one `index.html` that autoplays and loops.

## Watch out

Skill text is in Indonesian. It overlaps Studio's HyperFrames route, `animate` and `motion-designer`: use it as a complement and pick one route per job. Pages load GSAP and fonts from CDNs.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall bang-motion@framecore-works-toolbox`.
