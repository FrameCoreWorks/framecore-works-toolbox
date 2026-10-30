# Host-aware installation

Use the actual current host. Never infer that a tool is installed because it
appears in this catalog. The catalog plugin is independent of Creative Studio
and all listed tools. It contains no hooks or MCP servers. It does contain the
built-in Earshot launcher: a pinned, standard-library script that installs the
Earshot engine into a separate local runtime folder only after the user agrees
to its printed plan. Installing Toolbox does not install the engine or models.

| Host | Catalog installation | An individual tool |
| --- | --- | --- |
| Claude apps / Cowork | Add the FrameCoreWorks/framecore-works-toolbox marketplace (Customize > Plugins), then add `toolbox` | Add the selected reviewed entry through that marketplace |
| Claude Code | `claude plugin marketplace add FrameCoreWorks/framecore-works-toolbox`, then `claude plugin install toolbox@framecore-works-toolbox` | `claude plugin install <entry>@framecore-works-toolbox`, with its reviewed setup requirements; in a cloud session it lasts only for that container, so also give the claude.ai step above to keep it |
| ChatGPT Work | One portable Toolbox ZIP saved with Plugin Creator | Inspect a reviewed portable package and use its supported save/update route |
| Codex | Complete local package through the observed plugin route, or the repository's native-entry helper | Inspect the tool's own supported plugin/skill route and runtime requirements |

Full guides (the repository is public):
- https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/INSTALL.md
- https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/CHATGPT_INSTALL.md
- https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/CODEX_INSTALL.md

Use the host's actual available tools and the user's installation request as
authorization for the stated scope. Preserve existing installations and resolve
identity before updates. Do not promise that Claude commands, hooks or local
MCP configurations work in ChatGPT Work or Codex. If no reviewed route exists,
report Unknown / NOT_RUN and explain the missing requirement.
Never adapt, convert or repackage a Claude-format entry for ChatGPT Work or
Codex; that is not a route. Saving Toolbox ends the installation: do not go
on to inspect, download or install catalog entries unless the user asks for
specific ones (picking their numbers from the list counts as asking).

For use, select the installed plugin/skill or describe the task in ordinary
language. Claude slash commands apply to Claude. Saving a plugin, installing
an engine and observing a successful task are distinct verification steps.
