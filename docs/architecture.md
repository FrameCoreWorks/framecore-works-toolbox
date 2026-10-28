# One source, three installation routes

Owner request, 2026-10-28: Toolbox must follow Creative Studio's installability
pattern across Claude, ChatGPT Work and Codex. This extends the catalog's host
support while preserving the existing Claude marketplace and reviewed pins.

| Location | Responsibility |
| --- | --- |
| `.claude-plugin/marketplace.json` | Claude catalog of independently selected plugins |
| `plugins/toolbox/plugin.json` | Portable Agent Plugins 1.0 manifest |
| `plugins/toolbox/.codex-plugin/plugin.json` | Codex compatibility metadata |
| `plugins/toolbox/.claude-plugin/plugin.json` | Claude plugin metadata |
| `plugins/toolbox/skills/toolbox/` | Shared catalog and host-aware instructions |
| `scripts/package_plugins.py` | Validate and package one local plugin, without network access |
| `scripts/install_codex.py` | Native Codex catalog entry with a complete local bundle |

All manifests retain the same plugin name, version, description and author.
OpenAI presentation lives under `extensions.com.openai.interface` in the root
manifest and `interface` in its compatibility overlay. Portable skills occupy
`skills/<name>/SKILL.md`; the marketplace is excluded from each plugin ZIP.

The repository, marketplace and installable catalog plugin are separate scopes.
The catalog does not depend on Creative Studio and does not import the listed
plugins. Existing third-party records retain their Claude-specific evidence.
Adding portable metadata to the catalog does not convert those third-party
hooks, runtimes or servers.

## Independent adapters and Studio

Local adapters such as Earshot belong in their own `plugins/<name>/`
directory with all three manifests, their own instructions and a reviewed,
pinned upstream. They can be distributed separately from the same repository.
Keep upstream source outside this repository, as required by its existing rules;
retain attribution and document any adapter changes. Review and test each
adapter's actual supported hosts before registering it.

Adapters receive ordinary input files and metadata and return documented outputs.
They must not require sibling plugins. Creative Studio owns cross-plugin
selection, sequencing and handoff rules; neither Toolbox nor Earshot inherits
that orchestration responsibility. Earshot Audio 1.2.0 is now supplied in `plugins/earshot-audio/`. Its upstream
engine stays at 0.4.0, with external verified source resources and locked setup.
See [its installation notes](earshot-audio.md) and [review](../reviews/earshot-audio.md).

## Open Assets

The independent [Open Assets repository](https://github.com/FrameCoreWorks/framecore-open-assets)
already has this manifest pattern under `plugins/framecore-open-assets/` and
its own root Claude marketplace. Its three manifests were checked against the
saved ChatGPT Work 0.2.1 package on 2026-10-28. No duplicate manifest or plugin
is needed. Sharing an installation pattern does not create a dependency on it.
