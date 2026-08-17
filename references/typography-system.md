# Vintage Ticket Typography System

Typography is a three-role system, not one “old font.” Choose a complete recipe and describe letter construction, orientation, spacing, field relationship, and wear. Font names are visual anchors only; the image must still look printed and period-specific.

## Contents

- [Role system](#role-system)
- [Verified visual anchors](#verified-visual-anchors)
- [Typography recipes](#typography-recipes)
- [Title fitting](#title-fitting)
- [Print behaviour](#print-behaviour)

## Role system

1. **Destination/dish title** — the dominant silhouette. It may be formal, hand-painted, outlined, calligraphic, seal-like, or reversed out of a colour field.
2. **Ticket information** — quieter labels for price, coupon, issuer, holder, date, entry, or directions. It must not be an enlarged copy of the title face.
3. **Romanization/number** — mechanical, geometric, scientific, typewriter-like, or stamped. It must feel separately typeset.

Every output must make all three roles visibly different when all three are present. A sparse ticket may omit role 2 or 3, but may never use one generic Song face for every visible field.

## Verified visual anchors

| Anchor | Corpus use | Construction to describe |
|---|---|---|
| Noto Serif SC / Noto Serif CJK | formal Song/Ming title and compact official text | strong verticals, fine modulated horizontals, small triangular terminals, letterpress softness |
| Zhuque Fangsong | Republican book-ticket title or narrow information | tall tight proportions, right-lower visual centre, compact counters, sweeping撇捺, visible metal-type flavour |
| Noto Sans SC / Noto Sans CJK | institutional labels and heavy admin blocks | uniform squared strokes, compact spacing, stable knockout shapes |
| LXGW WenKai | Kai-like scenic caption and personal-memory line | handwritten but orderly skeleton, open counters, calm human rhythm; never use as every field |
| ZCOOL XiaoWei | decorative old-display or museum title | small flared terminals, compact literary display, slightly quirky lead-type silhouette |
| ZCOOL QingKe HuangYou | 1970s–1980s condensed display and band lettering | tall narrow geometric skeleton, blunt corners, strong vertical rhythm |
| Ma Shan Zheng | short hand-painted scenic title | upright sign-brush pressure changes, dry gaps, legible non-cursive rhythm |
| Noto Sans Mono / Noto Sans Mono CJK SC | serial, date, pinyin, ticket code | monospaced mechanical construction, imperfect baseline, selective ink loss |

Primary sources: [Noto CJK](https://github.com/notofonts/noto-cjk), [Zhuque Fangsong](https://github.com/TrionesType/zhuque), [LXGW WenKai](https://github.com/lxgw/LxgwWenKai), [ZCOOL XiaoWei](https://fonts.google.com/specimen/ZCOOL+XiaoWei), [ZCOOL QingKe HuangYou](https://fonts.google.com/specimen/ZCOOL+QingKe+HuangYou), and [Ma Shan Zheng](https://fonts.google.com/specimen/Ma+Shan+Zheng).

## Typography recipes

| ID | Destination title | Information | Roman/serial | Structural behaviour |
|---|---|---|---|---|
| T01 editorial stencil | custom heavy stencil/wood-sign display with intentional cut gaps | tiny neutral Song/Ming | tall mono vertical number | title shares space with a figure; serial isolated in ruled cell |
| T02 formal band | centered white Song/Ming or squared sans knockout | tiny condensed neutral labels | geometric uppercase Roman line | title lives inside a dominant colour band with generous top/bottom rules |
| T03 folk hand-lettered | Kai-like or restrained brush title, uneven baseline | compact Fangsong labels | loose spaced Romanization and rubber number | title may sit inside the drawing; avoid polished digital centring |
| T04 scientific plate | condensed industrial Chinese label, often vertical | tiny formal specimen words | italic serif Latin name + mono number | multiple scales, strict label-window relationship |
| T05 coupon ledger | modest Song/Ming destination, sometimes not largest | large bold administrative word in stub | duplicated mono serial/value | obvious contrast between formal main field and blunt coupon field |
| T06 outlined recreation | thick outlined, shadowed, rounded or squared custom title | plain compact sans | condensed slanted/uppercase Roman | title acts as graphic image; two-colour outline must show registration wear |
| T07 black calligraphic | expressive but legible brush title, two to six characters per line | tiny formal heading or none | wide geometric Roman footer or small seal | title may occupy 40–70% of the ticket and need not sit at top |
| T08 reverse knockout | white/cream title knocked out of saturated field | tiny same-colour dark labels outside field | mechanical number in separate pale zone | preserve strong positive/negative contrast; do not outline every glyph |
| T09 Republican book-ticket | Zhuque-Fangsong-like tall title, horizontal or vertical | small Song/Ming lead type | thin serif Romanization + stamped code | narrow rail, framed cartouche, or literary souvenir strip |
| T10 seal and banknote | square seal-script/clerical cartouche as main title | plain vertical caption | stamped price and checking mark | guilloche ground, title behaves like an emblem rather than headline |
| T11 art-deco souvenir | medallion, geometric display, or tall condensed title | delicate narrow Fangsong | geometric bilingual footer | saturated dark card, metallic line, coloured terminal band |
| T12 minimalist vertical | one huge geometric vertical title or two widely spaced words | tiny price only | optional fine mono | scene remains low and quiet; title column is the main balance mass |
| T13 museum portrait | small seal/display title above or below portrait | compact serif museum line | widely spaced uppercase museum name | portrait frame and bilingual footer establish hierarchy |
| T14 route/map label | sturdy compact block title on side rail | many tiny map labels | code, arrows, index figures | no huge centred headline; type follows map topology |
| T15 playful signboard | irregular painted display or mascot-integrated title | neutral printed price/issuer | condensed bright Latin word | aquarium, zoo, food, or family scene; keep all Chinese readable |
| T16 no-hero-title | destination set as modest caption, seal, or footer | one small functional field | number/value may be visually strongest | use when image/emblem or calligraphic atmosphere carries identity |

## Title fitting

- `2–4 Chinese characters`: allow T03, T07, T10, T11, T12, or T15; vertical, seal-like, or large display settings are viable.
- `5–7 characters`: prefer T01, T02, T06, T08, T09, or a two-line T07; reduce tracking before reducing legibility.
- `8+ characters`: use a narrow band, stacked two-line title, vertical rail, or split destination/descriptor. Never squeeze it into one giant Song headline.
- For Roman titles longer than 18 characters, use a narrow uppercase line, split at a natural hyphen/space, or place the Roman line in a footer. Do not let it compete with the Chinese title.
- Personal name and date stay in information or serial roles. They must never become the destination title.

## Print behaviour

- Vary orientation among horizontal, vertical, stacked, side-rail, cartouche, band, image-integrated, and footer settings.
- Apply dry ink or broken terminals selectively. Keep exact destination, user name, and date legible.
- Use slightly inconsistent tracking, a faint double impression, baseline wobble, or ink spread only when compatible with the recipe.
- Do not invent pseudo-Chinese characters as decoration. If the image model cannot render a nonessential small line correctly, omit that line rather than fabricate text.
- Never default to `bold Song title + small Song information + same Song number`. Run the fast silhouette check: if the title could be swapped with the immediately previous ticket without changing the composition, choose another recipe.

