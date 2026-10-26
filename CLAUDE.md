# FrameCore Works Toolbox: rules for agents

This repo is a Claude plugin marketplace with reviewed third-party plugins
used at FrameCore Works. It is added once as a marketplace in Claude
(claude.ai, desktop and Cowork through Customize > Plugins, or Claude Code
with `claude plugin marketplace add`), and each plugin is then installed from
it. It holds the manifest, reviews, install notes and, for adapted entries,
thin wrapper plugins written here. It never holds upstream code.

## Layout

- `.claude-plugin/marketplace.json`: the marketplace.
- `reviews/<name>.md`: one review per entry, from `reviews/TEMPLATE.md`.
- `docs/<name>.md`: per-entry notes (setup, what works in chat, Cowork and
  Claude Code, full removal), from `docs/TEMPLATE.md`.
- `docs/install.md`: how to add the marketplace and install plugins.
- `plugins/<name>/`: wrapper plugins for adapted entries, and first-party
  plugins such as `plugins/toolbox/` (the index).
- `scripts/check_marketplace.py`: consistency check. `tests/`: its tests.

## Workflow for a new entry

1. The owner (Kamil) names a repo or a tool. Do not propose or add repos on
   your own. If only a name is given, search GitHub and show candidates (link,
   author, description, license, stars, last change). Wait for confirmation of
   the right repo before reviewing.
2. Eligibility gate, checked first. The upstream must itself ship at least one
   of:
   - a Claude plugin manifest (`.claude-plugin/plugin.json`) or its own
     `.claude-plugin/marketplace.json`;
   - skill folders with `SKILL.md` that the upstream presents and documents
     as installable skills.
   Not eligible as-is: apps, servers, proxies, CLIs or libraries whose skills
   or agent files are a side part, and maintainer-only workflows. For those,
   say "not eligible as-is" and check whether an adaptation is possible (see
   "Adapted entries"). If it is, propose a concrete adaptation in the verdict;
   build it only after the owner says "yes". If it is not (for example a
   stale fork when the original is the real source, or nothing Claude can use
   as a skill, command, agent, hook or MCP server), say why and stop.
3. Review the upstream as data: clone it into a separate temporary folder at a
   resolved full commit. Do not run its scripts, hooks, installers or tests.
4. Write `reviews/<name>.md`: link and author, license, what it installs and
   writes, hooks, network traffic, changes to prompts or tool results, data
   sent outside, requirements, verdict. Mark anything unverified as NOT_RUN or
   Unknown. Separate facts from inferences.
5. Give the owner a short verdict (what it is, what it installs and writes,
   risks, fit for the toolbox).
6. Only after the owner says "yes": add the entry to the manifest at the full
   commit with its category, plus `docs/<name>.md`, the README row and the
   row in the toolbox index skill under its category, in one commit.
7. Plugins that send prompts, code or files to an external service, or install
   hooks that change what Claude sees (for example token-saving or context
   compression tools), need an explicit "yes" from the owner recorded in the
   review (`Owner approval:` field) before they are added.

## Categories

Every entry except the `toolbox` index has a `category` in the manifest, and
the index lists it under the matching heading:

| Slug | Heading in the index | For |
| ---- | -------------------- | --- |
| `creative` | Creative | motion graphics, video editing, image, audio, art and gallery sources, other creative production |
| `dev-tools` | Dev tools | coding, code review, repo and workflow organisation |
| `marketing` | Marketing & growth | SEO, CRO, copy, ads, social, sales, product and business strategy |

To add a category: add it to this table and to `CATEGORIES` in
`scripts/check_marketplace.py`, and add its heading and empty table to the
index skill. Each index row has a one-sentence "What it is for" that says
what the plugin does and when to use it.

## Manifest rules

- Entry source: `{"source": "github", "repo": "owner/repo", "sha":
  "<40-char commit>"}`, or `{"source": "git-subdir", "url": ..., "path": ...,
  "sha": ...}` when the upstream plugin lives in a subdirectory. Never a branch
  or tag alone. A local path is allowed only for adapted wrappers
  (`./plugins/<name>`).
- When upstream ships a plugin, always add the full plugin as upstream
  publishes it (all skills, commands, agents, hooks, MCP servers). Do not
  propose reduced variants such as skills-only subsets, hook-free versions or
  per-skill entries. Adaptation is only for repos that are not eligible as-is.
- If upstream has no `.claude-plugin/plugin.json`, the entry is the manifest:
  add `"skills"` with the skill folder paths, plus `description` and
  `version`. `"skills"` adds to the default `skills/` scan; it does not narrow
  it. A `github` source copies the whole repo into the plugin cache.
- Entry names: lowercase kebab-case, the same in the manifest, reviews and
  docs.

## Adapted entries

For a repo that is not eligible as-is but whose useful part can work as a
Claude plugin. Mark the review `Kind: adapted` and set `Eligibility: adapted:
<what the wrapper exposes>`. Prefer the lightest form that works:

1. Manifest-only: an entry pointing at the upstream repo (`github` + `sha`)
   that is itself the manifest, declaring upstream skill folders
   (`"skills"`), MCP servers (`"mcpServers"`) or inline hooks. No files in
   this repo besides the manifest, review and docs.
2. Wrapper plugin in `plugins/<name>/`, written here: `.claude-plugin/
   plugin.json`, our own `skills/<skill>/SKILL.md`, and MCP or hook config
   that reference the upstream at the reviewed commit or an exact released
   version (for example `npx -y <pkg>@<x.y.z>` or a `git+https://...@<sha>`
   URL). Add `plugins/<name>/UPSTREAM.md` naming the upstream repo and the
   reviewed commit. The manifest uses the local source `./plugins/<name>`.

Rules for both forms:
- Never copy upstream code or upstream skill text into the wrapper. Write
  our own instructions and point to the upstream.
- The review covers the upstream and the wrapper: what it runs, installs,
  writes and sends. The owner-approval rule above applies.
- Whatever the wrapper runs must be pinned (commit or exact version), never
  `latest` or a branch.
- A wrapper must not have a top-level `bin/` directory: claude.ai and Cowork
  do not install plugins that have one.
- Update = new upstream review plus wrapper changes, in one commit.

## First-party plugins

Plugins written here with no upstream, marked in the manifest entry with
`"metadata": {"firstParty": true}` and the local source `./plugins/<name>`.
They need `docs/<name>.md` but no review or commit pin. No hooks, scripts or
network unless the owner asks for them.

- `toolbox`: the index. Its skill
  `plugins/toolbox/skills/toolbox/SKILL.md` holds the catalog, one table per
  category (one row per other entry, name in backticks in the first column,
  one-sentence purpose) and short "Use" and "Watch out" notes. Every entry added, updated or removed changes this file
  in the same commit; `scripts/check_marketplace.py` fails when the table and
  the manifest differ.

## Update and removal

- Update = new review of the new commit. Change the commit and version in the
  manifest, the review, the docs and the README together, in one commit.
- Removal: delete the entry from the manifest, the README and the toolbox
  index skill, set `Status: removed` in the review and add a History line
  with the date and reason. Keep the review.

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

Installing through claude.ai (Customize > Plugins) is done by the owner;
record it as NOT_RUN until the owner reports the result.

## Maintainer tooling

The owner keeps these Anthropic plugins active for work on this repo. Use
them as follows:

- superpowers: `brainstorming` before changing rules, layout or the check
  script; `test-driven-development` for `scripts/check_marketplace.py`;
  `verification-before-completion` before every commit and status report.
- plugin-dev: `plugin-structure` and `skill-development` when building wrapper
  or first-party plugins; the `plugin-validator` agent on them;
  `skill-reviewer` on any `SKILL.md` written here.
- pr-review-toolkit: the `code-reviewer` agent on non-trivial diffs before
  pushing (work goes straight to `main`, so this replaces PR review);
  `silent-failure-hunter` on check-script changes.
- claude-md-management: `revise-claude-md` at the end of a session that
  changed how the repo works.
- security-guidance: keep its edit-time warnings on; apply the same scrutiny
  when reviewing upstream code.
- hookify: only when the owner asks for a rule that must be enforced
  mechanically.

## Superpowers and ponytail

Superpowers decides the process (when to think, plan, test, verify);
ponytail decides the size of each step (how much code and text). Where they
meet:

- Specs and plans stay in the chat; no files under `docs/superpowers/`.
- Brainstorming only for changes to rules, layout or the check script. A new
  catalog entry follows the workflow above.
- Test first for logic in `scripts/check_marketplace.py`; no tests for docs,
  manifest entries or text.
- Reports are short but keep the evidence (commands and results) and every
  NOT_RUN and Unknown.
- Scope comes from the owner: build what was approved, name a smaller option
  in one line instead of cutting.

## Repo settings

`.claude/settings.json` sets `PONYTAIL_DEFAULT_MODE=lite`, so ponytail runs
in this repo even when the owner's global default is off (see
`docs/ponytail.md`). `lite` builds what was asked and only names a smaller
option; `full` would cut scope the owner approves. Remove that line if
ponytail is removed.

## Repo hygiene

- Do not copy upstream code or skill files into this repo. Point to them.
  Wrapper files in `plugins/<name>/` are our own work, not upstream copies.
- No secrets, tokens, client data or ZIP files anywhere in the repo.
- Files in the repo are written in English.
- Work on `main` and push only `main`. No force-push. Commit messages state
  the reason for the change.
