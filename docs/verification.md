# Portable catalog verification

Date: 2026-10-28. Version: 1.0.0.
GitHub baseline: `e0e023432f7258792ecad07745306ea330e9c400`.
Imported repository tree: `ecaf375b0f5cb5ac7af5f59aca9d4d500c83b455`;
all 77 original files matched their Git blob identities before edits.

| Check | Result | Scope |
| --- | --- | --- |
| Existing marketplace tests | PASS, 29 tests | Existing pins, categories and catalog consistency |
| Distribution tests | PASS, 7 tests | Complete reproducible ZIP, manifest drift, prohibited files, isolated install/verify, repeat and conflict preservation |
| Marketplace check | PASS, 31 entries | No catalog entries added or removed |
| Portable package check | PASS | Three matching manifests and discoverable skills |
| Archive readback | PASS | Exactly one complete plugin; SHA-256 equality with source |
| Codex native file installation | PASS in temporary directories | No user installation or host activation implied |
| Current Claude CLI validation and install | NOT_RUN | Claude CLI unavailable in this environment |
| Fresh Claude, ChatGPT Work and Codex invocation | NOT_RUN | Requires actual host installation/activation |
| Third-party tools on Work / Codex | Unknown | This change does not adapt or execute catalog entries |
| Remote GitHub Actions | NOT_RUN at source preparation | Inspect the workflow for the published commit |

The prior Claude owner/CLI results in `docs/toolbox.md` remain historical evidence
for the older package. They are not tests of the new portable release.
Maintainer plugins listed in `CLAUDE.md` (Superpowers, plugin-dev and review
agents) are not available in this session; direct source review and the checks
above were used. No upstream installers, hooks or tests were executed.

Open Assets already has all three manifests at version 0.2.1. Its GitHub main
was `dcb26ae1f779e034a13442bbb4c50075abc8f6d7`; the saved Work source was read
back and checked during this task. Its package was not changed by this release.

Saving or updating an owned Work plugin is a separate deployment step. This
repository change prepares installation packages and guides; it does not create
an account plugin, install catalog tools or modify Creative Studio.
