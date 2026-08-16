# Vintage Ticket Typography System

Derived from the bundled ticket corpus and matched to close, verifiable online type families. These are **visual anchors** for image generation: describe the construction, weight, spacing, print wear, and field role as well as the family name. Do not assume an image model can use an installed font merely because it is named.

## Role system

Every ticket must choose three distinct roles:

1. **Destination title**: the largest and most characterful lettering. It may be Song/Ming, Fangsong, black-letter display, or limited brush title lettering.
2. **Ticket information**: compact, quieter type for `参观券` / `游览券`, issue fields, stub labels, and directions. It must not be an enlarged copy of the title face.
3. **Pinyin, `NO.`, and serial**: narrow Latin or monospaced/technical print. It should feel mechanically set, overprinted, stamped, or typed—not like body copy.

Never make the three roles visually identical. Keep the verified scenic-area name fully legible even when its printed strokes are worn.

## Online font anchors

| Corpus cue | Closest online anchor | Use in ticket | Construction to describe to the image model |
|---|---|---|---|
| formal Song/Ming lead type | Noto Serif SC / Noto Serif CJK | dignified title, museum/park-style heading, compact supporting text | modulated Song/Ming strokes, fine horizontals, sturdier verticals, restrained triangular terminals, slightly uneven letterpress edges |
| Republican-era bookish Fangsong | Zhuque Fangsong (朱雀仿宋) | literary scenic title or small information field | tall condensed proportion, tight inner space, gentle brush modulation, relaxed dots and sweeping left/right strokes, lead-type softness |
| 1960s–1980s block title and administration labels | Noto Sans SC / Noto Sans CJK bold | heavy title band, `副券`, `存根`, boxed administrative labels | squared industrial grotesque forms, heavy even stroke, compact tracking, slightly compressed phototypeset or woodblock character |
| expressive hand-painted destination sign | Ma Shan Zheng-inspired brush display | **only** a 2–6-character main scenic title; never body or serial | upright brush-script title with changing pressure, dry-brush gaps, sign-painting rhythm; keep every character readable and do not make it cursive chaos |
| mechanical number/Latin overprint | Noto Sans Mono / Noto Sans Mono CJK SC | `NO.`, serial, date-like code, pinyin divider line | narrow monospaced, ink-stamped or typewriter-like characters, imperfect baseline and selective numeric ink loss |

Use the named anchors as close visual references, not as permission to copy an existing ticket's lettering. Noto CJK offers both Sans and Serif Chinese families and multiple weights; Zhuque Fangsong is a modern open-source Fangsong project based on `南宋` metal type. Source links: <https://github.com/notofonts/noto-cjk>, <https://github.com/notofonts/noto-docs/blob/main/docs/website/use.md>, <https://github.com/TrionesType/zhuque>, <https://fonts.google.com/specimen/Ma+Shan+Zheng>.

## Typography recipes

Select one recipe compatible with the archetype for every new first-pass ticket. Do not repeat the immediately previous recipe, even when the palette or place changes.

| Recipe | Destination title | Ticket information | Pinyin / serial | Best layout behavior |
|---|---|---|---|---|
| A — dignified Song print | Noto Serif SC-inspired high-contrast Song/Ming, spaced horizontal title | smaller Zhuque Fangsong-inspired vertical labels | fine mono `NO.` and serial | panoramic scenic panel with narrow stub |
| B — Republican book-ticket | Zhuque Fangsong-inspired title, vertical or slightly tall horizontal setting | small Noto Serif SC-style lead type | thin serif pinyin plus stamped numeric code | central vignette with a vertical title rail |
| C — block-print excursion | compact Noto Sans SC-inspired heavy title in a banner | tiny Song/Ming labels with thin rules | bold mono serial, occasional boxed digits | silhouette composition or detachable two-panel ticket |
| D — signboard souvenir | restrained Ma Shan Zheng-inspired scenic title, maximum six Chinese characters | strictly neutral Noto Serif SC-style fields | typewriter-like mono pinyin and `NO.` | asymmetrical map-like layout with generous paper space |
| E — engraved official pass | narrow Song/Ming title in a framed cartouche | compact Noto Sans SC-style administrative labels | overprinted mono number plus small serif Roman line | formal border, seal panel, and low scenic strip |
| F — woodcut exhibition ticket | tall condensed black-letter display title, vertical or stacked | Zhuque Fangsong-inspired small print | faint stamped mono number | dense woodcut scene with a tall title rail |
| G — folk souvenir print | painted shop-sign or rounded hand-lettered title | irregular compact lead-type labels | loose red-rubber serial or tiny Roman line | folk-story picture ticket or decorative coupon pair |
| H — recreation-era graphic | rounded or squared 1970s display title in a bright colour field | plain compact black type | condensed technical number | modern recreation graphic or coloured state-run ticket |
| I — ink bookmark | restrained calligraphic title with generous breathing space | delicate narrow Song/Ming or Fangsong | fine value mark and small seal text | landscape bookmark or black-gold ink slip |

## Execution rules

- Choose a typography recipe before drawing the ticket, alongside palette and layout. The choice must alter letterforms, title orientation, spacing, and the hierarchy of small fields—not merely switch the ink color.
- Rotate title orientation between horizontal, vertical, framed, bannered, and stacked forms when the selected recipe calls for it. Do not use a centered horizontal headline on every ticket.
- Use brush display only for a short verified Chinese destination title. Use ordinary printed type for all other Chinese fields, pinyin, and numbers.
- Vary not only the name of the title face but its visual mechanics: title orientation, stroke contrast, width, spacing, colour, baseline, and whether it sits in a band, rail, vignette, or open field. Never solve type variation by recolouring the same Song/Ming layout.
- Allow imperfect letterpress evidence: slightly dry title strokes, worn terminals, broken rules, faint double-impression, small tracking inconsistencies, and occasional stamp misregistration. Do not add illegible random noise.
- Keep pinyin accurate. Do not turn Roman letters into fake glyphs, decorative pseudo-type, or unreadable AI text.
- A user's future first-generation request must receive a recipe automatically. Never ask them to choose a font, palette, or layout.

## Fast visual QA

- Could the title silhouette be mistaken for the title on the immediately prior ticket? If yes, choose another recipe.
- Are title, information, and serial visibly different systems? If no, rebuild the type hierarchy.
- Is the title still readable at normal viewing size after ageing? If no, reduce wear before returning.
- Does the title style match an actual cue in the reference library—Song, Fangsong, block print, signboard brush, engraving, or mechanical numbering—rather than a default AI "vintage Chinese" font? If no, revise.
