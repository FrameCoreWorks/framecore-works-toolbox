# hud: install notes

- Upstream: https://github.com/jarrodwatts/claude-hud
- Pinned commit: cf95a322afd18db045175d28962650ae7392ed77 (version 0.13.1)
- Review: [reviews/hud.md](../reviews/hud.md)

## Install

See [install.md](install.md). Plugin id: `hud@framecore-works-toolbox`.

## Setup after install

Node; Claude Code (status line).

## What works where

Claude Code only (status line).

## Use

Run its setup command once, `/hud:setup`, then `/hud:configure` to change what it shows.

Watch out: setup writes a statusLine entry; it replaces another status line such as ponytail's.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall hud@framecore-works-toolbox`. Delete files it created in your projects if you no longer need them.
