#!/usr/bin/env python3
"""Build distributable low-resolution style maps from the private 66-image corpus.

Every ticket is shown in full at its original aspect ratio. The generated sheets
remove filenames and metadata, reduce resolution, and add a STYLE ONLY watermark.
They are visual routing aids, not a replacement for the private reference archive.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps


SUPPORTED = {".jpg", ".jpeg", ".png", ".webp"}

GROUPS = {
    "01-editorial-band-graphic": [
        "R01", "R03", "R07", "R24", "R34", "R35", "R37", "R44", "R45", "R48", "R52", "R56"
    ],
    "02-scenic-stub-coupon": ["R04", "R10", "R11", "R13", "R19", "R20", "R25", "R38", "R50", "R60"],
    "03-specimen-map-fare-banknote": ["R09", "R30", "R31", "R42", "R53", "R54", "R64"],
    "04-panorama-calligraphy-minimal": ["R06", "R21", "R22", "R39", "R46", "R55", "R61", "R66"],
    "05-vertical-scenic-strip": ["R05", "R08", "R15", "R23", "R26", "R29", "R32", "R33", "R36", "R41"],
    "06-vertical-register": ["R02", "R27", "R28", "R43", "R47", "R57", "R58", "R59", "R63"],
    "07-vertical-souvenir-card": ["R12", "R14", "R16", "R18", "R40", "R49"],
    "08-vertical-dark-decorative": ["R17", "R51", "R62", "R65"],
}


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    names = (
        ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
        if bold
        else ["/System/Library/Fonts/Supplemental/Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    )
    for name in names:
        if Path(name).exists():
            return ImageFont.truetype(name, size)
    return ImageFont.load_default()


def image_map(source_dir: Path) -> dict[str, Path]:
    paths = sorted(path for path in source_dir.iterdir() if path.is_file() and path.suffix.lower() in SUPPORTED)
    if len(paths) != 66:
        raise SystemExit(f"Expected exactly 66 supported images in {source_dir}, found {len(paths)}")
    return {f"R{index:02d}": path for index, path in enumerate(paths, 1)}


def make_tile(path: Path, ref_id: str, size: tuple[int, int]) -> Image.Image:
    with Image.open(path) as source:
        source = ImageOps.exif_transpose(source).convert("RGB")
        # Keep the complete ticket—including its outer edge, stub, and full title
        # zones—while the modest cell size keeps this a low-resolution style map.
        art_box = (size[0] - 18, size[1] - 42)
        art = ImageOps.contain(source, art_box, method=Image.Resampling.LANCZOS)
        art = ImageEnhance.Contrast(art).enhance(0.96).filter(ImageFilter.GaussianBlur(0.12))

    tile = Image.new("RGB", size, "#ded5c2")
    x = (size[0] - art.width) // 2
    y = 8 + (art_box[1] - art.height) // 2
    tile.paste(art, (x, y))
    draw = ImageDraw.Draw(tile, "RGBA")
    draw.rectangle((0, size[1] - 28, size[0], size[1]), fill=(24, 25, 23, 205))
    draw.text((8, size[1] - 23), ref_id, font=font(14, True), fill=(245, 239, 222, 255))

    watermark = "STYLE ONLY"
    wm_font = font(max(14, min(size) // 10), True)
    box = draw.textbbox((0, 0), watermark, font=wm_font)
    width = box[2] - box[0]
    height = box[3] - box[1]
    draw.rectangle(
        ((size[0] - width) // 2 - 8, (size[1] - height) // 2 - 5,
         (size[0] + width) // 2 + 8, (size[1] + height) // 2 + 5),
        fill=(245, 239, 222, 54),
    )
    draw.text(((size[0] - width) // 2, (size[1] - height) // 2 - 2), watermark, font=wm_font, fill=(35, 34, 31, 88))
    draw.rectangle((0, 0, size[0] - 1, size[1] - 1), outline=(52, 47, 39, 190), width=2)
    return tile


def build_sheet(name: str, ids: list[str], paths: dict[str, Path], output_dir: Path, quality: int) -> Path:
    vertical = name.startswith(("05-", "06-", "07-", "08-"))
    columns = 5 if vertical else 3
    cell = (220, 390) if vertical else (380, 228)
    margin, gap, header, footer = 28, 16, 82, 48
    rows = (len(ids) + columns - 1) // columns
    width = margin * 2 + columns * cell[0] + (columns - 1) * gap
    height = header + footer + rows * cell[1] + (rows - 1) * gap
    sheet = Image.new("RGB", (width, height), "#eee7d8")
    draw = ImageDraw.Draw(sheet)
    title = name.split("-", 1)[1].replace("-", " ").upper()
    draw.text((margin, 16), title, font=font(24, True), fill="#24231f")
    draw.text((margin, 47), "LOW-RES PUBLIC STYLE MAP · DO NOT COPY LITERAL CONTENT", font=font(12), fill="#6b6254")

    for index, ref_id in enumerate(ids):
        row, column = divmod(index, columns)
        x = margin + column * (cell[0] + gap)
        y = header + row * (cell[1] + gap)
        sheet.paste(make_tile(paths[ref_id], ref_id, cell), (x, y))

    footer_text = "Composition, palette, type silhouette and print wear only. Never copy words, logos, seals, serials or artwork."
    draw.text((margin, height - footer + 13), footer_text, font=font(11), fill="#6b6254")
    output = output_dir / f"{name}.jpg"
    sheet.save(output, "JPEG", quality=quality, optimize=True, progressive=True, exif=b"")
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--quality", type=int, default=74)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    paths = image_map(args.source_dir)
    for name, ids in GROUPS.items():
        output = build_sheet(name, ids, paths, args.output_dir, args.quality)
        print(output)


if __name__ == "__main__":
    main()
