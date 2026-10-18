# Veo 3.1 + Google Flow notes for flow-min-helper

Distilled 2026-10-18 from `googleflow-stories` v2.47.0. Source of truth:
`modules/06-model-rules.md`, `08-video-prompt.md`, `08a-shot-composition.md`,
`07-image-workflow.md`, `docs/veo-stress-tests.md`, `docs/memories.md`.

## Plan on 8-second blocks, period

- User's plan: Veo 3.1 Lite shows **8s clips only**. Never plan 4/6/10s.
- **Only Lite performs Extend** (8s clips, both ratios). Fast/Quality: no extend.
  Quality: no ingredients/references either. Video-to-video: unsupported on all three.
- Extend takes **no images** — short continuation delta only (continue framing +
  the one change). A restated standalone script makes Flow build a new video.
- Omni Flash durations are a dated snapshot, not a planning basis.
- Verify against https://support.google.com/flow/answer/16352836 before advising;
  user's live UI beats docs.

## What Veo 3.1 Lite renders (user stress tests 1–5, small-sample, "proven so far")

Reliable: weather transitions in one shot, rain, frequent lightning + exposure
updates, wind on cloth/debris, dust drift, breakage/destruction **appearance**,
dramatic close-up reveal, one simple reaction (stumble, knee bend).
Unreliable, never the visible beat: earthquake/ground motion, **requested camera
shake (entirely absent, not weak)**, multi-step choreography, mid-clip
orientation reversals (stochastic 1/2 fail), unrequested angle drift.
Rules: **spectacle safe, motion not; show the result of a force, never the force;**
one dominant motion per clip + max one strong effect.

## Prompt habits (live-proven)

Camera first (size/angle/movement before action). Spoken lines in quotation
marks. Name ambience + specific effects in the audio line ("ambient only" says
nothing). Negatives as a plain list. One master context block per independently
generated clip (Extend delta carries none — inheritance is the contract).
Teller speaks (12–16 words/8s pace), every victim silent. Never camera shake,
one movement per shot, hold orientation within a clip. Reference images: 1–3
per clip is a ceiling; generate one at a time on demand.

## Images

One shot = one image, never collage/sheet/panels. Scene-only prompts (no
labels, no blueprint, never the answer, never the fingerprint). Mandatory
trailer verbatim at the end of every image prompt. ChatGPT's image tool
composes from the conversation's **concept**, not the scene prompt — proven
4/4 carryover (same kitchen frame across different draws) and POV storyboard
sheets. Mitigations: fresh chat per story, isolated-prompt Generate button
(sends only image prompt text), acceptance gate (reject mismatch, name the
failed item, retry once), Flow fallback with do-not-use line. No photoreal
styles, no real-human-face Tellers in auto draws; victims stay human rendered
in the stylized medium.

## Credit pool

50 daily Flow credits per account × 3 accounts (user + sibling + friend).
Every clip/retake spends pool: prefer 2-clip shapes when tight, no empty wait
clips, cap image retries at 1, prompts-first so text is never held by images.
