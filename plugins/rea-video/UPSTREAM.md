# Upstream

- Repository: https://github.com/JuneYaooo/rea-video (Apache-2.0, NOTICE: Copyright 2026 JuneYaooo)
- Reviewed commit: ab8580e38a1255425b0d3b481866590766932079 (package 0.1.0, 2026-11-13)

This wrapper contains no upstream code or skill text. Its skill is our own: it checks out the
upstream repository at the reviewed commit inside the user's project, after the user's yes,
skipping the sample videos in `docs/cases/`, installs exact package versions (our constraints
list, resolved for Python 3.13) in `rea-video/.venv` with the OCR extra, keeps the tool's
preferences and model downloads in the project, and then follows the upstream method from that
checkout. The upstream plugin is not listed directly because its documented install
(`pip install "rea-video[ocr] @ git+https://github.com/JuneYaooo/rea-video"` or
`scripts/install_skill.sh`) takes the current default branch with open version ranges and links
the skill into `~/.claude`, `~/.codex` and `~/.agents`, and its first run writes to `~/.rea-video`
and `~/.cache/rea-video`.
Review: ../../reviews/rea-video.md
