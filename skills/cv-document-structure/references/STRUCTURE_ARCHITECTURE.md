# CV Document Structure Architecture v1.0

## Mission

Construct a CV document whose **semantic structure, evidence priority, visual hierarchy, reading flow, and machine-readable structure agree with one another**.

A structure is good only when it preserves meaning across:

```text
candidate evidence
→ document encoding
→ human scan
→ detailed human reading
→ text extraction
→ section/entity parsing
```

## Layer L0 — Document context

Resolve:
- target role;
- career stage;
- occupation;
- region/jurisdiction;
- academic vs industry CV;
- known submission platform;
- likely reading medium;
- evidence volume.

Output:
`document_context`

## Layer L1 — Semantic section architecture

A section exists only if it has a coherent semantic purpose and useful evidence.

Core section candidates:
- Identity / Contact
- Summary / Profile
- Experience
- Projects
- Education
- Skills
- Certifications / Licenses
- Publications / Research
- Awards
- Leadership / Volunteering
- Selected Work / Portfolio

No section is mandatory solely because a template contains it, except the document must expose candidate identity/contact sufficiently for its use.

### Section naming rule

Prefer explicit semantic headings.

```text
Experience > Where I've Made an Impact
Education > My Learning Journey
Projects > Things I've Built
```

unless a known context justifies creative naming and parsing is verified.

## Layer L2 — Information priority and order

Ordering is a **decision problem**, not a template rule.

Priority dimensions:
1. role importance;
2. evidence strength;
3. recency;
4. relevance;
5. differentiating value;
6. reader expectation;
7. chronology/verification need.

### Ordering invariant

The document should surface the strongest high-relevance evidence before lower-value evidence, **without destroying chronology or semantic coherence**.

### Typical patterns

#### Experienced industry candidate
```text
Header
→ optional Summary
→ Experience
→ Projects / Skills / Certifications as relevance requires
→ Education
```

#### Student / early-career
```text
Header
→ optional Summary
→ Education OR Experience/Projects, whichever is more diagnostic
→ Projects / Experience
→ Skills
→ Activities / Awards if valuable
```

#### Career changer
```text
Header
→ concise transition Summary
→ Relevant Evidence / Projects or selected Skills
→ Complete Experience chronology
→ Education / Certifications
```

#### Academic CV
Use a separate academic structure. Do not force resume conventions.

These are **contextual defaults**, not universal laws.

## Layer L3 — Entry and evidence microstructure

### Experience entry

Keep these cognitively and structurally bound:

```text
ROLE TITLE
ORGANIZATION
LOCATION (optional/contextual)
DATE RANGE
BULLETS
```

Do not visually separate the date so far from the role that extraction/association becomes ambiguous.

### Bullet

A bullet is an evidence unit.

Possible components:

```text
contribution
+ context
+ method/tool
+ output
+ outcome
+ scope
```

Use only components supported by candidate evidence.

### Projects

Represent consistently:

```text
PROJECT NAME
role/context
date (if useful)
technology/domain
evidence bullets
link (if valuable)
```

### Education

Keep institution, credential, field, date, and relevant distinctions as a local group.

## Layer L4 — Typographic / spatial hierarchy

The purpose of typography is **structure recognition**, not decoration.

Hierarchy levels:

```text
H0 Candidate Name
H1 Section Heading
H2 Entry Title / Role / Project
M1 Organization / Institution
M2 Dates / Location / metadata
B1 Evidence bullet
B2 Supporting sub-detail
```

Visual variables:
- size;
- weight;
- whitespace;
- alignment;
- indentation;
- rule/line sparingly;
- case.

Do not use color as the only hierarchy cue.

### Engineering starting ranges

These are defaults, not scientific constants:

- page: A4 or Letter according to context;
- body: ~10.5–12 pt equivalent;
- line height: ~1.15–1.35× body size;
- section heading: ~1.1–1.35× body size plus weight;
- candidate name: ~1.4–2.0× body size;
- page margins: ~0.55–0.85 in equivalent;
- paragraph/bullet spacing: visibly distinct but compact;
- one body typeface family by default;
- at most one compatible display/accent family when justified.

If fitting content requires text below comfortable legibility, **remove lower-value content before shrinking further**.

## Layer L5 — Page flow, density, and length

### Length rule

Use:
```text
content sufficiency
+ relevance density
+ career stage
+ occupation
+ reader context
```

—not a fixed page count.

### Page-break invariants

Avoid:
- orphan section heading at page bottom;
- role title on one page with all bullets on next;
- date detached from the corresponding role;
- a bullet split where meaning becomes difficult to reconstruct;
- second page containing only low-value remnants.

Prefer:
- complete semantic chunks;
- balanced but not artificial page fill;
- meaningful continuation.

### Density rule

If a page feels crowded, optimize in this order:

1. remove irrelevant content;
2. merge redundant content;
3. shorten weakly diagnostic wording;
4. reduce excessive vertical spacing modestly;
5. reduce font size only within comfortable legibility;
6. add a page when evidence value justifies it.

## Layer L6 — Machine + accessibility structure

### Machine-readable invariants

- selectable text;
- logical reading order;
- conventional section names where appropriate;
- employer/title/date association remains clear;
- standard date text;
- URLs are real links or readable plain text;
- icons are never the only carrier of meaning;
- critical contact data is not image-only;
- decorative shapes do not interrupt extraction.

### Columns

Single-column is the default when:
- ATS/parser is unknown;
- maximum robustness is desired.

Two-column is allowed only after:
- extraction-order test;
- semantic association test;
- accessibility/reading-order test.

### Tables

Do not use tables purely for visual layout unless extraction is tested.

### Header/footer

Do not place critical identity/contact information only in page headers/footers when parser behavior is unknown.

## Layer L7 — Artifact verification

A CV is not structurally complete until the exported artifact is checked.

Required final checks:

### Human
- visual hierarchy obvious;
- top evidence findable;
- no crowding;
- no ambiguous grouping;
- page breaks coherent.

### Text extraction
- all material text extracted;
- order coherent;
- employer/title/date relationships preserved;
- bullets not merged across columns.

### PDF
- selectable text;
- Unicode preserved;
- links valid;
- no clipping;
- no hidden overflow;
- page count intended.

### Accessibility where feasible
- meaningful reading order;
- tagged headings if toolchain supports them;
- links have understandable text;
- document language/metadata where appropriate.
