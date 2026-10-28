# Earshot Audio: install notes

- Upstream: https://github.com/Leonxlnx/earshot (Leon Lin, MIT)
- Pinned commit: `591fa3e028032e6dce56620a20e932e35667e8d8` (engine 0.4.0)
- Wrapper: FrameCore Works 1.2.0; local source `plugins/earshot-audio/`
- Review: [reviews/earshot-audio.md](../reviews/earshot-audio.md)

## Plugin installation

| Host | Route | Verification |
| --- | --- | --- |
| Claude apps / Cowork | Add `earshot-audio` from the Toolbox marketplace | Current UI activation NOT_RUN |
| Claude Code | `claude plugin install earshot-audio@framecore-works-toolbox` | Current CLI unavailable; NOT_RUN |
| ChatGPT Work | Single-plugin ZIP through Plugin Creator, preserving an existing owned identity | Package checked; saved Work deployment NOT_RUN |
| Codex | Complete local plugin, or `install_codex.py --plugin earshot-audio` | Native file installation tested in isolation; client activation NOT_RUN |

From the repository root:

```sh
python3 scripts/package_plugins.py --plugin earshot-audio --output-dir ../earshot-dist
```

The ZIP contains only Earshot's wrapper, manifests and support files. No Studio,
Toolbox catalog, Open Assets, original engine code, real recordings or model weights
are required or bundled. The native Codex helper follows [CODEX_INSTALL.md](../CODEX_INSTALL.md)
with a separate bundle and `--plugin earshot-audio` for plan, install and verify.

## Engine setup after installation

Read the package [README](../plugins/earshot-audio/README.md). Inspect readiness and
the setup plan from the installed package. Only the `--yes` form performs setup:

```sh
python3 <plugin>/scripts/runtime.py status --json
python3.12 <plugin>/scripts/runtime.py install --tier light
python3.12 <plugin>/scripts/runtime.py install --tier light --yes
```

Setup verifies every upstream source file, keeps the original snapshot under the
selected runtime root, installs exact wheel versions with SHA-256 checks and uses
locked build tools. Defaults to `~/.framecore-works/earshot`; choose another root
with `EARSHOT_NATIVE_ROOT` or `--root`. Existing nonempty roots are preserved;
select a new one for replacement or a different tier. Old Studio-named runtime
paths are not required and are not modified automatically.

Light covers local measurement and procedural sound workflows, roughly 200 MB
plus the source snapshot. Full adds CPU PyTorch and semantic dependencies, roughly
1.5 GB total before the separate approximately 1.1 GB model download. Actual sizes
vary by wheel and platform. Full setup and inference remain NOT_RUN. The automatic
dependency locks target Python 3.12; availability on other OS/CPU combinations is
Unknown. FFmpeg/FFprobe are needed for media decode; Node.js is only needed by mux.

Models require the separately authorized `fetch-models --yes`. Normal commands
use pinned model revisions and offline settings. No API key or other plugin is
required. Hosted critique, MCP serving and audit downloads are excluded; arbitrary
Python and code recipes remain trusted-code execution, not a security sandbox.

## Use and removal

Ask Earshot to measure audio, choose effects, render a sound kit or review sync.
Readiness, computed measurements and actual human listening are separate facts.
Pass locally supplied recordings and metadata using the documented generic
[source record](../plugins/earshot-audio/skills/earshot/references/source-records.md).
The caller owns sourcing, the master timeline and approvals.

Remove the plugin with the host's controls (Claude CLI:
`claude plugin uninstall earshot-audio@framecore-works-toolbox`). For native Codex,
inspect its receipt before removing the entry and bundle. The separate engine,
cache and project files remain; remove a verified runtime root only on request.
