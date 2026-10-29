# Review: rea

## Entry

- Name: rea
- Status: active
- Upstream: https://github.com/morluto/rea
- Author: morluto
- License: MIT
- Commit: 5e30969cc5f1255d44ec7a1f1ca8dbac0af5e7c4
- Upstream version: 6.5.0
- Kind: adapted
- Eligibility: adapted: our own wrapper plugin `plugins/rea` with its own skill and the MCP server from npm `rea-agents@6.5.0` (`npx -y rea-agents@6.5.0 mcp`); the upstream skill is left out because it runs `rea-agents@latest` and the `setup` command
- Source: local wrapper ./plugins/rea (UPSTREAM.md names the reviewed commit)
- Reviewed on: 2026-10-29
- Reviewer: Claude (cloud orchestration thread), carrying over the Creative Studio registry review at the same commit
- Owner approval: "yes" from Kamil on 2026-10-29 (decision card "Przenieść wszystko do Toolboxa", then "decyzje są już podjęte" accepting the move list)

## What it is

REA (Reverse Engineer Anything): reverse engineering of software the user may analyse, across Electron and JavaScript apps, .NET assemblies, Android packages, websites through DevTools, network captures and native binaries with Ghidra, IDA or Hopper. Every finding comes with its evidence and unknowns.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, how an effect in an app or site is built (previously Studio's recommended extension `rea`) | Evidence-backed analysis of Electron apps, bundles and source maps where Studio's web motion probe stops | Studio trial 2026-10-15: rea-agents 6.5.0 ran setup --dry-run and doctor in a container; Toolbox install PASS; MCP start NOT_RUN |

Moved from Creative Studio's recommended-extension registry to Toolbox by owner decision 2026-10-29: Toolbox becomes the single source of installable recommendations and Studio points here.

## Files reviewed

Upstream cloned as data at the pinned commit into a temporary folder; no scripts, hooks or installers were run. Read: README.md, .agents/skills/reverse-engineer-anything/SKILL.md (it calls `npx -y rea-agents@latest doctor|setup|analyze-…` at lines 36, 50, 55, 70 and 78: unpinned, so it is not shipped), package.json (bin `rea`/`rea-agents`, engines), docs/installation.md (MCP registry section), .agents/skills/*/SKILL.md, LICENSE.

## What it installs and writes

The wrapper ships only our own files: `.claude-plugin/plugin.json`, the portable and Codex manifests, `.mcp.json` and `skills/rea/SKILL.md`. The plugin cache (the repository checkout). npx caches `rea-agents@6.5.0` in the npm cache when the MCP server first starts. Analysis output where the user asks. The upstream `setup` command would edit `~/.claude.json` and replace the skill; our skill forbids it and every `@latest` call.

## Hooks

None.

## Network traffic

The npm registry, once, to fetch rea-agents 6.5.0 for the MCP server. Analysis of a web target talks to that target only when the user asks.

## Changes to prompts or tool results

Our skill `rea:rea` loads by description on reverse-engineering tasks. The MCP server answers tool calls.

## Data sent outside

None found by default.

## Requirements

Node.js 22.19+, 24.11+ or 26+ with npm; a Chrome-family browser for web targets; Ghidra, IDA or Hopper only for native binaries.

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): PASS 2026-10-29 in an isolated CLAUDE_CONFIG_DIR: `claude plugin marketplace add` of this repository, `claude plugin install rea@framecore-works-toolbox` succeeded, `claude plugin list` showed it enabled, and a headless `claude -p` session listed its skills (`rea:reverse-engineer-anything`, first manifest-only form; repeated for the wrapper below). The install printed a note that the repository's package.json dependencies were not installed (it sets overrides); the MCP server runs from the pinned npm package instead. The MCP server was not started here: NOT_RUN.
- claude.ai / Cowork (Customize > Plugins): NOT_RUN until the owner reports the result

- Wrapper form (2026-10-29, after code review): `claude plugin validate plugins/rea` PASS, `package_plugins.py --plugin rea --check` PASS, isolated install result recorded in docs/verification.md.

## Risks

1. Analyse only software and sites the user owns or may examine. 2. The MCP server is fetched from npm at first start (pinned exact version).

## Verdict

accept with conditions: lawful targets only.

## History

- 2026-10-29: code review found the upstream skill calls `rea-agents@latest` and `setup`; changed from a manifest-only entry to our own wrapper that pins 6.5.0.
- 2026-10-29: added at 5e30969, moved from Creative Studio's recommended extensions.
