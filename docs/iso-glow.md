# iso-glow: app note

- Upstream: https://isoglow.dev/
- Pinned: sha256:6c88dba1424bada2ee651a1b273095f9a13b82dd9362f9bc873600b5bff6b0a1 (version archive iso-glow.zip (2026-10-18))
- Review: [reviews/iso-glow.md](../reviews/iso-glow.md)

Not a plugin: Toolbox lists it so you can find it, and you install it yourself.

## Install

Download https://isoglow.dev/iso-glow.zip, check `shasum -a 256 iso-glow.zip` equals 6c88dba1424bada2ee651a1b273095f9a13b82dd9362f9bc873600b5bff6b0a1 (stop and ask for a new review if it differs), then unzip into `~/.claude/skills` (Claude Code) or `~/.agents/skills` (Codex); in claude.ai upload the folder as a custom skill. Remove by deleting the `iso-glow` folder.

## Use

After installing, ask for a figure ("use the iso-glow skill to draw a lighthouse").

## Watch out

Not a Git repository: the archive pin is a checksum; a changed archive needs a new review.

## Full removal

Uninstall the app (or delete the skill folder) like any other; remove any MCP registration you added.
