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
| ChatGPT Work | One portable Toolbox ZIP saved with Plugin Creator | Its own private plugin, saved with Plugin Creator from the upstream's skill files ([below](#chatgpt-work-an-entry-as-a-private-plugin)) |
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
Never adapt or rewrite a Claude-format entry for ChatGPT Work or Codex; the
only packaging route is the one below for ChatGPT Work. Saving Toolbox ends the installation: do not go
on to inspect, download or install catalog entries unless the user asks for
specific ones (picking their numbers from the list counts as asking).

For use, select the installed plugin/skill or describe the task in ordinary
language. Claude slash commands apply to Claude. Saving a plugin, installing
an engine and observing a successful task are distinct verification steps.

## ChatGPT Work: an entry as a private plugin

ChatGPT Work cannot install from a Claude marketplace, so a picked entry is
saved as its own private plugin with Plugin Creator (owner request
2026-10-31). Work has no dependency between plugins: the entry's plugin and
Toolbox are saved and updated separately.

1. **What can come.** Only the upstream's own skill folders (`SKILL.md` and
   the files they use). Claude commands, hooks, MCP servers, agents and
   desktop apps do not run in Work: leave them out and say so in one line.
   An entry with nothing else stays "(Claude only)".
2. **Install, never adapt.** Read the skill files from the upstream at the
   full commit pinned in Toolbox's manifest (never a branch) through the
   GitHub connector, write each one unchanged into code execution, check it
   against its git blob SHA from the GitHub tree, and zip only when every
   file matches (as in Toolbox's "Update without a ZIP"). Do not rewrite,
   translate, shorten or merge the instructions and add no skill text of
   your own. A binary or oversized file that cannot be carried is reported,
   never guessed. Include the upstream `LICENSE`.
3. **Credit the original author.** Plugin name: the upstream's name.
   Manifest `author.name`: the author as the upstream credits them (for
   example `alchaincyf (花叔)`); `homepage` and `repository`: the upstream
   URL; `license`: the upstream licence; `version`: the upstream version, or
   `0.0.0+<short commit>`. The description opens with "By <author> ·
   <licence> · <upstream URL>. Installed unchanged from the FrameCore Works
   Toolbox catalog at <short commit>." Never name the user or FrameCore
   Works as the author; Toolbox is only the catalog that listed it. ChatGPT
   can show the account that saved a private plugin as "By ..." whatever the
   manifest says; then the description carries the real author, and the
   user is told so once.
4. **Programs during work.** Node, ffmpeg, Python packages or a browser the
   entry needs install in the conversation when a task first needs them
   ("Installs during work" in the Toolbox skill); nothing installs at save
   time, and a new conversation installs them again.
5. **Read back** the saved plugin (name, author, licence, version, file
   list) and say that its skill appears in a new conversation. An update is
   the same steps at Toolbox's new pin, through `update_plugin`.
