# Typography and Layout v1.1

## Goal

Make semantic hierarchy visible with minimal decoding effort.

Canonical hierarchy IDs and editorial consistency rules are defined in:
- `CONSISTENCY_STANDARD.md`
- `../structure-spec.json`

## Typeface

No universal serif/sans-serif winner.

Choose a typeface that:
- is legible at final size;
- has distinct regular/bold weights;
- has clear numerals and punctuation;
- embeds reliably in PDF;
- is available in the production toolchain;
- does not cause glyph substitution.

Safe engineering examples:
- Arial
- Helvetica
- Calibri/Aptos
- Source Sans
- Inter
- Georgia
- Charter

This is not a scientific ranking.

## Hierarchy recipe

Use at least two independent signals for major hierarchy changes.

Example:
- H1 section heading = weight + whitespace
- H2 entry title = weight + position
- M2 metadata = smaller size + secondary emphasis

Do not rely only on color.

## Size

Engineering starting range:
- B1/B2 body: 10.5–12 pt;
- M1/M2 metadata: typically no more than ~1 pt below body unless still clearly legible;
- H1 section heading: 11.5–14 pt;
- H0 candidate name: 16–24 pt.

If body must drop below roughly 10 pt to fit:
- edit content/density first.

## Line spacing

Starting range:
- B1/B2 body/bullets: 1.15–1.35×;
- M1/M2 metadata may be slightly denser;
- preserve distinct spacing between semantic groups.

## Line length

Avoid:
- very long continuous lines;
- extremely narrow sidebars for essential evidence.

Use line-length research as a constraint, not a hard CV number.

## Alignment

Prefer:
- left-aligned body text;
- consistent M2 date alignment;
- stable indentation.

Avoid full justification in dense CV text.

## Whitespace

Use whitespace to distinguish:
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

Use sparingly.

Avoid:
- boxing every section;
- excessive cards;
- decorative sidebars that fragment reading order.

## Icons

Icons may supplement text but cannot replace critical semantic labels.

## Columns

Use the canonical vocabulary:
- single-column
- multi-column

A two-column document is a specific multi-column implementation.

Do not place chronology or core evidence in separate visual streams without extraction validation.

## Measurement units

Configuration fields:
- typography in points (`pt`);
- margins in inches (`in`).

Use explicit field names such as:
- `body_size_pt_range`
- `margin_inch_range`

Avoid unit-ambiguous configuration names.
