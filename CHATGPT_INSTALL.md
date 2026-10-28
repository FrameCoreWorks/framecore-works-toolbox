# Install Toolbox in ChatGPT Work

1. Use an authorized GitHub connection to obtain this private repository at one
   resolved full commit. Inspect `plugins/toolbox/`; preserve its identity.
2. Build from the repository root with Python 3.10+:

   ```sh
   python3 scripts/package_plugins.py --plugin toolbox --output-dir ../toolbox-dist
   ```

3. Use the resulting `toolbox-1.0.2.zip` with Plugin Creator on the user's
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
Remove: use the host's plugin controls. Catalog removal does not remove separately
installed tools or their data.

## Earshot Audio

Build separately with `--plugin earshot-audio`; the output is
`earshot-audio-1.2.0.zip`. On an explicit Work installation/update request, inspect
the existing owned Earshot Audio identity and current release before saving.
Do not create a duplicate or assume a repository update updates the saved Work
plugin. A full migration from Work 1.1.0 must explicitly remove the observed old
vendored-source and copied real-sound paths: omitted files are otherwise retained.
Preserve user overlays, use the current release guard, read back the complete
inventory and confirm the one active Earshot skill. Runtime/model setup remains
separate. See [Earshot setup](docs/earshot-audio.md).
