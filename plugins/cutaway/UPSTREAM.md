# Upstream

- Repository: https://github.com/Nyxera0x/cutaway (MIT, Nyxera0x and whaleyxbt; built on
  whaleyxbt/claude-motion, MIT; recorded samples CC0 from Freesound; fonts Inter and
  JetBrains Mono SIL OFL 1.1 from npm)
- Reviewed commit: 5d8f1c6efe0ed65a8fc7647a7a2a3ee9fbb4d20a (package 1.0.0, 2026-11-06)

This wrapper contains no upstream code or skill text. Its skill is our own: it checks out the
upstream repository at the reviewed commit inside the user's project, after the user's yes,
installs the upstream lockfile with `npm ci`, and then follows the upstream method from that
checkout. The upstream skill is not listed directly because its documented install
(`npx skills add Nyxera0x/cutaway`) takes the current `main`, and its first run installs
packages and a browser in the skill folder without asking. The optional Kokoro narrator is our
addition, with pinned packages and hash-checked model files.
Review: ../../reviews/cutaway.md
