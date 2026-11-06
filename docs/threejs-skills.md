# threejs-skills: install notes

- Upstream: https://github.com/CloudAI-X/threejs-skills
- Pinned commit: 0e181866f095b5f06d005133876e926515390d95 (version unreleased, three.js r186)
- Review: [reviews/threejs-skills.md](../reviews/threejs-skills.md)

## Install

See [install.md](install.md). Plugin id: `threejs-skills@framecore-works-toolbox`.

## Setup after install

None.

## What works where

Chat, Cowork and Claude Code: skills (text only).

## Use

Ask a three.js or React Three Fiber task; the matching `threejs-*` skill loads by its description, or call `/threejs-skills:threejs-fundamentals` and the others by name.

## Watch out

Written for three.js r186; check the project's installed release before following an API.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall threejs-skills@framecore-works-toolbox`.
