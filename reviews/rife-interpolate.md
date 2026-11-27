# Review: rife-interpolate

## Entry

- Name: rife-interpolate
- Status: active
- Upstream: https://github.com/TNTwise/rife-ncnn-vulkan
- Author: TNTwise (fork of nihui/rife-ncnn-vulkan by nihui)
- License: MIT (program); RIFE models MIT (hzwer); bundled ncnn and libwebp BSD-3-Clause, MoltenVK Apache-2.0 (static, macOS)
- Commit: 5eea93c6e7079dda69d7a0ce9c1106ff5e641143
- Upstream version: release 20250112
- Kind: adapted
- Eligibility: adapted: our own wrapper plugin `plugins/rife-interpolate` with its own skill and a standard-library launcher that downloads the pinned release asset after the user's yes (SHA-256 checked) and runs it through ffmpeg; upstream is a command-line program with no skill or plugin manifest
- Source: local wrapper ./plugins/rife-interpolate (UPSTREAM.md names the reviewed commit)
- Reviewed on: 2026-11-27
- Reviewer: Claude (cloud project thread "Dodaj interpolator RIFE do Toolboxa i wtyczek")
- Owner approval: Kamil sent nihui/rife-ncnn-vulkan on 2026-11-27 for Toolbox, FrameCut, FrameMotion and Studio ("kandydat do Toolboxa ... jako interpolator do upłynnienia nagrań"), then chose the TNTwise fork on the decision card "Którą wersję RIFE wcielamy do wtyczek?" (option "Fork TNTwise (nowsze modele)")

## What it is

RIFE (Real-Time Intermediate Flow Estimation) frame interpolation as a portable ncnn + Vulkan program: it makes new frames between existing ones, for smoother playback, slow motion or filling in low-frame-rate renders. The TNTwise fork keeps nihui's program and adds RIFE models up to v4.26.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| FrameCut, smoothing or slowing a shot from footage | Learned interpolation instead of ffmpeg `minterpolate`, which warps and smears on real motion | nihui release 20221029 with rife-v4.6 ran on CPU in a Claude Code cloud container: a 12 fps test clip became 24 fps and the new middle frame sat between its neighbours (moving bar and squares). Fork binary run: NOT_RUN in the cloud (blocked by the session's safety check); Mac GPU run: NOT_RUN at review time |
| FrameMotion, Blender or other expensive renders at a low frame rate | Render fewer frames, interpolate the rest | NOT_RUN; code-rendered motion should be rendered at the target rate instead |

## Files reviewed

Both repositories cloned as data into a temporary folder; nothing upstream was built. Read: README.md, LICENSE, `.github/workflows/release.yml` (macOS build: x86_64 and arm64 joined with lipo, MoltenVK linked statically from the Vulkan SDK 1.2.162.0; Linux build on Ubuntu), `models/` list, git history (fork HEAD 13338e3 on 2026-02-04; nihui last commit a7532fc on 2022-10-23). Release assets downloaded and inspected without running: `macos.zip` 830,643,776 bytes, SHA-256 543bf845a6160d8ad29a10c2b7a0713e78781dc2505c62185f7d14c3265bb4c0, Mach-O universal binary (x86_64, arm64), 49 model folders; `ubuntu.zip` 825,856,265 bytes, SHA-256 a4166da15a9839350a3695c35d9e19288c5c48c0fc9afc5aacb766d3d7f8ab62. `rife-v4.26` is 11 MB.

## What it installs and writes

The wrapper ships only our own files: three manifests, `UPSTREAM.md`, `skills/rife-interpolate/SKILL.md` and `skills/rife-interpolate/scripts/rife.py`. After the user's yes the launcher downloads one release asset into a temporary folder under `~/.cache/framecore/rife/20250112` (or `FRAMECORE_RIFE_HOME`), checks SHA-256, keeps the program, LICENSE and the chosen models (about 45 MB) and deletes the archive. A run writes PNG frames into a temporary folder (deleted unless `--keep-frames`) and the output video where the user asks. Nothing is written into the project by install. The launcher test on 2026-11-27 (cloud) installed rife-v4.26 and rife-v4.6 in 31 s; 32 MB kept.

## Hooks

None.

## Network traffic

github.com release download, once, after the user's yes. The program itself makes no network requests (none found in its source; it reads and writes local images).

## Changes to prompts or tool results

Our skill `rife-interpolate:rife-interpolate` loads by description on frame-rate, smoothing and slow-motion tasks.

## Data sent outside

None.

## Requirements

Python 3, ffmpeg and ffprobe; macOS (Apple Silicon or Intel) or Linux x86_64. A Vulkan GPU for speed (macOS uses Metal through the bundled MoltenVK); without a driver the launcher uses the CPU.

## Install tests

- Launcher `plan` and `install --yes` (cloud, Linux x86_64): PASS 2026-11-27, SHA-256 matched, receipt written.
- Isolated Claude Code install: see docs/verification.md.
- Fork binary run in the cloud: NOT_RUN (blocked by the session's safety check). Mac run with GPU: NOT_RUN until recorded in docs/verification.md.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result.

## Risks

1. Interpolation invents frames: warping and ghosting on fast motion, small text, UI and crossing objects; the skill requires a frame check. 2. Unsigned binary from a personal fork; pinned by SHA-256, built by the fork's public GitHub Actions workflow. 3. 830 MB download once. 4. nihui's original is unmaintained since 2022; the fork is the maintained line.

## Verdict

accept with conditions: download only after the user's yes, frame check before delivery, one shot per run.

## History

- 2026-11-27: added at 5eea93c (release 20250112) as an adapted wrapper; nihui/rife-ncnn-vulkan (a7532fc, release 20221029) reviewed first and kept as the fallback.
