---
name: vintage-travel-ticket
description: Turn a user-supplied travel, landscape, city-street, personal-memory, or food photo into one finished vintage Chinese ticket, using the bundled old-ticket reference library. Use when the user asks for an old ticket, vintage admission ticket, retro travel coupon, scenic-area ticket, food tasting ticket, or wants a photo transformed into a 20th-century hand-drawn Chinese ticket design. Randomly vary proportion, layout, print era, illustration language, palette, paper stock, and typography from the library; verify the official place or food name before generating.
---

# Vintage Travel Ticket

Create a single finished travel, city-memory, or food-tasting ticket that feels like a mid-to-late 20th-century Chinese printed coupon: hand-drawn spot-color illustration, aged paper or card, practical ticket typography, ruled fields, and a small amount of imperfect print character.

Read [references/ticket-style-system.md](references/ticket-style-system.md), [references/archetype-system.md](references/archetype-system.md), and [references/typography-system.md](references/typography-system.md) before generating. These public reference documents are the visual corpus: synthesize their shared visual language and never trace or reproduce a specific ticket's literal artwork, copy, marks, or layout. If a user adds their own private `assets/reference-tickets/` folder, treat it as supplementary inspiration only.

## Default Generation

- Generate one ticket on the first pass. Do not ask about color, dimensions, ratio, layout, typography, or style choices.
- Randomly select a reference-derived archetype before every first pass. It determines whether the ticket is wide horizontal, compact horizontal, narrow vertical, or tall vertical; it also governs its layout, print era, illustration approach, and text hierarchy. Never treat `8:3` as the permanent default.
- Respect a user-supplied format or ratio when one is explicit; otherwise keep the archetype's ratio.
- Repaint the source as an authored flat hand-drawn travel, city, memory, or food illustration; do not place a photograph under a retro filter.
- Treat the source photo as semantic evidence only: retain its landmark, scene type, and a few distinctive living subjects, but deliberately discard the original camera crop, perspective, photographic lighting, surface texture, exact stone/leaf detail, and one-to-one object placement.
- Select a restrained 2–4 color spot-print recipe from the bundled reference system before interpreting the landscape. Let the source photo decide subject matter and where tones fall, but never let its dominant color force a green, brown, or any other default palette.
- Preserve the scene's key landmark, terrain, viewpoint, and atmosphere while simplifying it into printed illustration masses.
- Use Chinese as the primary language. Add a pinyin or Roman-letter line only when it suits the chosen reference-inspired composition; its presence and placement may vary, but its spelling must be accurate.
- Make every ticket an original composition. Vary the title rail, stub location, frame treatment, small ornament, and spot-color arrangement without drifting into modern UI, glossy travel ads, or a generic postcard.

## Variation Engine

Before each new first-pass ticket, select one option from **every** axis in [references/ticket-style-system.md](references/ticket-style-system.md). Keep the selection internal; do not ask the user to choose.

- Select one archetype first, then its compatible palette/paper, layout, illustration treatment, ageing profile, information grammar, and typography recipe. The reference library—not the source photograph—supplies these choices.
- Use the photo only for semantic anchors: a bamboo ravine can validly appear in cobalt and vermilion, plum and ochre, or jade and scarlet, not only naturalistic greens.
- Randomize the selection for a new ticket. If a prior ticket is visible in the same conversation, choose a different archetype and change at least **three** of aspect ratio, palette/paper, layout, illustration treatment, ageing profile, information grammar, and typography recipe. Never repeat the immediately previous full combination or the immediately previous title/body/serial type pairing. In particular, never make a category line such as `城市漫游券`, `海港纪念券`, or `山林游览券` the default information pattern.
- Fit the verified place or food name into the selected layout by scaling, wrapping, or moving title zones. Do not silently collapse every design into the same top-title-plus-right-stub arrangement, hand-drawn temple picture, or standard `副券 + NO.` pattern.

## Subject and Ticket-Type Lexicon

Classify the supplied photo before selecting ticket language. Keep the classification internal and let it affect the ticket type, subject treatment, and information fields.

- **Scenic area / landscape**: if a category label is selected, choose from `游览券`, `参观券`, `纪念券`, `正券`, `检票联`, or `存根`.
- **City street / neighbourhood / personal travel view**: if a category label is selected, choose from `城市漫游券`, `旅人纪念券`, `街区漫游券`, or `留念券`.
- **Food / dish / restaurant meal**: if a category label is selected, choose from `食味券`, `品鉴券`, `尝鲜券`, `餐叙券`, or `风味纪念券`. Make the verified dish name the title; use a dish, vessel, ingredient, or dining-scene motif rather than a scenic landmark.

All category labels are optional; use them only when the selected reference archetype and information grammar calls for one. Do not use a scenic-area label for a food photo by default, or turn a food ticket into a restaurant menu, product label, or packaged-food advertisement.

## Information Grammar Selection

Before composing text, choose exactly one reference-derived grammar. A ticket-type phrase is not a required field.

1. **Title token**: place name/dish name plus one of pinyin, serial, seal, or value mark; no category line.
2. **Price / value block**: title plus a boxed value, code, or check field; omit a category line unless it is structurally necessary.
3. **Coupon pair**: `正券` / `副券` or `存根` only when the physical perforated-pair archetype is selected.
4. **Functional label**: use a single category phrase such as `参观券`, `食味券`, or `检票联` only when it matches the chosen archetype.
5. **Memory field**: title plus user-supplied `旅人` / `持票人` / `留念日`; this can stand alone without a category phrase.
6. **Route / code card**: title plus route mark, gate/check word, direction arrow, or printed code; no category line.

Across successive outputs, rotate this grammar as aggressively as palette and layout. Do not insert a generic `城市漫游券` or `纪念券` merely to fill empty space.

## Name Verification Gate

On a first-generation request, use this sequence.

1. If the user did not state the scenic area, destination, or food name, ask only: `这张票对应的景区/地点或美食名称是哪里？如想在票面留下你的名字或日期，也可以一并告诉我。` Stop and wait.
2. After the user supplies a place, search for its canonical Chinese name. Prefer the attraction's official website; otherwise use a government culture-and-tourism, park-administration, museum, or other authoritative public page. For food, verify the conventional dish name using an official food standard, government culture/tourism source, industry authority, or the restaurant's official source when the user identifies a specific restaurant.
3. Use the verified Chinese place or dish name as the ticket's main title. If an official Romanization is available, prefer it; otherwise transliterate the verified Chinese name correctly without tone marks.
4. If the user voluntarily supplies a name and/or date in this first reply, place it in a small authentic field such as `持票人`, `旅人`, `留念日`, or a dedication line. Preserve names exactly. For an unambiguous full Gregorian date, standardize its display as zero-padded `YYYY.MM.DD` before printing: for example, `2026.5.01` becomes `2026.05.01`, and `2026-5-1` becomes `2026.05.01`. Preserve the date's meaning; do not add a date when it was not supplied, and do not guess an incomplete or ambiguous date.
5. If multiple places/dishes could match, or no authoritative source verifies the name, ask only for the province/city, dish/restaurant, or an official link. Do not guess, shorten, or fabricate a place, dish, or organization name.
6. If the user supplied both a clearly identified subject and an official name/link, skip the question and verify it directly.

## Ticket Construction

Build exactly one ticket from these layers.

1. **Paper and ink age**: apply the archetype's paper stock and ageing profile to the *printed content*, not only the background. Paper may be bright white, cool gray-white, cream, faded pink, pale jade, saturated green/blue, or dark card. Use archetype-appropriate wear: dry ink, offset passes, rubbed strokes, faded exposure, folds, stamp ghosts, pinholes, edge softness, or tiny foxing. Keep it print-process plausible—not a uniform grunge overlay or a default kraft filter.
2. **Subject illustration**: redraw the source using the archetype's illustration language, not a generic hand-drawn conversion. Depending on the selection, it may be sparse line engraving, flat screenprint, naïve souvenir illustration, woodcut massing, decorative cartoon, route-map graphic, black-and-gold ink image, or ornamental collage. For food, use dish and vessel anchors; for a place, use landscape or city anchors. Preserve recognition through a few anchors, never through photographic object-for-object replication.
3. **Information hierarchy**: set the verified destination or dish name as the largest text only when the archetype calls for it. Apply the selected information grammar; add one ticket-type phrase only when that grammar calls for it. `副券` is optional, not a standard field.
4. **Ticket details**: generate the archetype's plausible decorative metadata: choose 0–5 of ticket number, price/value, validity instruction, gate/checking label, category, printed code, date-like code, pinyin, Roman line, small seal, issue mark, or a user-supplied name/date, provided the selected grammar still reads as a ticket. Print every unambiguous user-supplied date in the canonical `YYYY.MM.DD` format. Do not claim a historical fact, official price, real date, or real issuing organization unless verified or supplied by the user.
5. **Typography**: select one complete recipe from [references/typography-system.md](references/typography-system.md): a title face, information face, and Latin/serial face with their visual construction and placement. Make the contrast between those roles visible. Use period-appropriate Chinese display lettering, compact printed characters, occasional vertical setting, small pinyin/Roman text, rules, boxed fields, and a limited ornamental device. Keep the text legible and correctly spelled.

## Required Avoids

- Do not ask initial preference questions about color, size, ratio, template, typography, or style.
- Do not copy literal words, logos, serial numbers, seals, landmarks, or one-for-one layout from any bundled reference ticket.
- Do not use contemporary app cards, QR codes, glossy gradients, 3D product renders, photorealism, neon cyberpunk, or generic scrapbook decoration.
- Do not merely place a clean line drawing or a near-1:1 photographic translation on aged paper. A source-aligned crop, realistic depth, individually rendered leaves/rocks, continuous smooth shading, or texture fidelity high enough to reconstruct the photograph fails.
- Do not limit ageing to beige paper, a darkened border, or a single noise layer. The title, illustration, rules, seal, and serial number must all show selectively imperfect ink coverage while remaining legible.
- Do not treat one generic bold Song-style headline, one generic small Song body, and one generic serial treatment as the permanent house style. Do not set every visible field in one face. Select and visibly execute the selected archetype's typography recipe.
- Do not force `城市漫游券`, `海港纪念券`, `山林游览券`, `食味券`, or any other category phrase onto every design. Empty space is not missing information; let the reference-selected grammar decide whether a category label appears at all.
- Do not make up a place or dish name, pinyin spelling, government organization, user name, user date, or historical claim.
- Do not place excessive text over the scene or allow the ticket to read as a poster rather than an admission ticket.

## Second-Round Editing

Enter this mode only when the user explicitly asks to change or add something after a ticket exists.

- If the user asks to add their name but does not provide it, ask only: `请提供希望印在票上的名字。`
- Put the supplied name in a small authentic ticket field such as `持票人`, `旅人`, or a dedication line; preserve the verified destination name and the overall ticket system.
- Accept explicit edits to text, color, date, ticket type, or size. Normalize any unambiguous user-supplied date to `YYYY.MM.DD`. Ask only for information essential to the requested edit.
- When the user explicitly requests a vertical ticket, make an H-family **long-strip ticket**, not a poster: default to width:height `1:3` and keep within the reference-derived `1:2.5`–`1:3.7` range unless the user supplies an exact ratio. Use a title rail, long scenic strip, stacked compartments, or a narrow detachable stub appropriate to this format. The shorter I-family souvenir card is allowed only when it is a random first-pass archetype or when the user specifically asks for a card. Never use `3:5` for a vertical ticket.
- Preserve all untouched elements and produce one revised ticket.

## Quality Check

Before returning the image, confirm that the output follows the selected archetype's ratio and information grammar unless the user explicitly edited it; an explicitly requested vertical ticket is a reference-derived long strip (`1:2.5`–`1:3.7`, default `1:3`) rather than a poster; the place or food name exactly matches an authoritative source; the subject reads through a few redesigned place, street, or dish anchors rather than its original photographic layout; any user-supplied name is exact, any unambiguous user-supplied date is normalized to `YYYY.MM.DD`, and neither field appears when not supplied; a ticket-type phrase is absent unless the selected grammar requires one; the selected paper, palette, layout, and illustration language visibly differ from the prior ticket; the selected typography recipe makes title, information, and serial/pinyin different systems; ticket metadata does not collapse into a permanent `副券 + NO.` pair; ink wear is visible across artwork and typography, not only the paper; and every visible text string is legible.
