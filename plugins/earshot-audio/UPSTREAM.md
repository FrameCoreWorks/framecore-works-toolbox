# Earshot upstream and wrapper origin

- Upstream: https://github.com/Leonxlnx/earshot
- Author: Leon Lin
- Version: 0.4.0
- Commit: `591fa3e028032e6dce56620a20e932e35667e8d8`
- Tree: `d6f2dbc43f7b38b2147cfd04bbd7aa9055701f1a`
- License: MIT; upstream copyright retained in LICENSE.

All 282 upstream file hashes were compared with the selected commit on 2026-10-28.
`upstream.json` records those hashes. No engine code, upstream skill text, model
weights or upstream real-sound resources are bundled in this wrapper. Authorized
runtime setup downloads and verifies the source, then keeps it under the chosen
runtime root, outside the plugin and this repository.

FrameCore Works wrapper 1.2.0 is based on its owned ChatGPT Work Earshot Audio
1.1.0 launcher, source-record adapter and workflow instructions. The uploaded
1.0.9 archive was older than that saved source. The previous wrapper's archived
0.3 snapshot and copied 0.4 real-sound files are not carried into Toolbox.

Changes: independent instructions, three host manifests, generic source-record
input, external pinned real-sound resources, exact dependency versions and wheel
hashes, non-destructive runtime setup and honest model-file checks. Upstream
`llm.py` and `mcp_server.py` are replaced with refusal stubs only in the installed
venv; the preserved upstream snapshot stays unchanged. Python `exec` is a user
code route, not an OS/network sandbox.

The owner explicitly requested this adapted distribution in Toolbox on
2026-10-28. This is an authorized exception to the catalog's usual preference
for installing an upstream plugin unchanged. No formal GitHub fork is created.
