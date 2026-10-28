# Install from the toolbox in Claude

For ChatGPT Work or Codex, use the [installation overview](../INSTALL.md).
This page documents the Claude route.

The toolbox includes a Claude plugin marketplace in a private GitHub repo:
`FrameCoreWorks/framecore-works-toolbox`. Add the marketplace once, then add
each plugin you want. Adding the marketplace does not install its plugins.

## Claude apps (claude.ai, desktop, Cowork)

1. Open Customize > Plugins > Add > Add marketplace.
2. Enter `FrameCoreWorks/framecore-works-toolbox`. The repo is private: when
   the dialog asks, connect GitHub and give the Claude GitHub App access to
   this repo.
3. Open the plugin in the list, read what it contains, select Add.
4. The plugin is saved to your account: its skills and commands work in chat,
   Cowork loads skills, commands, agents and hooks, and Claude Code receives it
   as `<name>@synced` at the next session start (`/reload-plugins` to load it
   in a running session).
5. Use: describe the task and Claude loads a matching skill, or type `/` and
   pick `plugin-name:skill-name`.
6. Turn off or remove: open the plugin in Customize > Plugins, use the
   Disable plugin toggle or Remove in its menu.
7. Updates: use Check for updates on the marketplace. Whether claude.ai
   installs the commit pinned in the manifest or the upstream branch is
   Unknown (NOT_RUN); compare the version shown with the README table.

What runs where (Claude docs): skills and commands run in chat, Cowork and
Claude Code; agents and hooks run in Cowork and Claude Code; mods run only in
Claude Code. A plugin with a top-level `bin/` folder is not installed by
claude.ai or Cowork.

## Claude Code CLI

Needs git access to the private repo (for example `gh auth login`).

```bash
claude plugin marketplace add FrameCoreWorks/framecore-works-toolbox
claude plugin install <name>@framecore-works-toolbox
claude plugin list
# after a new commit in the toolbox
claude plugin marketplace update framecore-works-toolbox
claude plugin update <name>@framecore-works-toolbox
# remove
claude plugin uninstall <name>@framecore-works-toolbox
```

Plugins installed this way stay on that machine and are not added to your
claude.ai account. Plugins added in claude.ai arrive in Claude Code as
`@synced` on their own; do not install the same plugin both ways.

Per-plugin setup, options and full removal steps are in `docs/<name>.md`.
