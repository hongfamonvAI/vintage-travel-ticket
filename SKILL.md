---
name: vintage-travel-ticket
description: Turn a user-supplied travel, landscape, city-street, personal-memory, object, transport, or food photo into one finished vintage Chinese ticket using a detailed design grammar distilled from 66 historical ticket references without distributing the private images. Use when the user asks for an old ticket, vintage admission ticket, retro travel coupon, scenic-area ticket, food tasting ticket, or wants a photo transformed into a 20th-century Chinese printed-ticket design. Randomly select a coherent structural archetype, illustration language, palette, paper, typography, information grammar, and print-ageing profile; verify the official place or food name before generating.
---

# Vintage Travel Ticket

Create a single finished travel, city-memory, object, transport, or food ticket that feels like a real mid-to-late 20th-century Chinese printed coupon. The public skill contains a reference-distilled design system rather than the private source images.

Always read [references/design-grammar.md](references/design-grammar.md), [references/ticket-style-system.md](references/ticket-style-system.md), and [references/visual-reference-routing.md](references/visual-reference-routing.md) before generating. Use the selected entries in [references/archetype-system.md](references/archetype-system.md), [references/palette-paper-system.md](references/palette-paper-system.md), [references/illustration-system.md](references/illustration-system.md), [references/typography-system.md](references/typography-system.md), and [references/print-ageing-system.md](references/print-ageing-system.md). Consult [references/corpus-design-index.md](references/corpus-design-index.md) only to diagnose repetition or find a less common precedent. Never reconstruct one index row literally.

## Default Generation

- Generate exactly one standalone ticket on the first pass and return exactly one finished version. Internal correction attempts are allowed, but expose only the final accepted ticket. Do not ask about color, dimensions, ratio, layout, typography, or style choices.
- Randomly select a reference-distilled archetype before every first pass. It determines whether the ticket is wide horizontal, compact horizontal, narrow vertical, or tall vertical; it also governs layout, print era, illustration approach, text hierarchy, information density, and compatible ageing. Never treat `8:3` as the permanent default.
- Respect a user-supplied format or ratio when one is explicit; otherwise keep the archetype's ratio.
- Repaint the source as an authored flat hand-drawn travel, city, memory, or food illustration; do not place a photograph under a retro filter.
- Treat the source photo as semantic evidence only: retain its landmark, scene type, and a few distinctive living subjects, but deliberately discard the original camera crop, perspective, photographic lighting, surface texture, exact stone/leaf detail, and one-to-one object placement.
- Preserve clearly visible place character before randomizing style: time of day, season, weather, ambient energy, signature light, and culturally recognisable mood are semantic anchors. Randomness may reinterpret their shapes and ink colours, but may not invert night into day, mist into hard sun, a festive crowd into an empty quiet scene, or a lush landscape into a sterile field unless the user asks.
- Select a restrained 2–4 colour spot-print recipe from the reference-distilled system before interpreting the subject. Let the photo decide subject matter and where tones fall, but never let its dominant colour force a green, brown, or any other default palette.
- Preserve the scene's key landmark, terrain, viewpoint, and atmosphere while simplifying it into printed illustration masses.
- Use Chinese as the primary language. Treat pinyin, English, and other Roman-letter place names as optional sampled fields, never as a completeness requirement. For mainland-Chinese destinations, default strongly toward Chinese-only historical ticket language; use pinyin or English only when the sampled language mode and the selected archetype both justify it. For overseas destinations, sample between Chinese-only and Chinese plus concise verified local-language accents. Those accents may be the official local name, established brand wording, city, neighbourhood/street, or supplied/verified year when they are genuinely relevant; use English only where it is locally appropriate. Keep them short and subordinate rather than turning the ticket into a bilingual poster.
- Make every ticket an original composition. Vary the title rail, stub location, frame treatment, small ornament, and spot-color arrangement without drifting into modern UI, glossy travel ads, or a generic postcard.

## Variation Engine

Before each new first-pass ticket, write a one-sentence **place-character brief** from the photo and verified destination context. Name two to four non-negotiable traits such as `night harbour / dense skyline lights / deep water reflections / glamorous urban energy`. Then run `python3 scripts/sample_ticket_recipe.py --subject <class> --orientation <any|horizontal|vertical> --region <mainland-cn|chinese-region|overseas> --mood <auto|day|night|dusk|misty|lush|warm|neutral>`. Add one `--avoid <profile>` for every recent profile visible in the conversation. Keep the brief and sampled recipe internal; do not ask the user to choose.

- Follow the sampled archetype, ratio, palette/paper, illustration, typography, information grammar, and ageing as one coupled design DNA. Do not independently reroll individual axes into an incoherent hybrid.
- Follow the sampled `language_mode`. `chinese-only` forbids a pinyin/English/local-name line; let a serial, value, seal, or code fill the Roman/number typography role instead. `chinese-plus-pinyin` permits accurate pinyin only. For an overseas destination, `chinese-plus-local` permits one to three concise verified local-language accents: the official local name or brand wording plus, when structurally useful, an established city, neighbourhood/street, or supplied/verified year. Do not translate decorative prose, invent slogans, or upgrade a Chinese-only draw to bilingual merely because the selected typography recipe contains a Roman example.
- Follow the sampled mood-compatible palette and compare the complete recipe against the place-character brief. If the archetype, paper, illustration language, or palette would erase or contradict a non-negotiable trait, reject the complete recipe and rerun the sampler; do not patch an incompatible pale/daytime design with a few dark accents.
- For an unmistakable night source, require a nocturnal reading: dark or saturated field, knockout lights or high-contrast spot accents, and visible light-on-water/building rhythm when present. Never turn it into a white daytime panorama or restrained minimalist daylight ticket merely for variety.
- Use the photo only for semantic anchors: a bamboo ravine can validly appear in cobalt and vermilion, plum and ochre, or jade and scarlet, not only naturalistic greens.
- Randomize the selection for a new ticket. If a prior ticket is visible in the same conversation, choose a different archetype and change at least **four** of aspect ratio, palette/paper, title position, illustration treatment, ageing profile, information grammar, and typography recipe. Never repeat the immediately previous full combination or title silhouette. In particular, never make a category line such as `城市漫游券`, `海港纪念券`, or `山林游览券` the default information pattern.
- Fit the verified place or food name into the selected layout by scaling, wrapping, or moving title zones. Do not silently collapse every design into the same top-title-plus-right-stub arrangement, hand-drawn temple picture, or standard `副券 + NO.` pattern.

## Visual Reference Layer

After the recipe sampler returns a profile, run `python3 scripts/select_style_references.py --profile <sampled-profile> --count 2`. Keep its JSON internal.

- In `public-contact-sheet` mode, attach only the one returned low-resolution historical style sheet and use the returned `reference_ids` to locate the relevant anonymous cells. Every cell shows a complete uncropped ticket at its original aspect ratio.
- In `public-hybrid` mode, attach the returned low-resolution historical style sheet and the one high-resolution generated-ticket contact sheet. Use the historical sheet for period structure and print logic, and use the generated sheet only to understand the breadth of successful complete executions. Never inherit any generated cell's destination, subject, wording, exact title silhouette, serial, or one-for-one layout.
- In `private-enhanced` mode, attach only the returned one or two private images. Do not also attach a contact sheet and do not inspect the rest of the private directory.
- Treat every routed image as style evidence only. The uploaded user photo remains the sole source of subject identity and scene content.
- The public generated-ticket library contains one authorised, metadata-stripped high-resolution contact sheet of complete generated outputs rather than individual routed templates. It may strengthen public GitHub generations, but it must remain a secondary range precedent so the system does not recursively collapse into its own prior layouts.
- The public generated-ticket library is strictly ticket-only. Never add, index, route, or attach a source photograph there. Files under `examples/` are README display material only and must never be read by the style selector or used as visual style references.
- Do not expose, return, publish, package, or describe a private filename or local private path. The private 66-image corpus must remain outside Git history.

## Subject and Ticket-Type Lexicon

Classify the supplied photo before selecting ticket language. Keep the classification internal and let it affect the ticket type, subject treatment, and information fields.

- **Scenic area / landscape**: if a category label is selected, choose from `游览券`, `参观券`, `纪念券`, `正券`, `检票联`, or `存根`.
- **City street / neighbourhood / personal travel view**: if a category label is selected, choose from `城市漫游券`, `旅人纪念券`, `街区漫游券`, or `留念券`.
- **Food / dish / restaurant meal**: if a category label is selected, choose from `食味券`, `品鉴券`, `尝鲜券`, `餐叙券`, or `风味纪念券`. Make the verified dish name the title; use a dish, vessel, ingredient, or dining-scene motif rather than a scenic landmark.

All category labels are optional; use them only when the selected reference archetype and information grammar calls for one. Do not use a scenic-area label for a food photo by default, or turn a food ticket into a restaurant menu, product label, or packaged-food advertisement.

## Information Grammar Selection

Before composing text, choose exactly one reference-derived grammar. A ticket-type phrase is not a required field.

1. **Title token**: place name/dish name plus one of pinyin/local wording, serial, seal, or value mark; no category line. Even here, retain one compact mechanical ticket signal when the selected archetype is at risk of reading as a poster.
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
3. Use the source and the official/authoritative destination page to identify the location's relevant signature character without replacing the photo with a generic stereotype. When the photo clearly shows night, rain, mist, snow, blossom, festival colour, or another strong condition, the photo wins and that condition enters the place-character brief.
4. Use the verified Chinese place or dish name as the ticket's main title. Determine the region as `mainland-cn`, `chinese-region`, or `overseas`, determine the source mood, then pass both to the sampler. Do not print a Roman line unless the sampled language mode permits it.
5. When `chinese-plus-pinyin` is sampled, use verified official pinyin when available; otherwise transliterate the verified Chinese name correctly without tone marks. When `chinese-plus-local` is sampled, use the verified official local-language or Roman-letter name. Never substitute English automatically for every destination.
6. If the user voluntarily supplies a name and/or date in this first reply, place it in a small authentic field such as `持票人`, `旅人`, `留念日`, or a dedication line. Preserve names exactly. For an unambiguous full Gregorian date, standardize its display as zero-padded `YYYY.MM.DD` before printing: for example, `2026.5.01` becomes `2026.05.01`, and `2026-5-1` becomes `2026.05.01`. Preserve the date's meaning; do not add a date when it was not supplied, and do not guess an incomplete or ambiguous date.
7. If multiple places/dishes could match, or no authoritative source verifies the name, ask only for the province/city, dish/restaurant, or an official link. Do not guess, shorten, or fabricate a place, dish, or organization name.
8. If the user supplied both a clearly identified subject and an official name/link, skip the question and verify it directly.

## Ticket Construction

Build exactly one ticket from these layers.

1. **Paper and ink age**: apply the sampled paper stock and exactly two primary ageing events to the *printed content*, not only the background. Paper may be warm white, cool gray-white, cream, pale tinted stock, saturated colour stock, or banknote-like stock. Keep wear print-process plausible—not a uniform grunge overlay or default kraft filter.
2. **Subject illustration**: redraw the source using the sampled illustration language, not a generic hand-drawn conversion. Reduce it to three to seven graphic masses and preserve recognition through two to four anchors. Depending on the selection, use engraving, screenprint, naïve souvenir colour, woodcut, map/schema, specimen plate, cut-paper silhouette, recreation graphic, halftone insert, calligraphic landscape, modular vignettes, cartoon emblem, or ornamental collage.
3. **Information hierarchy**: set the verified destination or dish name as the largest text only when the archetype calls for it. Apply the selected information grammar; add one ticket-type phrase only when that grammar calls for it. `副券` is optional, not a standard field.
4. **Ticket details**: generate the archetype's plausible decorative metadata: choose 0–5 of ticket number, price/value, validity instruction, gate/checking label, category, printed code, date-like code, small seal, issue mark, or a user-supplied name/date, provided the selected grammar still reads as a ticket. Add pinyin or Roman/local wording only when the sampled language mode permits it; for overseas `chinese-plus-local`, allow one to three concise verified accents rather than only a translated destination footer. Print every unambiguous user-supplied date in the canonical `YYYY.MM.DD` format. Do not claim a historical fact, official price, real date, or real issuing organization unless verified or supplied by the user.
5. **Typography**: select one complete recipe from [references/typography-system.md](references/typography-system.md): a title face, information face, and Latin/serial face with their visual construction and placement. Make the contrast between those roles visible. Use period-appropriate Chinese display lettering, compact printed characters, occasional vertical setting, small pinyin/Roman text, rules, boxed fields, and a limited ornamental device. Keep the text legible and correctly spelled. Before prompting a multi-line title, segment the verified name into inseparable semantic units and state the intended line breaks explicitly. Break only between units; resize, re-space, or move the title rather than splitting a proper name or fixed phrase. For example, set `城市之光书店` as `城市之光 / 书店`, never `城市之 / 光书店`.

## Ticket Recognisability Gate

Before prompting, specify a ticket-evidence set. The finished design must contain at least one **structural signal** and one **administrative signal**, integrated into the selected archetype rather than pasted on as decoration.

- Structural signals: purposeful outer frame/cut edge, serial cell, stub/perforation, value corner, seal block, footer band, side rail, title cap, route index, or a bounded image-plus-information division.
- Administrative signals: mechanical ticket number, value/price mark, checking/gate field, punch or stamp evidence, coupon label in a true coupon structure, compact issue/code field, or user-supplied holder/date.
- For sparse `J` or `L` tickets and broad-field `H` recreation graphics, do not rely on proportion and aged paper alone. Add a quiet but unmistakable mechanical number/value/check field and a purposeful frame, rail, terminal, or footer band.
- A category phrase such as `纪念券` is not required and must not be used merely to pass this gate.
- Reject and rebuild if removing the outer crop would make the composition read equally well as a poster, postcard, book cover, product label, or menu.

## Required Avoids

- Do not ask initial preference questions about color, size, ratio, template, typography, or style.
- Do not copy literal words, logos, serial numbers, seals, landmarks, or one-for-one layout from any source or index precedent.
- Do not use contemporary app cards, QR codes, glossy gradients, 3D product renders, photorealism, neon cyberpunk, or generic scrapbook decoration.
- Do not merely place a clean line drawing or a near-1:1 photographic translation on aged paper. A source-aligned crop, realistic depth, individually rendered leaves/rocks, continuous smooth shading, or texture fidelity high enough to reconstruct the photograph fails.
- Do not limit ageing to beige paper, a darkened border, or a single noise layer. The title, illustration, rules, seal, and serial number must all show selectively imperfect ink coverage while remaining legible.
- Do not treat one generic bold Song-style headline, one generic small Song body, and one generic serial treatment as the permanent house style. Do not set every visible field in one face. Select and visibly execute the selected archetype's typography recipe.
- Do not force `城市漫游券`, `海港纪念券`, `山林游览券`, `食味券`, or any other category phrase onto every design. Empty space is not missing information; let the reference-selected grammar decide whether a category label appears at all.
- Do not make up a place or dish name, pinyin spelling, government organization, user name, user date, or historical claim.
- Do not add English or pinyin to every ticket. In particular, do not make mainland-Chinese scenic tickets bilingual by default; a serial, value, route code, or seal can supply the contrasting mechanical type role.
- Do not choose title line breaks by character count alone. Never split an inseparable proper name or fixed phrase across lines; a visually balanced but semantically wrong wrap is a failed title.
- Do not sacrifice the source's time of day, weather, seasonal cue, signature lighting, or destination-specific atmosphere for random variation. A different print style is valid; a different place identity is not.
- Do not place excessive text over the scene or allow the ticket to read as a poster rather than an admission ticket.
- Do not let a large title plus one uninterrupted illustration occupy the design without a separate ticket-evidence set. Long proportion, rounded corners, aged paper, or a decorative border alone do not make a ticket.
- Do not load the full private corpus or all public contact sheets for one generation. Use only the selector output: at most two private references, or one low-resolution historical sheet plus the one high-resolution generated-ticket sheet.
- Do not use README comparison photos, user-source examples, or any file named as a source/original photo as style references. Only routed historical sheets, private historical tickets, and finished generated old-ticket images are eligible.
- Do not publish, display, return, package, or offer the private reference corpus for download.
- Do not create or return multiple ticket variants, alternative concepts, front-and-back views, before/after comparisons, contact sheets, grids, diptychs, or two tickets on one canvas. One request produces one standalone ticket image unless the user explicitly asks for multiple deliverables.

## Second-Round Editing

Enter this mode only when the user explicitly asks to change or add something after a ticket exists.

- If the user asks to add their name but does not provide it, ask only: `请提供希望印在票上的名字。`
- Put the supplied name in a small authentic ticket field such as `持票人`, `旅人`, or a dedication line; preserve the verified destination name and the overall ticket system.
- Accept explicit edits to text, color, date, ticket type, or size. Normalize any unambiguous user-supplied date to `YYYY.MM.DD`. Ask only for information essential to the requested edit.
- When the user explicitly requests a vertical ticket, make an M- or P-family **long-strip ticket**, not a poster: default to width:height `1:3` and keep within the reference-derived `1:2.5`–`1:3.7` range unless the user supplies an exact ratio. Use a title rail, long scenic strip, stacked compartments, or narrow register appropriate to this format. The shorter N-family souvenir card is allowed only when it is a random first pass or when the user specifically asks for a card. Never use `3:5` for a vertical ticket.
- Preserve all untouched elements and produce one revised ticket.

## Quality Check

Before returning the image, confirm that exactly one physical ticket appears on the canvas and exactly one final image will be returned; if the model creates duplicate tickets, two variants, a front/back pair, or a comparison layout, reject it and regenerate internally. Also confirm that the output follows the sampled design signature, `language_mode`, and place-character brief unless the user explicitly edited them; an explicitly requested vertical ticket is a long strip (`1:2.5`–`1:3.7`, default `1:3`) rather than a poster; at least one structural ticket signal and one administrative ticket signal are plainly visible; the design would not still read primarily as a poster, postcard, book cover, product label, or menu if its outer crop were removed; the place or food name exactly matches an authoritative source; every multi-line title breaks only at verified semantic-unit boundaries; clearly visible night/day, weather, season, signature lighting, and ambient energy remain recognisable after stylisation; a mainland-Chinese ticket is Chinese-only unless the sampler explicitly selected pinyin or bilingual text; an overseas bilingual draw uses only concise verified local-language accents; the subject reads through two to four redesigned anchors rather than its original photographic layout; any user name is exact and any unambiguous date is normalized to `YYYY.MM.DD`; a ticket-type phrase is absent unless the grammar requires one; a new version changes at least four design axes; the selected typography recipe makes title, information, and serial/number visibly different systems even when no Roman line is present; ticket metadata does not collapse into a permanent `副券 + NO.` pair; exactly two primary ageing events are visible across artwork and typography as well as paper; and every required text string is legible.
