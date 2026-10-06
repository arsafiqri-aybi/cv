# Evaluation Status — v1.1.0

## Root system

Static verification: **PASS** on prior validated release state.

Root evaluation architecture:
- 18 adversarial cases
- 10 rubric dimensions

Critical dimensions include:
- factual fidelity
- claim calibration
- fairness/privacy
- consistency

## Document Structure subsystem

Adversarial coverage:
- 23 cases

Coverage now includes:
- page length;
- section ordering;
- multi-column extraction;
- typography compression;
- academic CV exception;
- creative labels;
- date-format drift;
- ongoing-date normalization;
- unknown date precision;
- section-label drift;
- bullet punctuation/tense;
- technology casing;
- location formatting.

## Cross-file consistency

Automated audit checks:
- release version synchronization;
- canonical standard snapshot equality;
- canonical section IDs;
- hierarchy IDs;
- measurement-unit field names;
- date separator policy;
- candidate-date schema fields;
- runtime date-validator behavior.

## Behavioral evaluation limitation

Independent recruiter/model pass-rate is **NOT_CLAIMED**.

The repository provides adversarial specifications and deterministic structural checks, not external recruiter validation.

## GitHub Actions

`.github/workflows/validate.yml` runs the consistency-aware repository audit on every push to main and pull request.
