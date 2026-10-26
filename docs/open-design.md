# open-design: install notes

- Upstream: https://github.com/nexu-io/open-design
- Pinned commit: 26d60298f8129e229a1c10aab4df7ca25b1e9ad3 (version 1.0.0)
- Review: [reviews/open-design.md](../reviews/open-design.md)

## Install

See [install.md](install.md). Plugin id: `open-design@framecore-works-toolbox`.

## Setup after install

Install the Open Design app from its upstream instructions so that `od` is on PATH, and start its daemon (default port 7456).

## What works where

| Component | Chat | Cowork | Claude Code |
| --------- | ---- | ------ | ----------- |
| MCP `open-design` (local `od` daemon) | no | yes, with the app | yes, with the app |

## Use

With the app running, ask Claude to open or work on an Open Design project; the tools come from the `open-design` MCP server.

## Full removal

Remove it in Customize > Plugins, or run `claude plugin uninstall open-design@framecore-works-toolbox`. Uninstall the Open Design app separately if you installed it.
