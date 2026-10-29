# Review: scenario-kinetic-film

## Entry

- Name: scenario-kinetic-film
- Status: active
- Upstream: https://www.scenario.com/explorations/kinetic-film/
- Author: Scenario (scenario.com)
- License: Unknown for the code (no licence file in the archive; not in the MIT repo scenario-labs/skills). Bundled fonts Archivo, JetBrains Mono, Instrument Sans: SIL OFL 1.1
- Pin: sha256:2217ab5dbd452185a5c3c1509994da46b1ac20d2ebeaa888536244372ce73ebf
- Upstream version: archive scenario-kinetic-film-skill.zip (2026-10-29)
- Kind: app
- Eligibility: app note: not a plugin; a skill archive from a web page, not a Git repository, listed in plugins/toolbox/apps.json with manual install steps, never installed from the marketplace
- Source: none (manual install)
- Reviewed on: 2026-10-29
- Reviewer: Claude (cloud thread "Włącz skill Scenario Kinetic Film")
- Owner approval: "yes" from Kamil on 2026-10-29 (decision card "Notatka w Toolboxie po przebudowie")

## What it is

One skill for short kinetic-typography films (launch films, game teasers, trailers) built as code: a `spec.js` of scene blocks on the music's beat grid, a JavaScript engine where every frame is a pure function of time, Playwright and ffmpeg renders at 1080p or 4K with sub-frame motion blur, and `finish.py` gates that fail a film with too many still frames or holds over 0.6 s. Music, a sound-effect kit and key art come from the Scenario MCP server (paid credits, priced with a dry run before each run).

## Files reviewed

The archive as data, nothing executed: `SKILL.md`, 5 references, `engine/` (core.js, blocks.js, compositor.js, main.js, index.html, 3 OFL fonts with licences), 15 scripts (Node, Python, shell), 3 examples. 39 files, 1.3 MB.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, kinetic-type launch films and teasers | A ready engine scored with Scenario-generated music at an exact tempo and a sound kit, with measured dynamism gates and a 4K master check | Checksum, unzip into a temporary HOME skills folder and removal PASS; render, Scenario generation and host invocation NOT_RUN |

## Install (manual)

See [docs/scenario-kinetic-film.md](../docs/scenario-kinetic-film.md): download, check SHA-256 2217ab5dbd452185a5c3c1509994da46b1ac20d2ebeaa888536244372ce73ebf, unzip into `~/.claude/skills` or `~/.agents/skills`, install Playwright at an exact version.

## Hooks, MCP, prompts

No hooks, no MCP server bundled, no changes to prompts or tool results. The skill tells the agent to use the user's own Scenario MCP connection.

## Network traffic

Scripts serve the film folder on 127.0.0.1 only. `get_fonts.sh` downloads fonts from the `main` branch of google/fonts only when the bundled fonts are missing. The skill's instructions run `npm install playwright` without a version (unpinned: docs ask for an exact version) and send generation prompts and uploads to Scenario.

## Data sent outside

Prompts, and any files the user chooses to upload, to Scenario through its MCP server. No telemetry.

## Requirements

Node 18+, Playwright with Chromium or Chrome, ffmpeg and ffprobe, Python 3 with numpy and opencv-python-headless, a Scenario account with credits. Parts of `render.py` and `finish.py` assume macOS.

## Evidence

2026-10-29: archive from Kamil identical to the upstream download (its SHA-256 equals the hash in the download URL). Checksum, install into a temporary HOME and removal PASS. Rendering, Scenario runs and host activation NOT_RUN.

## Verdict

accept as an app note: listed for discovery with manual steps; Toolbox installs nothing and no upstream code is copied. Not a marketplace entry: no Git repository to pin, no code licence, unpinned Playwright install in the upstream instructions.

## History

- 2026-10-29: added as an app note by owner decision.
