# Old Chinese Ticket Style System

This is the compact visual specification. It is derived from an anonymous 66-ticket design index and does not require the private images at generation time.

Read [design-grammar.md](design-grammar.md) first. Then use [archetype-system.md](archetype-system.md), [palette-paper-system.md](palette-paper-system.md), [illustration-system.md](illustration-system.md), [typography-system.md](typography-system.md), and [print-ageing-system.md](print-ageing-system.md) as the compatible design axes. Consult [corpus-design-index.md](corpus-design-index.md) only when diagnosing repetition or needing a less common structural precedent.

## Corpus proportions

- 66 valid source tickets: 37 horizontal, 29 vertical.
- Common horizontal ratios: `2.4:1`–`3.1:1`; compact cards can be near `2:1`; rare friezes reach `4.7:1`.
- Vertical tickets split between souvenir cards (`1:1.7`–`1:2.2`) and long strips (`1:2.4`–`1:3.7`).
- A user-requested vertical ticket defaults to `1:3`, not `3:5`.
- A user-requested horizontal ticket is a full redesign, not a crop of a vertical ticket.

## Design constants

- Build one physical ticket with a scene/image zone and zero or one administrative zone. The administrative zone can be a stub, value corner, seal block, serial third, footer band, side rail, title cap, route index, or absent.
- Preserve meaningful paper. Formal and scenic families usually leave 20–45% of the ticket unprinted; high-chroma families may use solid fields.
- Use two to four spot inks. Paper is an active colour.
- Draw rules with purpose: division, inspection, value, serial, perforation, or frame. Do not decorate every empty area with boxes.
- Let typography sometimes dominate. The corpus includes tickets where calligraphy, a vertical title, a band headline, or a seal cartouche carries more weight than the picture.

## Source transformation

- Treat the uploaded photo as semantic evidence only. Retain two to four recognition anchors and rebuild the scene inside the selected archetype.
- Treat clearly visible time of day, weather, season, signature lighting, and ambient energy as recognition anchors too. Stylisation may simplify them but must not invert them.
- Write a compact place-character brief before sampling. Use the photo first; use verified destination context only to sharpen relevant traits, not to impose a generic tourist stereotype.
- Simplify foliage, crowds, stones, food texture, signs, and architectural repetition into large printed masses.
- Change crop, viewpoint, spatial depth, and object scale when needed. A source-aligned tracing fails even when it has an old-paper filter.
- Keep a person recognisable through hair, clothing silhouette, pose, and one accessory, but translate them through the selected illustration language.
- Make food a ticket subject through vessel, ingredients, cutaway, specimen label, or dining vignette—not product packaging.

## Information density

Choose zero to five secondary fields. Plausible fields include serial, value, price, pinyin/Romanization, check mark, gate, route, issue strip, seal, coupon label, holder, or user-supplied date.

- `副券`, `存根`, and `正券` appear only in a true detachable or register structure.
- A generic category phrase is never filler. `城市漫游券`, `纪念券`, `食味券`, and similar labels are optional.
- Never fabricate an official issuer, historical price, official seal, or date.
- An invented decorative value may be typographically plausible only when it is clearly non-factual; do not present it as an official current price.
- Preserve user names exactly and normalize unambiguous dates to `YYYY.MM.DD`.

## Geographic language selection

Treat language presence as a sampled design axis, not a mandatory footer.

| Region | Default weighting | Allowed secondary language |
|---|---|---|
| mainland China | strongly Chinese-only: approximately 80%; pinyin or verified bilingual text approximately 20% combined | pinyin or verified official Roman/local name only when sampled and structurally useful |
| Hong Kong, Macau, Taiwan, or another Chinese-language region | balance Chinese-only and locally plausible bilingual treatment | verified official local Roman name or established bilingual signage |
| overseas destination | sample between Chinese-only Chinese-travel ephemera and Chinese plus concise verified local-language accents | official local name or brand wording; when relevant, established city, neighbourhood/street, or supplied/verified year; not automatic English translation |

- `chinese-only`: print no pinyin, English, French, or other destination translation. Use serials, values, dates, seals, or route codes for Latin/numeral contrast.
- `chinese-plus-pinyin`: add accurate pinyin only; do not substitute an English translation.
- `chinese-plus-local`: for an overseas destination, add one to three concise verified local-language accents. Prefer the official local name or brand wording; optionally add an established city, neighbourhood/street, or supplied/verified year when it improves the ticket structure. Keep these subordinate to the Chinese title and never invent slogans or paragraph copy.
- A typography recipe mentioning a Roman footer describes a possible visual role, not a requirement to include English.
- Never add English to a mainland-Chinese scenic ticket merely because the image model or prompt template expects a bilingual travel design.

## Authentic oldness

- Age paper and ink together. Use two plausible events from [print-ageing-system.md](print-ageing-system.md).
- White and saturated tickets may look old through ink loss, fold dirt, stamp ghosts, torn perforations, and sun fade; they do not need beige paper.
- Keep wear local and directional. A uniform grunge overlay, dark vignette, or kraft-paper cast is not enough.

## Ticket recognisability

Every ticket must pair at least one structural signal with at least one administrative signal.

- Structural: purposeful frame/cut edge, serial cell, stub/perforation, value corner, seal block, footer band, side rail, title cap, route index, or bounded image/information division.
- Administrative: ticket number, value/price, checking/gate field, punch/stamp evidence, true coupon label, compact issue/code field, or user-supplied holder/date.
- Sparse and high-chroma designs are not exempt. A broad colour field, long ratio, rounded corners, or aged paper without a mechanical ticket field reads as a poster and must be rebuilt.
- Do not force a generic category phrase merely to create ticket character; use the selected grammar's number, value, checking, route, holder, or code logic instead.

## Anti-collapse checks

Reject and rebuild when any two of these are true:

- centred horizontal Song headline repeats the prior ticket;
- right-side stub repeats without structural reason;
- cream paper and green/red palette repeat by habit;
- illustration is a clean near-1:1 tracing of the photo;
- all information uses one type family;
- “纪念券” or another category phrase appears only to fill space;
- a mainland-Chinese destination receives English or pinyin despite a `chinese-only` draw;
- a night, mist, rain, snow, blossom, festival, or other obvious source condition is replaced by a contradictory generic atmosphere;
- ageing affects the paper but not the printed content;
- the result reads as a poster, postcard, product label, or menu instead of a ticket.
- the result lacks either a structural ticket signal or an administrative ticket signal.
