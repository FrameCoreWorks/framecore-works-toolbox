# Handover 2026-11-14: Toolbox 1.15.1 catalog welcome

The owner asked for a fixed, fuller welcome in every FrameCore Works companion plugin, English in the repository and translated by the model, with no link to Creative Studio, and approved the text on 2026-11-14. Open Assets 0.8.3, FrameMotion 0.1.4 and FrameCut 0.1.3 got the same pattern.

- `plugins/toolbox/skills/toolbox/assets/startup-welcome.en.md` holds the welcome; "Reply format" step 1 embeds it between `<!-- welcome:start -->` and `<!-- welcome:end -->` and places the host install line just before its last line, followed by the numbered catalog and the existing closing question.
- `tests/test_welcome.py` keeps the embedded copy byte-identical with the asset. Change both together.
- The skill description is at 1,019 of claude.ai's 1,024 characters; do not lengthen it.

Behaviour in a live client: NOT_RUN.
