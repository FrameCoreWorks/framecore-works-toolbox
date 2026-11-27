# Upstream

- Repository: https://github.com/TNTwise/rife-ncnn-vulkan (MIT, TNTwise; fork of
  https://github.com/nihui/rife-ncnn-vulkan, MIT, nihui)
- Reviewed commit: 5eea93c6e7079dda69d7a0ce9c1106ff5e641143 (release 20250112)
- Runtime: the release assets `macos.zip` (universal x86_64 + arm64, SHA-256
  543bf845a6160d8ad29a10c2b7a0713e78781dc2505c62185f7d14c3265bb4c0) and
  `ubuntu.zip` (SHA-256
  a4166da15a9839350a3695c35d9e19288c5c48c0fc9afc5aacb766d3d7f8ab62), pinned in
  `skills/rife-interpolate/scripts/rife.py`.
- Models: RIFE by hzwer (https://github.com/hzwer/Practical-RIFE, MIT),
  converted to ncnn by the fork; default `rife-v4.26`.

This wrapper contains no upstream code, binaries or models. Its skill and
launcher are our own. The launcher downloads the pinned asset only after the
user's yes, checks its SHA-256, keeps the program, LICENSE and the chosen
models in `~/.cache/framecore/rife/20250112` and deletes the archive.
Review: ../../reviews/rife-interpolate.md
