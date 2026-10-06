# CV Document Structure Architecture v1.1

## Mission

Construct a CV whose semantic structure, evidence priority, visual hierarchy, reading flow, metadata consistency, and machine-readable structure agree.

Canonical editorial authority:
- `CONSISTENCY_STANDARD.md`
- `DATE_STANDARD.md`

A structure is good only when it preserves meaning across:

```text
candidate evidence
→ document encoding
→ human scan
→ detailed human reading
→ text extraction
→ section/entity/date parsing
```

## L0 — Document context

Resolve:
- target role;
- career stage;
- occupation;
- region/jurisdiction;
- output language/locale;
- academic vs industry CV;
- known submission platform;
- reading medium;
- evidence volume.

## L1 — Semantic section architecture

Use canonical IDs from `CONSISTENCY_STANDARD.md`.

A section exists only if it has a coherent purpose and useful evidence.

Display labels may be localized but must remain semantically explicit.

## L2 — Information priority and order

Priority dimensions:
1. role importance;
2. evidence strength;
3. recency;
4. relevance;
5. differentiating value;
6. reader expectation;
7. chronology/verification need.

Surface strong high-relevance evidence before low-value evidence without breaking chronology or semantic coherence.

## L3 — Entry/evidence microstructure

Experience entry binds:

```text
H2 ROLE TITLE
M1 ORGANIZATION
M2 LOCATION + DATE RANGE
B1 EVIDENCE BULLETS
B2 SUPPORTING DETAIL
```

Dates follow `DATE_STANDARD.md`.

Project and Education entries use the same association principle.

## L4 — Typographic/spatial hierarchy

Canonical levels:
- H0 candidate name
- H1 section heading
- H2 entry title
- M1 organization/institution
- M2 dates/location/metadata
- B1 evidence bullet
- B2 supporting detail

Do not create visually different styles that imply extra hierarchy levels unless semantically meaningful.

## L5 — Page flow, density, and length

Do not use a fixed page count.

If crowded:
1. remove irrelevant content;
2. merge redundancy;
3. shorten weakly diagnostic wording;
4. simplify low-value metadata;
5. reduce excess spacing modestly;
6. adjust typography within legibility range;
7. add a page when valuable evidence still requires space.

Keep semantic chunks together where practical.

## L6 — Machine/accessibility structure

Required:
- selectable text;
- logical reading order;
- employer/title/date association;
- canonical section semantics;
- standard Unicode;
- meaningful link text;
- no image-only critical data.

Single-column is the default when platform is unknown and maximum robustness is desired.

Multi-column requires extraction and association testing.

## L7 — Artifact verification

Required checks:
- human hierarchy;
- text extraction;
- reading order;
- employer/title/date association;
- date display consistency;
- Unicode;
- links;
- clipping/overflow;
- page breaks;
- editorial consistency;
- accessibility structure where supported.
