# Earshot Audio: install notes

- Upstream: https://github.com/Leonxlnx/earshot (Leon Lin, MIT)
- Pinned commit: `591fa3e028032e6dce56620a20e932e35667e8d8` (engine 0.4.0)
- Built into Toolbox since 1.1.0: launcher `plugins/toolbox/capabilities/earshot/`,
  instructions `plugins/toolbox/skills/toolbox/references/earshot/`
- Review: [reviews/earshot-audio.md](../reviews/earshot-audio.md)

## Installation

There is no separate plugin. Install Toolbox (see [install.md](install.md),
[CHATGPT_INSTALL.md](../CHATGPT_INSTALL.md), [CODEX_INSTALL.md](../CODEX_INSTALL.md));
Earshot comes with it. The `earshot-audio` plugin of Toolbox 1.0.x is retired and
is not in the marketplace any more.

| Host | Route | Verification |
| --- | --- | --- |
| Claude apps / Cowork | Add or update `toolbox` from the Toolbox marketplace | UI activation NOT_RUN |
| Claude Code | `claude plugin install toolbox@framecore-works-toolbox` | Isolated install recorded in the review |
| ChatGPT Work | Toolbox ZIP through Plugin Creator, updating the existing Toolbox identity | Saved Work deployment pending |
| Codex | Complete local Toolbox plugin, or `install_codex.py` (default plugin `toolbox`) | Client activation NOT_RUN |

### Moving from the separate plugin

1. Install or update Toolbox to 1.1.0 or later.
2. Remove the old `earshot-audio` plugin with the host's controls (Claude CLI:
   `claude plugin uninstall earshot-audio@framecore-works-toolbox`; in ChatGPT
   Work, the saved Earshot plugin; in Codex, its native entry after checking the
   receipt). The engine runtime folder is not part of the plugin and stays.
3. Run `status --json` (below). An existing runtime appears under `candidates`;
   choose it with `--root` or `EARSHOT_NATIVE_ROOT`. Nothing is selected for you.

## Retiring installed copies (owner decision 2026-10-29)

The owner approved retiring every installed copy of the old separate Earshot
plugin (stage 6b of the Earshot migration). Status: **retired**. No route in
Toolbox or Creative Studio uses it, and no marketplace offers it. Removal is a
host step the owner does on each device or account; nothing in this repository
can remove an installed copy. Do it only after Toolbox 1.1.0 or later is
installed on that host, and keep the engine runtime folder (by default
`~/.framecore-works/earshot`, older ones under `~/.framecore-studio/extensions/earshot`):
it is not part of the plugin and Toolbox reuses it.

| Host | Old identity | How to remove it | Check afterwards |
| --- | --- | --- | --- |
| Claude Code | `earshot-audio@framecore-works-toolbox` (Toolbox 1.0.x) or `earshot-audio@framecore-works` (Creative Studio's marketplace up to Studio 1.151.0) | `claude plugin list`, then `claude plugin uninstall earshot-audio@<marketplace>` for each listed copy | `claude plugin list` shows no `earshot-audio`; a new conversation lists `toolbox:toolbox` |
| Claude apps / Cowork | Earshot Audio from either marketplace | Customize > Plugins, open Earshot Audio, uninstall | The plugin list shows FrameCore Works Toolbox and no Earshot Audio |
| ChatGPT Work | Saved standalone Earshot Audio plugin (Work 1.1.0, release `plugins_6ada290e…`) | First read back the saved Toolbox plugin at 1.1.0 or later. Then remove the Earshot Audio plugin in Work's plugin settings, or with Plugin Creator against its current release guard and its exact observed paths | Work's plugin list has no Earshot Audio; a new conversation answers a sound task through Toolbox |
| Codex | Native entry `<skills-dir>/earshot-audio/` made by `install_codex.py --plugin earshot-audio` | Open its `installation.json`: remove the entry only when `plugin` is `earshot-audio`. Delete that entry folder and the `bundle_dir` the receipt names, and nothing else | `install_codex.py verify` for the `toolbox` entry reports `FILES_VERIFIED`; no `earshot-audio` entry remains |

Report each host as `retired` only after its check passed; until then it stays
`pending` (owner-run, NOT_RUN here).

Observed on the owner's Mac and accounts, 2026-10-29 (Remote Control session with
the owner's Chrome, owner choice "remove now", before Toolbox was installed there):

| Host | Result |
| --- | --- |
| ChatGPT Work | `retired`: Earshot Audio 1.1.0 (`plugins_6ada290e00e08191a449126f758c8b7d`) uninstalled, gone from Installed after reload; the plugin itself stays on the account and can be reinstalled |
| Codex | Remote-plugin cache copy of 1.1.0 still present; expected to clear on the next account sync; no native entry found |
| Claude Code, claude.ai | Not installed; nothing to remove |

Toolbox was not installed on any of these hosts, so Earshot is unavailable there
until Toolbox 1.1.0 or later is added.

## Engine setup

Inspect readiness and the setup plan from the installed Toolbox package. Only the
`--yes` form changes anything:

```sh
python3 <toolbox>/capabilities/earshot/scripts/runtime.py status --json
python3.12 <toolbox>/capabilities/earshot/scripts/runtime.py install --tier light
python3.12 <toolbox>/capabilities/earshot/scripts/runtime.py install --tier light --yes
```

Setup verifies every upstream source file, keeps the original snapshot under the
selected runtime root, installs exact wheel versions with SHA-256 checks and uses
locked build tools. Defaults to `~/.framecore-works/earshot`; choose another root
with `EARSHOT_NATIVE_ROOT` or `--root`. Existing nonempty roots are preserved;
select a new one for replacement or a different tier.

Light covers local measurement and procedural sound workflows, roughly 360 MB (358 MB measured 2026-10-30)
plus the source snapshot. Full adds CPU PyTorch and semantic dependencies, roughly
1.5 GB before the separate approximately 1.1 GB model download. Full setup and
inference remain NOT_RUN. The dependency locks target Python 3.12; other OS/CPU
combinations are Unknown. FFmpeg/FFprobe decode media; Node.js is only for mux.

Models need the separately authorized `fetch-models --yes`, or, from another root
that already holds the pinned snapshots, `fetch-models --from <root> --yes`
(hard links or copies, no download, the other root unchanged).

## Older runtimes

`status` reports each root's `lock_conformance`. A root with the pinned engine but
without this launcher's lock record (for example one built by an earlier Studio
route in `~/.framecore-studio/extensions/earshot`) or with drifted packages is
`unlocked_legacy`. Prefer a new locked root plus `fetch-models --from`; running the
old venv needs the user's agreement and `--allow-unlocked`, and each run warns. A
root without real-sound source can get it with `attach-source --yes`. A root whose
engine commit differs from the pin is `unavailable`.

## Use and removal

Ask Toolbox to measure audio, choose effects, render a sound kit or review sync.
Readiness, computed measurements and actual human listening are separate facts.
For a caller's task, `capabilities/earshot/scripts/envelope.py` runs one operation
and writes a validated `framecore-task-result/1`. Pass local recordings and
metadata as documented in the
[source record](../plugins/toolbox/skills/toolbox/references/earshot/source-records.md)
reference. The caller owns sourcing, the master timeline and approvals.

Removing Toolbox removes the launcher. The separate engine, cache and project
files remain; remove a verified runtime root only on request.
