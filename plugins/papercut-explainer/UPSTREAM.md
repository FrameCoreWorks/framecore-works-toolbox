# Upstream

- Repository: https://github.com/0xS4N4TG/papercut-explainer (MIT, 0xS4N4TG; Remotion itself is
  source-available under its own licence, see the upstream THIRD_PARTY.md)
- Reviewed commit: ff8223abc8136cc09e8d7e9b62ecb5d080c389e1 (library 0.1.0, 2026-10-17)

This wrapper contains no upstream code or skill text. Its skill is our own: it checks out the
upstream repository at the reviewed commit inside the user's project, after the user's yes, and
then follows the upstream skills from that checkout. The upstream skills are not listed directly
because `papercut-setup` clones the unpinned default branch and `install.sh` runs
`npx -y skills@latest add remotion-dev/skills` (unpinned; that repository has no licence file)
and links skills into agent folders in the home directory.
Review: ../../reviews/papercut-explainer.md
