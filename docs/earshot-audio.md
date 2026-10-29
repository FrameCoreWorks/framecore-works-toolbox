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

Light covers local measurement and procedural sound workflows, roughly 200 MB
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
