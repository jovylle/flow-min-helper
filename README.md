# flow-min-helper

1-line idea → Clip 1 image prompt + 2× 8s Veo 3.1 Lite prompts. stdlib only.

## Use

```sh
python3 helper.py "a lighthouse keeper signals through dust as storm gathers"
python3 helper.py "idea..." --single   # Clip 1 only (save credits)
python3 helper.py --self-test
```

Paste image prompt into Flow image gen first (flow-first), then Clip 1 video (first-frame), then Clip 2 as Extend on Lite (no image).

Rules baked in: 8s only, Lite-only Extend, no shake, one move/shot, no photoreal humans, ambient-only no text.
