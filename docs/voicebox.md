# voicebox: app note

- Upstream: https://github.com/jamiepine/voicebox
- Pinned: 2bcb98d1a8b6fe05e15fbc1559e3085669e4035d (version 0.5.0)
- Review: [reviews/voicebox.md](../reviews/voicebox.md)

Not a plugin: Toolbox lists it so you can find it, and you install it yourself.

## Install

Download the v0.5.0 installer from https://github.com/jamiepine/voicebox/releases/tag/v0.5.0 (Linux: build from source per its README) and start the app. Claude Code: `claude mcp add voicebox --transport http --url http://127.0.0.1:17493/mcp --header "X-Voicebox-Client-Id: claude-code"`. Codex: add the same URL as a streamable HTTP MCP server. Claude desktop app: add its bundled `voicebox-mcp` binary as a local MCP server.

## Use

Install the app, then generate in it, or add its MCP server and ask for a voice-over.

## Watch out

Clone voices only with permission; check each engine model's licence.

## Full removal

Uninstall the app (or delete the skill folder) like any other; remove any MCP registration you added.
