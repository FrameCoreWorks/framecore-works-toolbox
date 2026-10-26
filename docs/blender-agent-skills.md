# blender-agent-skills: install notes

- Upstream: https://github.com/EL4CTEO/blender-skills
- Pinned commit: 71d031dab8bc6729504d11a78cbe91945401045f (version 1.1.0)
- Review: [reviews/blender-agent-skills.md](../reviews/blender-agent-skills.md)

## Install

See [install.md](install.md). Plugin id: `blender-agent-skills@framecore-works-toolbox`.

## Setup after install

Blender 5.2 installed locally.

## What works where

Claude Code and Cowork with Blender installed; chat: guidance only.

## Use

Ask for a 3D task in Blender, or `/blender-agent-skills:` and pick a skill.

Watch out: needs Blender 5.2 on the machine.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall blender-agent-skills@framecore-works-toolbox`. Delete files it created in your projects if you no longer need them.
