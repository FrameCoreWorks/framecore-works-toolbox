# rea: install notes

- Upstream: https://github.com/morluto/rea
- Pinned commit: 5e30969cc5f1255d44ec7a1f1ca8dbac0af5e7c4 (version 6.5.0)
- Review: [reviews/rea.md](../reviews/rea.md)

## Install

See [install.md](install.md). Plugin id: `rea@framecore-works-toolbox`.

## Codex

`plugins/rea/` also carries `.codex-plugin/plugin.json`, which declares the
skill and the same pinned MCP server (`npx -y rea-agents@6.5.0 mcp`). On the
user's installation request, install that complete directory through the
actual Codex host's local plugin route. Where no plugin route exists, the
native-entry helper installs the skill from a checkout at a verified commit:

```sh
python3 scripts/install_codex.py install --plugin rea --skills-dir "<skills-dir>" --bundle-dir "<bundle-dir>" --source-commit "<40-character-commit>"
```

The helper adds no MCP server; register the pinned command above as a local
MCP server in the user's Codex configuration, with their agreement, and never
run upstream's `setup`. Codex activation and a Codex run remain NOT_RUN.

## Setup after install

Node.js 22.19+, 24.11+ or 26+ with npm; a Chrome-family browser for web targets; Ghidra, IDA or Hopper only for native binaries.

## What works where

Claude Code and Cowork (Node 22.19+ for the MCP server); Codex through its own `.codex-plugin` package; chat: skill only.

## Use

Ask how a feature of an app, a bundle or a binary works; the skill calls the `rea` MCP tools.

## Watch out

Lawful targets only; native binaries need Ghidra, IDA or Hopper.

## Full removal

Remove it in Customize > Plugins or with `claude plugin uninstall rea@framecore-works-toolbox`.
