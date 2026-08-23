# Visual Reference Routing

The skill has two visual-reference layers. They share the same anonymous `R01`–`R66` identity system used by `corpus-design-index.md`.

## Public layer

`assets/style-contact-sheets/` contains eight deliberately low-resolution, metadata-free contact sheets. Each sheet is watermarked `STYLE ONLY`, groups multiple anonymous tickets by structural family, and shows every ticket in full at its original aspect ratio without cropping its frame, title, stub, or edge. These files may be distributed with the public GitHub skill.

`assets/generated-ticket-library/` contains one high-resolution, metadata-stripped contact sheet of authorised tickets generated with this skill. All generated tickets appear complete at their original aspect ratios in that single sheet. Its `index.json` records the included examples and their broad families. These are execution precedents, not historical evidence, and must never become the source of destination, subject identity, wording, serials, or exact layout.

This library is strictly ticket-only. Source photographs must never be copied into it, listed in its index, or returned by the selector. `examples/` exists only for human-readable README comparisons; the generation pipeline must never scan, attach, or route any file from that directory. The selector enforces a ticket-only `gNN-*.jpg` filename contract and rejects paths outside the generated-ticket directory.

Use the public layer when no complete private corpus is installed. After sampling a recipe, run:

```bash
python3 scripts/select_style_references.py --profile <sampled-profile> --count 2
```

- In `public-contact-sheet` mode, attach only the returned contact sheet. Read the returned `reference_ids` as the most relevant anonymous cells within that sheet.
- In `public-hybrid` mode, attach exactly the returned low-resolution historical sheet plus the one high-resolution generated-ticket sheet. Use the historical sheet to anchor proportion, information rhythm, type silhouette, and print wear; use the generated sheet only to understand the available range of complete executions. The pair is the complete public reference set—do not add more public sheets or examples.

## Private-enhanced layer

An owner may locally mount exactly 66 original references at `assets/private-reference/`. That directory is gitignored and must never be committed, packaged, quoted, displayed, returned, or offered for download.

When this complete local layer exists, the same selector automatically returns one or two compatible private images instead of a public contact sheet. Use only those returned images; do not additionally attach the contact sheet and do not browse the full folder.

## Separation of roles

- The user's uploaded photo supplies subject identity, place character, time of day, weather, people, food, and other semantic anchors.
- README source photographs are display-only and are not part of either visual-reference layer.
- The returned historical reference image or contact sheet supplies only abstract design cues: ticket proportion, structural rhythm, colour relationship, typography silhouette, illustration method, information density, and print-ageing character.
- The returned public generated-ticket sheet supplies only secondary range precedents. Change at least four major axes from the closest visible cell whenever the same destination or subject class is requested, and never repeat a cell's full signature.
- Never copy literal wording, logos, seals, serial numbers, issuer names, exact artwork, or a one-for-one layout from a reference.
- Never reveal a private filename or filesystem path in the user-facing response.
- Never load all eight historical sheets or all 66 originals into one generation. One routed low-resolution historical sheet plus the single high-resolution generated-ticket sheet, or one to two routed private images, is the maximum.

The selector is a routing aid, not a new style picker for the user. Keep its profile, mode, IDs, and paths internal.
