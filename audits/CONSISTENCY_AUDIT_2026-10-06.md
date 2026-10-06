# Repository-Wide Consistency Audit — 2026-10-06

## Scope

Audited:
- root release metadata;
- root CV Skill;
- candidate evidence schema/model;
- construction rules;
- document-structure Skill;
- section architecture;
- typography/layout;
- PDF/machine rules;
- decision matrix;
- output contract;
- evaluation cases;
- validators;
- GitHub Actions validation path.

## Material inconsistencies found and repaired

### C01 — Release version drift
Found:
- README: v1.1.0
- manifest/release notes/limitations/quality gates: v1.0.0/v1.0

Repair:
- release metadata synchronized to v1.1.0;
- component-version distinction documented.

### C02 — Date policy was display-only
Found:
- display examples existed;
- candidate schema accepted arbitrary strings.

Repair:
- normalized internal date standard added;
- ongoing dates use null + is_current=true;
- source precision preserved;
- validator rejects display tokens in normalized fields.

### C03 — Calendar validity gap
Found:
- lexical regex alone could allow impossible dates.

Repair:
- runtime validator now validates month/day against the calendar.

### C04 — Section identity drift
Found examples:
- Header / Contact
- Identity / Contact
- Volunteering / Leadership
- Leadership / Volunteering

Repair:
- canonical internal section IDs created;
- one default display label defined per English section;
- localization allowed without changing IDs.

### C05 — Hierarchy vocabulary drift
Found:
- structure spec used H0/H1/H2/M1/M2/B1/B2;
- output contract used generic metadata/body names.

Repair:
- output contract now requires exact hierarchy IDs.

### C06 — Measurement-unit ambiguity
Found:
- `margin_in_range` did not encode the unit.

Repair:
- canonical field is `margin_inch_range`;
- typography uses pt;
- unit naming documented.

### C07 — Column terminology drift
Found:
- one-column/two-column
- single/two-column
- multi-column

Repair:
- canonical terms: single-column and multi-column;
- two-column is a specific multi-column implementation.

### C08 — Runtime consistency was not an explicit stage
Repair:
- root and structure Skills now load consistency/date standards;
- Structure output contract now includes consistency specification.

### C09 — Duplicate standard drift risk
Repair:
- canonical standards live in `standards/`;
- runtime snapshots exist inside the Skill;
- automated audit requires byte-for-byte equality.

### C10 — Editorial consistency under-specified
Repair:
Canonical rules added for:
- technology casing;
- locations;
- metrics/numbers;
- acronyms;
- bullet tense/punctuation;
- links;
- terminology.

## Date standard summary

Internal:
```text
YYYY
YYYY-MM
YYYY-MM-DD
null
```

Ongoing:
```text
end_date = null
is_current = true
```

English month display:
```text
MMM YYYY – MMM YYYY
MMM YYYY – Present
```

Never invent missing month/day precision.

## Result

Repository architecture is now governed by explicit consistency sources instead of scattered examples.

GitHub Actions remains the final deterministic release check.
