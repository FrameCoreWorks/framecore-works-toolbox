# Review: opencreator

## Entry

- Name: opencreator
- Status: rejected
- Upstream: https://github.com/krillinai/OpenCreator
- Author: krillinai
- License: Apache-2.0 (code); its 108 prompt templates carry no licence
- Pin: f4dbed139ac80a8d12952b64c9b6def59e42dbcc
- Upstream version: 3.2.8
- Kind: app
- Eligibility: app note: not a plugin; listed in plugins/toolbox/apps.json with manual install steps, never installed from the marketplace
- Source: none (manual install)
- Reviewed on: 2026-10-29
- Reviewer: Claude (cloud orchestration thread), carrying over the Creative Studio registry review at the same pin
- Owner approval: "yes" from Kamil on 2026-10-29 (decision card "Przenieść wszystko do Toolboxa", then "decyzje są już podjęte" accepting the move list)

## What it is

A local desktop workspace around Codex CLI for creators: video translation with subtitles and dubbing (123 source languages), public video download, thumbnails, images, video and voice-overs through the user's model providers, scripts and stick-figure animations.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, video translation and dubbing outside Studio | Multi-language subtitles and dubbing Studio does not do itself | Installers hashed; app NOT_RUN |

Moved from Creative Studio's recommended-extension registry to Toolbox by owner decision 2026-10-29.

## Install (manual)

Download OpenCreator 3.2.8 from https://github.com/krillinai/OpenCreator/releases/tag/v3.2.8 and check its SHA-256 (mac-arm64.dmg 819849ba9389318ee3f4b2cde0464f1ff9f075618c32182f23233f48d91142ac; mac-x64.dmg a03817236e89cfe7213f452b25ea8fa96d87e0e1ea5ff858e4064f2735d7205e; win-x64.exe d03acd7d34501b1ee19c68feb5b29d2ad6c6bcd420ed586e81fc2193e6a2e88d). The Windows installer is unsigned. On first launch choose a Codex sign-in or a provider you trust.

## Network traffic

Rejected by the reject gate (default telemetry): `apps/desktop/src/main/telemetry.ts:7` reports usage to `https://admin.clawee.work/api/v1/public/desktop-usage` and `settings-store.ts:14` sets `telemetryEnabled: true`, so it is opt-out. Found by the Toolbox code review on 2026-10-29; the earlier Studio review missed it.

## Rights

Downloading other people's videos depends on each platform's terms and copyright. Its 108 templates have no licence: do not copy them. Check the stick-figure cast's terms before commercial reuse.

## Evidence

2026-10-20 (Studio review): repository read at v3.2.8, installers downloaded and hashed. The app was not installed or run: NOT_RUN.

## Verdict

reject: default telemetry (CLAUDE.md reject gate). Not listed in Toolbox; the owner may decide on an explicit exception.

## History

- 2026-10-29: proposed as an app note when moving Creative Studio's recommended extensions; rejected the same day for default telemetry, not listed.
