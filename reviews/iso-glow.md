# Review: iso-glow

## Entry

- Name: iso-glow
- Status: removed
- Upstream: https://isoglow.dev/
- Author: April Zhu
- License: MIT (built on iso-figure by Tolga Cohce, MIT)
- Pin: sha256:6c88dba1424bada2ee651a1b273095f9a13b82dd9362f9bc873600b5bff6b0a1
- Upstream version: archive iso-glow.zip (2026-10-18)
- Kind: app
- Eligibility: app note: not a plugin; listed in plugins/toolbox/apps.json with manual install steps, never installed from the marketplace
- Source: none (manual install)
- Reviewed on: 2026-10-29
- Reviewer: Claude (cloud orchestration thread), carrying over the Creative Studio registry review at the same pin
- Owner approval: "yes" from Kamil on 2026-10-29 (decision card "Przenieść wszystko do Toolboxa", then "decyzje są już podjęte" accepting the move list)

## What it is

A skill distributed only as an archive from its website (no Git repository): interactive isometric hairline figures where whatever is switched on glows in one accent colour, as single HTML pages, with a three.js 3D mode and a solid Lumen product style.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, isometric glow figures for pages | The original clickable figures next to Studio's video kit | Archive install and remove ran with a temporary HOME; host invocation NOT_RUN |

Moved from Creative Studio's recommended-extension registry to Toolbox by owner decision 2026-10-29.

## Install (manual)

Download https://isoglow.dev/iso-glow.zip, check `shasum -a 256 iso-glow.zip` equals 6c88dba1424bada2ee651a1b273095f9a13b82dd9362f9bc873600b5bff6b0a1 (stop and ask for a new review if it differs), then unzip into `~/.claude/skills` (Claude Code) or `~/.agents/skills` (Codex); in claude.ai upload the folder as a custom skill. Remove by deleting the `iso-glow` folder.

## Network traffic

One HTTPS download on install: the archive from isoglow.dev, checked against the SHA-256 above. 3D pages load three.js from a public CDN.

## Rights

Keep LICENSE with the skill. Pages end with a small "Made with ISO-GLOW" link the user may remove; finished figures belong to the user.

## Evidence

2026-10-18 (Studio review): zip, .skill and tar.gz downloaded; zip and .skill byte-identical; checksum, install, verify and remove ran with a temporary HOME. Install in a real host and invocation NOT_RUN.

## Verdict

accept as an app note: listed for discovery with manual steps; nothing is installed by Toolbox.

## History

- 2026-10-29: added as an app note, moved from Creative Studio's recommended extensions.
- 2026-10-31: removed by owner decision: Toolbox keeps only entries that install without accounts, API keys or separate desktop apps; it is a skill archive installed by hand, and the upstream archive has changed since review (sha256 28725d3b0f47ed0d4e1ec4411f6b0377a91d13960bd3a7a8224516b3a0017a36 seen in the 2026-10-30 Codex retest).
