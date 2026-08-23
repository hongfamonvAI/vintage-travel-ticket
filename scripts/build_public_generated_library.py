#!/usr/bin/env python3
"""Build the public generated-ticket library and authorised before/after examples.

The input directory is a maintainer-owned export folder. Only the explicitly listed
files are read. Every published image is resized, re-encoded, and stripped of EXIF.
Private historical reference tickets are never read by this script.
"""

from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageOps


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

    index: list[dict[str, object]] = []
    for entry in ENTRIES:
        ticket_source = args.input_dir / entry.ticket_name
        if not ticket_source.is_file():
            raise SystemExit(f"Missing generated ticket: {ticket_source}")

        library_output = library_dir / f"{entry.ref_id.lower()}-{entry.slug}.jpg"
        publish_jpeg(ticket_source, library_output, args.ticket_max_edge, args.quality)
        shutil.copyfile(library_output, examples_dir / f"{entry.slug}-ticket.jpg")

        if entry.source_name:
            source = args.input_dir / entry.source_name
            if not source.is_file():
                raise SystemExit(f"Missing example source: {source}")
            source_output = examples_dir / f"{entry.slug}-source.jpg"
            publish_jpeg(source, source_output, args.source_max_edge, args.quality)
        index.append(
            {
                "id": entry.ref_id,
                "file": library_output.name,
                "title": entry.title,
                "families": list(entry.families),
                "usage": "Public generated style reference only; do not copy literal content or layout.",
            }
        )

    (library_dir / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Published {len(index)} generated ticket references to {library_dir}")


if __name__ == "__main__":
    main()
