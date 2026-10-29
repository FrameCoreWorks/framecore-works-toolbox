# scenario-kinetic-film: app note

- Upstream: https://www.scenario.com/explorations/kinetic-film/
- Pinned: sha256:2217ab5dbd452185a5c3c1509994da46b1ac20d2ebeaa888536244372ce73ebf (version archive scenario-kinetic-film-skill.zip (2026-10-29))
- Review: [reviews/scenario-kinetic-film.md](../reviews/scenario-kinetic-film.md)

Not a plugin: Toolbox lists it so you can find it, and you install it yourself.

## Install

Download the "Skill" archive from the upstream page (https://iieqkinwjorxrzjp.public.blob.vercel-storage.com/explorations/2217ab5dbd452185a5c3c1509994da46b1ac20d2ebeaa888536244372ce73ebf/scenario-kinetic-film-skill.zip?download=1), check `shasum -a 256 scenario-kinetic-film-skill.zip` equals 2217ab5dbd452185a5c3c1509994da46b1ac20d2ebeaa888536244372ce73ebf (stop and ask for a new review if it differs), then unzip into `~/.claude/skills` (Claude Code) or `~/.agents/skills` (Codex). In the film folder install Playwright at an exact version (for example `npm install playwright@<x.y.z>`, not unpinned); the skill also needs Node 18+, ffmpeg and ffprobe, and Python 3 with `numpy` and `opencv-python-headless`. Music, sound effects and pictures come from the Scenario MCP server (`https://mcp.scenario.com`) with a Scenario account. Remove by deleting the `scenario-kinetic-film` folder.

## Use

After installing, ask for a kinetic-type launch film, teaser or trailer ("use the scenario-kinetic-film skill to make a 20 s teaser for my app at 128 BPM"). The skill prices every Scenario generation with a dry run and waits for your go before spending credits.

## Watch out

- No code licence in the archive (only the fonts are SIL OFL): use it as published, do not copy its code into FrameCore repositories.
- Paid: music, sounds and pictures use Scenario credits; prompts go to Scenario.
- Some checks assume macOS (memory probe, VideoToolbox decode check).
- Not a Git repository: the archive pin is a checksum; a changed archive needs a new review.
- Overlaps with `motion-designer` and Creative Studio's Motion Graphics; pick it when you want Scenario-generated music and sound.

## Full removal

Delete the skill folder and any film folders it created; remove the Scenario MCP registration if you added it only for this skill.
