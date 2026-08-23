#!/usr/bin/env python3
"""Select the smallest useful visual reference layer for a sampled profile."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path


SUPPORTED = {".jpg", ".jpeg", ".png", ".webp"}
DEFAULT_PRIVATE = "assets/private-reference"
DEFAULT_GENERATED = "assets/generated-ticket-library"

PROFILE_ROUTES = {
    "A": ("01-editorial-band-graphic.jpg", ["R01", "R34"]),
    "B": ("01-editorial-band-graphic.jpg", ["R03", "R44", "R45", "R52"]),
    "C": ("02-scenic-stub-coupon.jpg", ["R04", "R10", "R13", "R19", "R20", "R38", "R50", "R60"]),
    "D": ("03-specimen-map-fare-banknote.jpg", ["R09", "R64"]),
    "E": ("02-scenic-stub-coupon.jpg", ["R11", "R25"]),
    "F": ("04-panorama-calligraphy-minimal.jpg", ["R06", "R21", "R22", "R39"]),
    "G": ("03-specimen-map-fare-banknote.jpg", ["R31", "R42"]),
    "H": ("01-editorial-band-graphic.jpg", ["R07", "R24", "R35", "R37", "R48", "R56"]),
    "I": ("03-specimen-map-fare-banknote.jpg", ["R53", "R54"]),
    "J": ("04-panorama-calligraphy-minimal.jpg", ["R46", "R61"]),
    "K": ("03-specimen-map-fare-banknote.jpg", ["R30", "R64"]),
    "L": ("04-panorama-calligraphy-minimal.jpg", ["R55", "R66"]),
    "M": ("05-vertical-scenic-strip.jpg", ["R05", "R08", "R15", "R23", "R26", "R29", "R32", "R33", "R36", "R41"]),
    "N": ("07-vertical-souvenir-card.jpg", ["R12", "R14", "R16", "R18", "R40", "R49"]),
    "O": ("08-vertical-dark-decorative.jpg", ["R17", "R51", "R62", "R65"]),
    "P": ("06-vertical-register.jpg", ["R02", "R27", "R28", "R43", "R47", "R57", "R58", "R59", "R63"]),
}


def private_map(directory: Path) -> dict[str, Path]:
    if not directory.exists():
        return {}
    paths = sorted(path for path in directory.iterdir() if path.is_file() and path.suffix.lower() in SUPPORTED)
    if len(paths) != 66:
        return {}
    return {f"R{index:02d}": path for index, path in enumerate(paths, 1)}


def generated_map(directory: Path) -> dict[str, list[dict[str, object]]]:
    index_path = directory / "index.json"
    if not index_path.is_file():
        return {}
    try:
        records = json.loads(index_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}

    by_family: dict[str, list[dict[str, object]]] = {}
    for record in records:
        if not isinstance(record, dict):
            continue
        ref_id = record.get("id")
        filename = record.get("file")
        families = record.get("families")
        if not isinstance(ref_id, str) or not isinstance(filename, str) or not isinstance(families, list):
            continue
        path = directory / filename
        if not path.is_file() or path.suffix.lower() not in SUPPORTED:
            continue
        clean = {"id": ref_id, "path": path}
        for family in families:
            if isinstance(family, str) and family.upper() in PROFILE_ROUTES:
                by_family.setdefault(family.upper(), []).append(clean)
    return by_family


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True, help="Sampler profile, for example C-folk-scenic-stub")
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--private-dir", type=Path)
    parser.add_argument("--generated-dir", type=Path)
    parser.add_argument("--count", type=int, choices=[1, 2], default=2)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()

    family = args.profile.strip().upper()[0]
    if family not in PROFILE_ROUTES:
        raise SystemExit(f"Unknown profile family: {args.profile}")
    sheet, eligible = PROFILE_ROUTES[family]
    rng = random.Random(args.seed)
    chosen_ids = rng.sample(eligible, min(args.count, len(eligible)))
    private_dir = args.private_dir or args.skill_root / DEFAULT_PRIVATE
    private = private_map(private_dir)
    generated_dir = args.generated_dir or args.skill_root / DEFAULT_GENERATED
    generated = generated_map(generated_dir)

    if private:
        result = {
            "mode": "private-enhanced",
            "references": [str(private[ref_id]) for ref_id in chosen_ids],
            "reference_ids": chosen_ids,
        }
    elif family in generated and args.count == 2:
        chosen_generated = rng.choice(generated[family])
        result = {
            "mode": "public-hybrid",
            "references": [
                str(args.skill_root / "assets" / "style-contact-sheets" / sheet),
                str(chosen_generated["path"]),
            ],
            "reference_ids": chosen_ids + [chosen_generated["id"]],
        }
    else:
        result = {
            "mode": "public-contact-sheet",
            "references": [str(args.skill_root / "assets" / "style-contact-sheets" / sheet)],
            "reference_ids": chosen_ids,
        }
    result["usage"] = (
        "Style only. Never copy literal words, logos, seals, serials, artwork, "
        "subject identity, or one-for-one layout."
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
