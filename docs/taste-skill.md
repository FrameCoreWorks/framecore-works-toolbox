# taste-skill: install notes

- Upstream: https://github.com/Leonxlnx/taste-skill
- Pinned commit: f6b76575f949707b4e3c37cd86cb44b0b98643e8 (version 2.5.1)
- Review: [reviews/taste-skill.md](../reviews/taste-skill.md)

## Install

See [install.md](install.md). Plugin id: `taste-skill@framecore-works-toolbox`.

## Setup after install

Node 22 or newer and Chrome, Edge or Chromium for its checker and finish gate (ffmpeg optional).

## What works where

Chat: skill. Cowork and Claude Code: skill plus scripts and browser.

## Use

Ask for a landing page, a product page or an app screen with a strong art direction.

## Watch out

Found pictures keep their own licences; check each before client use. Since 2.5.1 the skill carries a Stop hook: while the skill is loaded in Claude Code, its finish gate (`gate.mjs`, up to 600 s) runs locally when Claude stops and writes its results to `.taste-skill/` in the project.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall taste-skill@framecore-works-toolbox`.
