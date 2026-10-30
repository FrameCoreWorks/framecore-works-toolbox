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

Installation and updates run on their own: never download a release ZIP, never ask the owner to attach or upload a
file. ChatGPT Work has no network in code execution and its update tool takes no URL. It reads repository files as
text through the GitHub connector, but that text cannot be moved into code execution (Work attempt 2026-10-30: 31
of 31 files read, 0 transferred). So the files go from the connector straight to Plugin Creator, and code execution
only checks what was saved:

1. Resolve `main` to one full commit. List `plugins/toolbox/` recursively at that commit through the connector; each
   entry carries its git blob `sha` and `size` (NEW). For an update, list the commit that released the saved version
   too (the commit named "Toolbox <version>" in the history; OLD).
2. Decide the files to write: for a first installation every file; for an update every path whose NEW hash differs
   from OLD or that is new, plus the delete paths (in OLD, not in NEW, present in the saved plugin). A saved file
   that differs from both OLD and NEW is a private edit: merge it, never overwrite it silently.
3. Read each of those files through the connector at the pinned commit and give its exact text to Plugin Creator as
   that path's file content; create the plugin (first installation, after checking no FrameCore Works Toolbox or
   Open Assets identity exists) or update the existing one with the delete paths under the current release guard.
4. Check the saved plugin in code execution: save `scripts/hosted_update.py` there (its text typed in, or read from the saved
   plugin where present), write EXPECT as {path: git blob sha} for the written files from NEW, then run
   `python3 hosted_update.py verify --expect EXPECT.json --saved SAVED_DIR --absent <delete paths>`. A mismatch
   names the path: write that file again from the connector, unchanged. Report save and verification separately.
   Without the script, this prints each saved file's git blob hash to compare with NEW:
   `python3 -c "import hashlib,pathlib,sys;[print(p,hashlib.sha1(b'blob %d\0'%len(d)+d).hexdigest()) for p in sys.argv[1:] for d in [pathlib.Path(p).read_bytes()]]" <paths>`.

Where code execution can read the whole repository (a host with network), `hosted_update.py plan` and `pack` build
the same update as a verified delta ZIP instead.

## Earshot Audio

Since Toolbox 1.1.0 Earshot is built into the Toolbox ZIP (`capabilities/earshot/`
and `skills/toolbox/references/earshot/`); there is no separate Earshot package to
build. Updating the saved Toolbox plugin adds it. A saved standalone Earshot Audio
plugin (Work 1.1.0) is a separate identity, retired by owner decision
2026-10-29: once Toolbox 1.1.0 or later is saved and read back, remove it with
its exact observed paths and the current release guard ([retirement
steps](docs/earshot-audio.md#retiring-installed-copies-owner-decision-2026-10-29)). Runtime/model setup remains separate and
existing runtime folders are kept. See [Earshot setup](docs/earshot-audio.md).
