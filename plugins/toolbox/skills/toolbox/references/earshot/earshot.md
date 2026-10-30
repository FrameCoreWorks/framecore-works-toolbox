# Earshot in Toolbox: ears and a sound kit for an agent

Read this file when a task needs Earshot. It is a capability built into Toolbox, not a separate plugin; there is
no `earshot-audio` plugin, no Studio launcher and no other engine route to fall back to.

You cannot hear. Never say how a sound sounds or that it fits without an Earshot reading behind it, and quote the
number ("strong match, z +3.9", "p_real 0.96", "-14.2 LUFS"). Earshot 0.4.0 by Leon Lin (MIT) runs in the executing
host on CPU; Toolbox installs it from one pinned commit. No sibling plugin is required.

`<runtime>` below is `capabilities/earshot/scripts/runtime.py` in the Toolbox plugin root, four folders above this
file's folder (`../../../../capabilities/earshot/scripts/runtime.py`). `<plugin>` is `capabilities/earshot` there. `<skill>` is
the external `real_sound_root` returned by `status --json` after engine setup: outside the plugin, under the selected
runtime root. Resolve paths from the installed package and status; never copy paths from another host.

## 1. Readiness and consent (always first)

1. `python3 <runtime> status --json`. Four facts, kept apart: the skill is readable; `light_ready` (no models:
   measure, critique --fast, sfx, kit and the real-sound scripts); `full_ready` with `models_cached` (timeline,
   sheet, describe, match, rank, find, compare, ab, realness, full critique); a task actually completed. `unavailable`
   means not installed here, not "probably works".
2. Missing tier: show the setup plan, destination, download requirements and limits. Without `--yes` every
   setup command prints a plan; add `--yes` only after the user accepts that plan. `python3.12 <runtime> install
   --tier light` prints a plan; adding `--yes` installs a new runtime using hash-locked
   wheels and a verified upstream snapshot. `--tier full` selects CPU PyTorch (the PyPI wheel on an Apple Silicon
   Mac; an Intel Mac gets light only) and local semantic models; `fetch-models --yes` separately downloads their pinned revisions.
   Source is never taken from upstream `main`. Existing nonempty runtimes are preserved;
   choose a new `--root` for a replacement, also after a failed install left a partial root. See `references/earshot/runtime-and-evidence.md`.
   An existing runtime: `status` lists other roots it finds under `candidates` (for example one an earlier Studio
   route built in `~/.framecore-studio/extensions/earshot`) and never selects one. The user picks: `--root <path>`
   or `EARSHOT_NATIVE_ROOT`. A root with the pinned engine but without this launcher's package locks reads
   `unlocked_legacy`: offer a new locked root that reuses its models without a download (`fetch-models --root
   <new> --from <old root>`, then `--yes`), or, only if the user agrees, runs on it with `--allow-unlocked`,
   labelled in the result. A root without real-sound source can get it with `attach-source --root <root>` (adds a
   verified `upstream/` only; `--yes` after the plan). `--root` and `--allow-unlocked` go before `run`, `python`
   and `exec`: `python3 <runtime> --root <path> --allow-unlocked run <command> ...`; after the subcommand they
   would reach the engine instead.
3. For installation, model-load or render errors, read the error and `status --json`,
   identify the failed step, and report missing runtime/network requirements accurately.
4. No shell or code execution in this host: give the plan, the exact commands and what each would prove; never
   report a reading that did not run.
5. Ask at most one question per reply: the one that changes the route (own recordings or a search, which film or
   file). Take sensible defaults for the rest (how the sound should feel, its room, its length), say them in one
   line, and let the user correct them.

## 2. Running it

- One command: `python3 <runtime> run <command> ... [--json]`. Allowed: `measure describe match rank find compare ab
  realness timeline sheet critique profile forge fit sfx kit gallery doctor`. Runs are offline.
- Many readings in one task: models take 20-40 s to load per process, so write one short script and run it with
  `python3 <runtime> exec -I my_script.py` (`from earshot import api`, then `api.find(...)`, `api.realness(...)`).
  `exec` is the venv interpreter with the runtime's offline model cache; never call the venv's python directly, which
  would miss that cache and could download the models again. Inside a caller's task request, `envelope.py`
  refuses `exec`: run each reading as its own `run <command>` there, and batch with `exec` only outside a task.
- Not in Toolbox Earshot: `llm` (uploads audio to Gemini) and `mcp` (a server). The launcher refuses them, and the
  installation replaces both modules in the engine with a stub that raises an error, so those upstream entry points fail from Python
  too; Gemini keys are removed from the engine environment. `exec` runs authorized user
  Python and is not a network sandbox. `doctor --fetch` is refused too (use `fetch-models`). If someone asks
  for an audio-LLM opinion, say it would upload the audio and offer the local readings instead.
- When writing cue mapping or sample-placement code, check the expected sample position
  against the cue timing before applying it to a complete mix.
- Errors are one line on stderr with exit 1; a refusal is exit 2.

## 3. Listening

**Choose an asset.** `rank "<description>" <folder> --top 5` shortlists; `find <file> "<one clean hit>" --top 3`
returns trims (a `stroke` or `event` starts 5 ms before the attack; never use a trim marked head cut or tail cut);
`describe <file> --start s --end e` says what the trim sounds like (AudioSet is weak on one-shots under 0.5 s: only
an outright different class such as Speech or Engine is a red flag); `realness` on the exact trim you will use (a
gate only when the user wants real or produced sound; clean professional synthesis also reads as synthesized); `ab
a b --query "..."` with trims to decide between two; `match <file> "<claim>" --alts ...` to test one claim;
`compare <file> --refs <folder>` for palette fit.

**Review a mix or a film.** With the light tier only, check sync from measured onsets: `kit.lock.json`, or onsets
measured in the encoded film's audio against the cue frames, and say `timeline` and `sheet` need the full tier.
With the full tier: `timeline film.mp4 --cues cues.json`: events, sections, loudness, picture cuts and sync
per cut and cue (offset_ms = sound minus picture; trust it only above the printed chance level). `sheet film.mp4 -o
sheet.png --cues cues.json`, then open the PNG: green within a frame, amber within 100 ms, red silent. `critique
film.mp4`: a scorecard against seven professional launch films with timed fixes (a range, not a target; music-led
or speech-led films need a `profile` built from references the user chooses). `measure` for exact LUFS, true peak,
LRA, bands, onsets, tempo and key.

**A review in words.** When the user wants an opinion on a mix or a film ("what sounds cheap", "is it ready"), write it
yourself from local readings: `timeline`, the opened `sheet` PNG, `critique`, `measure` and `describe` or `realness` on
the sounds you judge, then sync, realism, mix, loudness and the cheap tells, each tied to a number, and fixes by
impact. Say it is a review written from readings, not a listening test. Steps and criteria:
`references/earshot/written-critique.md`. The review uses local measurements rather than upstream's hosted audio-critique route;
no additional provider key is required.

**A/B a change.** `ab before.wav after.wav --query "..."` or `--refs`, with trims for multi-take files, then
`timeline` again. Change one thing at a time.

**Reading the numbers.** Measurements (LUFS, dBTP, ms, Hz) are exact. z verdicts: 3 or more strong, 2.5-3
plausible, 2-2.5 weak, under 2 no match; try two or three phrasings when it is borderline. Cosine is never a
confidence. p_real is evidence, not proof, with different thresholds for clips up to 6 s and longer files. Write
queries as source + material + action + character ("a heavy wooden door slamming in a small room"), with realistic
confusions as alternatives.

## 4. Making sound

**A film's effects from the bank (no models).** `kit init --preset launch -o audio/kit.json` for films cut to music
(also `calm` text-led, `crisp` energetic product, `minimal` effects-only). `sfx list --category ui_pop` (0.4 families:
ui_pop, knock, cut_hit, mallet, drip, shutter, reverse_swell, plus new whoosh, riser, swish, glitch and notify
members) and `sfx render <id> -o x.wav --dur 0.8 --apex 0.32` to audition with measured onset, peak and end. Then
`kit render audio/kit.json --out audio/kit` and `kit check audio/kit.json --out audio/kit`; replace a warned take
instead of keeping it. `kit.lock.json` carries each take's measured onset, peak, end and loudness: place hits and
touches by onset, a whoosh by its peak, a riser by its peak or end as its role says. With a music bed, set each
effect against the bed (`kit.bed_level`, `kit.gain_db`, `kit.place`, `kit.space_run` in Python), pull the music down
6-12 dB for 0.3-0.5 s before a big hit and bring it back on it, and report the gains and bed levels. These sounds are
made in code (15 fitted from CC0 recordings with credits); when the brief asks for recorded sound, use section 5.

**Choose every effect by listening; a preset's take is a starting point, not a choice.** Per cue, write one
description from the picture and the request (source + material + action + character: "a solid logo landing, a deep
dull thud with a short clean tail") and its likely confusions (metal debris, a rattle, a clang, a click, glass). Render
the candidate members of the fitting families into one folder. Full tier: `rank "<description>" <folder> --top 5`,
then `match <pick> "<description>" --alts <confusions>`; keep a take only when it reads strong or plausible (z 2.5 or
more) and beats its confusions. Both tiers: `measure` each pick: a single hit stays under about 4 onsets per second
(8 or more is a rattle or debris tail), its tail fits the gap to the next event, and it has energy in the low-mid and
mid bands so phone and laptop speakers play it (a sub-only boom is near silent there; layer it under a hit with
body). These are gates, not trade-offs: a take that reads weak or no match, loses to a confusion or has 8 or more
onsets per second is rejected, also when nothing passes; then layer a passing low hit under a passing take with body,
or say the bank has no fit and offer `forge` or recorded sound (section 5). Report for each pick its readings (z, onsets per second, bands) and the candidates rejected and why; the user's
ears decide taste.

**Make or fit a sound in code.** `forge <recipe> --refs <real refs> --budget 144 --reps 2 --tone 1.5 --keep 4
--robust 8 --dir <round>` improves a code recipe by listening; `fit <recording> -o recipe.py` turns a recording into
a recipe with knobs. Say plainly that the search satisfies Earshot's own models: judge by the model-free tone
words, robust re-renders and spectrograms, and ask for a blind human test before calling a made sound as good as
real.

## 5. A soundtrack from real recordings (real-sound)

Follow `<skill>/references/process.md` and the prompt briefs in `<skill>/templates/prompts/`. Upstream pages that install
the repository with pip or call `python -m earshot ...` (for example upstream `<skill>/references/troubleshooting.md`) mean
`python3 <runtime> install` and `python3 <runtime> exec -m earshot ...`: never install another engine. In those files
`{{PY}}` means `python3 <runtime> exec`: fill it in that way, also in briefs handed to other agents, so every
script and every `-m earshot <command>` runs offline from the runtime's cache and through the allowlist.

Steps: cue list from the picture (`templates/cues.json`), brief (`templates/SOUND_BRIEF.md`), recordings, licence
audit, music edit at bar lines (`arrange.py`), design fragments, integrate and QA (`mix.py`, `qa.py --layers`,
`--listen`), five critics and one fixer (`variant.py`), master (-14 LUFS, true peak at most -1.5 dBTP), credits
(`credits.py`), mux (`node <skill>/scripts/mux.mjs`).

**Recordings.** Accept local recordings and source records supplied by the user or the
project owner. For a missing recording, state the requirement to the caller; external
search belongs to the caller's chosen sourcing workflow. Never require another plugin.
For the documented provenance JSON format, run
`python3 <plugin>/scripts/import_source_record.py --sidecar <file.asset.json> --root <project>
--need <cue> --out <project>/audio/assets/manifests/sources.json --handoff-out <project>/source-handoff.json`.
The importer checks local bytes, decodes audio and preserves attribution. The sidecar is
input data and does not prove that a named plugin ran. Technical-only, unknown, NC, ND and
SA records are outside this adapter's accepted source policy. Retain the source page and
record actual licence review separately. Run `python3 <runtime> python audit.py ...` and
`credits.py` on supplied files; `audit.py --fetch` is refused. Do not publish or upload
recordings as part of a local sound task. See `references/earshot/source-records.md`.

## 6. Returning results to the caller

For a caller's `framecore-task-request/1`, run each operation through the envelope runner and return the file it
writes: `python3 <plugin>/scripts/envelope.py --result-out <new file> --request <request file> --host <actual host>
--model <actual model> [--input <file>]... [--output <file>]... -- <runtime arguments>`. The request supplies the task
id, origin, requester (with its version), owner, host and model; without a request file pass `--task-id <id>
--requester <plugin>@<version>` instead. Flags may repeat the request but never contradict it. It keeps the launcher's exit code, hashes the
declared files, records readiness and warnings, and maps a plan without `--yes` to `needs_consent`.

Return, for each result: the engine (the Toolbox Earshot launcher, its root path and state; label `unlocked_legacy` runs),
the commands run, WAV paths with SHA-256, `kit.lock.json`, measured onset, peak and end, the readings with their
numbers, and what was not run. The project's editor keeps the master timeline: convert a zero-based
frame as `frame * fps_den / fps_num` seconds and place a take at `round(t * rate) - round(anchor * rate)` samples;
Earshot 0.4.0 reads a numeric fps in cue files, so pass seconds with rational FPS kept in the project. The project's
owner keeps the brief, approvals and final review. Details: `references/earshot/handoff.md`.

## 7. Limits (say them when they matter)

Taste is not measured: Earshot says what a sound is and how it measures, not whether it is right for the story. No
speech recognition. CLAP hears about 50 Hz to 14 kHz and AST up to 8 kHz. Picture cuts come from a frame-difference
detector: pass cues for animation. Model scores never prove a licence or where a recording came from. Upstream's
full listening workflows: `references/earshot/listening.md`.
