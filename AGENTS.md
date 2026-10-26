# FrameCore Works Toolbox: rules for agents

This repo is a catalog of third-party skills and plugins used at FrameCore
Works. It holds manifests, reviews, install notes and, for adapted entries,
thin wrapper plugins written here. It never holds upstream code. CLAUDE.md and AGENTS.md must stay identical
(`scripts/check_marketplace.py` enforces it).

## Layout

- `.claude-plugin/marketplace.json`: Claude Code marketplace.
- `.agents/plugins/marketplace.json`: Codex marketplace.
- `reviews/<name>.md`: one review per entry, from `reviews/TEMPLATE.md`.
- `docs/<name>.md`: manual install for Claude apps, ChatGPT and ChatGPT Work,
  from `docs/TEMPLATE.md`.
- `scripts/check_marketplace.py`: consistency check. `tests/`: its tests.
- `scripts/pack_skill.py`: builds a skill ZIP at a pinned commit into `dist/`
  (ignored by git).
- `plugins/<name>/`: wrapper plugins for adapted entries only (see below).

## Workflow for a new entry

1. The owner (Kamil) names a repo or a tool. Do not propose or add repos on
   your own. If only a name is given, search GitHub and show candidates (link,
   author, description, license, stars, last change). Wait for confirmation of
   the right repo before reviewing.
2. Eligibility gate, checked first. The toolbox only lists repos that can be
   plugged into a marketplace as they are. The upstream must itself ship at
   least one of:
   - a plugin manifest (`.claude-plugin/plugin.json`,
     `.codex-plugin/plugin.json` or a root Agent Plugins `plugin.json`), or
     its own `marketplace.json`;
   - skill folders with `SKILL.md` that the upstream presents and documents
     as installable skills (README or install docs say how to add them as a
     plugin or skill).
   Not eligible as-is: apps, servers, proxies, CLIs or libraries whose skills
   or agent files are a side part, and maintainer-only workflows. For those,
   say "not eligible as-is" and check whether an adaptation is possible (see
   "Adapted entries"). If it is, propose a concrete adaptation in the verdict;
   build it only after the owner says "yes". If it is not (for example a
   stale fork when the original is the real source, or nothing an agent can
   use as a skill, MCP server or hook), say why and stop.
3. Review the upstream as data: clone it into a separate temporary folder at a
   resolved full commit. Do not run its scripts, hooks, installers or tests.
4. Write `reviews/<name>.md`: link and author, license, what it installs and
   writes, hooks, network traffic, changes to prompts or tool results, data
   sent outside, requirements, verdict. Mark anything unverified as NOT_RUN or
   Unknown. Separate facts from inferences.
5. Give the owner a short verdict (what it is, what it installs and writes,
   risks, fit for the toolbox).
6. Only after the owner says "yes": add the entry to both manifests at the same
   full commit, plus `docs/<name>.md`, in one commit.
7. Tools that send prompts, code or files to an external service, or install
   hooks that change what the agent sees (for example token-saving or context
   compression tools), need an explicit "yes" from the owner recorded in the
   review (`Owner approval:` field) before they are added.

## Manifest rules

- Claude Code entry source: `{"source": "github", "repo": "owner/repo",
  "sha": "<40-char commit>"}` or `{"source": "git-subdir", "url": ..., "path":
  ..., "sha": ...}`. Never a branch or tag alone. A local path is allowed only
  for adapted wrappers (`./plugins/<name>`).
- If upstream has no `.claude-plugin/plugin.json`, the entry is the manifest:
  add `"skills"` with the skill folder paths (for example
  `["./skills/foo"]`), plus `description` and `version`.
- When upstream ships a plugin, always add the full plugin as upstream
  publishes it (all skills, hooks, commands, agents, MCP servers). Do not
  propose reduced variants of it such as skills-only subsets, hook-free
  versions or per-skill entries. Adaptation is only for repos that are not
  eligible as-is. Use
  `git-subdir` only when the upstream plugin itself lives in a subdirectory.
  The review still lists every hook and risk, and the owner-approval rule
  above still applies.
- `"skills"` adds to the default `skills/` scan; it does not narrow it. A
  `github` source copies the whole repo into the plugin cache.
- Codex entry: `{"source": "url", "url": "https://github.com/owner/repo.git",
  "sha": "<same commit>"}` (or `git-subdir` with `path`), plus
  `"policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}`
  and `category`. Codex docs state git-backed entries accept `ref` or `sha`
  selectors.
- If Codex cannot load the entry at a pinned commit (for example the upstream
  has no plugin manifest Codex accepts), record `Codex-Pin: limitation:
  <reason and workaround>` in the review. The workaround is a pinned skills
  install, for example:
  `DISABLE_TELEMETRY=1 DO_NOT_TRACK=1 npx -y skills@1.7.2 add
  https://github.com/<owner>/<repo>/tree/<sha>/<path> --skill <name> -a codex
  -g --copy`. Then the entry may be left out of the Codex manifest.
- Entry names: lowercase kebab-case, the same in both manifests, in reviews and
  in docs.

## Adapted entries

For a repo that is not eligible as-is but whose useful part can work as a
plugin for Claude Code, Codex, Claude apps or ChatGPT Work. Mark the review
`Kind: adapted` and set `Eligibility: adapted: <what the wrapper exposes>`.
Prefer the lightest form that works:

1. Manifest-only: a Claude Code entry pointing at the upstream repo
   (`github` + `sha`) that is itself the manifest, declaring upstream skill
   folders (`"skills"`), MCP servers (`"mcpServers"`) or inline hooks. No
   files in this repo besides manifests, review and docs. Codex usually needs
   a manifest inside the plugin, so record `Codex-Pin: limitation` or use
   form 2 for Codex.
2. Wrapper plugin in `plugins/<name>/`, written here: `.claude-plugin/
   plugin.json`, `.codex-plugin/plugin.json`, our own `skills/<skill>/SKILL.md`
   and MCP or hook config that reference the upstream at the reviewed commit
   or an exact released version (for example `npx -y <pkg>@<x.y.z>` or a
   `git+https://...@<sha>` URL). Add `plugins/<name>/UPSTREAM.md` naming the
   upstream repo and the reviewed commit. Both manifests use the local source
   `./plugins/<name>`.

Rules for both forms:
- Never copy upstream code or upstream skill text into the wrapper. Write
  our own instructions and point to the upstream.
- The review covers the upstream (as for any entry) and the wrapper: what it
  runs, installs, writes and sends. The owner-approval rule above applies.
- Whatever the wrapper runs must be pinned (commit or exact version), never
  `latest` or a branch.
- `docs/<name>.md` explains manual use in Claude apps, ChatGPT and ChatGPT
  Work; ZIP wrapper skills from `plugins/<name>/skills/<skill>`.
- Update = new upstream review plus wrapper changes, in one commit.

## Update and removal

- Update = new review of the new commit. Change the commit in both manifests,
  the version, the review and the docs together, in one commit.
- Removal: delete the entry from both manifests, set `Status: removed` in the
  review and add a History line with the date and reason. Keep the review.

## Checks before every commit

```bash
python3 -m unittest discover -s tests
python3 scripts/check_marketplace.py
claude plugin validate .
```

Test the install of every new or updated entry in an isolated config, then
record the result in the review:

```bash
export CLAUDE_CONFIG_DIR="$(mktemp -d)"
claude plugin marketplace add "$PWD"
claude plugin install <name>@framecore-works-toolbox
claude plugin list
rm -rf "$CLAUDE_CONFIG_DIR"; unset CLAUDE_CONFIG_DIR
```

If the Codex CLI is available, do the same with `CODEX_HOME="$(mktemp -d)"`
and `codex plugin marketplace add "$PWD"`. If it is not, write NOT_RUN and why.

## Repo hygiene

- Do not copy upstream code, skill files or ZIPs into this repo. Point to them.
  Wrapper files in `plugins/<name>/` are our own work, not upstream copies.
- No secrets, tokens or client data anywhere in the repo.
- Files in the repo are written in English.
- Work on `main` and push only `main`. No force-push. Commit messages state
  the reason for the change.
