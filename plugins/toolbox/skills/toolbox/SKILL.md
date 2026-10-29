---
name: toolbox
description: >
  Lists the plugins in the FrameCore Works toolbox across Claude, ChatGPT Work
  and Codex, from FrameCoreWorks/framecore-works-toolbox, grouped by category
  (Creative, Dev tools, Marketing & growth) with a one-line description of each. Use when the user
  types "toolbox", "/toolbox", "show toolbox", "co jest w toolboxie", "lista
  toolbox", or asks which extra plugins or skills the toolbox has. Also
  load it first for a bare invocation of the FrameCore Works Toolbox plugin
  (an @FrameCore Works Toolbox mention with no other text, or a message that
  arrives empty with this plugin attached): answer with the catalog, never
  with "your message was empty". "Toolbox" here always means this plugin
  catalog, never a list of the host's own tools or connectors. Also the
  entry for Earshot, a local audio capability built into Toolbox: measuring
  loudness (LUFS, true peak), choosing or comparing sound effects, checking
  audio-to-picture sync, rendering cue effects from its sound bank, and
  Earshot task requests from Creative Studio. Not for music composition,
  voice-over, video editing or other creative production.
---

# Toolbox

Two jobs, kept apart. A catalog request gets the catalog below and nothing
else; do not start any other workflow or menu. An Earshot task (section
"Built-in capability: Earshot") runs the capability. A question about what
exists (also "toolbox audio") gets the catalog; a request naming a file, cue
list or audio task to run goes to Earshot. If a message is both, show the
catalog and offer the Earshot step.

## Reply format

1. One line: "FrameCore Works Toolbox: plugins by category." Do not
   state a plugin count; it goes stale and is easy to miscount.
2. For each category in the catalog, in order: its heading, then its table
   as it is. For a category with no rows, write "No plugins yet."
   Translate the "What it is for" text into the user's language; keep plugin
   names as they are.
3. Do not claim whether a plugin is installed; you cannot see that reliably.
4. Give one installation line for the actual host, following
   [installation](references/installation.md). In ChatGPT Work use Plugin
   Creator for an available portable package; in Codex use its observed plugin
   route or documented native skill installation; in Claude use the marketplace.
   Do not suggest Claude commands in another host or treat a catalog listing
   as an installable package for every host.
5. Give one use line for that host: describe the task or select its installed
   skill/plugin. Use Claude slash-command examples only in Claude.
6. Stop there. Only if the user asks about one plugin, give its "Use" and
   "Watch out" notes from the details below and its review link.

If the user asks for one category only ("toolbox creative"), show just that
category. Answer in the user's language. Keep it short.

## Host compatibility and independence

Unless a row explicitly names another host, the catalog's "Works in" cells and slash-command examples describe
Claude chat, Cowork and Claude Code. They do not establish ChatGPT Work or
Codex support for those third-party entries. Label that scope once above the
catalog. For an individual tool in another host, check its current reviewed
package and actual runtime requirements; otherwise report Unknown / NOT_RUN.
The Toolbox catalog itself is portable. Installing it installs this catalog
only; it neither bundles nor activates the other entries.

Each local wrapper must work without Creative Studio and without sibling
plugins. Toolbox maintains discovery and installation information. Creative
Studio owns cross-plugin selection, sequencing and handoffs. Do not invoke
Studio, Open Assets or another companion as a prerequisite for using Toolbox.

## Built-in capability: Earshot

Earshot is part of this plugin, not a catalog entry to install separately.
Its instructions are [references/earshot/earshot.md](references/earshot/earshot.md);
read that file before any Earshot step. Discovery for other plugins is
`capabilities.json` in the plugin root.

- Route here: a request to measure, hear, choose, compare or sync-check
  audio, trim a sound-effect take, render cue sound effects from the Earshot bank, or a
  `framecore-task-request/1` with `provider.capability: "earshot"`.
- First run `status --json` with the launcher named in the instructions.
  Setup, model downloads, model reuse from another root and adding source
  are plans until the user agrees; then add `--yes`. Return a needed setup as
  `needs_consent` with that plan, not as a failure.
- `status` lists other runtime roots under `candidates` and never picks one;
  the user chooses `--root`. For an `unlocked_legacy` root, offer a new locked
  root with `fetch-models --from <old root>`; use `--allow-unlocked` only with
  the user's agreement and label it in the result.
- For a request with a task id, run the operation through
  `capabilities/earshot/scripts/envelope.py` in the plugin root (syntax in
  the instructions, section 6) so the caller gets a validated
  `framecore-task-result/1` with hashes, readiness and what did not run.
  `envelope.py` refuses `exec`; run each reading as its own `run <command>`.
- There is no other route: no `earshot-audio` plugin, no `earshot-local`
  binary, no Studio `listen.py` bridge and no bare venv interpreter. If the
  launcher cannot run in this host, say so and give the commands; never
  report a reading that did not run.
- Toolbox does not call Creative Studio, Open Assets or any catalog entry.
  The caller keeps the brief, the master timeline and the final review.

## Catalog

### Creative

| Plugin | What it is for | Works in |
| ------ | -------------- | -------- |
| `earshot-audio` | Built into Toolbox: measures, selects and synthesizes audio, builds sound kits and assembles supplied recordings with cue and source evidence. | Built into Toolbox; not a separate install. Engine setup requires Python 3.12 and a consented local install; fresh host activation NOT_RUN |
| `ffmpeg-skill` | Synchronizes recordings, prepares multicam edits, converts HDR footage to SDR and performs local FFmpeg media operations. | Python and FFmpeg required; isolated skill-directory install tested; native client activation NOT_RUN |
| `animate` | Short animated videos in code (explainers, histories, product reels) in seven built-in styles or one from your references, rendered to MP4 after story, look and storyboard check-ins. | Claude Code and Cowork (needs Node, Playwright Chromium, ffmpeg); chat: skill loads, rendering Unknown |
| `motion-designer` | Launch films of your app (real UI in a phone or laptop frame) and other short videos from code, cut to music and rendered to MP4, loop, poster and HTML. | Claude Code and Cowork (needs node, Chrome, ffmpeg, python3); chat: skill loads, rendering Unknown |
| `logo-design` | Designs, critiques and delivers logos (brief, concepts, SVG construction, testing, brand guidelines) with a library of 1,400+ reference logos. | Chat, Cowork and Claude Code (scripts need python3) |
| `meta-ads-designer` | Art-directs and generates Meta/Instagram ads, posters and flyers with an AI image model, then checks the result. | Chat, Cowork and Claude Code (image generation needs an image tool or a fal.ai key) |
| `hallmark` | Designs web pages and app UIs that do not look AI-generated, with themes, a slop linter and optional generated images (Together AI). | Chat: skill. Cowork and Claude Code: skill plus scripts (Node, Chrome) |
| `open-design` | Connects Claude to the local Open Design app (139 design skills, 150 design systems, projects and previews) over MCP; needs the app installed. | Cowork and Claude Code with the Open Design app running; not chat |
| `video-shotcraft` | Cinematic product and promo videos in Remotion from 152 shot recipes and a production template. | Claude Code and Cowork (Node, Remotion); chat: skill loads, rendering Unknown |
| `brag` | Turns the project you just built into a short launch video with one command. | Claude Code and Cowork; chat: skill loads, rendering Unknown |
| `nateherk-design` | Builds premium scroll-driven websites (scrollytelling, motion, typography), optional kie.ai images. | Chat, Cowork and Claude Code |
| `sepia` | Removes AI patterns from fiction and professional prose without changing what it says. | Chat, Cowork and Claude Code |
| `blender-agent-skills` | Blender 5.2 workflows for 3D: modeling, UVs, PBR, rigging, animation and export. | Claude Code and Cowork with Blender installed; chat: guidance only |
| `wondelai-ux-design` | UX and UI design skills. | Chat, Cowork and Claude Code |

### Dev tools

| Plugin | What it is for | Works in |
| ------ | -------------- | -------- |
| `antislop` | Six rule skills that keep UI, copy and code from looking AI-generated, plus a local colour-contrast checker. | Chat: skills. Cowork and Claude Code: skills plus local contrast MCP (needs Python 3) |
| `web-quality-skills` | Web quality checks from Lighthouse and Core Web Vitals: speed, accessibility, best practices. | Chat, Cowork and Claude Code |

### Marketing & growth

| Plugin | What it is for | Works in |
| ------ | -------------- | -------- |
| `marketing-skills` | 52 marketing skills: CRO, copywriting, SEO, email, analytics and launch. | Chat, Cowork and Claude Code |

## Details

### ffmpeg-skill

- Use: ask for a local recording alignment, multicam edit, HDR-to-SDR conform or other
  supported media operation. Install the original entry separately from the catalog.
- Watch out: requires Python, FFmpeg and FFprobe. The tool's audio alignment does not
  establish lip sync or subject tracking. Transcription needs a separate engine and
  may download model weights. Check the actual host's installation route first.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/ffmpeg-skill.md

### earshot-audio

- Use: built into Toolbox; nothing else to install as a plugin. Ask Toolbox to measure
  audio, choose a sound, render cue effects or review sync (in Claude, `/toolbox:toolbox`
  with the task). The separate `earshot-audio` plugin of Toolbox 1.0.x is retired.
- Watch out: installing Toolbox does not install the engine or models. Check runtime
  status and approve a setup plan when needed; an existing runtime is listed, never
  picked for you. It works without Studio or other catalog entries. Full-tier
  inference and fresh host activation remain NOT_RUN.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/earshot-audio.md


### animate

- Use: describe the video ("a 45s explainer of how DNS works, math style,
  16:9") or `/animate:animate`; it asks questions first, then shows story,
  look and storyboard before rendering.
- Watch out: install Node 18+, Playwright Chromium and ffmpeg first; a
  voice-over uses your ElevenLabs connector or the system voice.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/animate.md

### motion-designer

- Use: describe the film ("a 20s launch film of my app, upbeat") or `/motion-designer:motion-designer`; it plans, asks for music and materials, then builds and renders.
- Watch out: setup may install system packages and voice or music engines; say yes only to what you need.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/motion-designer.md

### logo-design

- Use: ask for a logo or a logo critique, or `/logo-design:logo-design`.
- Watch out: the reference library holds real trademarks; do not ship them.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/logo-design.md

### antislop

- Use: loads by description on UI, copy and code work; `/antislop:antislop` for the full rule set.
- Watch out: its skills may load on many tasks; disable it in projects where you do not want its rules.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/antislop.md

### meta-ads-designer

- Use: ask for an ad, poster or flyer, or `/meta-ads-designer:meta-ads-designer`; default format 4:5.
- Watch out: with `FAL_KEY` set it sends prompts to fal.ai; without an image tool you get prompts, not images.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/meta-ads-designer.md

### hallmark

- Use: describe the page or redesign, or `/hallmark:hallmark`.
- Watch out: generated images go to Together AI only with `TOGETHER_API_KEY`; do not run `install-hook.mjs` unless you want a lint hook.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/hallmark.md

### open-design

- Use: with the app running, ask Claude to open or work on an Open Design project; the tools come from the `open-design` MCP server.
- Watch out: needs the Open Design app (`od`) installed and its daemon running; the app itself was not reviewed.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/open-design.md

### video-shotcraft

- Use: describe the product video, or `/video-shotcraft:video-shotcraft`.
- Watch out: needs Node and Remotion; overlaps with Studio's Remotion skill.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/video-shotcraft.md

### brag

- Use: in a finished project, ask for a launch video or `/brag:brag`.
- Watch out: overlaps with motion-designer; pick one per job.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/brag.md

### nateherk-design

- Use: ask for a scroll-driven landing page, or `/nateherk-design:scroll-craft`.
- Watch out: images go to kie.ai only with `KIE_AI_API_KEY`.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/nateherk-design.md


### sepia

- Use: ask to de-AI a text, or `/sepia:sepia`.
- Watch out: overlaps with Studio's Humanizer.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/sepia.md

### blender-agent-skills

- Use: ask for a 3D task in Blender, or `/blender-agent-skills:` and pick a skill.
- Watch out: needs Blender 5.2 on the machine.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/blender-agent-skills.md

### web-quality-skills

- Use: ask to audit or speed up a page, or `/web-quality-skills:`.
- Watch out: no special setup.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/web-quality-skills.md

### marketing-skills

- Use: ask a marketing task (landing page copy, CRO audit, email sequence).
- Watch out: integrations reach external services only with their API keys.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/marketing-skills.md


### wondelai-ux-design

- Use: ask a task in this area or call `/wondelai-ux-design:` and pick a skill.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/wondelai-ux-design.md
