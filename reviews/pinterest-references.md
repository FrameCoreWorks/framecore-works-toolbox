# Review: pinterest-references

## Entry

- Name: pinterest-references
- Status: active
- Upstream: https://github.com/terryso/mcp-pinterest
- Author: terryso
- License: MIT
- Commit: 7a6667d9625d8b5d797f2aaa74fd9e39f284445f
- Upstream version: 1.2.0
- Kind: adapted
- Eligibility: adapted: our own wrapper plugin `plugins/pinterest-references` with its own skill and the stdio MCP server from npm `pinterest-mcp-server@1.2.0` (`npx -y pinterest-mcp-server@1.2.0`); the upstream ships no Claude manifest or skills
- Source: local wrapper ./plugins/pinterest-references (UPSTREAM.md names the reviewed commit)
- Reviewed on: 2026-11-06
- Reviewer: Claude (cloud project thread "Dodaj Pinterest jako źródło referencji")
- Owner approval: "yes" from Kamil on 2026-11-06, the request "dodaj konektor Pinterest terryso/mcp-pinterest do FrameCore Works Toolbox", then the decision card "Dodać jako wyjątek właściciela" and "dodaj jako pelny dostep do pinterest przez ten mcp" (all three tools, download included)

## What it is

A stdio MCP server that searches public Pinterest pins by keyword without an account or API key. It drives
Google Chrome without a window through puppeteer-core on `pinterest.com/search/pins/`. Tools:
`pinterest_search` (title, image URL, pin link), `pinterest_get_image_info`, `pinterest_search_and_download`.
FrameCore uses it only as a source of references (moodboards, style, typography, composition), never of assets.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, `reference-pack-curator` and `research-evidence` (moodboards and style research for reels and campaigns) | Real-world style, typography and composition examples found by keyword, saved with pin link and author, where Studio previously had only the user's own references and Open Assets' public-domain/CC collections | Owner test 2026-11-06 from a cloud session: a search without login returned pins (PASS_REPORTED). Our own live MCP start in this review: NOT_RUN (the session's permission classifier blocked running external code). |
| FrameCore Open Assets, reference sourcing | A clearly separated reference-only route next to the licensed providers | Documentation route only; Open Assets does not call the server |

## Files reviewed

Upstream cloned as data into a temporary folder; `npm pack pinterest-mcp-server@1.2.0` downloaded the published
tarball without installing or running it. The tarball's `gitHead` is 7a6667d (2025-05-05, "chore(release): 1.2.0"),
present in the repository. Repository `main` is at 1.2.1 (f9a0b71, 2026-11-02, "stdio hygiene"), which is not
published on npm; npm versions are 1.0.0, 1.1.0 and 1.2.0. Read: `package.json`, `bin/cli.js`,
`dist/pinterest-mcp-server.js`, `dist/pinterest-scraper.js`, `dist/src/pinterest-download.js`,
`dist/src/filename-template.js`, LICENSE (MIT, "Pinterest MCP Server Contributors").

Facts from the code:
- No `child_process`, `eval` or `new Function`; no install scripts (`preinstall`/`postinstall`).
- Hosts: `https://www.pinterest.com` (search page) and the image URLs it returns (`i.pinimg.com`); axios downloads
  whatever image URL a tool call passes. Optional proxy from `MCP_PINTEREST_PROXY_SERVER`.
- No telemetry or analytics calls found.
- Chrome paths are fixed: macOS `/Applications/Google Chrome.app/...`, Linux `/usr/bin/google-chrome`, Windows
  `Program Files` (two). Chromium is not detected and there is no path override in 1.2.0.
- The scraper and downloader set a desktop Chrome user agent (`Chrome/120` and `Chrome/121` on macOS).
- `bin/cli.js` and the server print start-up lines with `console.log` to standard output, the stdio channel.
- Dependencies use caret ranges (`@modelcontextprotocol/sdk ^0.6.0`, `axios ^1.8.1`, `cheerio ^1.0.0`,
  `puppeteer-core ^24.3.0`), as for every npx-started entry.
- `headless: false` in a tool call opens a visible Chrome window; the default is headless.

## What it installs and writes

The wrapper ships only our own files: three manifests, `.mcp.json`, `mcp.json`, `UPSTREAM.md` and
`skills/pinterest-references/SKILL.md`. npx caches the package in the npm cache on first start. The server
writes and deletes a test file in its download folder at start, and saves downloads into
`MCP_PINTEREST_DOWNLOAD_DIR` (the wrapper sets `${HOME}/Pictures/pinterest-references`), one subfolder per keyword.
The skill copies kept pins into the project's `references/pinterest/` with a `.reference.json` sidecar.

## Hooks

None.

## Network traffic

The npm registry on first start; `www.pinterest.com` for each search; `i.pinimg.com` (or the image URL given)
for downloads and image info.

## Changes to prompts or tool results

Our skill `pinterest-references:pinterest-references` loads by description on moodboard and reference tasks.
Tool results contain pin titles from Pinterest, which are untrusted text.

## Data sent outside

The search keywords go to pinterest.com as a normal search. Nothing else found.

## Requirements

Google Chrome in its standard place; Node.js with npx. No account, no API key.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): see docs/verification.md for 1.10.0.
- MCP server start and a live search in this review: NOT_RUN (blocked by the session's permission classifier).
- Owner, cloud: search without login returned pins, PASS_REPORTED 2026-11-06.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

## Risks

1. Reject gate "impersonates another client": the server replaces the headless Chrome user agent with an ordinary
   desktop Chrome one. Admitted as an owner exception (decision card 2026-11-06), limited to public search on
   pinterest.com with no account, keys, cookies or proxy rotation; not a precedent for other entries.
2. Pinterest's terms restrict automated collection; keep searches small and occasional.
3. Images belong to their authors: reference only, enforced by our skill and the sidecar note.
4. Start-up output on stdout can confuse strict MCP clients (1.2.1 fixes it but is not on npm).
5. The self-contained rule allows "a browser"; Google Chrome must be installed (Chromium is not found).

## Verdict

accept with conditions: owner exception for the user agent; references only; pinned to 1.2.0.

## History

- 2026-11-06: added at 7a6667d (npm 1.2.0) through our wrapper, on the owner's request, with all three tools.
