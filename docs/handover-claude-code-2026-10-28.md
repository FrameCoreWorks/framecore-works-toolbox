# Claude handover — Toolbox 1.0.3 removal, 2026-10-28

## Owner decision and historical removal record

The owner explicitly authorized complete removal, verification and publication on
main. This bounded decision supersedes the default rule to retain removed reviews
for the following 15 entries only:

- ponytail
- hud
- planning-with-files
- archify
- wondelai-code-craftsmanship
- wondelai-systems-architecture
- notfair
- linkedin-agent
- wondelai-product-strategy
- wondelai-marketing-cro
- wondelai-sales-influence
- wondelai-product-innovation
- wondelai-strategy-growth
- wondelai-team-motivation
- wondelai-metaskills

These names are a removal record, not available tools or recommendations. Do not
restore them from an older handover, cached catalog or default review-retention rule.
The old content remains in Git history.

Baseline: `f68470c03f7268f0926cd5446fd100642aa6eb96`, catalog 1.0.2, 33 entries.
Result: catalog **1.0.3**, **17 tools plus the toolbox index = 18 entries**.
This record is part of the single main commit containing the complete removal.
The completion handover records the resulting commit IDs and publication checks.

## Changed files and execution configuration

- Remove the 15 marketplace objects from `.claude-plugin/marketplace.json`.
- Remove their README rows, catalog skill rows and all dedicated detail sections.
- Delete exactly `docs/<id>.md` and `reviews/<id>.md` for all 15 IDs: 30 files.
  There were no dedicated local wrappers for these IDs.
- Delete `.claude/settings.json`: its only value was
  `env.PONYTAIL_DEFAULT_MODE=lite`. No unrelated setting was present.
- Remove Ponytail-specific instructions and the repo-setting paragraph from
  `CLAUDE.md`. Preserve all five independent workflow bullets under
  “Independent workflow rules”, plus the unrelated maintainer-tool rules.
- No other managed MCP configuration, hook, alias, launcher, dependency, startup
  entry or installation setting for these tools was found in this repository.
  Their upstream hooks/MCP are not local configuration to delete here.
- Bump the three `plugins/toolbox/` manifests and the marketplace index entry
  together to 1.0.3; update current README, ChatGPT ZIP filename and catalog notes.
- Add the owner admission rule to `CLAUDE.md`, README, `docs/toolbox.md` and
  the review template. Add current verification and changelog records.
- Preserve scripts, validators, tests, CI, Earshot package, remaining per-tool
  docs/reviews and the four previously removed reviews byte-for-byte.
- Clarify explicit saved-file deletion and full inventory readback in
  `CHATGPT_INSTALL.md`; omission from an update archive does not delete a file.

No global configuration, existing user installation, service account, credential,
project data, recording, runtime, model or cache was deleted or updated.

## Retained tools and shared sources

All surviving marketplace tool objects are exactly equal to the baseline,
including version, category, full upstream commit, skill lists and settings:

| Category | Retained tools |
| --- | --- |
| Creative (14) | earshot-audio, ffmpeg-skill, animate, motion-designer, logo-design, meta-ads-designer, hallmark, open-design, video-shotcraft, brag, nateherk-design, sepia, blender-agent-skills, wondelai-ux-design |
| Dev tools (2) | antislop, web-quality-skills |
| Marketing (1) | marketing-skills |

The index is the eighteenth entry. Earshot remains its independent wrapper at
1.2.0. This task does not implement the earlier orchestration migration.

`wondelai-ux-design` retains `wondelai/skills` at
`c172996495bed0fcd26896a9416b2093fd7073f0`, version 1.8.0, and all 11 skills.
The shared `design-everyday-things` path remains. Removing other catalog groups
does not alter the upstream repository or certify what an already-installed
client exposes from its cache.

## New standing admission rule

From this decision onward, add or update a tool, asset or repository only when
its concrete improvement to FrameCore repositories is fully demonstrated. General
usefulness, popularity or a speculative promise is insufficient. The review
records the affected repository/task, concrete improvement and verification with
limitations before owner approval. Use the template's table; do not duplicate
parsed Entry keys.

The owner explicitly retained the 17 tools in this task. Their pins and reviews
are not retrospectively invalidated. Further removal requires a separate owner
decision. “Fully demonstrated” is an admission requirement, not a guarantee that
any tool succeeds on every possible input or host.

## Verification of the removal candidate

| Check | Result and scope |
| --- | --- |
| Repository unit tests | PASS, 37 |
| Earshot wrapper tests | PASS, 24, installed media Python 3.12.14 |
| check_marketplace.py | PASS, 18 entries |
| Portable checks | PASS, toolbox 1.0.3 and earshot-audio 1.2.0 |
| Both ZIP builds | PASS, built outside the repository |
| Catalog archive readback | PASS, all six files exactly equal source; all three manifests 1.0.3 |
| Catalog ZIP SHA-256 | `03518f89a31fdb956f4cdd024fd12904a1a0e4aa76c8a57c5df295b536d1ff91` |
| Hidden/ignored worktree and ZIP residue scan | PASS, 82 IDs/aliases/unique source strings/config keys; removed-tool hits allowed only in this historical handover and CHANGELOG |
| Surviving marketplace objects | PASS, all 17 unchanged |
| Deletion and preservation | PASS, 30 dedicated files gone; Earshot, scripts/tests, UX records and four historical removed reviews unchanged |
| Claude marketplace validation | PASS; existing advisory about Earshot README's install example remains non-blocking |
| Isolated Claude marketplace add/install/list | PASS; source folder confirmed, only toolbox 1.0.3 installed in a temporary CLAUDE_CONFIG_DIR |
| Negative installation | PASS: ponytail@framecore-works-toolbox is not found in that verified marketplace |
| Isolated Codex native install/verify | PASS, six files, FILES_VERIFIED; baseline SHA used only as fixture source marker, candidate hashes checked |
| Plan review | APPROVED by Claude CLI 2.1.302, requested/observed claude-opus-5-5; effort high requested |
| Fresh normal-client invocation and all global installations | NOT_RUN |
| Dedicated plugin-dev / pr-review-toolkit agents | NOT_RUN; unavailable on this host. Runner review and fresh inspection are separately recorded |
| Hosted Toolbox update/readback | pending / NOT_RUN; no verified editable Toolbox identity discovered |

Initial environment-only test failures are preserved in the task evidence:
the macOS default temporary path goes through `/var`, a symlink rejected by
the installer; the generic Python version does not match Earshot's 3.12 locks.
The passing runs use a canonical task temporary directory and the existing media
Python. No validator or assertion was weakened. Claude rejects marketplace source
`.` as invalid; `./` successfully resolves the exact source folder.

Final diff inspection, main publication/readback and CI outcomes are recorded
separately in the completion handover. These source checks do not prove client
activation or uninstall tools previously installed elsewhere.

## Already-installed client state — removal context only, NOT_RUN

This is a historical checklist for a separately scoped owner-authorized cleanup,
not an instruction to execute cleanup now. Inspect the actual installation scope
and preserve user data before any later removal.

| Removed component | Possible state to inspect in a later cleanup |
| --- | --- |
| All 15 | Old plugin registrations/cache, including `<id>@framecore-works-toolbox` or account-synced registrations. Catalog removal does not uninstall them |
| ponytail | Hooks; `~/.claude/.ponytail-*`; `~/.claude/ponytail-statusline.*`; a corresponding `statusLine` setting; `~/.config/ponytail/` including `band/` ledger/data; local or cloud `PONYTAIL_DEFAULT_MODE` and other tool-specific settings |
| hud | Its installed registration and configured status-line command; do not remove an unrelated status line |
| planning-with-files | Installed lifecycle hooks and project plan/recovery files; the files may contain valuable user work |
| notfair | Installed remote MCP connection, NotFair account authorization and optional Google credentials; do not revoke accounts or credentials in this task |
| archify, linkedin-agent and removed Wondelai groups | Registrations/cache and project files actually created by their use; do not infer ownership from generic filenames |

The older Studio handover reports that the owner had already uninstalled Ponytail
after contaminated evaluation replies. That is reported historical evidence,
not a fresh audit of every current client. No uninstall, data deletion or account
revocation is performed here. If a later uninstall is requested, use that client's
native controls and verified scope rather than deleting shared caches blindly.

## Studio scope

The companion record is maintained in Creative Studio's current Claude handover,
roadmap and development ledger under `CX-20261028-01`. Its baseline is
`9358ac746ee738f33063c5b210dd186c093a37d6`, including another author's Task 5
reference-file plan, which is preserved.

Only stale Toolbox recommendations and current-status wording are corrected.
No Studio skill, protected path, onboarding, independent integrated capability,
package/version or companion implementation is removed or changed. Historical
Ponytail evaluation/uninstall records and generic graphics HUD/hairstyle matches
remain unchanged. Open Assets is not edited.

## Synchronization and exact ChatGPT Work continuation prompt

Available plugin discovery returned no Toolbox match. A complete USER-scoped
owned-plugin listing returned six other plugins and no next cursor. This does
not establish that a workspace plugin is absent or inaccessible. No verified
editable Toolbox ID was obtained; no plugin was created or substituted.

Use this prompt in ChatGPT Work:

> Update the existing FrameCore Works Toolbox plugin from
> FrameCoreWorks/framecore-works-toolbox main, catalog 1.0.3. Resolve and record
> the exact source commit first, read CLAUDE.md and
> docs/handover-claude-code-2026-10-28.md, and build only plugins/toolbox with
> python3 scripts/package_plugins.py --plugin toolbox --output-dir <temporary-directory-outside-the-repository>.
> Verify every one of the six ZIP members against its source-file SHA-256 at
> that exact commit and the generated .zip.inventory.json receipt; all three
> manifests must be 1.0.3. The archive SHA above identifies the local build.
> A different ZIP compression library may change archive bytes without changing
> member content; per-member equality is authoritative. Use the exact result
> commit from the completion handover when main has advanced.
> Find and verify the existing Toolbox backend plugin ID; do not create a duplicate.
> If no unique editable identity is available, stop and report pending.
> Read its current source and every inventory page, preserve identity, audience
> and unrelated files, and use its current release ID as expected_release_id.
> Inspect for files belonging exclusively to the 15 removed entries named in
> this historical handover. Omit them from the update archive and pass their
> exact observed paths in delete_paths; omission alone is not deletion.
> Update that same plugin, then read back every inventory page, all manifests
> and the catalog skill. Confirm 1.0.3, 17 tool rows, all requested deletions
> absent and retained content preserved. If the saved version or source has
> advanced, reconcile the newer release rather than downgrade or overwrite it.
> Record the saved release ID and separately test a fresh Toolbox invocation.
> Do not update Earshot or other plugins, uninstall global tools or delete user data.

## What Claude should do next

Read this record and the matching Studio/Shared handovers before continuing.
Do not restore the deleted entries or expand the bounded removal. Keep the
prospective admission rule. Complete only the pending saved-plugin synchronization
through its existing identity when that capability becomes available; retain
NOT_RUN for fresh clients until actually tested. Any broader orchestration
migration remains a separate task.

