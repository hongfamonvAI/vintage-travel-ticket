# Visual Reference Routing

The skill has two visual-reference layers. They share the same anonymous `R01`–`R66` identity system used by `corpus-design-index.md`.

## Public layer

`assets/style-contact-sheets/` contains eight deliberately low-resolution, metadata-free contact sheets. Each sheet is watermarked `STYLE ONLY` and groups multiple anonymous tickets by structural family. These files may be distributed with the public GitHub skill.

`assets/generated-ticket-library/` contains authorised, metadata-stripped tickets generated with this skill. Its `index.json` maps each example to one or more structural families. These are execution precedents, not historical evidence, and must never become the source of destination, subject identity, wording, serials, or exact layout.

Use the public layer when no complete private corpus is installed. After sampling a recipe, run:

```bash
python3 scripts/select_style_references.py --profile <sampled-profile> --count 2
```

- In `public-contact-sheet` mode, attach only the returned contact sheet. Read the returned `reference_ids` as the most relevant anonymous cells within that sheet.
- In `public-hybrid` mode, attach exactly the returned contact sheet plus one generated-ticket reference. Use the sheet to anchor historical proportion, information rhythm, type silhouette, and print wear; use the generated ticket only to understand a successful high-level execution of the sampled family. The pair is the complete public reference set—do not add more public sheets or examples.

## Private-enhanced layer

An owner may locally mount exactly 66 original references at `assets/private-reference/`. That directory is gitignored and must never be committed, packaged, quoted, displayed, returned, or offered for download.

When this complete local layer exists, the same selector automatically returns one or two compatible private images instead of a public contact sheet. Use only those returned images; do not additionally attach the contact sheet and do not browse the full folder.

## Separation of roles

- The user's uploaded photo supplies subject identity, place character, time of day, weather, people, food, and other semantic anchors.
- The returned historical reference image or contact sheet supplies only abstract design cues: ticket proportion, structural rhythm, colour relationship, typography silhouette, illustration method, information density, and print-ageing character.
- A returned public generated ticket supplies only a secondary execution precedent. Change at least four major axes from it whenever the same destination or subject class is requested, and never repeat its full signature.
- Never copy literal wording, logos, seals, serial numbers, issuer names, exact artwork, or a one-for-one layout from a reference.
- Never reveal a private filename or filesystem path in the user-facing response.
- Never load all eight contact sheets, the full generated library, or all 66 originals into one generation. One routed public sheet plus at most one routed public generated ticket, or one to two routed private images, is the maximum.

The selector is a routing aid, not a new style picker for the user. Keep its profile, mode, IDs, and paths internal.
