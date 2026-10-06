# CV

**Release: v1.1.0 — PROJECT_COMPLETE_V1 release line**

Research-grounded architecture and runtime system for understanding, constructing, tailoring, structuring, and auditing CVs/resumes.

## Central model

> A CV is a strategically constructed but evidence-constrained representation of a candidate, used as one input in a socio-technical recruitment and selection system under uncertainty.

## Canonical standards

Repository-wide consistency is governed by:

- `standards/CONSISTENCY_STANDARD.md`
- `standards/DATE_STANDARD.md`

These are authoritative for:
- section IDs/display labels;
- date normalization/display;
- hierarchy IDs;
- typography/page units;
- location style;
- technology casing;
- metrics;
- acronyms;
- bullet punctuation/tense;
- links;
- column terminology.

Consistency never overrides factual precision.

## Runtime systems

### Root CV Skill
`SKILL.md`

Handles evidence, target role, mapping, claim calibration, CV construction, and audits.

### CV Document Structure Skill
`skills/cv-document-structure/SKILL.md`

Handles:
- semantic section architecture;
- page architecture;
- information hierarchy;
- entry microstructure;
- date/metadata consistency;
- typography/spacing;
- page-length decisions;
- single-column/multi-column decisions;
- PDF reading order;
- machine extraction robustness;
- final artifact QA.

## Protected distinctions

```text
interview success ≠ job-performance validity
writing quality ≠ capability
experience duration ≠ competence
perceived fit ≠ objective fit
parsing ≠ ranking
keyword overlap ≠ competence
quantification ≠ evidence quality
visual polish ≠ universal effectiveness
one page ≠ universal optimum
single-column ≠ universal requirement
serif/sans-serif ≠ universal readability ranking
display precision ≠ factual precision
```

## Automated validation

GitHub Actions:
`.github/workflows/validate.yml`

On pushes to main and pull requests it compiles validators and runs:
`python scripts/audit_repository.py`

The audit covers both the root CV system and document-structure consistency.

## Versioning

Repository release version: `1.1.0`.

Individual research/taxonomy components can retain their own version when their content has not changed.

## Repository map

- `standards/` — canonical consistency/date standards
- `orchestration/` — root execution control
- `research/` — CV science
- `graph/` — knowledge graph
- `candidate_evidence/` — candidate truth model
- `target_role/` — target-role model
- `reasoning/` — mapping and claim calibration
- `construction/` — core construction
- `skills/cv-document-structure/` — specialized structure Skill
- `audits/` — human/machine/factual/fairness audits
- `evaluation/` — root evaluation
- `release/` — release controls
- `scripts/` — deterministic validators

Scientific saturation is not claimed.
