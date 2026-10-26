# FrameCore Works Toolbox

Private Claude plugin marketplace with reviewed third-party plugins used at
FrameCore Works. Add it once in Claude (claude.ai, desktop, Cowork or Claude
Code), then add the plugins you want; Claude picks their skills by task or you
call them with `/`.

Every entry is pinned to a full upstream commit and has a security review in
`reviews/` and notes in `docs/`. This repo holds no upstream code. Repos that
are not plugins themselves can be added as adapted entries: a thin wrapper
plugin written here in `plugins/<name>/` that points to the reviewed upstream
commit.

## Plugins

Type `toolbox` in Claude to see this list, grouped by category. The index
itself: `toolbox` (first-party, this repo, skill everywhere,
[docs](docs/toolbox.md); no hooks, scripts or network).

### Creative

| Name | Upstream | Commit (version) | What it is for | Chat / Cowork / Claude Code | Notes | Review |
| ---- | -------- | ---------------- | -------------- | --------------------------- | ----- | ------ |
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
| ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | `09c434a` (5.3.2) | minimal code changes, code review, repo audit; plugin with always-on hooks | skills / skills + hooks / skills + hooks + mod | [docs](docs/ponytail.md) | [review](reviews/ponytail.md) |
| antislop | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | `5ca57fe` (3.2.23) | rules against generic AI output in UI, copy and code; contrast checker | skills / skills + MCP / skills + MCP | [docs](docs/antislop.md) | [review](reviews/antislop.md) |
| web-quality-skills | [addyosmani/web-quality-skills](https://github.com/addyosmani/web-quality-skills) | `afa8da9` (2.0.0) | Web quality checks from Lighthouse and Core Web Vitals: speed, accessibility, best practices. | skills / skills / skills | [docs](docs/web-quality-skills.md) | [review](reviews/web-quality-skills.md) |
| hud | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | `cf95a32` (0.13.1) | Status line for Claude Code: context use, active tools, agents, todos and cost. | - / - / status line | [docs](docs/hud.md) | [review](reviews/hud.md) |
| planning-with-files | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | `dcdfb27` (3.25.2) | File-based plans that survive /clear and compaction, re-injected every turn. | skills / skills + hooks / skills + hooks | [docs](docs/planning-with-files.md) | [review](reviews/planning-with-files.md) |
| compound-engineering | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | `9f5b16f` (3.32.2) | Every's compound engineering workflow: plan, build, review and turn lessons into reusable rules. | skills / skills + agents / skills + agents | [docs](docs/compound-engineering.md) | [review](reviews/compound-engineering.md) |
| skillspector | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | `d7338f5` (2.12.0) | Security review of a skill or plugin before you install it (NVIDIA SkillSpector scan plus source review). | skill / skill + CLI / skill + CLI | [docs](docs/skillspector.md) | [review](reviews/skillspector.md) |
| archify | [tt-a1i/archify](https://github.com/tt-a1i/archify) | `81c6be8` (3.2) | Interactive architecture, flow, sequence and ERD diagrams from an idea or a codebase, as standalone HTML. | skill / skill / skill | [docs](docs/archify.md) | [review](reviews/archify.md) |
| wondelai-code-craftsmanship | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` (1.8.0) | Code quality and software design skills. | skills / skills / skills | [docs](docs/wondelai-code-craftsmanship.md) | [review](reviews/wondelai-code-craftsmanship.md) |
| wondelai-systems-architecture | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` (1.8.0) | Systems architecture and distributed systems skills. | skills / skills / skills | [docs](docs/wondelai-systems-architecture.md) | [review](reviews/wondelai-systems-architecture.md) |

### Marketing & growth

| Name | Upstream | Commit (version) | What it is for | Chat / Cowork / Claude Code | Notes | Review |
| ---- | -------- | ---------------- | -------------- | --------------------------- | ----- | ------ |
| marketing-skills | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `e85f3cb` (2.13.0) | 52 marketing skills: CRO, copywriting, SEO, email, analytics and launch. | skills / skills / skills | [docs](docs/marketing-skills.md) | [review](reviews/marketing-skills.md) |
| seo | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | `6be93f4` (2.5.0) | Complete SEO toolkit: technical SEO, schema, GEO/AEO, local and e-commerce audits and reports. | skills / skills + hook / skills + hook | [docs](docs/seo.md) | [review](reviews/seo.md) |
| notfair | [nowork-studio/notfair-plugin](https://github.com/nowork-studio/notfair-plugin) | `ed835f2` (0.27.17) | SEO, GEO and Google/Meta Ads work through the NotFair service (remote MCP). | skills + MCP / skills + MCP / skills + MCP | [docs](docs/notfair.md) | [review](reviews/notfair.md) |
| linkedin-agent | [Jakeschincariol/linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill) | `add2c23` (1.0.0) | LinkedIn content: posts, comments, replies, profile score and a weekly plan. | skills / skills / skills | [docs](docs/linkedin-agent.md) | [review](reviews/linkedin-agent.md) |
| wondelai-product-strategy | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` (1.8.0) | Product strategy and innovation frameworks. | skills / skills / skills | [docs](docs/wondelai-product-strategy.md) | [review](reviews/wondelai-product-strategy.md) |
| wondelai-marketing-cro | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` (1.8.0) | Marketing and conversion optimization skills. | skills / skills / skills | [docs](docs/wondelai-marketing-cro.md) | [review](reviews/wondelai-marketing-cro.md) |
| wondelai-sales-influence | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` (1.8.0) | Sales, persuasion, and messaging skills. | skills / skills / skills | [docs](docs/wondelai-sales-influence.md) | [review](reviews/wondelai-sales-influence.md) |
| wondelai-product-innovation | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` (1.8.0) | Product innovation and validation frameworks. | skills / skills / skills | [docs](docs/wondelai-product-innovation.md) | [review](reviews/wondelai-product-innovation.md) |
| wondelai-strategy-growth | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` (1.8.0) | Business strategy and growth frameworks. | skills / skills / skills | [docs](docs/wondelai-strategy-growth.md) | [review](reviews/wondelai-strategy-growth.md) |
| wondelai-team-motivation | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` (1.8.0) | Team motivation and management skills. | skills / skills / skills | [docs](docs/wondelai-team-motivation.md) | [review](reviews/wondelai-team-motivation.md) |
| wondelai-metaskills | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` (1.8.0) | Fourteen guided journeys that orchestrate the whole skill library step by step: create, improve, and grow a business, website, or app, plus improve code quality, remove technical debt, design code architecture, optimize a conversion flow, and optimize an existing codebase for speed and structure. Each metaskill invokes the right skills phase by phase, asks the user questions at every decision point, and records results as living documents in the project docs/ folder. | skills / skills / skills | [docs](docs/wondelai-metaskills.md) | [review](reviews/wondelai-metaskills.md) |

## Install

Full steps: [docs/install.md](docs/install.md).

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
Before every commit:

```bash
python3 -m unittest discover -s tests
python3 scripts/check_marketplace.py
claude plugin validate .
```
