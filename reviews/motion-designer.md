# Review: motion-designer

## Entry

- Name: motion-designer
- Status: active
- Upstream: https://github.com/kaventro/motion-designer
- Author: kaventro (GitHub user)
- License: MIT
- Commit: 7d0b8bb78ddd2c91c57db9d1e83fcf711304bdb8
- Upstream version: 1.2.0
- Kind: plugin
- Eligibility: upstream ships `.claude-plugin/plugin.json` and its own `.claude-plugin/marketplace.json`
- Source: github
- Reviewed on: 2026-10-26
- Reviewer: Claude Code session for Kamil (FrameCore Works)
- Owner approval: not required (no hooks or MCP; the optional remote music server is opt-in through an environment variable)

GitHub metadata at review time: 108 stars, 8 forks, created 2026-09-28, last commit 2026-10-01.

## What it is

One skill, `motion-designer`, that makes short videos from code: launch films of apps (the real UI in an iPhone or a laptop window) and other short videos (titles, kinetic type, explainers), cut to music on the beat, checked frame by frame and rendered to MP4, a muted loop, a poster and one self-contained HTML. Ships Node, Python and shell scripts under `skills/motion-designer/scripts/`; also `docs/`, `evals/`, `examples/`, `site/` and `tests/` in the repo. No commands, agents, hooks or MCP servers.

## Files reviewed

`.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `skills/motion-designer/SKILL.md` (routing and steps), `skills/motion-designer/reference/setup.md`, `skills/motion-designer/scripts/install.sh`, `scripts/music_gen.py` (network part), and a scan of all `.js`, `.mjs`, `.py` and `.sh` files for URLs, process execution, environment variables and home-directory writes. Repo cloned as data at the pinned commit; nothing was run.

## What it installs and writes

- Install: the whole repo is copied into the plugin cache (github source).
- At use: films are written to the user's project (`out/`).
- `~/.cache/motion-designer/` (or `MOTION_DESIGNER_HOME`): a browser profile for headless Chrome, and optional engines installed on request: Chatterbox voices (Python venv), Kokoro voices (model files from GitHub releases), ACE-Step music (git clone).
- `scripts/install.sh <tool>` installs node, chrome, ffmpeg, python3, uv and others with the system package manager (`brew`, `sudo apt-get`/`dnf`/`pacman`) or `curl https://fnm.vercel.app/install | bash` for Node on Linux. The skill's setup reference says to show the exact command and install only after the user's yes.

## Hooks

None.

## Network traffic

- Optional engine downloads (only when the user agrees to install them): Kokoro models from `github.com/thewh1teagle/kokoro-onnx` releases, ACE-Step from `github.com/ace-step/ACE-Step-1.5`, Python packages through uv or pip, Node through fnm.
- Optional remote music generation: `scripts/music_gen.py` posts to `MOTION_DESIGNER_ACESTEP_URL` (with `MOTION_DESIGNER_ACESTEP_KEY`) only if the user sets that variable; otherwise it runs locally.
- `api.github.com` appears only in `site/site.js` (the project website), not in the skill.

## Changes to prompts or tool results

None beyond the plugin's own skill instructions or MCP tools when they are used.

## Data sent outside

Nothing by default. With `MOTION_DESIGNER_ACESTEP_URL` set, music prompts go to that server.

## Requirements

node 22+, Chrome or Chromium, ffmpeg and ffprobe, python3 3.9+; uv recommended; optional voice and music engines. macOS or Linux (Windows through WSL2). Rendering needs Claude Code or Cowork on a machine with these tools.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS (Claude Code 2.1.310): marketplace add and `claude plugin install motion-designer@framecore-works-toolbox` succeeded; `installed_plugins.json` records gitCommitSha 7d0b8bb78ddd2c91c57db9d1e83fcf711304bdb8. Using the plugin was NOT_RUN. Temporary config dir deleted.
- claude.ai (owner, 2026-10-26): toolbox synced at c607fff, every plugin synced. Warning: unrecognized key `$schema` in plugin.json stripped (it only points editors at a schema; no effect). Versions after adding the plugin: not reported yet.
- Cowork: NOT_RUN

## Risks

1. Setup can run system package installs (some with `sudo`) and a `curl | bash` for Node on Linux; the skill asks first, but read each command before saying yes.
2. Optional engines download large models into `~/.cache/motion-designer/`.
3. Young project with few stars (108); pinned by commit.

## Verdict

Accept with conditions: approve each setup install deliberately; keep the remote music URL unset unless wanted.

## History

- 2026-10-26: added at 7d0b8bb (version 1.2.0) under the owner's blanket approval for the shortlist.
