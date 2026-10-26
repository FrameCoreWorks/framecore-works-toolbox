# FrameCore Works Toolbox

Private Claude plugin marketplace with reviewed third-party plugins used at
FrameCore Works. Add it once in Claude (claude.ai, desktop, Cowork or Claude
Code), then add the plugins you want; Claude picks their skills by task or you
call them with `/`.

Every entry is pinned to a full upstream commit and has a security review in
`reviews/` and notes in `docs/`. This repo holds no upstream code. Repos that
are not plugins themselves can be added as adapted entries: a thin wrapper
plugin written here in `plugins/<name>/` that points to the reviewed upstream
commit.

## Plugins

Type `toolbox` in Claude to see this list, grouped by category. The index
itself: `toolbox` (first-party, this repo, skill everywhere,
[docs](docs/toolbox.md); no hooks, scripts or network).

### Creative

| Name | Upstream | Commit (version) | What it is for | Chat / Cowork / Claude Code | Notes | Review |
| ---- | -------- | ---------------- | -------------- | --------------------------- | ----- | ------ |

### Dev tools

| Name | Upstream | Commit (version) | What it is for | Chat / Cowork / Claude Code | Notes | Review |
| ---- | -------- | ---------------- | -------------- | --------------------------- | ----- | ------ |
| ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | `09c434a` (5.3.2) | minimal code changes, code review, repo audit; plugin with always-on hooks | skills / skills + hooks / skills + hooks + mod | [docs](docs/ponytail.md) | [review](reviews/ponytail.md) |

## Install

Full steps: [docs/install.md](docs/install.md).

- Claude apps: Customize > Plugins > Add > Add marketplace >
  `FrameCoreWorks/framecore-works-toolbox` (connect GitHub and give the Claude
  GitHub App access to this private repo), then Add each plugin.
- Claude Code CLI:

```bash
claude plugin marketplace add FrameCoreWorks/framecore-works-toolbox
claude plugin install <name>@framecore-works-toolbox
```

## Maintaining

Rules for adding, updating and removing entries are in [CLAUDE.md](CLAUDE.md).
Before every commit:

```bash
python3 -m unittest discover -s tests
python3 scripts/check_marketplace.py
claude plugin validate .
```
