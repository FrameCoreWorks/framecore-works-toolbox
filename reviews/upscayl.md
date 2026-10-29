# Review: upscayl

## Entry

- Name: upscayl
- Status: rejected
- Upstream: https://github.com/upscayl/upscayl
- Author: Upscayl team
- License: AGPL-3.0 (app); models have their own licences
- Pin: 4f39acfc6f88260d105920a64deff8431d5e1544
- Upstream version: 2.15.0
- Kind: app
- Eligibility: app note: not a plugin; listed in plugins/toolbox/apps.json with manual install steps, never installed from the marketplace
- Source: none (manual install)
- Reviewed on: 2026-10-29
- Reviewer: Claude (cloud orchestration thread), carrying over the Creative Studio registry review at the same pin
- Owner approval: "yes" from Kamil on 2026-10-29 (decision card "Przenieść wszystko do Toolboxa", then "decyzje są już podjęte" accepting the move list)

## What it is

A free desktop app that enlarges images two to four times with Real-ESRGAN models on a Vulkan graphics card, one image or a folder at a time, for Windows, macOS and Linux.

## Improvement evidence

| Affected FrameCore repository / task | Concrete improvement | Verification and limitations |
| --- | --- | --- |
| Creative Studio, static graphics upscaling rules | Local enlargement with a model safe for paid work | Installers hashed; app NOT_RUN |

Moved from Creative Studio's recommended-extension registry to Toolbox by owner decision 2026-10-29.

## Install (manual)

Download Upscayl 2.15.0 from https://github.com/upscayl/upscayl/releases/tag/v2.15.0 and check its SHA-256 before opening (win.exe 5dd7f58abafae2907fede489324a074cb6959a93c5714f3d0609650ab942ff3c; mac.dmg 0e53c9ee8c1800cb3e2ce0f574e4e1a35a51945e19ff2b93f33928bbd7fd4c5a; linux.AppImage 6459457e589bcb99e779ea442dce608bacda33916b7019a8862b7c6252aa8229; linux.deb ff221fe5b109ebe6b5116ba04c3c69b37a1121cda26b22995ea9346970207ded). Choose High Fidelity (CC BY 4.0) for paid work.

## Network traffic

Rejected by the reject gate (default telemetry): `renderer/components/posthog-provider-wrapper.tsx:15-35` initialises PostHog (`https://us.i.posthog.com`) on every launch and captures `app_launched` with system information; the in-app contribution switch only removes the provider wrapper after `init` has run. Found by the Toolbox code review on 2026-10-29; the earlier Studio review missed it.

## Rights

High Fidelity (HFA2k) CC BY 4.0; UltraSharp, Ultramix Balanced and Remacri CC BY-NC-SA 4.0 (non-commercial); Upscayl Standard, Lite and Digital Art: licence not stated (Unknown).

## Evidence

2026-10-19 (Studio review): repository read at v2.15.0, licences read, the four installers downloaded and hashed. The app was not run (no Vulkan GPU): NOT_RUN.

## Verdict

reject: default telemetry (CLAUDE.md reject gate). Not listed in Toolbox; the owner may decide on an explicit exception.

## History

- 2026-10-29: proposed as an app note when moving Creative Studio's recommended extensions; rejected the same day for default telemetry, not listed.
