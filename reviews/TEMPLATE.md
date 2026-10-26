# Review: <entry-name>

<!--
Copy this file to reviews/<entry-name>.md. The fields in the "Entry" list are
read by scripts/check_marketplace.py, so keep the "- Key: value" format.
Mark anything you did not verify as NOT_RUN or Unknown. Never guess.
-->

## Entry

- Name: <entry-name>
- Status: active
- Upstream: https://github.com/<owner>/<repo>
- Author: <GitHub owner, people or organization>
- License: <SPDX id, or Unknown if no LICENSE file>
- Commit: <full 40-character commit SHA>
- Upstream version: <version from plugin.json or tag, or none>
- Kind: <plugin | skills | adapted>
- Eligibility: <upstream manifest or documented skills that make it marketplace-ready, or "adapted: <what the wrapper exposes>">
- Claude Code source: <github | git-subdir (path) | url>
- Codex-Pin: <sha | limitation: reason and workaround>
- Reviewed on: <YYYY-MM-DD>
- Reviewer: <who ran the review>
- Owner approval: <not required | "yes" from Kamil on YYYY-MM-DD, quote>

## What it is

<One paragraph: what the skill or plugin does and which components it ships
(skills, commands, agents, hooks, MCP servers, scripts).>

## Files reviewed

<List of paths read at the pinned commit. Upstream was cloned as data into a
temporary folder; no scripts, hooks or installers were run.>

## What it installs and writes

<Files written on install and at runtime, locations (plugin cache, home dir,
project dir), config changes.>

## Hooks

<Each hook: event, matcher, command, what it does. "None" if none.>

## Network traffic

<Every host contacted, by which component, and when. "None found" if none.>

## Changes to prompts or tool results

<Does anything inject context, rewrite prompts, or alter what the agent sees
from tools? Token-saving and context-compression tools belong here.>

## Data sent outside

<Does it send prompts, code, files or telemetry to an external service? Which
service, and is it opt-in?>

## Requirements

<Runtimes, CLIs, API keys, accounts, OS limits.>

## Install tests

- Claude Code (isolated CLAUDE_CONFIG_DIR): <PASS | FAIL | NOT_RUN>, with the commands and output summary
- Codex CLI (isolated CODEX_HOME): <PASS | FAIL | NOT_RUN>, with the reason if not run
- Claude app / ChatGPT / ChatGPT Work: NOT_RUN (manual upload, see docs/<entry-name>.md)

## Risks

<Concrete risks, ordered by severity.>

## Verdict

<accept | accept with conditions | reject>, with a short reason.

## History

- <YYYY-MM-DD>: added at <short SHA>.
<!-- On removal set "Status: removed" above and add:
- <YYYY-MM-DD>: removed. Reason: <reason>. -->
