# Changes

## Toolbox 1.1.0 — 2026-10-29

- Built into Toolbox; the separate plugin is retired. See the repository CHANGELOG.

## 1.2.0 — 2026-10-28

- Move the FrameCore Works adaptation into Toolbox as an independently
  installable plugin, using the saved Work 1.1.0 wrapper as the source baseline.
- Remove companion-plugin invocation requirements; accept ordinary local inputs
  and return a generic handoff. Creative Studio retains workflow orchestration.
- Keep upstream 0.4.0 pinned; fetch real-sound resources into the external runtime
  instead of bundling upstream code or the historical 0.3 source.
- Lock dependency versions and hashes; preserve nonempty runtime destinations.
- Check exact model snapshot files and reject incomplete tensor containers;
  report inference as unverified until an actual model run occurs.
- Package separately for Claude, ChatGPT Work and Codex.
