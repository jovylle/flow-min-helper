# Project Context — flow-min-helper

Last updated: 2026-11-04. Current version: 0.9.3.

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
- Clip 2+ use the accepted Clip 1 image as ingredient/reference by default. Extend is opt-in.
- Prompts preserve the supplied story and accepted image; do not invent people, props, locations, dialogue, or story events.
- The Project asks for a Flow route from 0 to 9 at the start of a new chat unless the user already supplied one. It defaults to two clips for a supplied idea and includes a separate Flow link for each video prompt.

## Validation status

- The current CLI and Project self-checks are documented in `README.md`.
- Output in a real ChatGPT Project and video generation in Google Flow have not been manually verified.
- Flow compatibility and credit notes in `chatgpt-instructions.md` were checked on 2026-11-02 and may change; the active Flow UI takes precedence.

## History

See `docs/decisions.md` for the dated record, including earlier decisions that later changes superseded.
