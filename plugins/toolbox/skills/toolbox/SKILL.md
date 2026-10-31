---
name: toolbox
description: >
  Lists the plugins in the FrameCore Works toolbox across Claude, ChatGPT Work
  and Codex, from FrameCoreWorks/framecore-works-toolbox, grouped by category
  (Creative, Dev tools, Marketing & growth) with a one-line description of
  each. Use when the user types "toolbox", "/toolbox", "show toolbox", "co jest
  w toolboxie", "lista toolbox", or asks which extra plugins or skills the
  toolbox has. Also load it first for a bare invocation of this plugin (an
  @FrameCore Works Toolbox mention with no other text, or an empty message
  with this plugin attached): answer with the catalog, never with "your message
  was empty". "Toolbox" always means this catalog, never the host's own tools
  or connectors. Also the entry for Earshot, the local audio capability built
  into Toolbox: loudness (LUFS, true peak), choosing or comparing sound
  effects, audio-to-picture sync, cue effects from its sound bank, and Earshot
  task requests from Creative Studio. Not for music composition, voice-over,
  video editing or other creative production.
---

# Toolbox

Two jobs, kept apart. A catalog request gets the catalog below and nothing
else; do not start any other workflow or menu. An Earshot task (section
"Built-in capability: Earshot") runs the capability. A question about what
exists (also "toolbox audio") gets the catalog; a request naming a file, cue
list or audio task to run goes to Earshot. If a message is both, show the
catalog and offer the Earshot step.

## Reply format

Write for someone reading on a phone who has never used a terminal: short
lines, plain words, no command unless they ask how it works.

1. One line: "FrameCore Works Toolbox: tools I recommend next to Creative
   Studio. Pick the numbers you want." Do not state a plugin count; it goes
   stale and is easy to miscount.
2. Two blocks, numbered continuously (1, 2, 3 ... across both):
   - **Ready to use** (rows with Runs `ready`): work as soon as they are
     added.
   - **Installs tools for this conversation** (rows with Runs
     `session-install`). Under the heading, one line: "These install
     programs such as Node, ffmpeg or a browser when you first use them.
     The install lasts only for this conversation; a new one installs them
     again (the plugin itself stays added)." Also one line that you ask
     before any download over about 300 MB.
   - **Needs your computer** (rows with Runs `computer`), only when such a
     row exists: say what has to be on the computer in a few words.
3. Inside each block, group entries by the group before the colon in the
   "Menu" column, in this order: Design & web, Writing, Video & animation,
   Sound, Marketing, Code. Show each group name once as a short bold line
   (translated), then one line per entry: `number. name: menu text`, where
   the menu text is the part after the colon, translated. No second
   sentence, no requirements list, no "Works in" text. Keep plugin names as
   they are. Add "(built into Toolbox)" after Earshot and "(overlaps with
   Studio's ...)" only where the menu text already names an overlap.
4. In ChatGPT Work and Codex, add "(Claude only)" after the name of every
   third-party entry without a reviewed route for that host (see "Host
   compatibility" below); keep it in the list so the user sees what exists.
   In Claude, say nothing about hosts.
5. Do not claim whether a plugin is installed; you cannot see that reliably.
6. End with one question: "Which numbers do you want? You can also say
   none, or ask about one number." Stop there.

If the user asks for one category or group only ("toolbox creative"), show
just that, numbered the same way. Answer in the user's language. If the user
asks about one entry, give its full "What it is for", "How it helps Studio",
"Works in", "Use" and "Watch out" notes and its review link.

## After the user picks numbers

The picked numbers are the user's request for those entries. For each one,
in order, say in one plain sentence what will be added and where, then follow
[installation](references/installation.md) for the actual host:

- Claude Code with a shell: add the Toolbox marketplace once, then install
  each picked entry; a new conversation loads them. In a Claude Code cloud
  session (for example from the phone) the install lasts only for that
  session's container; to keep an entry, guide the user step by step to add
  the marketplace `FrameCoreWorks/framecore-works-toolbox` once under
  Customize > Plugins in claude.ai and turn the entry on there.
- Claude apps (claude.ai, desktop chat, Cowork): guide the user step by step
  through Customize > Plugins (add the marketplace once, then each entry).
- App notes and Earshot's engine: give their own steps (docs link; Earshot
  through its plan and the user's yes).
- ChatGPT Work and Codex: install only an entry that has a reviewed route
  for this host; for a "(Claude only)" entry say in one line that it works
  in Claude and give the Claude steps if the user wants them.

Report each picked entry as installed, waiting for the user's step, or not
available on this host. For a `session-install` entry, install its tools
into a temporary folder of this conversation (for example
`${TMPDIR:-/tmp}/framecore-session`) when the task first needs them, say
"installing X because Y needs it", ask first for anything over about
300 MB, and remind the user once that a new conversation installs them
again. If the host blocks the download (network policy, no shell), name the
blocked step and give the steps for a session or computer that allows it,
not a failed install. A "Needs your computer" entry picked without that
computer gets its steps for later.

## Host compatibility and independence

Unless a row explicitly names another host, the catalog's "Works in" cells and slash-command examples describe
Claude chat, Cowork and Claude Code. They do not establish ChatGPT Work or
Codex support for those third-party entries. Label that scope once above the
catalog. For an individual tool in another host, check its current reviewed
package and actual runtime requirements; otherwise report Unknown / NOT_RUN.
The Toolbox catalog itself is portable. Installing it installs this catalog
only; it neither bundles nor activates the other entries.

Never convert, rewrite, repackage or "adapt" a catalog entry into another
host's plugin format, and never inspect or download entries on your own after
Toolbox is installed. In ChatGPT Work or Codex an entry without its own
reviewed package for that host is listed as available in Claude only; say so
in one line and stop. Copying an upstream into a new package is not allowed
(Toolbox never holds or rebuilds upstream code). Install one entry only when
the user asks for that entry and the host has a reviewed route for it.

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

| Plugin | What it is for | How it helps Studio | Runs | Works in | Menu |
| ------ | -------------- | ------------------- | ---- | -------- | ---- |
| `earshot-audio` | Built into Toolbox: measures, selects and synthesizes audio, builds sound kits and assembles supplied recordings with cue and source evidence. | Gives Studio's films sound effects placed on the right frame and a loudness check before delivery. | session-install | Built into Toolbox. Installs its Python 3.12 engine (light about 470 MB) for the conversation after your yes; the full tier also downloads models (PyTorch, Hugging Face) and needs those hosts allowed. Claude Code (desktop, cloud, phone), Cowork, Codex and ChatGPT Work with public internet access on; fresh host activation NOT_RUN | Sound: loudness, sound effects and sync for your video |
| `animate` | Short animated videos in code (explainers, histories, product reels) in seven built-in styles or one from your references, rendered to MP4 after story, look and storyboard check-ins. | Turns a Studio script and storyboard into a rendered explainer or animated video. | session-install | Claude Code (desktop, cloud, phone) and Cowork install the tools for the conversation (Node 18+, Playwright Chromium, ffmpeg); claude.ai chat: skill loads, rendering Unknown | Video & animation: animated explainers rendered to MP4 |
| `motion-designer` | Launch films of your app (real UI in a phone or laptop frame) and other short videos from code, cut to music and rendered to MP4, loop, poster and HTML. | Renders Studio's app-launch and promo concepts as finished MP4 films cut to music. | session-install | Claude Code (desktop, cloud, phone) and Cowork install the tools for the conversation (Node 22+, Chromium, ffmpeg, python3; Linux works); claude.ai chat: skill loads, rendering Unknown | Video & animation: app launch films with real UI, cut to music |
| `logo-design` | Designs, critiques and delivers logos (brief, concepts, SVG construction, testing, brand guidelines) with a library of 1,400+ reference logos. | Gives Studio's brand and campaign work a real logo with construction and usage rules. | ready | Chat, Cowork and Claude Code (scripts need python3, which sessions have) | Design & web: logos with brand rules and SVG files |
| `hallmark` | Designs web pages and app UIs that do not look AI-generated, with themes, a slop linter and optional generated images (Together AI). | Builds the landing page or app screen that a Studio campaign points to, without the AI look. | ready | Chat: skill. Cowork and Claude Code: skill plus optional screenshot scripts (Node, Chromium) | Design & web: pages and app screens that do not look AI-made |
| `brag` | Turns the project you just built into a short launch video with one command. | Makes a quick launch video of a finished project when a full Studio production is not needed. | session-install | Claude Code (desktop, cloud, phone) and Cowork install the tools for the conversation (Node, HyperFrames tooling); claude.ai chat: skill loads, rendering Unknown | Video & animation: quick launch video of a finished project |
| `nateherk-design` | Builds premium scroll-driven websites (scrollytelling, motion, typography), optional kie.ai images. | Builds the scroll-driven website for a Studio campaign or brand story. | ready | Chat, Cowork and Claude Code | Design & web: premium scroll-driven websites |
| `sepia` | Removes AI patterns from fiction and professional prose without changing what it says. | Gives Studio's scripts and copy a second pass that removes AI-sounding prose. | ready | Chat, Cowork and Claude Code | Writing: removes the AI tone from text (overlaps with Studio's Humanizer) |
| `wondelai-ux-design` | UX and UI design skills. | Adds UX and UI design method when a Studio project includes an app or site screen. | ready | Chat, Cowork and Claude Code | Design & web: UX and UI method for app and site screens |
| `taste-skill` | Art direction for landing pages, product pages, dashboards and app screens, with openly licensed pictures and a real-browser check. | Gives Studio's web and screen work a researched art direction and a browser check. | ready | Chat: skill. Cowork and Claude Code: skill plus a browser check that installs for the conversation | Design & web: art direction for landing pages and screens |
| `hairline` | Isometric line figures that answer the pointer on a web page, drawn as one HTML file or added to a project as a library. | Adds interactive isometric line figures that match Studio's Hairline motion style on web pages. | ready | Chat: skills. Cowork and Claude Code: skills plus a browser check | Design & web: interactive isometric line figures for web pages |
| `huashu-art-motion` | Art-style animation in 36 styles from cave painting to Ghibli and 9 explainer grammars, with reference breakdown and shot-list checks. | Adds 36 art styles and 9 explainer grammars to Studio's animation ideas and shot lists. | session-install | Claude Code (desktop, cloud, phone) and Cowork install the tools for the conversation (Node, Chromium); chat: skill only | Video & animation: animation in 36 art styles |
| `anatomy` | Detailed interactive isometric SVG figures that explain a technical idea as a physical object, with optional WebGL shaders. | Explains a technical product in a Studio piece as a detailed isometric figure. | ready | Chat: skill. Cowork and Claude Code: skill plus optional checks (Node, Chromium) | Design & web: interactive isometric figures that explain a product |

### Dev tools

| Plugin | What it is for | How it helps Studio | Runs | Works in | Menu |
| ------ | -------------- | ------------------- | ---- | -------- | ---- |
| `antislop` | Six rule skills that keep UI, copy and code from looking AI-generated, plus a local colour-contrast checker. | Keeps the UI, copy and code around Studio's work from looking AI-generated. | ready | Chat: skills. Cowork and Claude Code: skills plus a local contrast checker (Python 3) | Writing: rules so UI, copy and code do not look AI-made |
| `web-quality-skills` | Web quality checks from Lighthouse and Core Web Vitals: speed, accessibility, best practices. | Checks the speed and accessibility of the pages a Studio campaign sends people to. | ready | Chat, Cowork and Claude Code; a Lighthouse audit installs for the conversation | Code: speed and accessibility check of a web page |
| `rea` | Reverse engineering of apps, sites and binaries you may analyse, each finding with its evidence, through a pinned local MCP server. | Shows how an existing app or site builds an effect, so Studio can plan a lawful reference. | session-install | Claude Code (desktop, cloud, phone) and Cowork install the tools for the conversation (Node 22.19+ for its MCP server, Chromium for web pages); native binaries also need Ghidra, IDA or Hopper, which are desktop apps; Codex through its own `.codex-plugin` package; chat: skill only | Code: shows how an app or site builds an effect |

### Marketing & growth

| Plugin | What it is for | How it helps Studio | Runs | Works in | Menu |
| ------ | -------------- | ------------------- | ---- | -------- | ---- |
| `marketing-skills` | 52 marketing skills: CRO, copywriting, SEO, email, analytics and launch. | Adds the marketing side of a Studio campaign: positioning, landing-page copy, ads, email and launch. | ready | Chat, Cowork and Claude Code | Marketing: 52 skills for copy, SEO, ads, email and launch |

## Details

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
- Watch out: Node 18+, Playwright Chromium and ffmpeg install for the conversation on first use; a
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

### hallmark

- Use: describe the page or redesign, or `/hallmark:hallmark`.
- Watch out: generated images go to Together AI only with `TOGETHER_API_KEY`; do not run `install-hook.mjs` unless you want a lint hook.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/hallmark.md

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

### taste-skill

- Use: Ask for a landing page, a product page or an app screen with a strong art direction.
- Watch out: Found pictures keep their own licences; check each before client use.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/taste-skill.md

### hairline

- Use: Ask for an isometric line figure or run `/hairline-create` with an idea.
- Watch out: Interactive pages, not seekable video; for video use Studio's Hairline kit.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/hairline.md

### huashu-art-motion

- Use: Ask for an animation in an art style or an explainer grammar (Kurzgesagt-like, whiteboard).
- Watch out: Skill text is in Chinese; do not reuse its showcase characters or likenesses.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/huashu-art-motion.md

### anatomy

- Use: Ask for an isometric technical figure or an interactive explainer of a system.
- Watch out: Publishing to its public gallery happens only on request; never by default.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/anatomy.md

### rea

- Use: Ask how a feature of an app, a bundle or a binary works; the skill calls the `rea` MCP tools.
- Watch out: Lawful targets only; native binaries need Ghidra, IDA or Hopper.
- Review: https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/reviews/rea.md

