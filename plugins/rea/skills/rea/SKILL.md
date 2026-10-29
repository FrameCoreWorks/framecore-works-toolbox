---
name: rea
description: Reverse engineer software the user owns or may examine with REA (pinned rea-agents 6.5.0): Electron and JavaScript apps or ASAR archives, .NET assemblies, Android packages, firmware, network captures, browser pages already open, and native binaries through Ghidra, IDA or Hopper. Use when a question depends on a shipped app or binary rather than its source, for example how an app builds an effect or what a bundle does. Not for ordinary source repositories, image or prompt reconstruction, or bypassing protection, licences or logins.
---

# REA (pinned)

Every finding needs evidence. Report what REA returned, its unknowns and its
limits; never present a guess as a finding.

## Before you start

- Confirm the target is the user's own or one they may lawfully examine. If not,
  stop and say why.
- For a complete source repository, use normal repository reading instead.
- Use the `rea` MCP tools when this session lists them. Pick the first tool from
  the target: an extracted app or ASAR goes to the JavaScript application
  analysis, an archive or package to the binary or artifact inspection, an
  Android package to the Android inspection, a .NET assembly to the managed
  inspection, a capture file to the capture inspection, an open browser page to
  the browser target listing. Read each tool's own schema before calling it.

## When the tools are missing

1. The server starts with `npx -y rea-agents@6.5.0 mcp`; the first start fetches
   that exact version from npm (Node.js 22.19+, 24.11+ or 26+). If npm or the
   network is blocked, say so and stop.
2. A CLI fallback for a JavaScript tree or ASAR needs no MCP:
   `npx -y rea-agents@6.5.0 analyze-javascript-application /absolute/path --json`.
   Read its evidence the same way.
3. Never run `rea-agents@latest`, an unpinned version, or REA's `setup` or
   `--install-hopper`: they change client configuration or fetch unreviewed
   code. Toolbox registers the server through this plugin instead.
4. Native binaries need Ghidra, IDA or Hopper already installed by the user.
   Do not install engines, Java, Node.js or other software yourself.

## Report

- What was examined (path, hash when REA gives one), which tools ran.
- Findings with their evidence, then unknowns and what did not run.
- Use findings to understand a technique. Do not copy the target's code, assets
  or text into the user's work.
