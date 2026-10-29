# Install Toolbox in ChatGPT Work

1. Use an authorized GitHub connection to obtain this private repository at one
   resolved full commit. Inspect `plugins/toolbox/`; preserve its identity.
2. Build from the repository root with Python 3.10+:

   ```sh
   python3 scripts/package_plugins.py --plugin toolbox --output-dir ../toolbox-dist
   ```

3. Use the resulting `toolbox-1.0.3.zip` with Plugin Creator on the user's
   installation request. The ZIP contains one plugin at its root, including
   `plugin.json`, both compatibility manifests and all skill resources. Do not
   upload the whole marketplace or combine third-party packages into this ZIP.
4. Before creating, search for an existing owned FrameCore Works Toolbox plugin.
   If found, inspect its current source and update that identity with a current
   release guard. Preserve audience and private settings; avoid duplicates.
5. Inspect the returned component diagnostics and read back the saved manifests
   and `skills/toolbox/SKILL.md`. Verify the catalog skill is actually readable
   in a fresh host invocation before claiming activation.

Ask for "toolbox" or select FrameCore Works Toolbox. The catalog identifies
tools and installation requirements; it does not install all tools it lists.
For third-party entries without a reviewed portable package, ChatGPT Work
compatibility remains Unknown. Local engines need code execution, dependencies
and permitted network access separately from plugin registration.

Update: rebuild from a verified source commit and update the same saved plugin.
Inspect its complete current file inventory first. Updates overlay the existing
release: omitted files survive. For obsolete files actually present in that saved
plugin, supply exact observed paths through `delete_paths`, then read back the
complete inventory and confirm their absence. Preserve unrelated files, identity,
audience and the current release guard. Do not infer deletion from ZIP omission.
Remove: use the host's plugin controls. Catalog removal does not remove separately
installed tools or their data.

## Earshot Audio

Since Toolbox 1.1.0 Earshot is built into the Toolbox ZIP (`capabilities/earshot/`
and `skills/toolbox/references/earshot/`); there is no separate Earshot package to
build. Updating the saved Toolbox plugin adds it. A saved standalone Earshot Audio
plugin (Work 1.1.0) is a separate identity: once Toolbox 1.1.0 is saved and read
back, retire it only on the owner's explicit request, with its exact observed
paths and the current release guard. Runtime/model setup remains separate and
existing runtime folders are kept. See [Earshot setup](docs/earshot-audio.md).
