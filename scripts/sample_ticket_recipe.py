#!/usr/bin/env python3
"""Sample one coherent reference-distilled ticket recipe.

The sampler contains no private images or literal ticket designs. It only couples
compatible structural, colour, illustration, typography, information, and wear
families distilled in the public reference documents.
"""

from __future__ import annotations

import argparse
import json
import random


PROFILES = {
    "A-editorial-serial": {
        "orientation": "horizontal", "ratio": (2.8, 3.3), "weight": 1,
        "subjects": ["city", "portrait-memory", "architecture"],
        "layout": "12–20% serial cell; editorial figure/title field; optional narrow side rail",
        "palettes": ["P01", "P06", "P07", "P15"],
        "illustrations": ["I03", "I05", "I10", "I14"],
        "typography": ["T01", "T07"],
        "grammars": ["title-token", "memory-field", "value-block"],
    },
    "B-institutional-band": {
        "orientation": "horizontal", "ratio": (2.5, 3.2), "weight": 2,
        "subjects": ["architecture", "city", "object/specimen", "transport"],
        "layout": "three stacked bands; emblem corners; centered knockout title",
        "palettes": ["P03", "P11", "P17"],
        "illustrations": ["I04", "I12"],
        "typography": ["T02", "T08"],
        "grammars": ["title-token", "functional-label", "issuer-strip"],
    },
    "C-folk-scenic-stub": {
        "orientation": "horizontal", "ratio": (2.4, 3.3), "weight": 4,
        "subjects": ["landscape", "architecture", "city", "portrait-memory", "food"],
        "layout": "18–28% side stub and one framed or open scenic panel",
        "palettes": ["P02", "P05", "P07", "P18"],
        "illustrations": ["I01", "I02", "I03", "I12"],
        "typography": ["T03", "T05", "T15"],
        "grammars": ["coupon-pair", "value-block", "memory-field", "functional-label"],
    },
    "D-specimen-educational": {
        "orientation": "horizontal", "ratio": (2.8, 3.5), "weight": 1,
        "subjects": ["food", "object/specimen", "transport"],
        "layout": "small stub; isolated specimen window; scientific label rails",
        "palettes": ["P01", "P03", "P10", "P16"],
        "illustrations": ["I07", "I12", "I13"],
        "typography": ["T04", "T13"],
        "grammars": ["scientific-label", "value-block"],
    },
    "E-formal-coupon-pair": {
        "orientation": "horizontal", "ratio": (2.2, 2.8), "weight": 1,
        "subjects": ["landscape", "architecture", "object/specimen"],
        "layout": "two unequal perforated halves; quiet framed image",
        "palettes": ["P01", "P04", "P15"],
        "illustrations": ["I01", "I02"],
        "typography": ["T05", "T09"],
        "grammars": ["coupon-pair"],
    },
    "F-framed-panorama": {
        "orientation": "horizontal", "ratio": (2.4, 3.2), "weight": 4,
        "subjects": ["landscape", "architecture", "city", "portrait-memory", "food"],
        "layout": "65–85% panorama; remainder is admin box, title rail, price corner, or open paper",
        "palettes": ["P01", "P02", "P04", "P08", "P15", "P18"],
        "illustrations": ["I01", "I02", "I03", "I09", "I10"],
        "typography": ["T03", "T07", "T09", "T16"],
        "grammars": ["title-token", "value-block", "memory-field", "issuer-strip"],
    },
    "G-map-module-grid": {
        "orientation": "horizontal", "ratio": (2.0, 2.7), "weight": 2,
        "subjects": ["landscape", "architecture", "city", "food", "transport"],
        "layout": "full map or two-to-four unequal image modules plus a narrow index rail",
        "palettes": ["P01", "P08", "P09", "P18"],
        "illustrations": ["I02", "I06", "I11"],
        "typography": ["T08", "T14", "T16"],
        "grammars": ["route-code", "value-block", "issuer-strip"],
    },
    "H-recreation-graphic": {
        "orientation": "horizontal", "ratio": (2.1, 3.1), "weight": 2,
        "subjects": ["architecture", "city", "portrait-memory", "food", "transport"],
        "layout": "dynamic title/image overlap on a broad colour field; optional thin terminal",
        "palettes": ["P03", "P06", "P09", "P11", "P17"],
        "illustrations": ["I03", "I05", "I12"],
        "typography": ["T06", "T08", "T15"],
        "grammars": ["title-token", "functional-label", "memory-field"],
    },
    "I-transport-fare": {
        "orientation": "horizontal", "ratio": (2.1, 2.9), "weight": 2,
        "subjects": ["city", "transport", "landscape"],
        "layout": "vehicle or vessel image plus a 20–35% fare, price, or serial zone",
        "palettes": ["P03", "P10", "P11"],
        "illustrations": ["I01", "I02", "I04", "I06", "I13"],
        "typography": ["T03", "T05", "T08"],
        "grammars": ["transport-fare"],
    },
    "J-calligraphic-field": {
        "orientation": "horizontal", "ratio": (2.4, 3.0), "weight": 1,
        "subjects": ["landscape", "architecture", "portrait-memory"],
        "layout": "50–75% typography field; one small dark vignette; optional Roman footer",
        "palettes": ["P07", "P13", "P15"],
        "illustrations": ["I01", "I02", "I10"],
        "typography": ["T07", "T16"],
        "grammars": ["title-token", "memory-field"],
    },
    "K-banknote-seal": {
        "orientation": "horizontal", "ratio": (2.3, 2.8), "weight": 1,
        "subjects": ["landscape", "architecture", "object/specimen", "food"],
        "layout": "guilloche ground; seal cartouche; small image; isolated value corner",
        "palettes": ["P04", "P14", "P16"],
        "illustrations": ["I01", "I07", "I09", "I13"],
        "typography": ["T10", "T13"],
        "grammars": ["value-block", "issuer-strip"],
    },
    "L-minimal-emblem": {
        "orientation": "horizontal", "ratio": (2.5, 3.1), "weight": 2,
        "subjects": ["landscape", "architecture", "city", "object/specimen", "transport"],
        "layout": "one fine frame; one low panorama or symmetric emblem; one large open title zone",
        "palettes": ["P01", "P03", "P11", "P15"],
        "illustrations": ["I01", "I04", "I06", "I08"],
        "typography": ["T02", "T12", "T16"],
        "grammars": ["title-token"],
    },
    "M-vertical-scenic-strip": {
        "orientation": "vertical", "ratio": (2.5, 3.7), "weight": 5,
        "subjects": ["landscape", "architecture", "city", "portrait-memory", "food"],
        "layout": "60–80% tall image column; title on edge or base; compact value/serial foot",
        "palettes": ["P01", "P05", "P07", "P10", "P15"],
        "illustrations": ["I01", "I02", "I03", "I09", "I10", "I13"],
        "typography": ["T03", "T09", "T12", "T13"],
        "grammars": ["title-token", "value-block", "functional-label", "memory-field"],
    },
    "N-vertical-souvenir-card": {
        "orientation": "vertical", "ratio": (1.7, 2.2), "weight": 2,
        "subjects": ["landscape", "architecture", "portrait-memory", "food", "object/specimen"],
        "layout": "framed image or decorative panel with small caption/price base",
        "palettes": ["P05", "P08", "P12", "P14", "P18"],
        "illustrations": ["I03", "I09", "I12", "I14"],
        "typography": ["T03", "T11", "T13", "T15"],
        "grammars": ["title-token", "memory-field", "value-block"],
    },
    "O-vertical-dark-decorative": {
        "orientation": "vertical", "ratio": (1.7, 3.3), "weight": 1,
        "subjects": ["architecture", "portrait-memory", "object/specimen", "food"],
        "layout": "saturated dark field; one knockout figure/motif; small header and footer",
        "palettes": ["P12", "P13"],
        "illustrations": ["I02", "I08", "I10", "I14"],
        "typography": ["T07", "T10", "T11", "T16"],
        "grammars": ["title-token", "value-block", "memory-field"],
    },
    "P-vertical-register": {
        "orientation": "vertical", "ratio": (2.6, 3.7), "weight": 4,
        "subjects": ["landscape", "architecture", "city", "transport", "object/specimen"],
        "layout": "repeated serial/title cells; stacked vignettes; or striped lower coupon",
        "palettes": ["P01", "P03", "P05", "P10", "P11"],
        "illustrations": ["I01", "I04", "I06", "I13"],
        "typography": ["T02", "T05", "T09", "T14"],
        "grammars": ["coupon-pair", "issuer-strip", "route-code"],
    },
}

AGEING = [
    "dry plate + edge softness",
    "low-pressure letterpress + handling rub",
    "registration shift + fold dirt",
    "sun fade + broken rules",
    "stamp ghost + perforation wear",
    "handling rub + plate misalignment",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--orientation", choices=["any", "horizontal", "vertical"], default="any")
    parser.add_argument(
        "--subject",
        choices=["landscape", "architecture", "city", "portrait-memory", "food", "object/specimen", "transport"],
        default="landscape",
    )
    parser.add_argument("--avoid", action="append", default=[], help="profile id to exclude; repeatable")
    parser.add_argument("--seed", type=int)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rng = random.Random(args.seed)
    choices = []
    for profile_id, profile in PROFILES.items():
        if profile_id in args.avoid:
            continue
        if args.orientation != "any" and profile["orientation"] != args.orientation:
            continue
        if args.subject not in profile["subjects"]:
            continue
        choices.extend([profile_id] * profile["weight"])
    if not choices:
        raise SystemExit("No compatible profile. Remove an --avoid value or relax orientation.")

    profile_id = rng.choice(choices)
    profile = PROFILES[profile_id]
    ratio = round(rng.uniform(*profile["ratio"]), 2)
    result = {
        "profile": profile_id,
        "orientation": profile["orientation"],
        "ratio": f"{ratio}:1" if profile["orientation"] == "horizontal" else f"1:{ratio}",
        "layout": profile["layout"],
        "palette": rng.choice(profile["palettes"]),
        "illustration": rng.choice(profile["illustrations"]),
        "typography": rng.choice(profile["typography"]),
        "information_grammar": rng.choice(profile["grammars"]),
        "ageing": rng.choice(AGEING),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

