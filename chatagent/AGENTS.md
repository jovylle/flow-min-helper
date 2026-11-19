# chatagent — driving ChatGPT Projects from an agent

Read `../AGENTS.md` first. This folder holds the process for an agent that runs the Flow helper Projects inside the user's ChatGPT web account through the Browse MCP. There is no code here.

## The Projects

| Project | URL | Source file in this repo |
| --- | --- | --- |
| Flow Mukbang Story Helper | https://chatgpt.com/g/g-p-6af1e03df35481918cd3689bf3bcfc48/project | `../mukbang-story-helper.md` |
| Flow Story Helper (general) | https://chatgpt.com/g/g-p-6ad48ac07dc48191b12d589614a4d7b8/project | `../general-story-helper.md` |
| Flow Horror Riddle Helper (pinned) | https://chatgpt.com/g/g-p-6afe7076bd448191b1dfc8b507e8741e/project | `../horror-riddle-helper.md` |

Each Project's Instructions field only says: "Read and follow the workflow in the attached pasted.txt source file for every request." The real instructions are one source named `pasted.txt`. Memory is Project-only.

## Updating a Project's instructions

1. Edit the `.md` file here, bump `Version:` in all three helper files, commit, and push (git is the backup).
2. Copy the file into a private folder under `/private/tmp/<name>/`. Browse `files.read` refuses the bare shared temp dir.
3. Project → Sources → Add sources → Paste text → fill the content box → Save. A "File already exists" dialog appears: choose **Upload anyway**.
4. Wait until the new item stops showing "Adding", then delete the OLD `pasted.txt` (the one with the older date) using Actions → Delete → Delete.
5. Reload Sources and verify that exactly one `pasted.txt` with today's date is listed. Remove the temp folder.

Add the new one before deleting the old one, so the Project is never empty.

## Running mukbang chats (one food per chat)

The models are the user's girlfriend and mother. Consent was confirmed on 2026-11-19, and the videos are for their own Facebook pages. Photos are not stored in this repo; ask the user to attach them again in the new thread.

Per chat:

1. Open the mukbang Project URL and wait about 4 seconds.
2. Upload the photo: `page.locator('input[type=file]').first().setInputFiles(path)` (path under `/private/tmp/<name>/`), then wait about 4 seconds.
3. Click the "New chat in …" textbox and use `page.keyboard.insertText(msg)`, NOT `keyboard.type`. Then press Enter.
4. Message template: `Mukbang idea. Eater: the woman in the attached photo (keep her face and identity exactly). Food: <food — description, plus "with X as the dipping sauce" if any>. One food only; do not add a second food.`
5. Check the reply: the status line starts with `model:`, it has 2 `CLIP n VIDEO` blocks, 2 `flow.google` links and a `Generate image` button, and it does not ask for another food.
6. Click `Generate image` once, using a JS click inside `page.evaluate`; a normal click is covered by the composer. Then wait about 60 seconds and check for the image.

Never click Generate image more than once per chat without the user's OK. The Project allows one extra try, and a double click spends it.

## Lessons from the 2026-11-19 run (8 chats)

- `keyboard.type` across several tabs at once mixes the text, because they share one keyboard. Typing the samgyupsal message got merged with ramen, and that image was then blocked by content policy. Use `insertText`, and send one tab at a time or one delegate per tab.
- A failed loop can still have clicked some buttons. Before retrying, check each tab's state (images present, buttons left).
- Delete stray duplicate tabs with the `tabs` tool (`action: close`). Do not close the user's own tabs or the `ep0x-flow` tabs.
- Every chat added an "elegant, expensive-looking outfit". That isn't in the instruction file, so it's probably Project memory from older chats. Ask the user before adding a rule to keep the photo's clothing.
- The user approved all 7 images. Samgyupsal still needs a fresh, clean chat.

## Parallel work

The user's standing rule is to delegate through T3 `delegate_task` (Haiku 5.5, effort medium), giving one delegate per chat. Every delegate must use `insertText`, work only in its own tab, click Generate image once, and report the chat URL, the image count, and any refusal. The orchestrator verifies each result before reporting to the user.

## Open items

- Redo samgyupsal (girlfriend) in a fresh chat with one clean message.
- Decide whether to add a "keep the photo's clothing" rule.
- The mukbang and general Projects still hold 0.10.3 text; only the version line differs from 0.11.0.
