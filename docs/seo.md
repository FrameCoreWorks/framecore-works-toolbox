# seo: install notes

- Upstream: https://github.com/AgriciDaniel/claude-seo
- Pinned commit: 6be93f45064ffbadced572b5d5c95f55fd263af0 (version 2.5.0)
- Review: [reviews/seo.md](../reviews/seo.md)

## Install

See [install.md](install.md). Plugin id: `seo@framecore-works-toolbox`.

## Setup after install

Python for scripts and the hook; optional API keys.

## What works where

Cowork and Claude Code (hook); chat: skills only.

## Use

Ask for an SEO audit or schema review.

Watch out: a local hook validates structured data after every edit.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall seo@framecore-works-toolbox`. Delete files it created in your projects if you no longer need them.
