# Typography and Layout v1.0

## Goal

Make semantic hierarchy visible with minimal decoding effort.

## Typeface

No universal serif/sans-serif winner.

Choose a typeface that:
- is highly legible at final size;
- has distinct regular/bold weights;
- has clear numerals and punctuation;
- embeds reliably in PDF;
- is available in the production toolchain;
- does not cause unusual glyph substitution.

Safe engineering defaults:
- Arial
- Helvetica
- Calibri/Aptos
- Source Sans
- Inter
- Georgia
- Charter
- other conventional families with reliable embedding

The list is not a scientific ranking.

## Hierarchy recipe

Use **at least two independent signals** for major hierarchy changes.

Example:
- Section heading = weight + whitespace
- Entry title = weight + position
- Metadata = smaller size + muted emphasis

Do not rely only on:
- color;
- all-caps;
- thin divider lines.

## Size

Starting range:
- body: 10.5–12 pt equivalent;
- metadata: not more than ~1 pt below body unless clearly legible;
- section: 11.5–14 pt equivalent;
- name: 16–24 pt equivalent.

These are engineering defaults.

If body must drop below ~10 pt equivalent to fit:
- first edit content/density;
- do not compress by typography alone.

## Line spacing

Starting range:
- body/bullets: 1.15–1.35×;
- tight metadata can be slightly denser;
- preserve enough vertical separation between semantic groups.

## Line length

Avoid:
- very long continuous lines;
- extremely narrow sidebars for essential text.

A CV bullet is scanned differently from prose; use adjacent line-length research as a readability constraint, not a fixed target.

## Alignment

Prefer:
- left-aligned body text;
- consistent date alignment;
- stable indentation.

Avoid full justification in dense CV text because spacing irregularity can reduce scan quality.

## Whitespace

Whitespace is structural.

Use it to distinguish:
- sections;
- entries;
- bullet groups.

Do not remove all whitespace to force one page.

## Color

Default:
- high-contrast text;
- restrained accent color if desired.

Never encode meaning only through color.

## Rules / borders

Use sparingly to clarify boundaries.

Avoid:
- boxed every section;
- excessive cards;
- decorative sidebars that fragment reading order.

## Icons

Icons may supplement text but cannot replace critical semantic labels.

Bad:
- envelope icon with no email text.

Good:
- readable email text, optionally preceded by a small icon.

## Multi-column

Two-column is a conditional technique.

Allowed for:
- low-risk secondary information;
- portfolios where layout benefit is meaningful;
- known parser/tested pipeline.

Do not put:
- chronology split across columns;
- employer/title on different visual streams;
- core evidence in narrow sidebars without extraction validation.
