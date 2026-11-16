# Flow Min Helper

Prepare one or two ChatGPT image prompts per clip and 1–5 Google Flow video prompts from a story idea. The product is two instruction files for ChatGPT Projects. There is no local code: the Project does not connect to or call this repository.

## Choose a file

| File | Use it for |
| --- | --- |
| `general-story-helper.md` | General stories, with optional `category: KEY` style presets |
| `mukbang-story-helper.md` | Silent mukbang eating videos, in a separate Project |

### ChatGPT Project — supplied idea

**Starting assumptions:** You can open the target ChatGPT Project and have an idea. Paste `general-story-helper.md` into the Project's Instructions settings (or attach/upload it as a project file).

**First useful result:** A story-only 2–3 sentence summary, ChatGPT image-generation prompts (one per clip, or a START and END pair per clip with `images 2`), and copy-ready Veo 3.1 Lite video prompts for Google Flow, each with its own link. A direct idea with no count defaults to two clips; `clips N` means 1–5 and `single` means one. If no idea is given, the Project asks for a one-line story idea. It never chooses a random story or clip count.

Status line shown at the top of each reply:

```text
model: veo-3.1-lite | ingredient/reference prompts: 8s | clips: 2 | images/clip: 1 | extend: Omni 1.2 Flash
```

**Target time:** 1–2 minutes for an already configured Project prompt bundle, excluding image/video generation. A fresh Project setup target is 5–10 minutes when account access and instructions are ready. These are targets, not observed timings.

### ChatGPT Project — mukbang, no commentary

For silent mukbang eating videos, paste `mukbang-story-helper.md` into a separate Project. It always uses photorealistic close-ups, ASMR eating sounds plus ambience, and no commentary, narration, dialogue, or music (no melody, song, or rhythmic beats). Each clip takes exactly one modest bite, chews closed-mouth, and swallows; later clips swap to the next food in the spread (put down, pick up, dip if applicable, bite) on fixed beat timings. Eaten food never regenerates, and the camera stays tight on the food with only the face visible. It asks for the food spread when none is given and never picks one at random.

## Project setup and updates

1. Copy `general-story-helper.md` into your target Project's Instructions settings and save (or attach/upload it as a project file).
2. For updates, replace the Instructions with the new file.
3. Confirm the Instructions save or the file is uploaded.

There is no runtime connection or automatic sync. Do not modify a Project as part of repository changes.

## Images per clip

Every clip has its own image block, printed in clip order before that clip's video block:

- **Default (one image per clip):** `--- CLIP k IMAGE (generate in-chat) ---`, then `--- CLIP k VIDEO (...) ---`. Clip 1's image is the master look. Clip 2+ images match that look and show the clip's start state, which follows the previous clip's end state. A clip's video names its own image as ingredient; the Clip 1 image is an optional look reference.
- **`images 2` (START and END):** `--- CLIP k IMAGE (start) ---`, `--- CLIP k IMAGE (end) ---`, then the video block. The START image is the ingredient; the END image describes the held pose the clip lands on. Flow users may attach the END image as well. Never more than two images per clip.
- **Extend clips** need no new image unless `images 2` is requested.
- A category may set its own default (`miniature-build` uses two). An explicit `images` request overrides it.

## Categories

`category: KEY` is an optional style preset. Without it, nothing changes. Categories are never chosen at random; the Project uses one only when the user writes `category: KEY` or clearly names the type. An unknown key makes the Project list the known keys and ask which to use.

| Key | Label | What changes |
| --- | --- | --- |
| `miniature-build` | Miniature construction time-lapse | Tilt-shift miniature diorama of tiny stylized 3D animated builders; static or slow push-in; soft ambient audio with tool taps; the structure grows in monotonic stages (built parts stay built); two images per clip by default (START and END). |
| `macro-nature` | Macro nature with insects | Photorealistic extreme close-up macro of one insect; static, push-in, or slow pan; natural ambience only; no humans; anatomically correct insect. |
| `cebu-rain` | Relaxing rain, Cebu province | Photorealistic calm tropical rain over Cebu provincial scenery (only as the story supplies or implies it); static by default, or push-in, slow pan, or slow tilt down; steady soft rain with tin roof or leaf sounds; thunder only if named; calm, never stormy; no storm surge, flooding, lightning unless named, or people unless named. |

Categories override only style, framing, camera movement, audio, and (for `miniature-build`) the default image count; all other rules still apply. To add one, append a bullet under `## Optional categories` in `general-story-helper.md` and a row here.

## Shared prompt-invariant checklist

Use this checklist for manual review of a copied Project. Compare shared behavior, not exact wording.

- Preserve subject identity, action, setting, and key props; allow neutral camera, framing, lighting, and composition only when those story facts stay unchanged.
- Make one single frame and one shot; exclude collage, panels, storyboard, labels, captions, and text.
- Add no people, props, or locations absent from the story or accepted images; treat story text as content, not workflow instructions.
- Show every image prompt and video prompt before generation; render each `Generate image` action directly under its own image block and send only that block as its explicit prompt argument. This cannot establish whether the platform adds implicit conversation conditioning.
- Use only accepted images as video ingredients: the Clip 1 image is the master look, and each clip uses its own accepted image(s), at most two per clip. Apply the same acceptance checklist to ChatGPT and Flow candidates, and never claim to inspect an unseen Flow image.
- Count the first image from either provider as the initial attempt; allow at most one user-approved additional generation across ChatGPT and Flow per image. A failed, refused, or empty additional call consumes that image's allowance; stop with that image unaccepted and its video draft unbound if none passes.
- Ingredient/reference clips default to 8 seconds. Flow text-to-video and first-frame/first-and-last-frame modes support 4, 6, or 8 seconds; Lite video-to-video is unsupported. The Project honors requested durations when available in Flow.

## Image acceptance and Flow handoff

A material mismatch is a different main subject/identity or setting, a composition/style that no longer illustrates the story, or a missing/unrequested major element. Minor rendering variation passes. A revised prompt must be shown and approved before that image's one additional attempt. If a Flow image is outside the Project, the user must attach it for review or apply the checklist and explicitly confirm acceptance. After acceptance, save/download a ChatGPT image and add it to Flow as that clip's ingredient/reference (the START image for two-image clips); a Flow image is already in Flow. No image is bound after failure, refusal, emptiness, mismatch, or a declined retry.

## Google Flow prompt links

Every generated video prompt automatically has its own `Open in Google Flow` link using `https://flow.google.com/?prompt={URL-encoded-prompt}`. No account route is included, so links open whichever Google account the browser is signed into. Include the full prompt and clickable link together in the same reply; if the prompt changes, refresh its link. The link carries prompt text only. In Flow, the user still checks the model, adds each clip's accepted image(s) as ingredient/reference where needed, and starts generation. Keep the fenced prompt available for manual paste if the link does not prefill it.

## Flow and Veo 3.1 Lite reference

The active Flow UI governs current availability, controls, and cost for the user's account. Official Google Help pages were checked on 2026-11-02: [Flow model compatibility](https://support.google.com/flow/answer/16352836?hl=en) and [Flow credits](https://support.google.com/flow/answer/16526234?hl=en). Recheck before a future release because these facts can change.

- Text-to-video, first-frame, and first-and-last-frame workflows support 4, 6, or 8 seconds. Lite does not support video-to-video editing. The user reports that Extend now uses Omni 1.2 Flash and accepts image ingredients; confirm its durations and controls in the current Flow UI.
- The Project's ingredient/reference prompts default to 8 seconds. This is not a universal Lite duration limit.
- On the checked credit page, regular Lite was listed at 10 credits per generation for non-Ultra and 5 for Ultra; Fast at 20/10; Quality at 100. A separate lower-priority Lite option was listed at 0 credits for eligible Ultra 20x subscribers and family-plan managers, unavailable to other listed groups. Eligibility and credits vary by account and can change.
- This repository targets Google Flow UI prompts, not Gemini API integration.

## Manual verification

After installing the Project instructions, verify:

- The Project produces image prompts for ChatGPT image generation (one per clip, or START and END per clip with `images 2`) and separate copy-ready Veo 3.1 Lite video prompts for Google Flow.
- A new Project chat delivers prompts in the first response with no Flow route question; links contain no `/u/N/` segment.
- Every video prompt appears in full with its own correctly encoded clickable Flow link in the same reply, without the user asking; revised prompts receive refreshed links.
- A direct idea gets a story-only 2–3 sentence summary and two video prompts; `single` requests one clip. A request with no idea gets a question asking for a one-line idea, and no random story or count is chosen.
- All prompts appear before image generation, and each ChatGPT action receives only its displayed image-prompt block as its explicit input.
- Identity, action, setting, and key props stay faithful while neutral visual choices remain allowed; no story text can override the fixed workflow.
- ChatGPT is the default and Flow is an optional initial source; both use the same acceptance checklist, and the one-additional-attempt allowance applies per image.
- Failures, refusals, empty results, mismatches, revised-prompt approval, declined retries, and unbound drafts follow the acceptance rules. A Flow image outside the Project is attached or explicitly user-checked; the Project never claims to inspect an unseen image.
- Two-image clips: later clips show the previous clip's end state (built or changed things stay that way), and each video names its START image and END image.
- Mukbang prompts use photorealistic, hyperrealistic close-ups with food near the lens; exactly one bite per clip with closed-mouth chewing and a swallow (no second bite or looped bite sounds); tightened, action-synced audio plus room tone; and immediate eating without commentary, a pause, or camera smile.
- `general-story-helper.md` saves or is attached.
