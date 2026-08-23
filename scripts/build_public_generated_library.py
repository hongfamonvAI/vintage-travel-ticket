#!/usr/bin/env python3
"""Build one high-resolution generated-ticket sheet and README examples.

The input directory is a maintainer-owned export folder. Only the explicitly listed
files are read. Every published image is resized, re-encoded, and stripped of EXIF.
Private historical reference tickets are never read by this script.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


GENERATED_SHEET_NAME = "generated-ticket-contact-sheet.jpg"


@dataclass(frozen=True)
class Entry:
    ref_id: str
    slug: str
    title: str
    source_name: str | None
    ticket_name: str
    families: tuple[str, ...]


ENTRIES = (
    Entry("G01", "albuquerque", "阿尔伯克基", None, "阿尔伯克基老门票.png", ("A",)),
    Entry("G02", "paris", "巴黎", "巴黎原照片.JPG", "巴黎老门票.png", ("M",)),
    Entry("G03", "porcelain-palace", "景德镇瓷宫", "景德镇瓷宫原照片.JPG", "景德镇瓷宫老门票.png", ("M",)),
    Entry("G04", "xiamen-shapowei", "厦门沙坡尾", "厦门沙坡尾原照片.JPG", "沙坡尾老门票.png", ("C", "H")),
    Entry("G05", "quanzhou", "泉州", "泉州原照片.JPG", "泉州老门票.png", ("B", "H")),
    Entry("G06", "jeju-island", "济州岛", "济州岛原照片.JPG", "济州岛老门票.png", ("L",)),
    Entry("G07", "victoria-harbour", "维多利亚港", "维洛利亚港原照片.JPG", "维多利亚港老门票.png", ("A", "H")),
    Entry("G08", "roland-garros", "罗兰·加洛斯球场", "罗兰加洛斯原照片.JPG", "罗兰加洛斯老门票.png", ("G",)),
    Entry("G09", "menton", "芒通", "芒通原照片.JPG", "芒通老门票.png", ("F",)),
    Entry("G10", "west-lake", "西湖", "西湖原照片.JPG", "西湖老门票.png", ("M",)),
    Entry("G11", "chungking-mansions", "重庆大厦", "重庆大厦原照片.JPG", "重庆大厦老门票.png", ("B", "H")),
    Entry("G12", "qingcheng-suxiangu", "青城山宿仙谷", "青城山宿仙谷原照片.JPG", "青城山宿仙谷老门票.png", ("P",)),
    Entry("G13", "xiamen-yubao", "厦门芋包", None, "厦门芋包老门票.png", ("F",)),
)


def publish_jpeg(source: Path, output: Path, max_edge: int, quality: int) -> None:
    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
        image.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary = output.with_name(f".{output.stem}.publishing.jpg")
        image.save(
            temporary,
            "JPEG",
            quality=quality,
            optimize=True,
            progressive=True,
            exif=b"",
        )
        temporary.replace(output)


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


def ticket_orientation(path: Path) -> str:
    with Image.open(path) as image:
        return "horizontal" if image.width >= image.height else "vertical"


def make_ticket_tile(source_path: Path, entry: Entry, size: tuple[int, int]) -> Image.Image:
    tile = Image.new("RGB", size, "#e8e4db")
    art_box = (size[0] - 44, size[1] - 104)
    with Image.open(source_path) as opened:
        source = ImageOps.exif_transpose(opened).convert("RGB")
        art = ImageOps.contain(source, art_box, method=Image.Resampling.LANCZOS)
    x = (size[0] - art.width) // 2
    y = 18 + (art_box[1] - art.height) // 2
    tile.paste(art, (x, y))

    draw = ImageDraw.Draw(tile)
    draw.rectangle((0, size[1] - 68, size[0], size[1]), fill="#252724")
    draw.text((20, size[1] - 55), entry.ref_id, font=font(28, True), fill="#f3eee2")
    draw.text(
        (102, size[1] - 55),
        entry.slug.replace("-", " ").upper(),
        font=font(28),
        fill="#f3eee2",
    )
    draw.rectangle((0, 0, size[0] - 1, size[1] - 1), outline="#706b61", width=2)
    return tile


def build_generated_sheet(
    ticket_sources: dict[str, Path], output: Path, quality: int
) -> None:
    horizontal = [entry for entry in ENTRIES if ticket_orientation(ticket_sources[entry.ref_id]) == "horizontal"]
    vertical = [entry for entry in ENTRIES if ticket_orientation(ticket_sources[entry.ref_id]) == "vertical"]

    margin = 56
    gap = 32
    header = 144
    section_header = 64
    footer = 76
    horizontal_cell = (1450, 620)
    vertical_cell = (700, 1640)
    horizontal_columns = 2
    vertical_columns = 4
    horizontal_rows = (len(horizontal) + horizontal_columns - 1) // horizontal_columns
    vertical_rows = (len(vertical) + vertical_columns - 1) // vertical_columns
    content_width = max(
        horizontal_columns * horizontal_cell[0] + (horizontal_columns - 1) * gap,
        vertical_columns * vertical_cell[0] + (vertical_columns - 1) * gap,
    )
    horizontal_height = horizontal_rows * horizontal_cell[1] + max(0, horizontal_rows - 1) * gap
    vertical_height = vertical_rows * vertical_cell[1] + max(0, vertical_rows - 1) * gap
    width = margin * 2 + content_width
    height = (
        header
        + section_header
        + horizontal_height
        + gap * 2
        + section_header
        + vertical_height
        + footer
    )
    sheet = Image.new("RGB", (width, height), "#f1eee7")
    draw = ImageDraw.Draw(sheet)
    draw.text((margin, 30), "GENERATED VINTAGE TICKET REFERENCE SHEET", font=font(42, True), fill="#252724")
    draw.text(
        (margin, 88),
        "FULL TICKETS · ORIGINAL ASPECT RATIOS · EXECUTION REFERENCE ONLY",
        font=font(22),
        fill="#6b655b",
    )

    y = header
    draw.text((margin, y + 10), "HORIZONTAL TICKETS", font=font(28, True), fill="#343530")
    y += section_header
    for index, entry in enumerate(horizontal):
        row, column = divmod(index, horizontal_columns)
        x = margin + column * (horizontal_cell[0] + gap)
        tile_y = y + row * (horizontal_cell[1] + gap)
        sheet.paste(make_ticket_tile(ticket_sources[entry.ref_id], entry, horizontal_cell), (x, tile_y))

    y += horizontal_height + gap * 2
    draw.text((margin, y + 10), "VERTICAL TICKETS", font=font(28, True), fill="#343530")
    y += section_header
    for index, entry in enumerate(vertical):
        row, column = divmod(index, vertical_columns)
        x = margin + column * (vertical_cell[0] + gap)
        tile_y = y + row * (vertical_cell[1] + gap)
        sheet.paste(make_ticket_tile(ticket_sources[entry.ref_id], entry, vertical_cell), (x, tile_y))

    draw.text(
        (margin, height - footer + 24),
        "Use as a range reference. Never copy destination text, serials, seals, figures, or one-for-one layouts.",
        font=font(20),
        fill="#6b655b",
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, "JPEG", quality=quality, optimize=True, progressive=True, exif=b"")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--source-max-edge", type=int, default=1600)
    parser.add_argument("--ticket-max-edge", type=int, default=1800)
    parser.add_argument("--quality", type=int, default=86)
    args = parser.parse_args()

    if not args.input_dir.is_dir():
        raise SystemExit(f"Input directory does not exist: {args.input_dir}")

    library_dir = args.skill_root / "assets" / "generated-ticket-library"
    examples_dir = args.skill_root / "examples"
    library_dir.mkdir(parents=True, exist_ok=True)
    examples_dir.mkdir(parents=True, exist_ok=True)

    ticket_sources: dict[str, Path] = {}
    for entry in ENTRIES:
        ticket_source = args.input_dir / entry.ticket_name
        if not ticket_source.is_file():
            raise SystemExit(f"Missing generated ticket: {ticket_source}")
        ticket_sources[entry.ref_id] = ticket_source

        ticket_example = examples_dir / f"{entry.slug}-ticket.jpg"
        publish_jpeg(ticket_source, ticket_example, args.ticket_max_edge, args.quality)

        if entry.source_name:
            source = args.input_dir / entry.source_name
            if not source.is_file():
                raise SystemExit(f"Missing example source: {source}")
            source_output = examples_dir / f"{entry.slug}-source.jpg"
            publish_jpeg(source, source_output, args.source_max_edge, args.quality)
    sheet_output = library_dir / GENERATED_SHEET_NAME
    build_generated_sheet(ticket_sources, sheet_output, max(args.quality, 90))

    (library_dir / "index.json").write_text(
        json.dumps(
            {
                "id": "GENERATED-SHEET-01",
                "file": GENERATED_SHEET_NAME,
                "contains": [
                    {
                        "id": entry.ref_id,
                        "title": entry.title,
                        "families": list(entry.families),
                    }
                    for entry in ENTRIES
                ],
                "usage": "High-resolution generated-ticket range reference only; never copy literal content or layout.",
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Published one generated-ticket contact sheet with {len(ENTRIES)} complete tickets to {sheet_output}")


if __name__ == "__main__":
    main()
