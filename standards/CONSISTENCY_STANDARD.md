# CV Consistency Standard v1.1

## Purpose

This is the canonical editorial and structural consistency standard for the CV repository.

Consistency must never override truth. If source evidence has lower precision than the preferred display format, preserve the lower precision rather than inventing missing detail.

## 1. Terminology

### Project term

Use **CV** as the default project term.

Use **CV/resume** when:
- describing trigger coverage;
- addressing international terminology differences.

Preserve **résumé/resume** spelling inside publication titles, quotations, or source-specific discussion.

### Internal identifiers

Use lowercase `snake_case`.

Examples:
- `professional_summary`
- `leadership_volunteering`
- `start_date`
- `is_current`

### Display labels

Default English display labels use title case.

Canonical section IDs and default labels:

| ID | Default display |
|---|---|
| `contact` | no heading required; rendered in header/contact block |
| `summary` | Professional Summary |
| `experience` | Experience |
| `projects` | Projects |
| `education` | Education |
| `skills` | Skills |
| `certifications` | Certifications |
| `publications_research` | Publications & Research |
| `awards` | Awards |
| `leadership_volunteering` | Leadership & Volunteering |
| `portfolio` | Selected Work |

Localized CVs may localize display labels, but internal IDs remain unchanged.

Do not use multiple display labels for the same section inside one CV.

## 2. Date standard

See `DATE_STANDARD.md`.

Core rules:
- internal normalized dates use ISO-like partial precision;
- display dates use one locale/language convention per CV;
- date ranges use an en dash `–`, not a hyphen;
- never invent month/day precision;
- ongoing entries use `end_date: null` + `is_current: true`;
- English display token for ongoing work is `Present` unless localization requires another term.

## 3. Hierarchy IDs

Canonical hierarchy:

| ID | Role |
|---|---|
| H0 | candidate name |
| H1 | section heading |
| H2 | entry title / role / project |
| M1 | organization / institution |
| M2 | dates / location / secondary metadata |
| B1 | evidence bullet |
| B2 | supporting sub-detail |

Do not create alternate IDs for these same functions without a versioned architecture change.

## 4. Page and measurement units

Canonical machine-readable units:
- typography: points (`pt`);
- page margins: inches (`in`) in configuration;
- PDF geometry may be converted to points internally by renderers.

Field names must include the unit:
- `body_size_pt_range`
- `margin_inch_range`

Avoid ambiguous names such as `margin_in_range`.

Page size:
- A4 or Letter is context-dependent;
- do not force one globally.

## 5. Names and titles

Preserve official spelling/casing for:
- candidate name;
- employer;
- institution;
- credential;
- product;
- technology;
- certification.

Examples:
- JavaScript, not Javascript
- GitHub, not Github
- PostgreSQL, not Postgresql
- Node.js, not NodeJS unless source requires otherwise

Do not silently "correct" a legal/official title into a more impressive title.

## 6. Locations

Choose one display pattern per CV where possible.

Examples:
- `Jakarta, Indonesia`
- `Austin, TX, USA`

Do not mix:
- country-only;
- city-only;
- full address;
- city-country

without a contextual reason.

Full street address is not a default requirement.

## 7. Numbers and metrics

Within a CV:
- use one locale for decimal/group separators;
- use one currency convention;
- use consistent percent spacing;
- do not add unsupported decimal precision;
- use en dash for numeric ranges where appropriate.

Examples in English-style formatting:
- `20%`
- `1,250 users`
- `$1.2M`
- `Rp85,000` only if that is the chosen locale/style.

Do not convert currencies or units unless the conversion is requested and sourced.

## 8. Acronyms

If an acronym may be ambiguous:
- spell out on first material use;
- optionally include acronym in parentheses;
- use the same acronym thereafter.

Known industry-standard acronyms may remain abbreviated when context makes them unambiguous.

## 9. Bullet grammar and punctuation

Choose one dominant bullet style per CV/section:

### Fragment style
- concise action/evidence fragments;
- terminal periods optional, but must be consistent.

### Sentence style
- complete sentences;
- use terminal punctuation consistently.

Do not mix fragment/no-period and sentence/period patterns randomly within the same section.

### Tense default

Engineering default:
- past completed work → past tense;
- current ongoing responsibility → present tense;
- completed achievement in current role → past tense.

Truth and meaning override tense symmetry.

## 10. Link style

Every material link must be:
- alive when checked;
- human-readable;
- actually clickable in final artifact where supported;
- consistently labeled.

Do not mix raw tracking URLs with clean labels without reason.

## 11. Section ordering vocabulary

Use canonical section IDs in reasoning/JSON.

Display order is contextual and may change, but the identity of each section must not.

## 12. Column vocabulary

Use:
- `single-column`
- `multi-column`

Use `two-column` only when specifically referring to a two-column implementation.

Do not alternate between "two column", "2-column", and "dual column" inside the same specification.

## 13. Versioning

Repository release uses Semantic Versioning-like labels:
- current release: `1.1.0`

Component research/taxonomy versions may remain lower when their scientific content has not changed.

Always distinguish:
- **release version**
- **component version**

Do not infer that every component must be renumbered for every repository release.

## 14. Source-of-truth hierarchy

For consistency conflicts:

1. factual candidate evidence;
2. root `standards/`;
3. machine-readable schema/spec;
4. subsystem runtime skill;
5. supporting reference docs;
6. examples.

If an example conflicts with the standard, the example is wrong.

## 15. Final consistency gate

Before release/final artifact, audit:
- version labels;
- date format and precision;
- section IDs and display labels;
- hierarchy IDs;
- employer/title/date association;
- location style;
- technology casing;
- number/metric style;
- bullet tense/punctuation;
- links;
- page units;
- column terminology;
- machine extraction order.
