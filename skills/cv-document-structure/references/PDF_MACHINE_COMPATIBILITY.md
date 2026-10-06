# PDF, Machine Parsing, and Reading Order v1.1

## Core idea

A visually correct CV can still be structurally broken.

Use:
- `CONSISTENCY_STANDARD.md`
- `DATE_STANDARD.md`

for editorial and date conventions.

## Semantic extraction targets

A robust document should allow extraction of:

```text
PERSON
CONTACT
SECTION
ORGANIZATION
ROLE
DATE_START
DATE_END
INSTITUTION
DEGREE
SKILL
PROJECT
CERTIFICATION
URL
```

## Reading-order test

After export:

1. extract all text;
2. inspect sequence;
3. verify:
   - name/contact first;
   - section heading before section content;
   - role adjacent to employer/date;
   - date belongs to the correct entry;
   - bullets remain under correct role;
   - multi-column streams do not interleave incorrectly;
   - page 2 begins in intended sequence.

## Failure classes

### P0 — Missing text
Material text absent from extraction.

### P1 — Order corruption
All words exist but sequence is wrong.

### P2 — Association corruption
Role/date/employer or school/degree associations are mixed.

### P3 — Section loss
Content exists but section boundaries are not recoverable.

### P4 — Character corruption
Glyph/Unicode substitution damages meaning.

### P5 — Link corruption
Visible URL/link is broken or points elsewhere.

### P6 — Date corruption
A date is missing, altered, or associated with the wrong entry.

### P7 — Editorial drift
Extracted content exposes inconsistent labels/date styles/technology names that were not intentional.

## PDF structural defaults

Prefer:
- native text PDF;
- embedded fonts;
- logical content order;
- standard Unicode;
- consistent H1 section semantics;
- standard bullet characters;
- real hyperlinks.

Avoid:
- scanned image-only CV;
- rasterized text;
- critical text in shapes;
- overlapping text boxes;
- hidden white keyword text.

## Tagged PDF

Where supported, tagged PDF with meaningful heading structure improves accessibility and makes reading order explicit.

Do not claim tagged PDF guarantees ATS ranking.

## Parser assumptions

Never conflate:
- extraction;
- entity recognition;
- retrieval;
- ranking;
- rejection.

A document can parse perfectly and still rank poorly.
