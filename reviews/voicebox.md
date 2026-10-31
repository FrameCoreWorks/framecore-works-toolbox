# Review: voicebox

## Entry

- Name: voicebox
- Status: removed
- Upstream: https://github.com/jamiepine/voicebox
- Author: Jamie Pine (jamiepine)
- License: MIT (app); each engine's model has its own licence
- Pin: 2bcb98d1a8b6fe05e15fbc1559e3085669e4035d
- Upstream version: 0.5.0
- Kind: app
- Eligibility: app note: not a plugin; listed in plugins/toolbox/apps.json with manual install steps, never installed from the marketplace
- Source: none (manual install)
- Reviewed on: 2026-10-29
- Reviewer: Claude (cloud orchestration thread), carrying over the Creative Studio registry review at the same pin
- Owner approval: "yes" from Kamil on 2026-10-29 (decision card "Przenieść wszystko do Toolboxa", then "decyzje są już podjęte" accepting the move list)

## What it is

A local voice studio desktop app (macOS, Windows; Linux from source) running several TTS engines (Qwen3-TTS with voice design, Chatterbox Multilingual with Polish, HumeAI TADA, Kokoro, LuxTTS): voice cloning from seconds of audio, voices designed from a description, long texts, a multi-voice Stories editor, a REST API and an MCP server on 127.0.0.1:17493.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Voice Narration plugin (Creative Studio repository) and Studio voice-overs | A no-code local voice route; Voice Narration can call its REST API | README and terms read; app NOT_RUN |

Moved from Creative Studio's recommended-extension registry to Toolbox by owner decision 2026-10-29.

## Install (manual)

Download the v0.5.0 installer from https://github.com/jamiepine/voicebox/releases/tag/v0.5.0 (Linux: build from source per its README) and start the app. Claude Code: `claude mcp add voicebox --transport http --url http://127.0.0.1:17493/mcp --header "X-Voicebox-Client-Id: claude-code"`. Codex: add the same URL as a streamable HTTP MCP server. Claude desktop app: add its bundled `voicebox-mcp` binary as a local MCP server.

## Network traffic

Model downloads when an engine is first chosen in the app. The REST API and MCP server listen on localhost only.

## Rights

Clone a voice only with its owner's documented permission; never impersonate a real person; disclose synthetic voices where required. Check the chosen engine model's licence before client work.

## Evidence

2026-10-16 (Studio review): README, release tags and responsible-use terms read at v0.5.0. The app was not installed or run: NOT_RUN.

## Verdict

accept as an app note: listed for discovery with manual steps; nothing is installed by Toolbox.

## History

- 2026-10-29: added as an app note, moved from Creative Studio's recommended extensions.
- 2026-10-31: removed by owner decision: Toolbox keeps only entries that install without accounts, API keys or separate desktop apps; it is a separate desktop app to install.
