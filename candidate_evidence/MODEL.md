# Candidate Evidence Model v1.1

## Purpose

Store candidate reality before CV wording.

The model prevents:
1. wording silently changing facts;
2. team outcomes being misattributed;
3. invented metrics;
4. invented date precision.

## Canonical evidence unit

```text
FACT
→ CONTEXT
→ TASK
→ CONTRIBUTION
→ OUTPUT
→ OUTCOME
→ SCOPE
→ PROVENANCE
→ CONFIDENCE
→ ALLOWED CLAIM STRENGTH
```

## Date normalization

Canonical normalized date fields accept:

```text
YYYY
YYYY-MM
YYYY-MM-DD
null
```

For ongoing evidence:
- `end_date = null`
- `is_current = true`

Do not store `Present`/`Sekarang` in normalized date fields.

If source precision is lower than desired display precision, preserve the lower precision.

Optional `date_source_text` may preserve the original wording.

Display formatting belongs to the document layer:
- `standards/DATE_STANDARD.md`

## Evidence rules

### R1 — Fact first
A CV statement must be reconstructible from one or more evidence records.

### R2 — Contribution attribution
Distinguish sole, primary, shared, supporting, and unknown ownership.

### R3 — Metrics
Use a metric only when supplied/supported and meaningfully attributable.

### R4 — Uncertainty
Narrow, omit, or preserve uncertainty. Do not compensate with stronger verbs.

### R5 — Verification status
`verified` means checked against available referenced support, not universal certainty.

### R6 — Sensitive information
Apply relevance, jurisdiction, privacy, and discrimination-risk review.

### R7 — Chronology
Do not alter dates to hide gaps.

If date sources materially conflict:
- emit `FACT_CONFLICT`;
- resolve before finalization where material.

## Claim-strength map

- `direct`
- `bounded`
- `descriptive_only`
- `do_not_use`

## Non-equivalences

```text
participation ≠ ownership
responsibility ≠ achievement
team result ≠ individual causal effect
duration ≠ competence
tool exposure ≠ mastery
credential ≠ demonstrated performance
metric ≠ evidence quality
display precision ≠ factual precision
```

## Runtime requirement

Before generating final CV copy, build or infer a candidate evidence inventory.

If facts are missing, do not fabricate them.
