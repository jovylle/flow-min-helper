# flow-min-helper

1-line idea → Clip 1 image prompt + 2× 8s Veo 3.1 Lite prompts. stdlib only.

## Use

```sh
python3 helper.py "a lighthouse keeper signals through dust as storm gathers"
python3 helper.py                       # no idea: random story, random 1-3 clips
python3 helper.py "idea..." --single   # Clip 1 only (save credits)
python3 helper.py "idea..." --clips 5   # 1-5 clips, Clip 1 image as ingredient on every clip
python3 helper.py "idea..." --clips 3 --extend  # clips 2+ as Extend instead
python3 helper.py --version
python3 helper.py --self-test
```

Paste image prompt into Flow image gen first (flow-first), then Clip 1 video (Clip 1 image as ingredient, not first-frame), then Clip 2+ as ingredient clips (default) or Extend on Lite (`--extend`).

Rules baked in: 8s only, Lite-only Extend, no shake, one move/shot, no photoreal humans, ambient-only no text.
