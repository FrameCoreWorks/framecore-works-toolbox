# Upstream

- Repository: https://github.com/morluto/rea (MIT, morluto)
- Reviewed commit: 5e30969cc5f1255d44ec7a1f1ca8dbac0af5e7c4 (release 6.5.0)
- Runtime: npm package `rea-agents@6.5.0`, started as `npx -y rea-agents@6.5.0 mcp`
  (stdio MCP server, as documented in the upstream `docs/installation.md`).

This wrapper contains no upstream code or skill text. Its skill is our own and
pins every REA call to 6.5.0. The upstream skill is not included because it runs
`rea-agents@latest` and its `setup` command, which rewrites client configuration.
Review: ../../reviews/rea.md
