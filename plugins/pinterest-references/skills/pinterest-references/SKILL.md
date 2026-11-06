---
name: pinterest-references
description: "Search public Pinterest pins by keyword with the pinned pinterest-mcp-server 1.2.0 to build moodboards and style, typography, colour and composition references for reels, ads and campaigns. Use for a moodboard, style research or a reference pack. Saved images keep their pin link and author. References only: never a source of licensed assets for finished work; for usable free media use Open Assets."
---

# Pinterest references (pinned)

Pinterest images belong to their authors. Use them to look at, compare and
describe; never place them, trace them or ship them in finished work.

## Tools

The `pinterest` MCP server of this plugin (`npx -y pinterest-mcp-server@1.2.0`)
gives three tools; read each schema before calling it:

- `pinterest_search`: keyword search, returns title, image URL and pin link per pin.
- `pinterest_get_image_info`: details for one image URL.
- `pinterest_search_and_download`: search and save the images into
  `MCP_PINTEREST_DOWNLOAD_DIR`, one subfolder per keyword. This plugin sets it to
  `~/Pictures/pinterest-references`; a user-level install sets its own folder.

All three tools are available; pick the one the task needs.

Keep `headless` at its default `true`. Keep `limit` small (10 to 20 per query)
and run a few precise queries instead of one large one.

## Work

1. Turn the brief into 3 to 6 short queries in English (style, subject, era,
   typography, palette, composition), for example `swiss poster grid typography`.
2. Search, then show the pins as a short list: title, pin link, what is useful
   in it (colour, type, layout, motion idea). Pick with the user.
3. For each picked pin, open its pin link and read the author or the original
   source shown there. Write `Unknown` when the page does not show it; never
   guess.
4. Save picked pins: either call `pinterest_search_and_download` for a whole
   query, or download single picked images from their image URL. Copy the files
   the user keeps into the project's `references/pinterest/` folder (create it),
   one file per pin. Next to each file write `<file>.reference.json`:

```json
{
  "kind": "reference-only",
  "source": "pinterest",
  "pin_url": "https://www.pinterest.com/pin/...",
  "image_url": "https://i.pinimg.com/...",
  "title": "...",
  "author": "... or Unknown",
  "original_source": "URL the pin links to, or Unknown",
  "query": "...",
  "retrieved_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "rights": "Not cleared. Reference only; do not use in finished work.",
  "tool": "pinterest-mcp-server@1.2.0"
}
```

5. Report what was saved, the queries used and anything without an author.

## When the tools are missing or fail

- No `pinterest` tools in this session: say the connector is not installed and
  continue without it (the user's own references, Open Assets, or a written
  style description). Do not stop the task.
- The server needs Google Chrome in its standard place (macOS
  `/Applications/Google Chrome.app`, Linux `/usr/bin/google-chrome`, Windows
  `Program Files`) and Node.js with npx. If Chrome is missing, say so; do not
  install software yourself.
- No results, a block or a login wall: report it once and do not retry in a loop,
  rotate proxies or sign in for the user.
- Never run another version than 1.2.0 or `@latest`.

## Never

- Use a Pinterest image as an asset, texture, background or frame in delivered
  work, or hand it to an image or video generator as material to copy.
- Remove the pin link or author from a saved reference.
- Bulk-download whole boards or profiles.
