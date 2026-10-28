# Input and output contract

Accept project/revision, requested operation, local input paths and source records,
sample rate, rational `fps_num`/`fps_den`, zero-based cue frames, trims and speed
changes, sound roles, approved palette and acceptance criteria. Obtain only missing
facts that materially affect execution. These are ordinary data; no caller plugin
or orchestration framework is required.

Return the engine version/commit, runtime readiness, commands actually run, output
paths and SHA-256, `kit.lock.json` where produced, measured onset/peak/end, placement
in samples, measurements supporting each choice, and explicit unexecuted checks.
Retain source attribution and hashes; processing creates a new output/hash linked
to its inputs. A verified decode does not imply licence review or creative approval.

For frame `f`, time is `f * fps_den / fps_num`. Place a take at
`round(time * sample_rate) - round(anchor * sample_rate)`, using its measured onset,
peak or end as the requested anchor. Resolve negative starts explicitly. Earshot
0.4.0 cue files use numeric fps; pass seconds when exact rational timing matters.
Verify the encoded output, not only an intermediate WAV. Light-tier sync checks
use measured onsets; semantic timeline checks require the full models.

The caller owns the master timeline, approvals, sourcing route and final review.
Return missing-input requirements rather than invoking another plugin. Preserve
accepted edits and silent deliveries unless the user requests a change.
