---
name: toolbox
description: >
  Lists the plugins in the FrameCore Works toolbox (Kamil's private Claude
  marketplace FrameCoreWorks/framecore-works-toolbox), grouped by category
  (Creative, Dev tools) with a one-line description of each. Use when the user
  types "toolbox", "/toolbox", "show toolbox", "co jest w toolboxie", "lista
  toolbox", or asks which extra plugins or skills the toolbox has. Not for
  creative production work.
---

# Toolbox

Show the catalog below. Do not start any other workflow or menu.

## Reply format

1. One line: "FrameCore Works Toolbox: <N> plugins in <M> categories."
2. For each category in the catalog, in order: its heading, then its table
   as it is. For a category with no rows, write "No plugins yet."
   Translate the "What it is for" text into the user's language; keep plugin
   names as they are.
3. Do not claim whether a plugin is installed; you cannot see that reliably.
4. One line on how to add a plugin: claude.ai, desktop and Cowork:
   Customize > Plugins > Discover, search the name, Add; Claude Code:
   `claude plugin install <name>@framecore-works-toolbox`. Installed plugins
   are listed in Customize > Plugins under "From marketplaces you added".
5. One line on how to use a plugin: describe the task, or type `/` and pick
   `<plugin>:<skill>`.
6. Stop there. Only if the user asks about one plugin, give its "Use" and
   "Watch out" notes from the details below and its review link.

If the user asks for one category only ("toolbox creative"), show just that
category. Answer in the user's language. Keep it short.

## Catalog

### Creative

| Plugin | What it is for | Works in |
| ------ | -------------- | -------- |
| `animate` | Short animated videos in code (explainers, histories, product reels) in seven built-in styles or one from your references, rendered to MP4 after story, look and storyboard check-ins. | Claude Code and Cowork (needs Node, Playwright Chromium, ffmpeg); chat: skill loads, rendering Unknown |
| `motion-designer` | Launch films of your app (real UI in a phone or laptop frame) and other short videos from code, cut to music and rendered to MP4, loop, poster and HTML. | Claude Code and Cowork (needs node, Chrome, ffmpeg, python3); chat: skill loads, rendering Unknown |
| `logo-design` | Designs, critiques and delivers logos (brief, concepts, SVG construction, testing, brand guidelines) with a library of 1,400+ reference logos. | Chat, Cowork and Claude Code (scripts need python3) |
| `meta-ads-designer` | Art-directs and generates Meta/Instagram ads, posters and flyers with an AI image model, then checks the result. | Chat, Cowork and Claude Code (image generation needs an image tool or a fal.ai key) |
| `hallmark` | Designs web pages and app UIs that do not look AI-generated, with themes, a slop linter and optional generated images (Together AI). | Chat: skill. Cowork and Claude Code: skill plus scripts (Node, Chrome) |
| `open-design` | Connects Claude to the local Open Design app (139 design skills, 150 design systems, projects and previews) over MCP; needs the app installed. | Cowork and Claude Code with the Open Design app running; not chat |

### Dev tools

| Plugin | What it is for | Works in |
| ------ | -------------- | -------- |
| `ponytail` | Keeps code changes minimal (YAGNI, stdlib first); also code review, repo audit and a list of deferred shortcuts. Use for coding work, not creative work. | Chat: skills. Cowork and Claude Code: skills plus always-on hooks. Claude Code: plus band mod |
| `antislop` | Six rule skills that keep UI, copy and code from looking AI-generated, plus a local colour-contrast checker. | Chat: skills. Cowork and Claude Code: skills plus local contrast MCP (needs Python 3) |

## Details

### animate

- Use: describe the video ("a 45s explainer of how DNS works, math style,
  16:9") or `/animate:animate`; it asks questions first, then shows story,
  look and storyboard before rendering.
- Watch out: install Node 18+, Playwright Chromium and ffmpeg first; a
  voice-over uses your ElevenLabs connector or the system voice.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/animate.md

### ponytail

- Use: coding tasks pick it up by description; `/ponytail:ponytail-review`,
  `/ponytail:ponytail-audit`, `/ponytail:ponytail-debt`; levels with
  `/ponytail lite|full|ultra|off`.
- Watch out: in Cowork and Claude Code its hooks inject the ruleset into
  every session and subagent, also in creative work; turn it off there with
  `/ponytail off`, or make it on-demand with `PONYTAIL_DEFAULT_MODE=off`
  (see the plugin's docs in the toolbox repo). Keep the `webhookUrl` option
  empty.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/ponytail.md

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
