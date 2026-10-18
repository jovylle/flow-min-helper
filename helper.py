#!/usr/bin/env python3
"""flow-min-helper: 1-line idea -> Clip 1 image prompt + 2x 8s Veo 3.1 Lite prompts. stdlib only."""
import argparse
import random
import re
import sys

__version__ = "0.7.0"
MODEL = "veo-3.1-lite"
DUR = "8s"
TRAILER = ("One single frame of one composed scene \u2014 a single shot. No storyboard, no panels,\n"
           "no numbered cards, no grids, no timestamp chips, no captions, titles, watermarks,\n"
           "labels, or any text or documentation in the image. Display no plan, no production\nnotes.")

BANNED_CAMERA = ["shake", "shaky", "tremble", "trembling", "earthquake", "quiver"]
BANNED_HUMAN = ["photoreal human", "photorealistic human", "real person", "photograph of a person"]
MOVEMENTS = ["slow push-in", "slow pull-back", "slow pan right", "slow pan left",
             "slow tilt up", "slow tilt down", "static shot", "tracking shot", "orbit shot"]
# shortcut: three hand-written ideas picked at random when no idea is given, upgrade to model-written or a larger list when repeats show.
STORIES = [
    "hooded keeper in a ruined courtyard as storm gathers",
    "a lighthouse keeper signals through dust as storm gathers",
    "a lone courier crosses a flooded harbor at night as lightning cracks",
]


def clean(s):
    s = s.strip()
    s = re.sub(r"\s+", " ", s)
    return s


def pick_movement(idea):
    low = idea.lower()
    for m in MOVEMENTS:
        if m in low:
            return m
    return "slow push-in"


def sanitize(idea):
    low = idea.lower()
    for b in BANNED_CAMERA:
        if b in low:
            idea = re.sub(b, "still frame with falling dust and debris", idea, flags=re.I)
    for b in BANNED_HUMAN:
        if b.lower() in low:
            idea = re.sub(b, "stylized 3D animated figure", idea, flags=re.I)
    # default non-photoreal guard
    if "photoreal" in idea.lower():
        idea = re.sub(r"photoreal\w*", "stylized 3D animated", idea, flags=re.I)
    return clean(idea)


def status_block(nclips=2):
    return (f"model: {MODEL} | {DUR} only | clips: {nclips} | extend: Lite-only",
            "image: flow-first single frame | audio: ambient-only, no text")


def story_text(idea, master=""):
    s = sanitize(idea)
    if master:
        s += f". Master details, same in every clip: {sanitize(master)}"
    return s


def image_prompt(idea, master=""):
    idea = story_text(idea, master)
    move = pick_movement(idea)
    base = (f"Stylized 3D animated scene (not photorealistic humans): {idea}. "
            f"Eye-level medium-wide shot, {move}, single composed scene, "
            f"moody night lighting, cool palette with warm accent, cinematic grade, portrait 9:16.")
    return f"{base}\n{TRAILER}"


def clip_video(idea, k, n, master=""):
    # shortcut: the action beat is generic (brace, dust, storm) for every story, upgrade with per-story beats when stories need distinct actions.
    idea = story_text(idea, master)
    move = pick_movement(idea)
    return clean(
        f"Clip {k} of {n}, 0-8s, one continuous shot. Story: {idea}. "
        f"STYLE LOCK: stylized 3D animation, cool palette, night light, no photoreal humans. "
        f"Match Clip 1 ingredient image look (medium, palette, lighting, grade); subject and composition unchanged. "
        f"CAMERA FIRST: eye-level medium-wide shot, {move}, camera holds orientation, no shake. "
        f"Subject and setting as in the story; one dominant action: subject braces as wind rises and dust swirls. "
        f"Lighting: cold moonlight, volumetric dust, consistent grade. "
        f"Continuity: same figure, wardrobe, location, and props as the Clip 1 image and story text. "
        f"Add nothing that is not in the story or the Clip 1 image. "
        f"Audio: ambient wind, cloth movement, distant thunder. No dialogue, no narration, "
        f"no subtitles, no captions, no text overlays. "
        f"End: subject braced facing storm, framing held for Extend.")


def clip2_extend_delta():
    return clean(
        "Continue the previous clip's final frame, framing, and camera movement with no cut or new shot. "
        "A lightning flash brightens the scene and dust surges past as the subject sinks slightly to one knee. "
        "Settle holding that braced pose with storm ambient ongoing, ready to chain further. "
        "Audio: same ambient storm tone continues, no speech.")


def build(idea="", clips=None, extend=False, master=""):
    idea = clean(idea) or random.choice(STORIES)
    if clips is None:
        clips = random.randint(1, 3)
    if not 1 <= clips <= 5:
        raise ValueError("clips must be 1-5")
    s1, s2 = status_block(clips)
    out = [s1, s2, "",
           "--- CLIP 1 IMAGE (generate inside Flow) ---",
           image_prompt(idea, master), "",
           "--- CLIP 1 VIDEO (8s, Veo 3.1 Lite, ingredient: Clip 1 image) ---",
           clip_video(idea, 1, clips, master)]
    for k in range(2, clips + 1):
        if extend:
            out += ["", f"--- CLIP {k} EXTEND (8s, Veo 3.1 Lite Extend, no image) ---",
                    clip2_extend_delta()]
        else:
            out += ["", f"--- CLIP {k} VIDEO (8s, Veo 3.1 Lite, ingredient: Clip 1 image) ---",
                    clip_video(idea, k, clips, master)]
    return "\n".join(out)


def self_test():
    # shortcut: fixed-string asserts only, no golden files; upgrade to golden samples if prompts drift.
    img = image_prompt("hooded keeper in a ruined courtyard as storm gathers")
    assert "No storyboard, no panels" in img, "trailer missing"
    assert "photoreal" not in img.lower() or "not photoreal" in img.lower()
    assert "9:16" in img and "portrait" in img.lower()
    c1 = clip_video("storm keeper test", 1, 2)
    assert "ingredient image" in c1.lower()
    assert "no shake" in c1.lower()
    low = c1.lower()
    assert sum(m in low for m in MOVEMENTS) == 1, "must name exactly one movement"
    for bad in ["no dialogue", "no subtitles", "ambient"]:
        assert bad in low, bad
    c2 = clip2_extend_delta()
    n = len(c2.split())
    assert 30 <= n <= 90, f"extend delta {n} words"
    assert "no cut" in c2.lower()
    s1, s2 = status_block()
    assert "veo-3.1-lite" in s1 and "8s" in s1
    full = build("a lighthouse keeper signals through dust as storm gathers")
    assert full.count("---") >= 4
    for seed in range(20):
        random.seed(seed)
        out = build()
        n = int(re.search(r"clips: (\d)", out).group(1))
        assert 1 <= n <= 3 and out.count("VIDEO (") + out.count("EXTEND (") == n, (seed, n)
    five = build("storm keeper", clips=5)
    assert five.count("--- CLIP ") == 1 + 1 + 4, five.count("--- CLIP ")
    assert "clips: 5" in five
    m = "hooded keeper, long grey coat, silver beard, lantern in left hand"
    mb = build("storm keeper", clips=3, master=m)
    assert mb.count(m) == 4, mb.count(m)
    ingr = build("storm keeper", clips=3)
    assert ingr.count("ingredient: Clip 1 image") == 3
    assert "EXTEND" not in ingr
    ext = build("storm keeper", clips=3, extend=True)
    assert ext.count("EXTEND (") == 2 and "ingredient: Clip 1 image" not in ext.split("CLIP 2 EXTEND")[1]
    try:
        build("storm keeper", clips=6)
        raise AssertionError("clips=6 must fail")
    except ValueError:
        pass
    print("self-test: OK (image trailer, 1-move, ambient-only, extend 40-70w, status 2-line, 1-5 clips, ingredient default, extend opt-in)")


def main(argv=None):
    p = argparse.ArgumentParser(description="1-line idea -> Flow Clip 1 image + 1-5x 8s Lite prompts")
    p.add_argument("idea", nargs="?", help="one-line story idea")
    p.add_argument("--version", action="version", version=__version__)
    p.add_argument("--clips", type=int, default=None, help="number of 8s clips, 1-5 (default: random 1-3)")
    p.add_argument("--single", action="store_true", help="only Clip 1 (same as --clips 1)")
    p.add_argument("--extend", action="store_true", help="clips 2+ use Extend instead of the Clip 1 image as ingredient")
    p.add_argument("--master", default="", help="character, setting, palette details reused verbatim in every prompt")
    p.add_argument("--self-test", action="store_true", help="run built-in checks")
    a = p.parse_args(argv)
    if a.self_test:
        self_test()
        return 0
    idea = a.idea or clean(sys.stdin.read())
    try:
        print(build(idea, clips=1 if a.single else a.clips, extend=a.extend, master=a.master))
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
