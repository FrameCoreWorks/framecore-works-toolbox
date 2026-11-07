# Upstream

- Repository: https://github.com/dsauce/stickman-kino (MIT, Prerit Ahuja; fonts SIL OFL 1.1,
  GSAP under GreenSock's no-charge standard licence, HyperFrames Apache-2.0; see the upstream
  THIRD_PARTY_NOTICES.md)
- Reviewed commit: d3d665301c0b62f04c885785e6bd6044de0785c6 (npm stickman-kino 1.0.0, 2026-10-08)

This wrapper contains no upstream code or skill text. Its skill is our own: it checks out the
upstream repository at the reviewed commit inside the user's project, after the user's yes,
installs the upstream lockfile with `npm ci`, and then follows the upstream skills from that
checkout. The upstream plugin is not listed directly because `stickman setup` installs
`kokoro-onnx` and `soundfile` without pinned versions and fetches system packages with
`apt-get download`, and because its top-level `bin/` directory stops claude.ai and Cowork from
installing it. The wrapper pins the optional voice packages and never runs `setup`.
Review: ../../reviews/stickman-kino.md
