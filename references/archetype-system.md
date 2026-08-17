# Reference-Distilled Ticket Archetypes

Choose exactly one archetype before every first-pass generation. These sixteen families were distilled from the 66-ticket corpus. They define a whole system—ratio, spatial allocation, illustration, text hierarchy, information grammar, and print era—not merely a palette.

## Horizontal families

| ID | Archetype | Ratio | Spatial allocation | Compatible image/type/grammar |
|---|---|---:|---|---|
| A | editorial serial ticket | `2.8:1`–`3.3:1` | 12–20% serial cell, 65–78% editorial image/title, 8–15% narrow rail | caricature, stencil or calligraphic display; `title-token`, `memory-field`, `value-block` |
| B | institutional band banner | `2.5:1`–`3.2:1` | three stacked bands; emblem corners; title centred in dominant field | flat screenprint, knockout type, geometric Romanization; `functional-label` or `title-token` |
| C | folk scenic stub | `2.4:1`–`3.3:1` | 18–28% side stub plus one framed or open scenic panel | naïve colour or loose contour; hand title + small lead type; `coupon-pair`, `value-block`, `memory-field` |
| D | specimen/educational ticket | `2.8:1`–`3.5:1` | small stub, isolated specimen window, label rails | scientific engraving or cartoon emblem; condensed labels + italic Latin; `scientific-label`, `value-block` |
| E | formal coupon pair | `2.2:1`–`2.8:1` | two unequal halves with clear perforation and quiet framed image | monochrome engraving; Song/Fangsong + mechanical number; `coupon-pair` only |
| F | framed panorama | `2.4:1`–`3.2:1` | 65–85% panorama; remaining space becomes admin box, title rail, price corner, or nothing | engraving, folk colour, woodcut, painterly insert; any non-route grammar |
| G | map or modular grid | `2.0:1`–`2.7:1` | full map or two-to-four unequal image cells with index/admin rail | schema, woodcut modules, reversed band title; `route-code`, `value-block`, `issuer-strip` |
| H | high-chroma recreation graphic | `2.1:1`–`3.1:1` | dynamic title/image overlap, broad colour field, optional thin terminal | recreation graphic or cartoon; outlined/sign-painted title; `title-token`, `functional-label`, `memory-field` |
| I | transport fare ticket | `2.1:1`–`2.9:1` | vehicle/vessel image plus 20–35% fare, price, or serial zone | engraving or screenprint; brush/block title + mechanical fare; `transport-fare` |
| J | calligraphic field | `2.4:1`–`3.0:1` | 50–75% typography field, one small dark vignette, optional Roman footer | brush calligraphy + sparse engraving; `title-token` or `memory-field` |
| K | banknote and seal slip | `2.3:1`–`2.8:1` | guilloche ground, seal cartouche, small scenic or object insert | engraving/halftone, seal-script display, stamped value; `value-block`, `issuer-strip` |
| L | minimal emblem panorama | `2.5:1`–`3.1:1` | one fine frame, one low panorama or symmetric emblem, large open title zone | clean screenprint/engraving, geometric vertical or spaced title; `title-token` |

## Vertical families

| ID | Archetype | Ratio | Spatial allocation | Compatible image/type/grammar |
|---|---|---:|---|---|
| M | scenic bookmark | `1:2.5`–`1:3.7` | 60–80% tall scenic column, title on edge or base, compact value/serial foot | engraving, woodcut, painterly/halftone insert; vertical title; `value-block`, `functional-label`, `title-token` |
| N | souvenir card | `1:1.7`–`1:2.2` | framed image or decorative panel, small caption/price base | folk colour, portrait medallion, ornament, cartoon; expressive title; `memory-field`, `title-token` |
| O | dark decorative pass | `1:1.7`–`1:3.3` | saturated dark field, one knockout figure/motif, small header/footer | cut-paper, ornamental collage, woodcut; seal/calligraphy/art-deco Roman; `title-token`, `value-block` |
| P | vertical administrative register | `1:2.6`–`1:3.7` | repeated serial/title cells, stacked vignettes, or striped lower coupon | fine engraving or institutional screenprint; condensed vertical type + mono number; `coupon-pair`, `issuer-strip`, `route-code` |

## Selection weights

When orientation is not specified, use the corpus-level `56% horizontal / 44% vertical` split. Within an orientation, do not weight every family equally:

- frequent: `C`, `F`, `M`, `P`;
- medium: `B`, `G`, `H`, `I`, `N`, `L`;
- occasional: `A`, `D`, `E`, `J`, `K`, `O`.

Occasional families remain essential. Ensure at least one in every four successive outputs uses a medium or occasional family when enough conversation history is visible.

## Structural rules

- The archetype controls where the scene, title, ticket information, empty paper, and wear live. Do not keep the same top headline and right stub after switching archetypes.
- A stub appears only in `C`, `D`, `E`, `I`, or `P`, and even there it is not mandatory unless the grammar is `coupon-pair`.
- `J` and `L` deliberately allow almost no ticket-type phrase. Empty paper is part of the composition.
- An explicitly requested vertical ticket defaults to `M` or `P` at about `1:3`; never use a poster-like `3:5` ratio.
- An explicitly requested horizontal ticket must be redrawn around `A`–`L`; never crop a vertical card.
- Very long horizontal output above `4:1` is allowed only as a rare frieze variant of `F`, `I`, or `L`.
- Keep user-supplied name/date in a small field compatible with the family. In a sparse `J` or `L` ticket, one quiet dedication line can replace an administrative box.

