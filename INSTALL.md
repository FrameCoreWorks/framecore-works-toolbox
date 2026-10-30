# Install FrameCore Works Toolbox

The repository is both a Claude marketplace and the source of the independently
installable `toolbox` catalog plugin. The same local plugin directory supplies
all three hosts; adding the catalog does not install its listed tools.

| Host | Route | Installed component |
| --- | --- | --- |
| Claude apps / Claude Code | [Claude installation](docs/install.md) | Marketplace plus selected individual plugins |
| ChatGPT Work | [ChatGPT installation](CHATGPT_INSTALL.md) | One private portable `toolbox` package through Plugin Creator |
| Codex | [Codex installation](CODEX_INSTALL.md) | Local plugin where supported, or one native entry backed by the complete catalog bundle |

This GitHub repository is public; no GitHub sign-in is needed to read it.
Source access is separate from host installation.
Each third-party entry needs its own host compatibility review; Claude hooks,
commands and MCP configurations are not automatically portable.

See [architecture](docs/architecture.md) for manifests and package boundaries,
and [verification](docs/verification.md) for observed versus untested behavior.
