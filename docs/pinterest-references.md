# pinterest-references: install notes

- Upstream: https://github.com/terryso/mcp-pinterest
- Pinned commit: 7a6667d9625d8b5d797f2aaa74fd9e39f284445f (npm `pinterest-mcp-server@1.2.0`)
- Wrapper: [plugins/pinterest-references](../plugins/pinterest-references/) (our own skill; starts the pinned npm package as a local MCP server)
- Review: [reviews/pinterest-references.md](../reviews/pinterest-references.md)
- License: MIT. Version: 1.2.0. Category: Creative.

**References only, not assets.** Pinterest images belong to their authors. Use them for moodboards and
style, typography and composition research; never place them in finished work. For free media you may use,
take Open Assets.

## Install

See [install.md](install.md). Plugin id: `pinterest-references@framecore-works-toolbox`.

```bash
claude plugin install pinterest-references@framecore-works-toolbox
```

Advanced alternative without the plugin (a user-level MCP server with your own download folder).
Use one route, not both:

```bash
claude mcp add pinterest -s user -e MCP_PINTEREST_DOWNLOAD_DIR="$HOME/Pictures/pinterest-references" -- npx -y pinterest-mcp-server@1.2.0
```

## Requirements

- Google Chrome in its standard place: macOS `/Applications/Google Chrome.app`, Linux `/usr/bin/google-chrome`,
  Windows `C:\Program Files\Google\Chrome\Application\chrome.exe`. Chromium is not detected by 1.2.0.
- Node.js with npx; the first start downloads `pinterest-mcp-server@1.2.0` and its dependencies from npm.
- No Pinterest account and no API key.
- Optional environment: `MCP_PINTEREST_DOWNLOAD_DIR` (folder for the download tool),
  `MCP_PINTEREST_FILENAME_TEMPLATE` (file names), `MCP_PINTEREST_PROXY_SERVER` (an HTTP or SOCKS proxy you run).

## Setup after install

None. All three tools (`pinterest_search`, `pinterest_get_image_info`, `pinterest_search_and_download`) work
after install; the download tool saves into `~/Pictures/pinterest-references/<keyword>/` (the plugin sets
`MCP_PINTEREST_DOWNLOAD_DIR`). The plugin's skill copies the pins you keep into the project's `references/pinterest/` folder with a
`.reference.json` next to each file (pin link, image link, title, author or `Unknown`, query, date and the
"reference only" note).

## What works where

Claude Code on a computer with Chrome: search and saving. Claude Code cloud: the container has
`/usr/bin/google-chrome`; the owner reported a search returning pins without login (PASS_REPORTED 2026-11-06).
Cowork: Unknown (Chrome in the VM not verified). claude.ai chat: the skill loads, no MCP search.
Codex: through the wrapper's `.codex-plugin` package, NOT_RUN. ChatGPT Work: no local MCP server (Claude only).

## Use

Ask for a moodboard, style research or a reference pack, for example "find Swiss poster typography
references for a reel".

## Watch out

- The server opens pinterest.com in Chrome without a window and sets an ordinary desktop Chrome user agent;
  Pinterest's terms limit automated access. Keep searches small and occasional.
- 1.2.0 prints start-up lines to standard output; Claude Code tolerates them, other MCP clients may log errors.
- Never switch to `@latest` or another version without a new review.

## Full removal

`claude plugin uninstall pinterest-references@framecore-works-toolbox` (or Customize > Plugins), or
`claude mcp remove pinterest -s user` for the advanced route. Delete the project's `references/pinterest/`
folder if you no longer need the references; npx keeps the package in the npm cache until it is cleaned.
