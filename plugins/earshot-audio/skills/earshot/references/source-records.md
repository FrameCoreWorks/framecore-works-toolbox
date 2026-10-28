# Local source records

`scripts/import_source_record.py` accepts an audio file and its JSON sidecar.
Any caller can produce this format. It does not require or invoke Open Assets.
The compatibility command `scripts/import_open_assets.py` accepts the same CLI.

Required fields: `technical_test_only: false`, `rights_status: "eligible"`,
`category` (`audio`, `music` or `sfx`), `verification.kind: "audio"`, `provider`,
`id`, `title`, `creator`, `source_page`, `license`, `license_url`, `attribution`,
`selected_variant.url`, absolute `saved_path`, `sha256` and byte count `bytes`.
The local file must remain inside the selected project root and be at most 32 MiB.
The sidecar is at most 1 MiB. FFmpeg/FFprobe must be available for full local decode.

The adapter accepts matching canonical Creative Commons URLs for CC0, PDM and
CC BY 2.0, 2.5, 3.0 or 4.0. Other records are refused by this adapter's policy;
this is not a general legal verdict. Sidecar fields do not establish authenticity,
copyright ownership, actual licence-page review or creative suitability.

The output manifest preserves source identity, attribution and verified byte
hash. Optional `--handoff-out` writes a generic asset record with creative review
`not_reviewed`; `--studio-out` remains a compatibility spelling. No plugin API is
called. Output paths must be new, distinct and outside the plugin package.
