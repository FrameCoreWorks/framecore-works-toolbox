# FrameCore Works Toolbox

FrameCore Works tool catalog for **Claude, ChatGPT Work and Codex**, maintained
in a public GitHub repository. The repository remains a Claude marketplace;
its `toolbox` catalog is also an independently installable portable plugin.

**Catalog plugin version: 1.18.2.** One source directory, `plugins/toolbox/`,
contains the portable manifest, Codex and Claude compatibility manifests, and
shared host-aware instructions. [Choose an installation route](INSTALL.md).

**Quick start.** After installing, type `toolbox` in the chat: you get the
numbered catalog, and you pick only the tools you want. Earshot (audio
loudness, sound effects, sync) is built in, so it needs no separate install;
ask for it by name, for example "check the loudness of this file with Earshot".

Every third-party entry is pinned to a full upstream commit and has a review in
`reviews/` and notes in `docs/`. This repo holds no upstream code (the MIT reel style packs built in from 1.14.0 moved to FrameMotion with Toolbox 1.17.0). Adapted entries
can have a thin wrapper in `plugins/<name>/` pointing to the reviewed upstream.
Installing the catalog does not install these entries; their existing host
compatibility notes describe Claude and must be verified separately elsewhere.

## Plugins

The current marketplace contains **12 tools plus the toolbox index: 13 entries**. The index also lists the built-in Earshot capability. Since 1.17.0 every motion graphics entry and the reel style packs live in [FrameMotion](https://github.com/FrameCoreWorks/framemotion), which bundles them in full; Toolbox lists no motion tools. Since 1.4.0 Toolbox lists only tools that install without accounts, API keys or separate desktop apps, so there are no app notes (`plugins/toolbox/apps.json` is empty). Since 1.2.0 Toolbox is the single place for the tools Creative Studio recommends.

**What an entry can reach.** Most entries are instructions plus local scripts. Read the review before installing these: `antislop`, `rea` and `pinterest-references` start a pinned local MCP server (`pinterest-references` opens Google Chrome without a window to search pinterest.com); `taste-skill` checks its pages in a local browser (`taste-skill` also runs its finish gate as a Stop hook while the skill is loaded); `nateherk-design` can call kie.ai for images, only when you give it your own key; `rife-interpolate` downloads its pinned program (about 830 MB, once) only after your yes. The "Chat / Cowork / Claude Code" column shows the same per host. Installing the catalog installs none of them; each one is installed separately and only when you choose it.

Type `toolbox` in the host where the catalog is installed to see this list, grouped by category. The index
itself: `toolbox` (first-party, this repo, skill everywhere,
[docs](docs/toolbox.md); no hooks or MCP servers; carries the built-in Earshot launcher, which writes or downloads nothing without the user's --yes).

### Creative

| Name | Upstream | Commit (version) | What it is for | Chat / Cowork / Claude Code | Notes | Review |
| ---- | -------- | ---------------- | -------------- | --------------------------- | ----- | ------ |
| earshot-audio | [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) | `591fa3e` (engine 0.4.0; built into Toolbox 1.1.0) | Local audio measurements, sound kits and soundtracks from supplied recordings. Built into the `toolbox` plugin; no separate install. | built in; fresh host activation NOT_RUN | [docs](docs/earshot-audio.md) | [review](reviews/earshot-audio.md) |
| logo-design | [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) | `7340903` (1.4.5) | logo design from brief to SVG and brand guidelines | skill / skill + scripts / skill + scripts | [docs](docs/logo-design.md) | [review](reviews/logo-design.md) |
| hallmark | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | `7ec8682` (2.0.0) | web pages and app UI that do not look AI-generated | skill / skill + scripts / skill + scripts | [docs](docs/hallmark.md) | [review](reviews/hallmark.md) |
| nateherk-design | [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) | `75d81f7` (0.3.1) | Builds premium scroll-driven websites (scrollytelling, motion, typography), optional kie.ai images. | skill / skill / skill | [docs](docs/nateherk-design.md) | [review](reviews/nateherk-design.md) |
| sepia | [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | `fb06be7` (0.12.4) | Removes AI patterns from fiction and professional prose without changing what it says. | skills / skills / skills | [docs](docs/sepia.md) | [review](reviews/sepia.md) |
| wondelai-ux-design | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` (1.8.0) | UX and UI design skills. | skills / skills / skills | [docs](docs/wondelai-ux-design.md) | [review](reviews/wondelai-ux-design.md) |
| taste-skill | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `12af471` (2.1.5) | Art direction for landing pages, product pages, dashboards and app screens, with openly licensed pictures and a real-browser check. | skill / skill + scripts / skill + scripts | [docs](docs/taste-skill.md) | [review](reviews/taste-skill.md) |
| pinterest-references | [terryso/mcp-pinterest](https://github.com/terryso/mcp-pinterest) | `7a6667d` (1.2.0; our wrapper `plugins/pinterest-references`) | Moodboards and style, typography and composition references from public Pinterest pins, saved with pin link and author. **References only, not assets.** Needs Google Chrome and Node.js (npx). | skill (no search) / Unknown / skill + MCP | [docs](docs/pinterest-references.md) | [review](reviews/pinterest-references.md) |
| rife-interpolate | [TNTwise/rife-ncnn-vulkan](https://github.com/TNTwise/rife-ncnn-vulkan) | `5eea93c` (20250112; our wrapper `plugins/rife-interpolate` 1.1.1) | Smoother video (24/30 to 60 fps), slow motion and filled-in low-frame-rate renders with RIFE on your graphics card. Downloads the pinned program once after your yes. | skill (no run) / Unknown / skill + script | [docs](docs/rife-interpolate.md) | [review](reviews/rife-interpolate.md) |

### App notes (not plugins)

None. Toolbox 1.4.0 removed the four app notes (owner decision 2026-10-31: no separate desktop apps or manual installs); their reviews stay in `reviews/` with Status: removed.

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

ChatGPT Work needs OpenAI's **Plugin Creator** installed first (side menu > Plugins > search "Plugin Creator" > the one by OpenAI > Install); see [Before you start](CHATGPT_INSTALL.md#before-you-start-install-plugin-creator-one-time).

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

## Licence

FrameCore Works' own files in this repository (the catalog, reviews, docs, the index plugin, wrapper plugins and the Earshot launcher) are licensed under [Apache-2.0](LICENSE). Every catalog entry keeps its upstream licence, shown in its review and docs; the Earshot engine is MIT (Leon Lin) and is installed separately, never copied here.
