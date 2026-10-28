# FrameCore Works Toolbox

FrameCore Works tool catalog for **Claude, ChatGPT Work and Codex**, maintained
in a private GitHub repository. The repository remains a Claude marketplace;
its `toolbox` catalog is also an independently installable portable plugin.

**Catalog plugin version: 1.0.3.** One source directory, `plugins/toolbox/`,
contains the portable manifest, Codex and Claude compatibility manifests, and
shared host-aware instructions. [Choose an installation route](INSTALL.md).

Every third-party entry is pinned to a full upstream commit and has a review in
`reviews/` and notes in `docs/`. This repo holds no upstream code. Adapted entries
can have a thin wrapper in `plugins/<name>/` pointing to the reviewed upstream.
Installing the catalog does not install these entries; their existing host
compatibility notes describe Claude and must be verified separately elsewhere.

## Plugins

The current marketplace contains **17 tools plus the toolbox index: 18 entries**.

Type `toolbox` in the host where the catalog is installed to see this list, grouped by category. The index
itself: `toolbox` (first-party, this repo, skill everywhere,
[docs](docs/toolbox.md); no hooks, scripts or network).

### Creative

| Name | Upstream | Commit (version) | What it is for | Chat / Cowork / Claude Code | Notes | Review |
| ---- | -------- | ---------------- | -------------- | --------------------------- | ----- | ------ |
| earshot-audio | [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) | `591fa3e` (engine 0.4.0; wrapper 1.2.0) | Local audio measurements, sound kits and soundtracks from supplied recordings. Independent portable wrapper. | portable package; fresh host activation NOT_RUN | [docs](docs/earshot-audio.md) | [review](reviews/earshot-audio.md) |
| ffmpeg-skill | [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | `1ae1bdf` (2.17.3) | Local recording sync, multicam, HDR-to-SDR and media preparation with FFmpeg. | native marketplace install and client activation NOT_RUN | [docs](docs/ffmpeg-skill.md) | [review](reviews/ffmpeg-skill.md) |
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

### Dev tools

| Name | Upstream | Commit (version) | What it is for | Chat / Cowork / Claude Code | Notes | Review |
| ---- | -------- | ---------------- | -------------- | --------------------------- | ----- | ------ |
| antislop | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | `5ca57fe` (3.2.23) | rules against generic AI output in UI, copy and code; contrast checker | skills / skills + MCP / skills + MCP | [docs](docs/antislop.md) | [review](reviews/antislop.md) |
| web-quality-skills | [addyosmani/web-quality-skills](https://github.com/addyosmani/web-quality-skills) | `afa8da9` (2.0.0) | Web quality checks from Lighthouse and Core Web Vitals: speed, accessibility, best practices. | skills / skills / skills | [docs](docs/web-quality-skills.md) | [review](reviews/web-quality-skills.md) |

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
  `FrameCoreWorks/framecore-works-toolbox` (connect GitHub and give the Claude
  GitHub App access to this private repo), then Add each plugin.
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
