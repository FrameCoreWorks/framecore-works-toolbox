# papercut-explainer: install notes

- Upstream: https://github.com/0xS4N4TG/papercut-explainer
- Pinned commit: ff8223abc8136cc09e8d7e9b62ecb5d080c389e1 (version 0.1.0 (library))
- Wrapper: [plugins/papercut-explainer](../plugins/papercut-explainer/) (our own skill; checks out the upstream at the pinned commit)
- Review: [reviews/papercut-explainer.md](../reviews/papercut-explainer.md)

## Install

See [install.md](install.md). Plugin id: `papercut-explainer@framecore-works-toolbox`.

## Setup after install

None up front. On first use the skill asks once, then clones papercut-explainer (about 35 MB) into `papercut-explainer/` in the project at the pinned commit. Renders need git, Node.js 20+, ffmpeg and python3 with numpy and Pillow; the local voice is a separate, asked download of several GB.

## What works where

Chat: skill only (scripts, storyboards, style prompts). Cowork and Claude Code: skill plus renders. Codex and ChatGPT Work: the wrapper has a skill folder, so it can be saved as a private plugin; renders NOT_RUN.

## Use

Ask for a cut-paper or papercut explainer reel from a link: a repository, product page or announcement.

## Watch out

Never move the checkout off the pinned commit without a new review; Remotion needs a paid licence for companies above its size threshold.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall papercut-explainer@framecore-works-toolbox`, delete the project's `papercut-explainer/` folder and, if the voice was installed, `~/.local/share/papercut-explainer`.
