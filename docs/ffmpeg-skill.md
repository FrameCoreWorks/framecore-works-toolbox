# ffmpeg-skill: app note

- Upstream: https://github.com/kajisho5/ffmpeg-skill
- Pinned commit: `1ae1bdf1ca0adbb1606fbca493948b1bbb2f83ff` (version 2.17.3, MIT).
- Review: [reviews/ffmpeg-skill.md](../reviews/ffmpeg-skill.md).

## Install in Claude Code (by hand)

claude.ai and Cowork refuse plugins with a top-level `bin/`, and this upstream
ships one, so it is an app note, not a marketplace entry: the Toolbox
marketplace does not install it. In Claude Code, clone it at the pinned commit
and add the clone as its own marketplace:

```bash
git clone https://github.com/kajisho5/ffmpeg-skill ~/.claude/framecore-apps/ffmpeg-skill
git -C ~/.claude/framecore-apps/ffmpeg-skill checkout 1ae1bdf1ca0adbb1606fbca493948b1bbb2f83ff
claude plugin marketplace add ~/.claude/framecore-apps/ffmpeg-skill
claude plugin install ffmpeg-skill@ffmpeg-skill
```

Tested 2026-10-29 in an isolated Claude Code 2.1.312 config: the plugin
installed and was enabled at the pinned version. A newer upstream commit needs
a new review before you move the checkout.

## Other hosts

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

In Claude Code: `claude plugin uninstall ffmpeg-skill@ffmpeg-skill`, then
`claude plugin marketplace remove ffmpeg-skill` and delete
`~/.claude/framecore-apps/ffmpeg-skill`. On other hosts use their own removal route.
For a manual upstream native skill installation, inspect its recorded target
and remove only the installed `ffmpeg-skill` directory when authorized; the
installer's `--uninstall` targets are host-specific. Separately review any MCP
configuration, downloaded models and generated media; do not delete user
files or shared FFmpeg installations as a side effect.
