# meta-ads-designer: install notes

- Upstream: https://github.com/aievolutionpl/meta-ads-designer
- Pinned commit: 656ce907380448389559958f055c8b43d71ab26e (version 6.5.0)
- Review: [reviews/meta-ads-designer.md](../reviews/meta-ads-designer.md)

## Install

See [install.md](install.md). Plugin id: `meta-ads-designer@framecore-works-toolbox`.

## Setup after install

Optional: `pip install pillow numpy`; set `FAL_KEY` only if you want fal.ai generation.

## What works where

| Component | Chat | Cowork | Claude Code |
| --------- | ---- | ------ | ----------- |
| Skill `meta-ads-designer` | yes | yes | yes |
| fal.ai generation (`FAL_KEY`) | Unknown | yes | yes |

## Use

Ask for an ad, poster or flyer, or `/meta-ads-designer:meta-ads-designer`; default format 4:5.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall meta-ads-designer@framecore-works-toolbox`. Unset `FAL_KEY` if you set it.
