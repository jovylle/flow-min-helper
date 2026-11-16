# Project Context — flow-min-helper

Last updated: 2026-11-16. Current version: 0.10.0.

## What this repository does

Flow Min Helper is a pair of ChatGPT Project instruction files. They turn a story summary into ChatGPT image prompts (one or two per clip) and Google Flow video prompts. The repository contains no code. The Project has no runtime connection to this repository.

## Project files

- `general-story-helper.md` is the general-story instruction file, copied into a ChatGPT Project's Custom Instructions (or attached as a project file). It is the whole product.
- `mukbang-story-helper.md` is the silent mukbang instruction file, for a separate Project.
- `README.md` explains setup and the manual review checklist; `docs/decisions.md` records durable decisions and their history.

## Product rules

- The Project never chooses a random story or clip count. With no idea, it asks for a one-line story idea (2026-11-16).
- A supplied idea without an explicit count defaults to two clips. `clips N` means 1–5; `single` means one.
- Clip 1 image prompts specify portrait 9:16 unless the user requests another aspect ratio.
- Each clip has its own image block: one image by default, or a START and END pair with `images 2` (miniature-build defaults to 2). Clip 1's image is the master look; later clips match it and show their start state (end state too in two-image mode). Each video names its own image(s), max two per clip (2026-11-16).
- Extend is opt-in, uses Omni 1.2 Flash, and needs no new image unless `images 2`; it can optionally use an accepted image ingredient, per the user's Flow update; check the current UI.
- Prompts preserve the supplied story and accepted image; do not invent people, props, locations, dialogue, or story events.
- Mukbang prompts visibly dip applicable foods before biting when a dipping sauce is supplied; the first image starts at the dip when necessary.
- Mukbang prompts allow exactly one bite per clip (closed-mouth chewing, one swallow) with tightened audio; Clips 2+ state food 1's single bite (2026-11-16).
- Optional categories (`category: miniature-build|macro-nature|cebu-rain` in the Project) are style presets only; miniature-build sets two images per clip by default (2026-11-16). Without one, nothing changes; they are never chosen at random (2026-11-16).
- The Project never asks for a Flow account route. Links are `https://flow.google.com/?prompt=…` with no `/u/N/` segment, so the browser's signed-in account decides. A supplied idea defaults to two clips and each video prompt gets its own link.

## Validation status

- The manual Project checklist is in `README.md`.
- Output in a real ChatGPT Project and video generation in Google Flow have not been manually verified.
- Flow compatibility and credit notes in `general-story-helper.md` were checked on 2026-11-02 and may change; the active Flow UI takes precedence.

## History

See `docs/decisions.md` for the dated record, including earlier decisions that later changes superseded.
