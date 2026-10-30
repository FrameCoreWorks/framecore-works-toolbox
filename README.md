# FrameCore Works Toolbox

FrameCore Works tool catalog for **Claude, ChatGPT Work and Codex**, maintained
in a public GitHub repository. The repository remains a Claude marketplace;
its `toolbox` catalog is also an independently installable portable plugin.

**Catalog plugin version: 1.2.5.** One source directory, `plugins/toolbox/`,
contains the portable manifest, Codex and Claude compatibility manifests, and
shared host-aware instructions. [Choose an installation route](INSTALL.md).

Every third-party entry is pinned to a full upstream commit and has a review in
`reviews/` and notes in `docs/`. This repo holds no upstream code. Adapted entries
can have a thin wrapper in `plugins/<name>/` pointing to the reviewed upstream.
Installing the catalog does not install these entries; their existing host
compatibility notes describe Claude and must be verified separately elsewhere.

## Plugins

The current marketplace contains **20 tools plus the toolbox index: 21 entries**. The index also lists the built-in Earshot capability and four app notes (a desktop app, a skill archive and two Claude Code plugins that claude.ai and Cowork cannot host, listed in `plugins/toolbox/apps.json` with manual install steps in `docs/`). Since 1.2.0 Toolbox is the single place for the tools Creative Studio recommends.

Type `toolbox` in the host where the catalog is installed to see this list, grouped by category. The index
itself: `toolbox` (first-party, this repo, skill everywhere,
[docs](docs/toolbox.md); no hooks or MCP servers; carries the built-in Earshot launcher, which writes or downloads nothing without the user's --yes).

### Creative

| Name | Upstream | Commit (version) | What it is for | Chat / Cowork / Claude Code | Notes | Review |
| ---- | -------- | ---------------- | -------------- | --------------------------- | ----- | ------ |
| earshot-audio | [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) | `591fa3e` (engine 0.4.0; built into Toolbox 1.1.0) | Local audio measurements, sound kits and soundtracks from supplied recordings. Built into the `toolbox` plugin; no separate install. | built in; fresh host activation NOT_RUN | [docs](docs/earshot-audio.md) | [review](reviews/earshot-audio.md) |
| animate | [cth9191/animate](https://github.com/cth9191/animate) | `7e5eb56` (0.4.0) | animated explainers and reels in code, rendered to MP4 | skill (render Unknown) / skill + render / skill + render | [docs](docs/animate.md) | [review](reviews/animate.md) |
| motion-designer | [kaventro/motion-designer](https://github.com/kaventro/motion-designer) | `7d0b8bb` (1.2.0) | app launch films and short code videos cut to music, MP4/loop/poster | skill (render Unknown) / skill + render / skill + render | [docs](docs/motion-designer.md) | [review](reviews/motion-designer.md) |
| logo-design | [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) | `7340903` (1.4.5) | logo design from brief to SVG and brand guidelines | skill / skill + scripts / skill + scripts | [docs](docs/logo-design.md) | [review](reviews/logo-design.md) |
| meta-ads-designer | [aievolutionpl/meta-ads-designer](https://github.com/aievolutionpl/meta-ads-designer) | `656ce90` (6.5.0) | Meta/social ads, posters and flyers made with an image model | skill / skill + scripts / skill + scripts | [docs](docs/meta-ads-designer.md) | [review](reviews/meta-ads-designer.md) |
| hallmark | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | `7ec8682` (2.0.0) | web pages and app UI that do not look AI-generated | skill / skill + scripts / skill + scripts | [docs](docs/hallmark.md) | [review](reviews/hallmark.md) |
| open-design | [nexu-io/open-design](https://github.com/nexu-io/open-design) | `26d6029` (1.0.0) | bridge to the local Open Design app (design skills, systems, previews) | - / MCP with the app / MCP with the app | [docs](docs/open-design.md) | [review](reviews/open-design.md) |
| video-shotcraft | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | `43bd349` (1.0.0) | Cinematic product and promo videos in Remotion from 152 shot recipes and a production template. | skill / skill + render / skill + render | [docs](docs/video-shotcraft.md) | [review](reviews/video-shotcraft.md) |
| brag | [latent-spaces/brag](https://github.com/latent-spaces/brag) | `669ab92` (0.5.0) | Turns the project you just built into a short launch video with one command. | skill / skill + render / skill + render | [docs](docs/brag.md) | [review](reviews/brag.md) |
| nateherk-design | [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) | `75d81f7` (0.3.1) | Builds premium scroll-driven websites (scrollytelling, motion, typography), optional kie.ai images. | skill / skill / skill | [docs](docs/nateherk-design.md) | [review](reviews/nateherk-design.md) |
| sepia | [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | `fb06be7` (0.12.4) | Removes AI patterns from fiction and professional prose without changing what it says. | skills / skills / skills | [docs](docs/sepia.md) | [review](reviews/sepia.md) |
| blender-agent-skills | [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills) | `71d031d` (1.1.0) | Blender 5.2 workflows for 3D: modeling, UVs, PBR, rigging, animation and export. | skills / skills + Blender / skills + Blender | [docs](docs/blender-agent-skills.md) | [review](reviews/blender-agent-skills.md) |
| wondelai-ux-design | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` (1.8.0) | UX and UI design skills. | skills / skills / skills | [docs](docs/wondelai-ux-design.md) | [review](reviews/wondelai-ux-design.md) |
| taste-skill | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `12af471` (2.1.5) | Art direction for landing pages, product pages, dashboards and app screens, with openly licensed pictures and a real-browser check. | skill / skill + scripts / skill + scripts | [docs](docs/taste-skill.md) | [review](reviews/taste-skill.md) |
| hairline | [lucasmarkes/hairline](https://github.com/lucasmarkes/hairline) | `37d2e78` (0.5.1) | Isometric line figures that answer the pointer on a web page, drawn as one HTML file or added to a project as a library. | skills / skills + browser / skills + browser | [docs](docs/hairline.md) | [review](reviews/hairline.md) |
| huashu-art-motion | [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | `8a0d7d7` (1.2.0) | Art-style animation in 36 styles from cave painting to Ghibli and 9 explainer grammars, with reference breakdown and shot-list checks. | skill / skill + render / skill + render | [docs](docs/huashu-art-motion.md) | [review](reviews/huashu-art-motion.md) |
| anatomy | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | `e948829` (unreleased) | Detailed interactive isometric SVG figures that explain a technical idea as a physical object, with optional WebGL shaders. | skill / skill + scripts / skill + scripts | [docs](docs/anatomy.md) | [review](reviews/anatomy.md) |

### App notes (not plugins)

Desktop apps, skill archives and plugins with a top-level `bin/` (which claude.ai and Cowork refuse) that Toolbox lists for discovery. You install them yourself with the steps in their docs; the marketplace never installs them.

| Name | Upstream | Pin (version) | What it is for | Where it runs | Notes | Review |
| ---- | -------- | ------------- | -------------- | ------------- | ----- | ------ |
| ffmpeg-skill | [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | commit `1ae1bdf1ca0adbb1606fbca493948b1bbb2f83ff` (2.17.3) | Local recording sync, multicam, HDR-to-SDR and media preparation with FFmpeg. | Claude Code plugin installed by hand (top-level `bin/`: not claude.ai or Cowork) | [docs](docs/ffmpeg-skill.md) | [review](reviews/ffmpeg-skill.md) |
| pixel-plugin | [willibrandon/pixel-plugin](https://github.com/willibrandon/pixel-plugin) | commit `dee350645b705916655c013f208bf5580ecb9317` (0.5.0) | Pixel art drawn in Aseprite from a conversation: sprites, palettes, dithering, frame animation and GIF or spritesheet export. | Claude Code plugin installed by hand (top-level `bin/`: not claude.ai or Cowork); Aseprite | [docs](docs/pixel-plugin.md) | [review](reviews/pixel-plugin.md) |
| voicebox | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | commit `2bcb98d1a8b6fe05e15fbc1559e3085669e4035d` (0.5.0) | Local desktop voice studio: cloning, designed voices, multi-voice stories, with a localhost REST API and MCP server. | desktop app; agents over localhost MCP or REST | [docs](docs/voicebox.md) | [review](reviews/voicebox.md) |
| iso-glow | [isoglow.dev](https://isoglow.dev/) | `sha256:6c88dba1424bada2ee651a1b273095f9a13b82dd9362f9bc873600b5bff6b0a1` (archive) | Isometric hairline figures where the switched-on part glows, as single HTML pages. | skill archive installed by hand | [docs](docs/iso-glow.md) | [review](reviews/iso-glow.md) |

### Dev tools

| Name | Upstream | Commit (version) | What it is for | Chat / Cowork / Claude Code | Notes | Review |
| ---- | -------- | ---------------- | -------------- | --------------------------- | ----- | ------ |
| antislop | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | `5ca57fe` (3.2.23) | rules against generic AI output in UI, copy and code; contrast checker | skills / skills + MCP / skills + MCP | [docs](docs/antislop.md) | [review](reviews/antislop.md) |
| web-quality-skills | [addyosmani/web-quality-skills](https://github.com/addyosmani/web-quality-skills) | `afa8da9` (2.0.0) | Web quality checks from Lighthouse and Core Web Vitals: speed, accessibility, best practices. | skills / skills / skills | [docs](docs/web-quality-skills.md) | [review](reviews/web-quality-skills.md) |
| rea | [morluto/rea](https://github.com/morluto/rea) | `5e30969` (6.5.0) | Reverse engineering of apps, sites and binaries you may analyse, each finding with its evidence, through a pinned local MCP server. | skill / skill + MCP / skill + MCP | [docs](docs/rea.md) | [review](reviews/rea.md) |

### Marketing & growth

| Name | Upstream | Commit (version) | What it is for | Chat / Cowork / Claude Code | Notes | Review |
| ---- | -------- | ---------------- | -------------- | --------------------------- | ----- | ------ |
| marketing-skills | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `e85f3cb` (2.13.0) | 52 marketing skills: CRO, copywriting, SEO, email, analytics and launch. | skills / skills / skills | [docs](docs/marketing-skills.md) | [review](reviews/marketing-skills.md) |

## Install

| Host | Guide | Route |
| --- | --- | --- |
| Claude apps / Claude Code | [Claude installation](docs/install.md) | Marketplace and selected plugins |
| ChatGPT Work | [ChatGPT installation](CHATGPT_INSTALL.md) | Portable single-plugin ZIP through Plugin Creator |
| Codex | [Codex installation](CODEX_INSTALL.md) | Local plugin or native entry with the complete bundle |

Host activation and runtime compatibility are recorded separately in
[verification](docs/verification.md). The shared layout and independence rules
are in [architecture](docs/architecture.md).

Existing Claude routes:

- Claude apps: Customize > Plugins > Add > Add marketplace >
  `FrameCoreWorks/framecore-works-toolbox`, then Add each plugin.
- Claude Code CLI:

```bash
claude plugin marketplace add FrameCoreWorks/framecore-works-toolbox
claude plugin install <name>@framecore-works-toolbox
```

## Maintaining

Rules for adding, updating and removing entries are in [CLAUDE.md](CLAUDE.md).
Only tools, assets and repositories with a fully demonstrated, concrete improvement
to FrameCore repositories qualify for new admission or a future entry update.
Record the affected repository/task, benefit and verification in the review;
general usefulness or an unverified promise is insufficient.
Before every commit:

```bash
python3 -m unittest discover -s tests
python3 scripts/check_marketplace.py
python3 scripts/package_plugins.py --check
python3 scripts/package_plugins.py --output-dir ../toolbox-dist
claude plugin validate .
```
