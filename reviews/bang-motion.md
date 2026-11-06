# Review: bang-motion

## Entry

- Name: bang-motion
- Status: active
- Upstream: https://github.com/bangtutorial/bang-motion
- Author: Bang Tutorial (bangtutorial)
- License: MIT
- Commit: c1aa65e921c970d858705fcb4a53a8294d1a4131
- Upstream version: 1.19.0
- Kind: plugin
- Eligibility: upstream ships .claude-plugin/plugin.json and its own .claude-plugin/marketplace.json
- Source: github (the full upstream plugin)
- Reviewed on: 2026-11-06
- Reviewer: Claude (cloud project thread)
- Owner approval: "yes" from Kamil on 2026-11-06, quote: "No to GL Transition dodajemy. Ten Cloud AIX też. No i myślę, że Bank Motion też będzie dodany, bo to przez tego, że dubluje, może być używany jako uzupełnienie"

## What it is

One skill, `bang-motion` (root SKILL.md, written in Indonesian), with eight references, seven starter HTML files and optional scripts. It builds browser motion graphics that move like video rather than slides: product openers and promos, bumpers and idents, channel intros, kinetic typography, lower thirds and five explainer styles (visual journalism, cartoon stage, catalogue, sketch, collage) as one `index.html` that autoplays and loops, with HTML, CSS, GSAP and optional three.js. A required style brief derives the look from the brand. Optional tools: `serve.py` (local no-cache server), `snap.mjs` and `export-frames.mjs` (puppeteer screenshots and MP4 export), `kepala-ekspresi.py` (PIL, numpy, OpenCV) and an After Effects route through the user's Higgsfield MCP bridge. No commands, agents, hooks or MCP servers of its own.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, browser motion graphics (openers, promos, explainers) | A second method next to Studio's HyperFrames route and Toolbox's `animate` and `motion-designer`, used as a complement by owner decision: anti-slide rules, five explainer styles and seven starters | Overlap with `animate`, `motion-designer` and HyperFrames is known and accepted by the owner (2026-11-06). Isolated Claude Code install PASS and the skill is listed (`bang-motion:bang-motion`); an A/B render NOT_RUN |

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: .claude-plugin/plugin.json and marketplace.json, SKILL.md, README.md, LICENSE, references (8 files), scripts (serve.py, snap.mjs, export-frames.mjs, kepala-ekspresi.py, vo-pauses.html, scripts/ae/bridge/*), starter list (45 tracked files).

## What it installs and writes

The plugin cache (about 2.4 MB). At use: the `index.html` and assets in the user's project; frames and an MP4 only when the user runs the export script.

## Hooks

None.

## Network traffic

Generated pages load GSAP 3.12.5 (cdnjs.cloudflare.com, cdn.jsdelivr.net), three@0.161.0 when used, and Google Fonts. The optional scripts need puppeteer, which their comments install with an unpinned `npm i puppeteer` (the AE bridge declares `^25.10.0`). The optional AE route uses the user's Higgsfield MCP and its CDN.

## Changes to prompts or tool results

None. The skill loads by its description.

## Data sent outside

None by default. The optional After Effects route exports frames through the user's own Higgsfield MCP bridge; it applies only when the user has After Effects and that bridge set up.

## Requirements

A browser. Optional: Python 3 (server, face script with PIL, numpy, OpenCV), Node with puppeteer (screenshots, MP4 export), ffmpeg, After Effects with the Higgsfield bridge.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-11-06: `claude plugin install bang-motion@framecore-works-toolbox` succeeded, `claude plugin list` showed it enabled at 1.19.0, and a headless `claude -p` session listed `bang-motion:bang-motion` (the root SKILL.md is discovered).
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Skill text is in Indonesian; the answer still follows the user's language, but quoted rules may come back in Indonesian. 2. Optional scripts suggest an unpinned `npm i puppeteer`; install an exact version when the user asks for export. 3. Pages depend on CDNs at playback; for offline delivery bundle GSAP and the fonts. 4. Overlaps Studio's motion routes; pick one route per job.

## Verdict

accept (owner decision, as a complement to Studio's motion routes).

## History

- 2026-11-06: added at c1aa65e.
