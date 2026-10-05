# Candidate Evidence Model v1

## Purpose

Store candidate reality **before** CV wording.

The model prevents three common failures:

1. wording silently changes facts;
2. team outcomes are misattributed to the candidate;
3. unavailable metrics are invented to make bullets look stronger.

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

Not every unit needs every field.

## Evidence rules

### R1 — Fact first

A CV sentence must be reconstructible from one or more evidence records.

### R2 — Contribution attribution

Distinguish:
- sole;
- primary;
- shared;
- supporting;
- unknown.

Do not turn team output into sole ownership.

### R3 — Metrics

A metric may be used only when:
- supplied by the user or a source;
- its meaning is understood;
- attribution is not misleading.

Never back-calculate or invent a metric merely because quantified bullets are fashionable.

### R4 — Uncertainty

When an evidence record is uncertain:
- narrow the claim;
- preserve ambiguity if material;
- or omit it.

Do not use stronger verbs to compensate for weak support.

### R5 — Verification status

`verified` does not mean universally true; it means the available evidence has been checked against the referenced support.

### R6 — Sensitive information

Sensitive data should not be included merely because it exists in the candidate record.

The construction engine must apply:
- relevance;
- jurisdiction;
- privacy;
- discrimination-risk review.

## Claim-strength map

- `direct` — may be stated directly within evidence bounds.
- `bounded` — may be stated with careful scope/attribution.
- `descriptive_only` — include only as neutral fact if relevant.
- `do_not_use` — exclude from CV generation.

## Non-equivalences

```text
participation ≠ ownership
responsibility ≠ achievement
team result ≠ individual causal effect
duration ≠ competence
tool exposure ≠ mastery
credential ≠ demonstrated performance
metric ≠ evidence quality
```

## Runtime requirement

Before generating final CV copy, build or infer a candidate evidence inventory.

If candidate facts are missing, do not fabricate. Produce:
- a bounded draft with placeholders,
- a request for missing evidence,
- or an evidence-gap report,
depending on the user's task.
