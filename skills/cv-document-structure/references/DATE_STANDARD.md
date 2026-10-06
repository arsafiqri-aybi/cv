# Date and Chronology Standard v1.1

## Purpose

Define one canonical approach to storing, displaying, sorting, and auditing dates.

## A. Internal normalized representation

Accepted normalized forms:

```text
YYYY
YYYY-MM
YYYY-MM-DD
null
```

Examples:
- `2024`
- `2024-07`
- `2024-07-15`

Do not store display strings such as:
- `Jul 2024`
- `July 2024`
- `Present`
- `Sekarang`

inside normalized date fields.

Preserve source wording separately when needed.

## B. Ongoing entries

Represent ongoing work as:

```json
{
  "start_date": "2024-07",
  "end_date": null,
  "is_current": true
}
```

Do not store `"Present"` as `end_date`.

## C. Precision integrity

Never invent missing precision.

If evidence only supports:
`2023`

do not normalize it to:
`2023-01`

for visual consistency.

If exact day is known internally, the CV may still display month/year because day-level detail is usually unnecessary.

## D. English display default

For month-precision career entries:

```text
MMM YYYY – MMM YYYY
MMM YYYY – Present
```

Examples:
- `Jan 2024 – Sep 2026`
- `Jul 2025 – Present`

For year-only evidence:

```text
YYYY – YYYY
YYYY – Present
```

Examples:
- `2021 – 2023`
- `2024 – Present`

Use spaces around the en dash.

## E. Localization

The CV may localize month names and the ongoing token.

Examples:
- English: `Jan 2024 – Present`
- Indonesian: `Jan 2024 – Sekarang`

Do not mix languages inside one CV unless intentionally bilingual.

## F. Precision consistency vs factual consistency

Preferred:
- same display precision within comparable entries.

But factual precision wins.

Allowed:
- one older education record displayed as `2019` while employment entries use `Jan 2024 – Present`, if only the year is known/relevant.

Not allowed:
- inventing months to make rows visually uniform.

## G. Expected dates

For future expected completion, label explicitly.

Examples:
- `Expected Jun 2027`
- localized equivalent.

Do not present a future expected date as already completed.

## H. Date ordering

Default career chronology is reverse chronological when appropriate.

Sort using normalized dates:
1. current entries first when otherwise comparable;
2. latest end date;
3. latest start date.

Do not reorder simply to hide gaps.

## I. Date conflicts

If sources disagree:
- mark `FACT_CONFLICT`;
- do not silently select one;
- resolve from candidate/source evidence before finalization when material.

## J. Parser/display integrity

Dates must remain:
- plain selectable text;
- visually associated with the correct role/institution;
- extractable in the intended reading order.

## K. Prohibited mixed styles in one CV

Avoid mixtures such as:

```text
Jan 2024 - Present
2022–23
07/2021 — 09/2022
March '20 to May '21
```

Choose one language, separator, month style, and range convention.

## L. Canonical separator

Display date range separator:
- en dash: `–`

Internal ISO separator:
- hyphen: `-`

These serve different purposes.
