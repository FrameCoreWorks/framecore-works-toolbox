# Upstream

- Repository: https://github.com/patch-gg/pixelfx (MIT, Patch; parts adapted from Hugo Duprez's
  Sprite Fusion effects and rehan-remade's Hollow Crown, both MIT; see the upstream NOTICE.md)
- Reviewed commit: a84159688af3ca37a4be05a0d422b94451b2e24e (version 0.3.0, 2026-10-31)

This wrapper contains no upstream code or skill text. Its skill is our own: it checks out the
upstream repository at the reviewed commit inside the user's project, after the user's yes, and
then follows the upstream skill from that checkout. The upstream plugin is not listed directly
because its skill clones the unpinned default branch next to the project before anything else.
The Patch Pixel font in the upstream `gallery/fonts` is Patch's own (all rights reserved) and is
never shipped in a deliverable.
Review: ../../reviews/pixelfx.md
