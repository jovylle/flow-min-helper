# Project Context — flow-min-helper

Last updated: 2026-11-10. Current version: 0.9.5.

## What this repository does

Flow Min Helper prepares a story summary, a Clip 1 image prompt, and Google Flow video prompts. It has two separate paths: a ChatGPT Project workflow and a local Python CLI. The Project has no runtime connection to this repository.

## Project files

- `chatgpt-instructions.md` is the single, self-contained file copied into the ChatGPT Project's Custom Instructions (or attached as a project file).
- `helper.py` is the local standard-library CLI. Do not attach or execute it in the ChatGPT Project.
- `README.md` explains setup and usage; `docs/decisions.md` records durable decisions and their history.

## Product rules

- Random story and clip-count choices use Python's `random` module in `helper.py`; the Project never chooses randomly.
- No-idea defaults to a random story and 1–3 clips. For an idea without an explicit count, the CLI also chooses 1–3 clips. `--clips` accepts 1–5; `--single` selects one.
- Clip 1 image prompts specify portrait 9:16 unless the user requests another aspect ratio.
- Clip 2+ use the accepted Clip 1 image as ingredient/reference by default. Extend is opt-in, uses Omni 1.2 Flash, and can optionally use an accepted image ingredient, per the user's Flow update; check the current UI.
- Prompts preserve the supplied story and accepted image; do not invent people, props, locations, dialogue, or story events.
- Mukbang prompts visibly dip applicable foods before biting when a dipping sauce is supplied; the first image starts at the dip when necessary.
- The Project never asks for a Flow account route. Links are `https://flow.google.com/?prompt=…` with no `/u/N/` segment, so the browser's signed-in account decides. A supplied idea defaults to two clips and each video prompt gets its own link.

## Validation status

- The current CLI and Project self-checks are documented in `README.md`.
- Output in a real ChatGPT Project and video generation in Google Flow have not been manually verified.
- Flow compatibility and credit notes in `chatgpt-instructions.md` were checked on 2026-11-02 and may change; the active Flow UI takes precedence.

## History

See `docs/decisions.md` for the dated record, including earlier decisions that later changes superseded.
