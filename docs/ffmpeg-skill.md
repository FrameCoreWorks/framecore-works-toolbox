# ffmpeg-skill: installation and use

- Upstream: https://github.com/kajisho5/ffmpeg-skill
- Pinned commit: `1ae1bdf1ca0adbb1606fbca493948b1bbb2f83ff` (version 2.17.3, MIT).
- Review: [reviews/ffmpeg-skill.md](../reviews/ffmpeg-skill.md).

## Installation

The Toolbox catalog lists this independently installed original; selecting or
installing the catalog does not install ffmpeg-skill, FFmpeg, models or MCP.

For Claude's marketplace, the entry is `ffmpeg-skill@framecore-works-toolbox`.
The upstream ships its own Claude plugin manifest and marketplace, and this
catalog pins the complete original repository. Native marketplace installation
and skill discovery have not been tested in this session. The upstream has a
top-level `bin/`; claude.ai / Cowork compatibility is unknown. Do not claim an
installation succeeded until the host shows the actual installed skill.

For Codex or another local skill host, use the upstream's documented native
skill installer from a checkout verified at the pinned commit. Select and
approve the exact target directory first: its installer writes files and can
refresh an existing target. A clean custom directory was tested; actual Codex
registration and a fresh Codex conversation remain NOT_RUN. Do not silently
replace an existing installation. The tested source is the original at the
commit above; an npm package of the same version has not been compared here.

ChatGPT Work can use a local CLI only when the actual host exposes the required
filesystem and process tools. No portable Work package or stdio MCP connection
for this entry has been established. Offer a host-specific setup plan and report
missing capabilities; a marketplace listing is not native Work installation.

## Requirements and setup

Python 3.10+ recommended, FFmpeg/FFprobe 6.1+ recommended; individual operations
need particular encoders or filters. Run the tool's `doctor` when checking the
actual machine. Its 42 tools are described by the generated contract; the
optional local stdio MCP server advertises 12 by default. Connecting the server
is a separate user-requested action.

Transcription needs an optional Whisper or Parakeet engine/model. Some engines
download weights on first use; check engine, model, destination and network
scope before activating them. No model or engine is installed by the catalog.

## Use and evidence

Ask for an authorized local operation, such as aligning a camera with a recorder,
converting HDR to SDR or preparing a multicam edit. Keep originals, identify
outputs and inspect the actual result. Audio correlation does not confirm lip
sync, and contact sheets do not track or identify subjects. `--dry-run` has
documented measurement/verification exceptions; `--plan` writes a plan.
When used with FrameCut, Studio owns the accepted board and master timeline.

## Full removal

Remove the selected entry through the host's own plugin or skill removal route.
For a manual upstream native skill installation, inspect its recorded target
and remove only the installed `ffmpeg-skill` directory when authorized; the
installer's `--uninstall` targets are host-specific. Separately review any MCP
configuration, downloaded models and generated media; do not delete user
files or shared FFmpeg installations as a side effect.
