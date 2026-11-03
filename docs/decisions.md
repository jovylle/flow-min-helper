# Decisions — flow-min-helper

Short ADR-style log. Newest first.

## 2026-11-04 — Use portrait 9:16 for image prompts (0.9.2)

- Context: generated Clip 1 images should fit the intended portrait format.
- Decision: specify portrait 9:16 in every image prompt unless the user explicitly requests another aspect ratio.
- Consequence: both the Project recipe and local CLI output use portrait 9:16 by default.

## 2026-11-04 — Separate mutable workflow from stable Project reference (0.9.2)

- Context: routine Project changes should not require replacing stable reference files.
- Decision: `chatgpt-project-workflow.md` is the frequently updated behavior file; `chatgpt-project-source.md` holds supporting prompt recipes and dated Flow facts; `chatgpt-instructions.md` is the stable Instructions-field text; `helper.py` remains local CLI code.
- Consequence: initial setup attaches both Project source files and saves the Instructions once. Routine workflow updates replace only `chatgpt-project-workflow.md`; update the reference file only when its content changes.

## 2026-11-03 — Ask for route and include links automatically (0.9.2)

- Context: users want to select a Flow route per chat and receive working prompt links without a follow-up request.
- Decision: ask for one route digit from 0–9 at the start of each Project chat unless supplied in the first message; include a full prompt and a separate encoded Flow link for every video prompt in the same reply, refreshing links when prompts change.
- Consequence: a new chat may need one route-selection turn before prompt generation. No route is assumed across chats.

## 2026-11-03 — Per-prompt Google Flow links (0.9.1)

- Context: users want to open a generated video prompt directly in Google Flow and select a Flow route.
- Decision: attach a separately URL-encoded `Open in Google Flow` link to every video prompt. Start at route `/u/6/` from the user's example; allow `Flow user N` for indices 0–9 within the current chat.
- Consequence: links carry prompt text only. The user still selects the model, attaches ingredient images, and starts generation in Flow.
- Status: superseded by the 0.9.2 decision above, which asks for a route at the start of each Project chat.

## 2026-10-19 — Summary is a block above the prompts (0.9.0)

- Context: readers need a fast read before the prompts.
- Decision: `--- STORY SUMMARY ---` after the status block. CLI `--summary` sets it, defaulting to the idea. ChatGPT writes 2-3 plain sentences from the user's story only.
- Consequence: `build()` without `summary=` shows the raw idea, not a model summary. Open decision 1.

## 2026-10-18 — Ingredient clips default, Extend opt-in (0.5.0)

- Context: each clip must match the Clip 1 image, not chain from last frame.
- Decision: every clip after Clip 1 uses the Clip 1 image as ingredient. Extend only with `--extend` or the `extend` command.
- Consequence: continuity relies on the image plus restated text.

## 2026-10-18 — Random choices use Python, never an LLM (AGENTS.md)

- Context: a model cannot pick randomly in a reliable or reproducible way.
- Decision: story pick and clip count come from Python's `random`, via `build()`.
- Consequence: ChatGPT must run the attached `helper.py` (code interpreter) or the user pastes CLI output.

## 2026-10-18 — Master block is pasted verbatim (0.6.0)

- Context: character details drift between clips when rewritten.
- Decision: `--master` text is appended unchanged to every image and video prompt.
- Consequence: no face lock. Voice deferred until spoken lines exist.

## 2026-10-18 — No setting or storm words unless the story has them (0.8.0)

- Context: a hardcoded storm leaked into a pig-farm story.
- Decision: the default lighting and audio are neutral. Storm content lives only in the three storm stories.
- Consequence: the built-in story bank keeps its own storm wording.
