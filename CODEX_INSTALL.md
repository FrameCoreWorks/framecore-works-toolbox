# Install Toolbox in Codex

Obtain this private repository through an authorized GitHub connection at a
resolved full commit. `plugins/toolbox/` is the complete portable package and
also includes `.codex-plugin/plugin.json` for compatible local plugin clients.
Use the actual host's documented local plugin route when available; do not
invent CLI commands or install both routes for the same user/scope.

## Native entry with the complete bundle

The same direct-source pattern used by Creative Studio is available without
requiring a local plugin installer. Python 3.10+ is sufficient. On the user's
installation request, resolve the actual Codex skill scope (`.agents/skills`
for the selected project or `~/.agents/skills` for the user) and a persistent
bundle location outside every skill-discovery root. Inspect active scopes for
an existing `toolbox` skill/plugin first. Preserve existing or edited content.

The assistant substitutes absolute paths and the verified source commit:

```sh
python3 scripts/install_codex.py plan --skills-dir "<skills-dir>" --bundle-dir "<bundle-dir>" --source-commit "<40-character-commit>"
python3 scripts/install_codex.py install --skills-dir "<skills-dir>" --bundle-dir "<bundle-dir>" --source-commit "<40-character-commit>"
python3 scripts/install_codex.py verify --skills-dir "<skills-dir>" --bundle-dir "<bundle-dir>" --source-commit "<40-character-commit>"
```

The helper makes no network requests. It copies the entire catalog package,
creates one native `toolbox` entry pointing to the bundled skill, and records
file hashes and source commit. `plan` writes nothing. Existing conflicting or
partial installations are rejected. Identical repeats are read-only. The helper
checks its selected scope; the assistant checks other scopes and active plugins.

After saved-file verification, refresh the actual Codex skills view or start a
new session and invoke Toolbox. A receipt proves file installation, not host
activation. This fallback exposes the catalog skill, not a hosted plugin UI.

Update: inspect local edits, preserve them, choose a new versioned bundle path
and replace only the previously installed entry under the user's update request.
This helper deliberately does not overwrite an installation. Remove only the
verified `toolbox` entry and its bundle after checking the receipt and local edits.
Third-party plugins and their data are separate installations.

## Earshot Audio

Earshot is built into the Toolbox bundle since 1.1.0; the `toolbox` entry and
its bundle carry it, so there is no separate `--plugin earshot-audio` install.
An older native `earshot-audio` entry can be removed after checking its receipt;
its runtime folder is separate and stays. This installs no engine or model weights.
See [Earshot setup](docs/earshot-audio.md) for the separate runtime plan.
