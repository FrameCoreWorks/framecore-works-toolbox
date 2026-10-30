# Install Toolbox in ChatGPT Work

1. Use an authorized GitHub connection to obtain this public repository at one
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
6. Stop after the readback. Installing Toolbox installs the catalog and its
   built-in Earshot launcher only. Do not inspect, download, convert or adapt
   the third-party catalog entries for Work: most are Claude plugins with no
   reviewed Work package, and Toolbox never rebuilds upstream code. List them
   as Claude-only when asked.

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
file. What ChatGPT Work's tools allow (attempts of 2026-10-30): Plugin Creator's `create_plugin` and `update_plugin`
take only `archive`, an absolute path to a ZIP in code execution (a data URL is refused with `INVALID_ARGUMENT`);
code execution has no network (github.com does not resolve); the GitHub connector returns file text to the model
but writes no file into code execution. So the model itself writes each file's text into code execution, checks
it against the git blob hashes and zips it there:

1. Resolve `main` to one full commit. List `plugins/toolbox/` recursively at that commit through the connector; each
   entry carries its git blob `sha` and `size` (NEW). Search Plugin Creator's saved plugins for FrameCore Works
   Toolbox: none means a first installation; otherwise this is an update of that identity (list the commit that released the saved
   version, the commit named "Toolbox <version>" in the history, as OLD).
2. Choose the files: a first installation takes every file; an update takes every path whose NEW hash differs from
   OLD or that is new, deletes the paths in OLD but not in NEW, and merges any private edit by hand.
   Without network in code execution leave out `capabilities/earshot/requirements/light.txt` and `full.txt`
   (230 KB of hash locks; 29 files and 150 KB remain):
   the Earshot engine cannot be installed there anyway, and its launcher then reports the missing locks instead of
   installing. A later update from a host with network adds them.
3. Read each chosen file through the connector and write its exact text in code execution under
   `/mnt/data/toolbox/<path>` (`pathlib.Path(...).write_text(text, encoding='utf-8')`; for a long file several
   cells that append in order). Keep every character, including the final newline. Write
   `/mnt/data/expect.json` as {path: git blob sha} for the chosen files, copied from NEW.
4. Check and zip in one cell; it writes the ZIP only when every file matches:

   ```python
   import hashlib,json,pathlib,zipfile
   R=pathlib.Path('/mnt/data/toolbox');E=json.load(open('/mnt/data/expect.json'))
   bad=[p for p,h in E.items() if not (R/p).is_file() or hashlib.sha1(b'blob %d\0'%len(d:=(R/p).read_bytes())+d).hexdigest()!=h]
   print('BAD',bad) if bad else print('OK',len(E))
   if not bad:
       with zipfile.ZipFile('/mnt/data/toolbox.zip','w',zipfile.ZIP_DEFLATED) as z:[z.write(R/p,p) for p in sorted(E)]
   ```

   For each path in `BAD`, read the file again from the connector and rewrite it unchanged; never patch it by guess.
5. First installation: `create_plugin(archive="/mnt/data/toolbox.zip")`. Update: `update_plugin` with the same
   archive, the delete paths and the current release guard; an update overlays the saved release, so a ZIP of only
   the changed files is enough. Read back the saved manifests and skill, and report save and checks separately.

Where code execution can read the whole repository (a host with network), the repository's own package script, or
`hosted_update.py plan` and `pack`, build the same archive directly.

## Earshot Audio

Since Toolbox 1.1.0 Earshot is built into the Toolbox ZIP (`capabilities/earshot/`
and `skills/toolbox/references/earshot/`); there is no separate Earshot package to
build. Updating the saved Toolbox plugin adds it. A saved standalone Earshot Audio
plugin (Work 1.1.0) is a separate identity, retired by owner decision
2026-10-29: once Toolbox 1.1.0 or later is saved and read back, remove it with
its exact observed paths and the current release guard ([retirement
steps](docs/earshot-audio.md#retiring-installed-copies-owner-decision-2026-10-29)). Runtime/model setup remains separate and
existing runtime folders are kept. See [Earshot setup](docs/earshot-audio.md).
