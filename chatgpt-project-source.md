# Flow Min Helper — ChatGPT Project Reference

This supporting source contains prompt recipes and dated Google Flow reference facts. The current behavior contract lives in `chatgpt-project-workflow.md`. Attach both files during setup; replace the workflow file for routine changes and update this reference only when its recipes or Flow facts change.

## Prompt recipes

### Clip 1 image

Use one story-faithful scene. For non-mukbang, default to stylized 3D animation, not photorealistic humans. For mukbang, default to photorealistic, hyperrealistic humans, food, and setting, with believable anatomy and food proportions. Preserve the story's subject identity, action, setting, and key props. Neutral camera, framing, lighting, and composition choices are allowed only when they do not change those facts. For non-mukbang, default to an eye-level medium-wide shot; for mukbang, use a close-up or medium close-up with food filling the near foreground close to the lens and the eater visible behind it. Use appetizing natural light, realistic textures and reflections, natural proportions, one composed scene, and portrait 9:16. Append the exact image trailer in `chatgpt-project-workflow.md`.

### Veo 3.1 Lite video

Write one copy-ready paragraph, camera first. State clip number/count and one continuous 0–8 second shot; size, angle, one movement, and held orientation; the story action; style; match to the accepted Clip 1 image; continuity; permitted sounds; a plain negative list; and a held end pose. Keep one dominant visible action. For mukbang, default to photorealistic, hyperrealistic people and food; use close natural ASMR sounds synchronized to eating, shell/utensil contact, and sauce handling as applicable, plus quiet ambience only; no speech or music. Start eating immediately and keep food near the lens in a close-up/medium close-up while the eater remains visible, using natural perspective.

### Lite Extend delta

Use 40–70 words. Continue the previous final frame, framing, and movement without a cut or new shot; apply one small story-based change; settle into a held end state; continue ambient sound only. Do not restate character, wardrobe, location, lighting, palette, style, or voice.

## Flow and Veo 3.1 Lite reference

These Flow UI facts were checked on 2026-11-02. They are references, not account guarantees; the active Flow model selector and UI govern current availability and cost. Recheck before relying on them.

- [Flow model compatibility](https://support.google.com/flow/answer/16352836?hl=en) and [Flow credits](https://support.google.com/flow/answer/16526234?hl=en).
- Text-to-video, first-frame, and first-and-last-frame workflows support 4, 6, or 8 seconds. Ingredients/references-to-video and Extend are 8 seconds. Lite does not support video-to-video editing. The CLI keeps ingredient/reference prompts at 8 seconds; do not describe every Lite mode as 8-second-only.
- On the checked credit page, regular Lite was listed at 10 credits per generation for non-Ultra and 5 for Ultra; Fast at 20/10; Quality at 100. A separate lower-priority Lite option was listed at 0 credits for eligible Ultra 20x subscribers and family-plan managers, unavailable to other listed groups. Eligibility and costs can change; the user's Flow UI takes precedence.
- This Project targets Flow UI prompts, not Gemini API integration.
