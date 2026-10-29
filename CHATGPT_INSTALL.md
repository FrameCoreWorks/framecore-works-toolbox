# Install Toolbox in ChatGPT Work

1. Use an authorized GitHub connection to obtain this private repository at one
   resolved full commit. Inspect `plugins/toolbox/`; preserve its identity.
2. Build from the repository root with Python 3.10+:

   ```sh
   python3 scripts/package_plugins.py --plugin toolbox --output-dir ../toolbox-dist
   ```

3. Use the resulting `toolbox-<version>.zip` from code execution with Plugin
   Creator on the user's installation request. Where code execution cannot reach
   the repository, build it from files read as text instead ([Update without a
   ZIP](#update-without-a-zip-owner-decision-2026-10-29)); never ask the user to
   upload a ZIP. The ZIP contains one plugin at its root, including
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

Update: build the update from files read as text ([Update without a ZIP](#update-without-a-zip-owner-decision-2026-10-29)) and update the same saved plugin; rebuilding with `package_plugins.py` stays an option only where code execution can read the whole repository.
Inspect its complete current file inventory first. Updates overlay the existing
release: omitted files survive. For obsolete files actually present in that saved
plugin, supply exact observed paths through `delete_paths`, then read back the
complete inventory and confirm their absence. Preserve unrelated files, identity,
audience and the current release guard. Do not infer deletion from ZIP omission.
Remove: use the host's plugin controls. Catalog removal does not remove separately
installed tools or their data.

## Update without a ZIP (owner decision 2026-10-29)

The update runs on its own: never download a release ZIP, never ask the owner to attach or upload a file. ChatGPT
Work has no network in code execution and its update tool does not take a URL, but it reads repository files as
text through the GitHub connector, so the update is built there:

1. Resolve `main` to one full commit. List `plugins/toolbox/` recursively at that commit through the connector;
   each entry carries its git blob `sha` and `size`. Save the listing as `{"tree": [{"path", "type": "blob",
   "sha", "size"}]}` (NEW). Do the same at the commit that released the saved version (the commit named "Toolbox <version>" in the history) for OLD; without
   it the baseline is unknown and nothing is deleted.
2. Read `scripts/hosted_update.py` at the pinned commit through the connector and save it in code execution (standard library
   only, no network).
3. With the saved plugin's files in code execution:
   `python3 hosted_update.py plan --new NEW.json --old OLD.json --prefix plugins/toolbox --saved SAVED_DIR --out plan.json`.
4. Read every `fetch` path from `plugins/toolbox/<path>` through the connector and save it unchanged under the same
   relative path (a binary file as `<path>.b64` with base64 content).
5. `python3 hosted_update.py pack --new NEW.json --prefix plugins/toolbox --plan plan.json --files FETCHED_DIR --out delta.zip`
   checks every file against its git blob hash and writes `delta.zip` plus `delta.zip.json`. A mismatch stops it
   with the path; read that file again unchanged.
6. Pass `delta.zip` from code execution to the update tool with the plan's `delete_paths` under the current
   release guard (if it cannot take a code-execution file, pass the same verified files as file contents). Merge
   `review` paths by hand. Read back the affected files and confirm the deleted paths are absent.

A first installation follows the same steps without `--old` and `--saved`: the plan then reads every file.

## Earshot Audio

Since Toolbox 1.1.0 Earshot is built into the Toolbox ZIP (`capabilities/earshot/`
and `skills/toolbox/references/earshot/`); there is no separate Earshot package to
build. Updating the saved Toolbox plugin adds it. A saved standalone Earshot Audio
plugin (Work 1.1.0) is a separate identity, retired by owner decision
2026-10-29: once Toolbox 1.1.0 or later is saved and read back, remove it with
its exact observed paths and the current release guard ([retirement
steps](docs/earshot-audio.md#retiring-installed-copies-owner-decision-2026-10-29)). Runtime/model setup remains separate and
existing runtime folders are kept. See [Earshot setup](docs/earshot-audio.md).
