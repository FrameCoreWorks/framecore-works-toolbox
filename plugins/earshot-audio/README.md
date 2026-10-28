# Earshot Audio 1.2.0

Independent FrameCore Works adapter for [Earshot 0.4.0 by Leon Lin](https://github.com/Leonxlnx/earshot).
Measure, choose and synthesize sound, assemble supplied recordings, and return
audio files with cue, source and measurement evidence. See [UPSTREAM.md](UPSTREAM.md).

Install this directory as one plugin: portable `plugin.json`, Codex compatibility
metadata and the Claude manifest all use `earshot-audio` version 1.2.0. Its one
skill is `earshot`. Toolbox distributes it; no other plugin is required.

## Engine setup

Plugin installation and engine setup are separate. Python 3.12, an available
wheel for each locked dependency, and permitted download hosts are needed for
automatic setup. FFmpeg/FFprobe are required for video and decoded source import;
Node.js is needed for the optional upstream `mux.mjs` workflow.

```sh
python3 scripts/runtime.py status --json
python3.12 scripts/runtime.py install --tier light
# After the user approves this plan and destination:
python3.12 scripts/runtime.py install --tier light --yes
```

Default runtime: `~/.framecore-works/earshot`. Override with `EARSHOT_NATIVE_ROOT`
or `--root`. A nonempty target is preserved: use a new root for replacement or
for changing tiers. The old `~/.framecore-studio/extensions/earshot` is not moved
or overwritten. It can be inspected explicitly; the new real-sound resource
layout requires this wrapper's setup in a new root.

For semantic models choose `--tier full` in the install plan, then explicitly
run `fetch-models --yes`. This is a larger, separate setup. No model weights are
included. Locks are resolved for Python 3.12; actual full-tier setup and inference
have not been tested in this release. Other OS/CPU wheel availability is Unknown.

```sh
python3 scripts/runtime.py run measure /absolute/path/sound.wav --json
python3 scripts/runtime.py run sfx list
python3 scripts/runtime.py python audit.py --help
```

`status` gives `real_sound_root`, where the pinned upstream scripts, references
and templates live after setup. The wrapper checks that snapshot before running
a real-sound Python script. The source-record importer works without the engine:

```sh
python3 scripts/import_source_record.py --sidecar /project/sound.asset.json --root /project --need hit --out /project/source-manifest.json --handoff-out /project/source-handoff.json
```

See [source records](skills/earshot/references/source-records.md) and
[output contract](skills/earshot/references/handoff.md). `import_open_assets.py`
is a compatibility command for the same local-data format, not an integration
that discovers, invokes or installs another plugin.

## Boundaries

Normal engine commands use offline model settings. Hosted audio critique (`llm`),
MCP serving and upstream audit downloads are excluded. Arbitrary authorized
Python through `exec` is not sandboxed by this wrapper. Model file checks do not
prove inference; taste and actual listening remain separate from measurements.
Code recipes used by `forge`/`fit` execute code and must come from a trusted project.

Removing the plugin does not remove its external runtime, model cache or project
outputs. Inspect the configured root before deleting any of those separately.
