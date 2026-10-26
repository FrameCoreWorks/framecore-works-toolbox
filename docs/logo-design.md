# logo-design: install notes

- Upstream: https://github.com/kaankiziltug/logo-design-skill
- Pinned commit: 734090317a2155c5bf1ae8bd4cc85c6848a0128f (version 1.4.5)
- Review: [reviews/logo-design.md](../reviews/logo-design.md)

## Install

See [install.md](install.md). Plugin id: `logo-design@framecore-works-toolbox`.

## Setup after install

Nothing required; python3 for the audit and render scripts.

## What works where

| Component | Chat | Cowork | Claude Code |
| --------- | ---- | ------ | ----------- |
| Skill `logo-design` | yes | yes | yes |
| Python scripts (audit, PNG render) | Unknown | yes | yes |

## Use

Ask for a logo or a logo critique, or `/logo-design:logo-design`.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall logo-design@framecore-works-toolbox`. It leaves no files outside your projects.
