# Review: pixel-plugin

## Entry

- Name: pixel-plugin
- Status: active
- Upstream: https://github.com/willibrandon/pixel-plugin
- Author: Brandon Williams (willibrandon)
- License: MIT
- Commit: dee350645b705916655c013f208bf5580ecb9317
- Upstream version: 0.5.0
- Kind: plugin
- Eligibility: upstream ships .claude-plugin/plugin.json and its own marketplace.json
- Source: github
- Reviewed on: 2026-10-29
- Reviewer: Claude (cloud orchestration thread), carrying over the Creative Studio registry review at the same commit
- Owner approval: "yes" from Kamil on 2026-10-29 (decision card "Przenieść wszystko do Toolboxa", then "decyzje są już podjęte" accepting the move list)

## What it is

Pixel art drawn through Aseprite from a conversation. Ships four skills (creator, animator, professional, exporter), five commands (`/pixel-setup`, `/pixel-new`, `/pixel-palette`, `/pixel-export`, `/pixel-help`) and the `aseprite` MCP server, a prebuilt pixel-mcp v0.5.0 binary in `bin/` for five platforms (about 40 tools).

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, pixel sprites and retro looks for reels and trailers (previously Studio's recommended extension `pixel-plugin`) | Hand-drawn pixel sprites and frame animation in Aseprite, which Studio's own pixel effects do not draw | Studio review 2026-10-22 read skills, commands and the engine source; Toolbox install PASS; drawing with Aseprite NOT_RUN |

Moved from Creative Studio's recommended-extension registry to Toolbox by owner decision 2026-10-29: Toolbox becomes the single source of installable recommendations and Studio points here.

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: README.md, CLAUDE.md, .claude-plugin/plugin.json and marketplace.json, .mcp.json, skills/*/SKILL.md, commands/*.md, config/, docs/, bin/ (listed, not executed).

## What it installs and writes

The plugin cache (about 35 MB with the five binaries). `/pixel-setup` writes `~/.config/pixel-mcp/config.json` with the Aseprite path. Exports go where the user asks.

## Hooks

None.

## Network traffic

None found. A static look at the Linux binary on 2026-10-22 found the Go runtime and MCP libraries, no network addresses and no telemetry; the binary was not executed.

## Changes to prompts or tool results

Skills and commands load on request. The MCP server only answers tool calls.

## Data sent outside

None found.

## Requirements

Aseprite 1.3.0 or later installed and licensed by the user (commercial, not bundled). Claude Code with local MCP (Cowork and claude.ai refuse plugins with a top-level `bin/`). `bin/pixel-mcp` is a bash launcher, so native Windows needs a bash shell (Git Bash or WSL).

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-10-29 in an isolated CLAUDE_CONFIG_DIR: `claude plugin marketplace add` of this repository, `claude plugin install pixel-plugin@framecore-works-toolbox` succeeded, `claude plugin list` showed it enabled, and a headless `claude -p` session listed its skills (9 skills and commands under `pixel-plugin:`). The MCP server was not started (it runs an unverified prebuilt binary and needs Aseprite): NOT_RUN.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. The `bin/` binaries could not be matched to source; treat them as third-party executables. 2. claude.ai and Cowork refuse plugins with a top-level `bin/`, so this works in Claude Code only (Cowork NOT_RUN). 3. Upstream has had no commit for about a year.

## Verdict

accept with conditions: Claude Code only, Aseprite required, binaries unverified.

## History

- 2026-10-29: added at dee3506, moved from Creative Studio's recommended extensions.
