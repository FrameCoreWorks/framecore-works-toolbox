# FrameCore Works Toolbox

Private catalog of third-party skills and plugins used at FrameCore Works, for
Claude Code, Codex, the Claude apps, ChatGPT and ChatGPT Work.

Every entry points to an upstream GitHub repo pinned to a full commit, has a
security review in `reviews/` and manual install notes in `docs/`. This repo
holds no upstream code.

## Entries

| Name | Upstream | Commit | Kind | Claude Code | Codex | Apps | Review |
| ---- | -------- | ------ | ---- | ----------- | ----- | ---- | ------ |
| ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | `09c434a` (5.3.2) | plugin with hooks | tested | NOT_RUN (sha pinned) | manual, [docs](docs/ponytail.md) | [review](reviews/ponytail.md) |

## Install

The repo is private, so every environment needs GitHub access to
`FrameCoreWorks/framecore-works-toolbox` (git credentials or `gh auth login`).

### Claude Code

```bash
claude plugin marketplace add FrameCoreWorks/framecore-works-toolbox
claude plugin install <name>@framecore-works-toolbox
# update the catalog after a new commit here
claude plugin marketplace update framecore-works-toolbox
# remove
claude plugin uninstall <name>@framecore-works-toolbox
```

Inside a session the same works with `/plugin marketplace add ...` and
`/plugin install <name>@framecore-works-toolbox`.

### Codex

```bash
codex plugin marketplace add FrameCoreWorks/framecore-works-toolbox
codex plugin marketplace upgrade framecore-works-toolbox
codex plugin marketplace remove framecore-works-toolbox
```

Codex docs describe installing plugins from a marketplace through the Plugins
Directory in the ChatGPT desktop app (Codex / Work mode); the CLI commands
above register the catalog. Entries whose review says `Codex-Pin: limitation`
are not in the Codex manifest; install their skills with the pinned command
from `docs/<name>.md`, for example:

```bash
DISABLE_TELEMETRY=1 DO_NOT_TRACK=1 npx -y skills@1.7.2 add \
  https://github.com/<owner>/<repo>/tree/<sha>/<path> --skill <name> -a codex -g --copy
```

### Claude apps, ChatGPT, ChatGPT Work

These apps do not install from GitHub. Each `docs/<name>.md` lists the files to
upload and how to remove them. General steps: [docs/apps.md](docs/apps.md).
To build an upload ZIP at the pinned commit:

```bash
python3 scripts/pack_skill.py <owner>/<repo> <sha> <path/to/skill>
```

## Maintaining

Rules for adding, updating and removing entries are in [AGENTS.md](AGENTS.md)
(same text as [CLAUDE.md](CLAUDE.md)). Before every commit:

```bash
python3 -m unittest discover -s tests
python3 scripts/check_marketplace.py
claude plugin validate .
```
