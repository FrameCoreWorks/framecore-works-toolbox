---
name: toolbox
description: >
  Lists the plugins in the FrameCore Works toolbox (Kamil's private Claude
  marketplace FrameCoreWorks/framecore-works-toolbox), grouped by category
  (Creative, Dev tools, Marketing & growth) with a one-line description of each. Use when the user
  types "toolbox", "/toolbox", "show toolbox", "co jest w toolboxie", "lista
  toolbox", or asks which extra plugins or skills the toolbox has. Also
  load it first for a bare invocation of the FrameCore Works Toolbox plugin
  (an @FrameCore Works Toolbox mention with no other text, or a message that
  arrives empty with this plugin attached): answer with the catalog, never
  with "your message was empty". "Toolbox" here always means this plugin
  catalog, never a list of Claude's own tools or connectors. Not for
  creative production work.
---

# Toolbox

Show the catalog below. Do not start any other workflow or menu.

## Reply format

1. One line: "FrameCore Works Toolbox: plugins by category." Do not
   state a plugin count; it goes stale and is easy to miscount.
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
| `video-shotcraft` | Cinematic product and promo videos in Remotion from 152 shot recipes and a production template. | Claude Code and Cowork (Node, Remotion); chat: skill loads, rendering Unknown |
| `brag` | Turns the project you just built into a short launch video with one command. | Claude Code and Cowork; chat: skill loads, rendering Unknown |
| `nateherk-design` | Builds premium scroll-driven websites (scrollytelling, motion, typography), optional kie.ai images. | Chat, Cowork and Claude Code |
| `sepia` | Removes AI patterns from fiction and professional prose without changing what it says. | Chat, Cowork and Claude Code |
| `blender-agent-skills` | Blender 5.2 workflows for 3D: modeling, UVs, PBR, rigging, animation and export. | Claude Code and Cowork with Blender installed; chat: guidance only |
| `wondelai-ux-design` | UX and UI design skills. | Chat, Cowork and Claude Code |

### Dev tools

| Plugin | What it is for | Works in |
| ------ | -------------- | -------- |
| `ponytail` | Keeps code changes minimal (YAGNI, stdlib first); also code review, repo audit and a list of deferred shortcuts. Use for coding work, not creative work. | Chat: skills. Cowork and Claude Code: skills plus always-on hooks. Claude Code: plus band mod |
| `antislop` | Six rule skills that keep UI, copy and code from looking AI-generated, plus a local colour-contrast checker. | Chat: skills. Cowork and Claude Code: skills plus local contrast MCP (needs Python 3) |
| `web-quality-skills` | Web quality checks from Lighthouse and Core Web Vitals: speed, accessibility, best practices. | Chat, Cowork and Claude Code |
| `hud` | Status line for Claude Code: context use, active tools, agents, todos and cost. | Claude Code only (status line) |
| `planning-with-files` | File-based plans that survive /clear and compaction, re-injected every turn. | Cowork and Claude Code (hooks); chat: skills only |
| `archify` | Interactive architecture, flow, sequence and ERD diagrams from an idea or a codebase, as standalone HTML. | Chat, Cowork and Claude Code |
| `wondelai-code-craftsmanship` | Code quality and software design skills. | Chat, Cowork and Claude Code |
| `wondelai-systems-architecture` | Systems architecture and distributed systems skills. | Chat, Cowork and Claude Code |

### Marketing & growth

| Plugin | What it is for | Works in |
| ------ | -------------- | -------- |
| `marketing-skills` | 52 marketing skills: CRO, copywriting, SEO, email, analytics and launch. | Chat, Cowork and Claude Code |
| `notfair` | SEO, GEO and Google/Meta Ads work through the NotFair service (remote MCP). | Chat (remote MCP), Cowork and Claude Code |
| `linkedin-agent` | LinkedIn content: posts, comments, replies, profile score and a weekly plan. | Chat, Cowork and Claude Code |
| `wondelai-product-strategy` | Product strategy and innovation frameworks. | Chat, Cowork and Claude Code |
| `wondelai-marketing-cro` | Marketing and conversion optimization skills. | Chat, Cowork and Claude Code |
| `wondelai-sales-influence` | Sales, persuasion, and messaging skills. | Chat, Cowork and Claude Code |
| `wondelai-product-innovation` | Product innovation and validation frameworks. | Chat, Cowork and Claude Code |
| `wondelai-strategy-growth` | Business strategy and growth frameworks. | Chat, Cowork and Claude Code |
| `wondelai-team-motivation` | Team motivation and management skills. | Chat, Cowork and Claude Code |
| `wondelai-metaskills` | Fourteen guided journeys that orchestrate the whole skill library step by step: create, improve, and grow a business, website, or app, plus improve code quality, remove technical debt, design code architecture, optimize a conversion flow, and optimize an existing codebase for speed and structure. Each metaskill invokes the right skills phase by phase, asks the user questions at every decision point, and records results as living documents in the project docs/ folder. | Chat, Cowork and Claude Code |

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

### hud

- Use: run its setup command once, `/hud:setup`, then `/hud:configure` to change what it shows.
- Watch out: setup writes a statusLine entry; it replaces another status line such as ponytail's.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/hud.md

### planning-with-files

- Use: start a long task with its planning skill; plans live in your project.
- Watch out: its hooks inject the plan every turn; overlaps with Superpowers plans.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/planning-with-files.md


### archify

- Use: ask for a diagram of a system or plan, or `/archify:archify`.
- Watch out: runs a small update check when used.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/archify.md

### marketing-skills

- Use: ask a marketing task (landing page copy, CRO audit, email sequence).
- Watch out: integrations reach external services only with their API keys.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/marketing-skills.md


### notfair

- Use: connect NotFair, then ask for SEO or ads analysis.
- Watch out: its MCP sends your requests and ad data to notfair.co.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/notfair.md

### linkedin-agent

- Use: ask for LinkedIn posts or a weekly plan.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/linkedin-agent.md

### wondelai-product-strategy

- Use: ask a task in this area or call `/wondelai-product-strategy:` and pick a skill.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/wondelai-product-strategy.md

### wondelai-ux-design

- Use: ask a task in this area or call `/wondelai-ux-design:` and pick a skill.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/wondelai-ux-design.md

### wondelai-marketing-cro

- Use: ask a task in this area or call `/wondelai-marketing-cro:` and pick a skill.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/wondelai-marketing-cro.md

### wondelai-sales-influence

- Use: ask a task in this area or call `/wondelai-sales-influence:` and pick a skill.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/wondelai-sales-influence.md

### wondelai-product-innovation

- Use: ask a task in this area or call `/wondelai-product-innovation:` and pick a skill.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/wondelai-product-innovation.md

### wondelai-strategy-growth

- Use: ask a task in this area or call `/wondelai-strategy-growth:` and pick a skill.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/wondelai-strategy-growth.md

### wondelai-team-motivation

- Use: ask a task in this area or call `/wondelai-team-motivation:` and pick a skill.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/wondelai-team-motivation.md

### wondelai-code-craftsmanship

- Use: ask a task in this area or call `/wondelai-code-craftsmanship:` and pick a skill.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/wondelai-code-craftsmanship.md

### wondelai-systems-architecture

- Use: ask a task in this area or call `/wondelai-systems-architecture:` and pick a skill.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/wondelai-systems-architecture.md

### wondelai-metaskills

- Use: ask a task in this area or call `/wondelai-metaskills:` and pick a skill.
- Watch out: none.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/wondelai-metaskills.md
