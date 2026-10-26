# planning-with-files: install notes

- Upstream: https://github.com/OthmanAdi/planning-with-files
- Pinned commit: dcdfb278de53fdb69b2067ea173dbb1de45345a3 (version 3.25.2)
- Review: [reviews/planning-with-files.md](../reviews/planning-with-files.md)

## Install

See [install.md](install.md). Plugin id: `planning-with-files@framecore-works-toolbox`.

## Setup after install

sh, Python for helper scripts.

## What works where

Cowork and Claude Code (hooks); chat: skills only.

## Use

Start a long task with its planning skill; plans live in your project.

Watch out: its hooks inject the plan every turn; overlaps with Superpowers plans.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall planning-with-files@framecore-works-toolbox`. Delete files it created in your projects if you no longer need them.
