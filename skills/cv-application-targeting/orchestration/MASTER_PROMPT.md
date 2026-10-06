# Application Targeting Master Prompt

## Mission

Generate the strongest truthful CV variant for a specific target application without rewriting candidate reality.

## Target unit

Do not use `company` alone as the targeting unit.

Use:

```text
TARGET APPLICATION
=
company
× vacancy
× target role
× context
```

## Source-of-truth order

1. candidate master evidence base;
2. verified target vacancy/source;
3. target role model;
4. verified material company context;
5. explicit inference;
6. heuristic.

## Route

```text
TARGET APPLICATION
→ REQUIREMENT EXTRACTION
→ ROLE MODEL
→ CANDIDATE EVIDENCE RETRIEVAL
→ REQUIREMENT ↔ EVIDENCE MAP
→ GAP DIAGNOSIS
→ TAILORING DECISIONS
→ CLAIM CALIBRATION
→ CV VARIANT
→ HUMAN/MACHINE/INTEGRITY AUDITS
```

## Protected constraints

- no fact invention;
- no skill invention;
- no title inflation;
- no fake company familiarity;
- no culture mimicry;
- no keyword stuffing;
- no hiding hard constraints;
- no claim that company-specific personalization independently guarantees interviews.

## Completion

The output must be application-specific where evidence permits, but candidate truth must remain invariant across variants.
