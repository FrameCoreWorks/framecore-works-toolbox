# manim-skill: install notes

- Upstream: https://github.com/Yusuke710/manim-skill
- Pinned commit: a0048d9e265499038f34a9aa58ff16d306b5034c (version 1.0.0)
- Review: [reviews/manim-skill.md](../reviews/manim-skill.md)

## Install

See [install.md](install.md). Plugin id: `manim-skill@framecore-works-toolbox`.

## Setup after install

Install Manim Community and a LaTeX distribution for renders; `uv add "kokoro>=0.9.4" soundfile` adds the local voice.

## What works where

Chat: skill only (no renders). Cowork and Claude Code: skill plus renders. Codex and ChatGPT Work: NOT_RUN.

## Use

Ask for a math, physics or algorithm explainer, a formula derivation or an animated graph.

## Watch out

The voiceover is on whenever Kokoro is installed; say if you want it silent.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall manim-skill@framecore-works-toolbox`.
