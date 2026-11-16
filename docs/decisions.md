# Decisions — flow-min-helper

Short ADR-style log. Newest first.

## 2026-11-17 — No music of any kind in any Project (0.10.2)

- Context: the Projects banned "music" in several places, but not melody, song, or rhythmic beats, and the wording varied between files and categories. The owner wants only ambience and sounds the visible things make.
- Decision: audio is ambient-only in both files. Banned: music of any kind, melody, song, singing, humming, score, drum or beat, and any beat or rhythmic pattern built from sounds (no drum-like tapping, no repeating loop). Speech stays opt-in when supplied. Categories may not add music. Mukbang keeps its one-bite sound design, with the bite and chew sounds limited to what the eater does.
- Consequence: rules are restated in each Project's status line, audio rule, negatives, and Extend delta, so they do not depend on another file. Not verified in Flow yet.

## 2026-11-17 — Generate image actions inline per image block (0.10.1)

- Context: the `Generate image` action was specified once, after the whole prompt bundle, so the action was easy to miss or not rendered at all. The user expected one button per clip.
- Decision: each image block in `general-story-helper.md` gets its own `Generate image` action directly beneath it, in the same reply, in clip order. Two-image clips get one under START and one under END. Extend clips without an image block get none.
- Consequence: the action's rendering is up to ChatGPT; the file can only request it. If it still does not render, the fallback is a note under the block and the fenced prompt. `mukbang-story-helper.md` keeps its single after-bundle action until it is updated the same way. Both versions moved to 0.10.1 to keep AGENTS.md's version sync.

## 2026-11-16 — Rename instruction files

- Decision: `chatgpt-instructions.md` is now `general-story-helper.md` and `mukbang-instructions.md` is now `mukbang-story-helper.md`, so each name says which Project it belongs to. Older entries below keep the old names as history.

## 2026-11-16 — Remove the local CLI; the instruction files are the product (0.10.0)

- Context: nothing executed `helper.py`. The ChatGPT Project files were already the only path the user used, and the CLI duplicated their rules (categories, per-clip images, status line) in a second place that had to be kept in sync. Its random story and clip-count picks also conflicted with the rule that the Project never chooses randomly.
- Decision: delete `helper.py` and its self-test. `general-story-helper.md` is the whole product, and `mukbang-story-helper.md` is its separate sibling. With no idea, the Project asks for a one-line story idea and never chooses a random story or clip count. Categories and images-per-clip stay in the instruction files, and the Project no longer points to a local command.
- Consequence: categories and images-per-clip now live only in the instruction files; there is no CLI to check them against. Random story and count selection is gone, so a user who wants a random pick must choose one themselves. Version lines in both instruction files move to 0.10.0 together.
- Status: supersedes the 2026-10-18 random-in-Python decision. Earlier CLI-specific entries are kept as history.

## 2026-11-16 — Per-clip images: one or two per clip (0.9.8)

- Context: all clips reused the Clip 1 image as ingredient. Build-state categories (miniature construction) need each clip to start from the previous clip's end state, which one shared image cannot show. Miniature also has an open conflict from 0.9.7 for this reason.
- Decision: every clip gets its own image block. Default is one image per clip (`--- CLIP k IMAGE (generate in-chat) ---`); `--images 2` gives each clip a START and END image (`(start)` and `(end)`). A category may set the default; `miniature-build` defaults to 2. Clip 1's image stays the master look; later clips match it and show their start state (end state in two-image mode). Built and changed things stay that way. Each clip's video names its own image(s), with at most two images per clip. Extend clips need no new image unless `--images 2`. Output is interleaved per clip (image blocks, then that clip's video). Accepted images are added to Flow per clip, and the one-additional-generation allowance applies per image.
- Consequence: the status line gains `images/clip: N`, so single-clip output is no longer byte-identical to 0.9.7 (the image and video blocks are unchanged). Each image block adds one generation for the user, so a two-image clip costs twice as many image generations. Not verified in ChatGPT or Flow.
- Status: resolves the 0.9.7 miniature open item, since clips 2+ now have their own start image. Mukbang (`mukbang-story-helper.md`) is a separate Project and is not changed.

## 2026-11-16 — Relaxing rain, Cebu province category (cebu-rain, 0.9.8)

- Context: a calm, slow, tropical rain look for quiet scenes was requested. The existing presets (stylized build time-lapse, macro insects) did not fit.
- Decision: add `cebu-rain` as an opt-in preset. Photorealistic calm rain over Cebu provincial scenery, supplied or implied by the story only. Static by default. Steady soft rain audio; thunder only if named. Negatives: no storm surge or flooding, no lightning unless named, no people unless named, no named landmark, town, or business, no text. Default one image per clip.
- Consequence: the scenery pool (nipa or bamboo huts, tin roofs, leaves, fields, hillside road, coast) appears as allowed vocabulary, not as required content. The model may still add detail; check prompts against the story before using them.

## 2026-11-16 — Optional style categories via --category (0.9.7)

- Context: some ideas need a fixed visual style (miniature construction time-lapse, macro insects) that the default stylized-3D and photoreal-humans rules do not fit.
- Decision: add `CATEGORIES` in `helper.py` with two presets, `miniature-build` and `macro-nature`. A category replaces only the style, framing, camera-movement, and audio defaults, and adds its own negatives and rules. Categories are opt-in (`--category KEY` or `category: KEY`) and are never picked at random. Unknown keys fail with an actionable error; `--list-categories` shows the registry.
- Consequence: with no category, output is byte-identical to 0.9.6. The Project documents both presets under `## Optional categories`, and the non-category wording now says "without a category" where it would otherwise conflict. `macro-nature` allows photorealism and has no humans, so the human-style rule does not apply to it.
- Open: `miniature-build` asks that clip k start from clip k-1's built state, but clips 2+ still use the Clip 1 image as ingredient. The two conflict; the text follows the requested rule, so verify in Flow or consider `--extend`.

## 2026-11-16 — Single-bite mukbang choreography and tighter audio (mukbang 0.9.6)

- Context: a second bite in a clip caused Veo glitches: distorted mouths, mismatched bite marks, and food reappearing. The spec gave no bite count, no swallow beat, and vague audio rules.
- Decision: exactly one bite per clip, then 3–4 closed-mouth chews and a swallow, on fixed beat timings. Audio is one bite sound, synced chewing, one swallow, contact sounds only on touch, and quiet room tone, with matching negatives. Clips 2+ state that food 1 has had one bite and stays on its plate, and that the clip starts from the prior clip's ending state.
- Consequence: not verified in Flow. The clip 2+ start state (food 1 still in hand, put down in the first beat) departs from the "food 1 down" wording in the request; check it in Flow before relying on it.

## 2026-11-10 — Dip before biting

- When a dipping sauce is supplied, show the applicable food being dipped before its bite, including later and Extend clips. Start the first image at the dip instead of mid-bite when needed; sauce coatings alone do not imply dipping.

## 2026-11-08 — Omni Extend and image ingredients (0.9.5)

- Context: the user reports Flow Extend now uses Omni 1.2 Flash and accepts an image ingredient.
- Decision: retain opt-in Extend, continue the preceding video, and allow an accepted image ingredient. Honor requested durations in the Project; the CLI keeps its 8-second default. Preserve requested speech and story beats without contradictory audio status.
- Consequence: verify model, ingredient controls, and duration in Flow; this capability report has not been independently verified. Supersedes the earlier Lite-only, no-image Extend guidance.

## 2026-11-06 — No Flow account route in links (0.9.4)

- Context: asking "which Flow user, 0–9" at the start of every Project chat cost a turn and forced the user to know which digit mapped to which Google account. The user's preference is the default of no account at all.
- Decision: links are `https://flow.google.com/?prompt={encoded}` with no `/u/N/` segment; the browser's signed-in account decides. The route question, the `Flow route:` status field, and the awaiting-choice state are removed. A user-named `/u/N/` is honored for that one reply only.
- Consequence: prompts are delivered in the first response with nothing to wait for. Trade-off: with several accounts signed in, the browser default wins, so a link can open a different credit pool than intended; the manual escape hatch is the user typing `Flow user N` or pasting the fenced prompt.
- Status: supersedes the 2026-11-03 route-selection decision.

## 2026-11-04 — Consolidate ChatGPT Project instructions into a single file (0.9.3)

- Context: maintaining separate workflow and reference files complicated copying and updating instructions in ChatGPT Projects. Users prefer managing a single self-contained file even if it spans hundreds or thousands of lines.
- Decision: consolidate all behavior rules, route options, recipes, and Flow reference facts into `chatgpt-instructions.md`, removing `chatgpt-project-workflow.md` and `chatgpt-project-source.md`.
- Consequence: ChatGPT Project configuration requires only copying or uploading one file (`chatgpt-instructions.md`).
- Status: supersedes the earlier 2026-11-04 decision that split mutable workflow from stable reference.

## 2026-11-04 — Use portrait 9:16 for image prompts (0.9.2)

- Context: generated Clip 1 images should fit the intended portrait format.
- Decision: specify portrait 9:16 in every image prompt unless the user explicitly requests another aspect ratio.
- Consequence: both the Project recipe and local CLI output use portrait 9:16 by default.

## 2026-11-04 — Separate mutable workflow from stable Project reference (0.9.2)

- Context: routine Project changes should not require replacing stable reference files.
- Decision: `chatgpt-project-workflow.md` is the frequently updated behavior file; `chatgpt-project-source.md` holds supporting prompt recipes and dated Flow facts; `chatgpt-instructions.md` is the stable Instructions-field text; `helper.py` remains local CLI code.
- Consequence: initial setup attaches both Project source files and saves the Instructions once. Routine workflow updates replace only `chatgpt-project-workflow.md`; update the reference file only when its content changes.
- Status: superseded by the 0.9.3 decision consolidating everything into `chatgpt-instructions.md`.

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
- Consequence: random choices stay in the CLI. The earlier plan to attach and run `helper.py` in ChatGPT was superseded by the 2026-11-04 Project file separation decision.
- Status: superseded by the 2026-11-16 CLI removal decision (random choices are no longer made anywhere; the Project asks for an idea).

## 2026-10-18 — Master block is pasted verbatim (0.6.0)

- Context: character details drift between clips when rewritten.
- Decision: `--master` text is appended unchanged to every image and video prompt.
- Consequence: no face lock. Voice deferred until spoken lines exist.

## 2026-10-18 — No setting or storm words unless the story has them (0.8.0)

- Context: a hardcoded storm leaked into a pig-farm story.
- Decision: the default lighting and audio are neutral. Storm content lives only in the three storm stories.
- Consequence: the built-in story bank keeps its own storm wording.
