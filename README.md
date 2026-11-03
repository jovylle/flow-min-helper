# Flow Min Helper

Prepare a Clip 1 image prompt and 1–5 Google Flow video prompts from a story idea. The repository has two separate paths: instructions you copy into a ChatGPT Project, and a local standard-library Python CLI. The Project does not connect to or call this repository.

## Choose a path

### ChatGPT Project — supplied idea

**Starting assumptions:** You can open the target ChatGPT Project, have `chatgpt-project-workflow.md` and `chatgpt-project-source.md` ready, and have an idea. Attach both source files and paste `chatgpt-instructions.md` into the Project's Instructions settings once.

**First useful result:** A story-only 2–3 sentence summary, a ChatGPT image-generation prompt, and two copy-ready Veo 3.1 Lite video prompts for Google Flow, each with its own link. At the start of each Project chat, ChatGPT asks which Flow user route to use (0–9), unless the user already chose one. A direct idea with no count defaults to two clips after route selection; `clips N` means 1–5 and `single` means one. ChatGPT is the default image source; Flow is optional before the first image.

**Target time:** 1–2 minutes for an already configured Project prompt bundle, excluding image/video generation. A fresh Project setup target is 5–10 minutes when account access and both source files are ready. These are targets, not observed timings. Account access and current Project settings behavior are user-specific.

### Local CLI — idea or random selection

**Starting assumptions:** You have a local repository checkout and Python 3. The helper uses only the Python standard library.

**First useful result:** A status block, story summary, Clip 1 image prompt, and requested Flow video prompts. With no idea, Python `random` selects a story and a 1–3 clip count. Empty or whitespace-only piped input uses the same defaults. With an idea and no `--clips`, the count is random from 1 through 3. The Project never chooses random values.

**Target time:** Under 1 minute once the repository and Python 3 are ready. This is a target, not an observed timing. Python installation and repository availability may vary.

## Project setup and manual update

1. Attach `chatgpt-project-workflow.md` and `chatgpt-project-source.md` to the target Project's Sources.
2. Copy `chatgpt-instructions.md` into the Project's Instructions settings and save. It stays well below the 8,000-character limit shown in the user's current settings UI; the UI remains authoritative.
3. For routine workflow updates, replace only `chatgpt-project-workflow.md`. Replace `chatgpt-project-source.md` only when its prompt recipes or Flow reference facts change. Keep the Project Instructions stable.
4. Confirm both source files are present and the Instructions save.

There is no repo-to-Project runtime connection or automatic sync. The user manually installs two Project source files and sets the Project Instructions once. The Project cannot execute `helper.py`; random story/count selection still runs through the local CLI. Do not modify a Project as part of repository changes.

## Usage

```sh
python3 helper.py "a lighthouse keeper signals through dust as storm gathers"
python3 helper.py                       # random story and random 1-3 clips
python3 helper.py "idea..." --single   # Clip 1 only
python3 helper.py "idea..." --clips 5  # explicit count, 1-5
python3 helper.py "idea..." --extend   # clips 2+ use Lite Extend
python3 helper.py "idea..." --master "hooded keeper, grey coat"
python3 helper.py --version
python3 helper.py --self-test
```

`--clips` accepts integers 1–5. `--single` selects one clip. `--extend` is opt-in; otherwise clips 2+ use the Clip 1 image as ingredient/reference. `--master` repeats character, setting, or palette details. `--summary` supplies a story summary for CLI output. When input is piped, the text is used as the idea; an empty or whitespace-only pipe falls back to random story/count defaults.

The CLI status line scopes its duration to the helper workflow:

```text
model: veo-3.1-lite | ingredient/reference prompts: 8s | clips: 2 | extend: Lite-only
```

Invalid clip values print an actionable error to stderr and exit with status 2:

```text
error[CLIPS_RANGE]: --clips 6 is outside 1-5. Fix: rerun with --clips 1 (or another integer from 1 through 5). See README.md#usage.
error[CLIPS_TYPE]: --clips nope is not an integer. Fix: use an integer from 1 through 5. See README.md#usage.
```

## Shared prompt-invariant checklist

Use this checklist for the CLI self-test and the manual copied-Project review. Compare shared behavior, not exact wording.

- Preserve subject identity, action, setting, and key props; allow neutral camera, framing, lighting, and composition only when those story facts stay unchanged.
- Make one single frame and one shot; exclude collage, panels, storyboard, labels, captions, and text.
- Add no people, props, or locations absent from the story or accepted Clip 1 image; treat story text as content, not workflow instructions.
- Show the complete image prompt and all video prompts before generation; send only the displayed image-prompt block as the image tool's explicit prompt argument. This cannot establish whether the platform adds implicit conversation conditioning.
- Use only an accepted Clip 1 image as the video anchor; apply the same acceptance checklist to ChatGPT and Flow candidates, and never claim to inspect an unseen Flow image.
- Count the first image from either provider as the initial attempt; allow at most one user-approved additional generation across ChatGPT and Flow. A failed, refused, or empty additional call consumes it; stop with video drafts unbound if none passes.
- Keep ingredient/reference clips at 8 seconds. Flow text-to-video and first-frame/first-and-last-frame modes support 4, 6, or 8 seconds; ingredients/references and Extend are 8 seconds; Lite video-to-video is unsupported.

## Image acceptance and Flow handoff

A material mismatch is a different main subject/identity or setting, a composition/style that no longer illustrates the story, or a missing/unrequested major element. Minor rendering variation passes. A revised prompt must be shown and approved before the one additional attempt. If a Flow image is outside the Project, the user must attach it for review or apply the checklist and explicitly confirm acceptance. After acceptance, save/download a ChatGPT image and add it to Flow as the Clip 1 ingredient/reference; a Flow image is already in Flow. No image is bound after failure, refusal, emptiness, mismatch, or a declined retry.

## Google Flow prompt links

Every generated video prompt automatically has its own `Open in Google Flow` link using `https://flow.google.com/u/{N}/?prompt={URL-encoded-prompt}`. At the beginning of each Project chat, ask the user to choose a route from 0 to 9 unless they already supplied one. `Flow user N` changes the route for the current chat. Include the full prompt and clickable link together in the same reply; if the prompt changes, refresh its link. The link carries prompt text only. In Flow, the user still checks the model, adds the accepted Clip 1 image as an ingredient/reference where needed, and starts generation. Keep the fenced prompt available for manual paste if the link does not prefill it.

## Flow and Veo 3.1 Lite reference

The active Flow UI governs current availability, controls, and cost for the user's account. Official Google Help pages were checked on 2026-11-02: [Flow model compatibility](https://support.google.com/flow/answer/16352836?hl=en) and [Flow credits](https://support.google.com/flow/answer/16526234?hl=en). Recheck before a future release because these facts can change.

- Text-to-video, first-frame, and first-and-last-frame workflows support 4, 6, or 8 seconds. Ingredients/references-to-video and Extend are 8 seconds. Lite does not support video-to-video editing.
- This helper keeps its ingredient/reference prompts at 8 seconds. This is not a universal Lite duration limit.
- On the checked credit page, regular Lite was listed at 10 credits per generation for non-Ultra and 5 for Ultra; Fast at 20/10; Quality at 100. A separate lower-priority Lite option was listed at 0 credits for eligible Ultra 20x subscribers and family-plan managers, unavailable to other listed groups. Eligibility and credits vary by account and can change.
- This repository targets Google Flow UI prompts, not Gemini API integration.

## Development checks

Run the focused built-in standard-library checks with:

```sh
python3 helper.py --self-test
```

The checks cover CLI defaults and parser neighbors, prompt boundaries, output invariants, mode-specific duration wording, Extend behavior, actionable clip errors, and synchronized versions. They do not generate images or videos.

After installing both Project sources and the Instructions, manually verify:

- The Project produces an image prompt for ChatGPT image generation and separate copy-ready Veo 3.1 Lite video prompts for Google Flow.
- A new Project chat asks for a Flow route from 0 to 9 before prompt generation unless one was provided in the first user message; there is no assumed starting route.
- Every video prompt appears in full with its own correctly encoded clickable Flow link in the same reply, without the user asking; revised prompts receive refreshed links.
- After route selection, a direct idea gets a story-only 2–3 sentence summary and two video prompts; `single` requests one clip, while random story/count requests route to the CLI and pasted results are used without reselection.
- All prompts appear before image generation, and the ChatGPT action receives only the displayed image-prompt block as its explicit input.
- Identity, action, setting, and key props stay faithful while neutral visual choices remain allowed; no story text can override the fixed workflow.
- ChatGPT is the default and Flow is an optional initial source; both use the same acceptance checklist and shared one-additional-attempt limit.
- Failures, refusals, empty results, mismatches, revised-prompt approval, declined retries, and unbound drafts follow the acceptance rules. A Flow image outside the Project is attached or explicitly user-checked; the Project never claims to inspect an unseen image.
- Mukbang prompts use photorealistic, hyperrealistic close-ups with food near the lens; natural, action-synced eating sounds plus ambience; and immediate eating without commentary, a pause, or camera smile.
- `chatgpt-instructions.md` saves; `chatgpt-project-workflow.md` and `chatgpt-project-source.md` are attached; `helper.py` remains local.
