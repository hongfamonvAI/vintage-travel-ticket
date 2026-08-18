# Reference-Distilled Design Grammar

Use this file as the decision engine. It converts the 66-ticket corpus into coherent design DNA without shipping or reproducing the private images.

## Contents

- [Core rule](#core-rule)
- [Recipe sequence](#recipe-sequence)
- [Coupling matrix](#coupling-matrix)
- [Variation memory](#variation-memory)
- [Prompt construction order](#prompt-construction-order)

## Core rule

Randomize **coherent bundles**, not isolated decorations. A ticket is believable when geometry, image method, typography, information grammar, paper, palette, and wear appear to come from one print era and production method.

Do not begin with `cream paper + scenic drawing + Song title + right stub`. Begin with one structural archetype from [archetype-system.md](archetype-system.md), then use the coupling matrix below.

## Recipe sequence

1. Classify the source as `landscape`, `architecture`, `city`, `portrait-memory`, `food`, `object/specimen`, or `transport`.
2. Respect an explicit orientation. Otherwise choose horizontal with probability `0.56` and vertical with probability `0.44`, reflecting the corpus while preserving meaningful variation.
3. Determine the destination region as `mainland-cn`, `chinese-region`, or `overseas`.
4. Select one compatible archetype. Run `scripts/sample_ticket_recipe.py --region <region>` when available; use its result, including `language_mode`, as the internal art direction.
5. Select a paper-and-palette family compatible with the archetype from [palette-paper-system.md](palette-paper-system.md).
6. Select one primary illustration language and one supporting mark language from [illustration-system.md](illustration-system.md). The supporting language may appear only in a seal, map, border, inset, or micro-vignette.
7. Select one typography recipe from [typography-system.md](typography-system.md). Title, information, and number/Roman roles must remain visibly distinct. When `language_mode` is `chinese-only`, fulfil the third role with a serial, date, value, seal, or route code—not forced English.
8. Select exactly one information grammar: `title-token`, `value-block`, `coupon-pair`, `functional-label`, `memory-field`, `route-code`, `issuer-strip`, `scientific-label`, or `transport-fare`.
9. Select two primary ageing events and zero or one subtle secondary event from [print-ageing-system.md](print-ageing-system.md). Apply them only where physically plausible.
10. Recompose the source into three to seven graphic masses. Use recognition anchors, not its original crop.
11. Before generation, write a one-line internal signature: `archetype / ratio / paper-palette / illustration / title recipe / grammar / language mode / ageing`. Compare it with visible prior outputs.

## Coupling matrix

`Strong` combinations mirror recurring corpus logic. `Allowed` combinations are plausible with care. Blank combinations should not be used.

| Structural family | Engraving | Folk colour | Woodcut | Screenprint | Map/schema | Calligraphic | Halftone | Cartoon |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| editorial serial | Allowed | Strong | Allowed | Strong |  | Strong |  | Allowed |
| institutional banner | Allowed |  |  | Strong | Allowed |  |  | Allowed |
| scenic stub | Strong | Strong | Allowed | Allowed |  | Allowed |  | Allowed |
| specimen/educational | Strong | Allowed | Allowed | Allowed | Strong |  | Strong | Allowed |
| coupon pair | Strong | Allowed | Allowed | Allowed |  |  |  |  |
| framed panorama | Strong | Strong | Strong | Allowed | Allowed | Allowed | Allowed |  |
| map/module grid | Allowed | Allowed | Strong | Strong | Strong |  |  | Allowed |
| recreation graphic |  | Allowed | Allowed | Strong | Strong | Allowed |  | Strong |
| transport fare | Strong |  | Allowed | Strong | Strong | Allowed | Allowed | Allowed |
| calligraphic field | Strong |  | Strong | Allowed |  | Strong |  |  |
| banknote/seal | Strong | Allowed | Allowed | Allowed | Strong | Allowed | Allowed |  |
| vertical scenic strip | Strong | Strong | Strong | Allowed | Allowed | Allowed | Strong |  |
| vertical souvenir card | Strong | Strong | Allowed | Strong |  | Allowed | Strong | Allowed |
| vertical dark/decorative | Strong | Allowed | Strong | Strong |  | Strong |  |  |
| vertical register | Strong | Allowed | Allowed | Strong | Allowed |  | Strong |  |
| minimal emblem | Strong |  | Allowed | Strong | Strong | Allowed |  | Allowed |

## Variation memory

- Never repeat the immediately previous archetype or full signature.
- Across the last three visible tickets, avoid reusing the same title silhouette, paper temperature, stub position, and dominant ink together.
- A requested “another version” must change at least four of: orientation/ratio, archetype, title location, paper family, dominant palette, illustration language, information grammar, typography recipe, ageing profile.
- A requested orientation change is a redesign. Reflow information and illustration; never crop or rotate the previous composition.
- Do not interpret randomization as equal probability for every possible cross-product. Sample a coherent archetype first, then vary only compatible subchoices.

## Prompt construction order

Write the image prompt in this order so later details do not erase earlier structure:

1. finished ticket and exact ratio;
2. structural archetype and spatial allocation in percentages;
3. source-derived recognition anchors and required recomposition;
4. illustration method and abstraction level;
5. paper, ink count, and exact palette roles;
6. title, information, and serial/number typography roles;
7. sampled language mode and exact verified text strings; explicitly state that no Roman line is allowed for `chinese-only`;
8. information grammar and which fields are absent;
9. print wear on paper **and ink**;
10. negative constraints: no photo, no generic poster, no invented words, no default stub.
