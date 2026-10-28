# Changes

## Toolbox catalog 1.0.2 — 2026-10-28

- Add the owner's selected `ffmpeg-skill` entry as a separately installed upstream
  plugin pinned to `1ae1bdf1ca0adbb1606fbca493948b1bbb2f83ff` (2.17.3, MIT).
- Record isolated installer and synthetic runtime evidence alongside per-host
  installation gaps; no FFmpeg engine, speech model or MCP server is installed
  merely by installing this catalog.

## Toolbox catalog 1.0.1 / Earshot Audio 1.2.0 — 2026-10-28

- Add the independently installable FrameCore Works Earshot adapter to the Creative category.
- Preserve the pinned upstream engine, move original source resources outside the repo and lock dependency setup.
- Support the Earshot bundle in the Codex native-entry helper and test it without sibling plugins.
- Keep input/output handoffs generic; cross-plugin orchestration belongs to Creative Studio.

## Toolbox catalog 1.0.0 — 2026-10-28

- Preserve the existing Claude marketplace and all 30 third-party entries.
- Add portable and Codex compatibility manifests to the existing `toolbox`
  plugin; synchronize its Claude manifest and marketplace version.
- Make catalog instructions host-aware and distinguish the catalog's
  portability from each third-party tool's independently verified support.
- Add deterministic single-plugin packaging and a native Codex entry backed
  by the complete bundle, with receipt verification and conflict preservation.
- Add per-host installation guides, distribution tests and CI.
- Keep Studio orchestration and sibling plugins independent of Toolbox.

Earlier unversioned catalog history remains in Git and the per-entry reviews.
