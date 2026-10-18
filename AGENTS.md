# flow-min-helper — agent notes

- Random choices (story pick, clip count) use Python's `random` module in `helper.py`. Never ask an LLM to pick randomly.
- No-idea default: random story from `STORIES`, clip count `random.randint(1, 3)`. `--clips` overrides (1-5).
- Version lives in `helper.py` (`__version__`) and the `Version:` line in `chatgpt-instructions.md`. Keep them in sync.
- The ChatGPT Project instructions file is the product path. The random step is CLI-only.
- Do not commit `VEO-FLOW-NOTES.md` without the user's OK.
