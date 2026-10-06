# CV

**Release: v1.1.0 — PROJECT_COMPLETE_V1 + Document Structure Subsystem**

Research-grounded architecture and runtime system for understanding, constructing, tailoring, structuring, and auditing CVs/résumés.

## Central model

> A CV is a strategically constructed but evidence-constrained representation of a candidate, used as one input in a socio-technical recruitment and selection system under uncertainty.

```text
WORK / ROLE REALITY
↕
CANDIDATE REALITY
↓
EVIDENCE
↓
SIGNALING
↓
RELEVANCE / FIT
↓
DOCUMENT REPRESENTATION
↙                    ↘
HUMAN INTERPRETATION   MACHINE INTERPRETATION
↘                    ↙
SCREENING OUTCOME
↓
FEEDBACK
```

## Runtime systems

### Root CV Skill
`SKILL.md`

Handles:
- evidence;
- target role;
- mapping;
- claim calibration;
- CV construction;
- audits.

### CV Document Structure Skill
`skills/cv-document-structure/SKILL.md`

Handles:
- semantic section architecture;
- section inclusion/order;
- page architecture;
- information hierarchy;
- entry microstructure;
- typography/spacing;
- one-vs-two page decisions;
- single-vs-multi-column decisions;
- PDF reading order;
- machine extraction robustness;
- final artifact structure QA.

Its research base explicitly separates:
- CV-specific research;
- adjacent document science;
- technical standards;
- parser research;
- technical benchmarks;
- engineering defaults;
- contextual heuristics.

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
one column ≠ universal requirement
serif/sans-serif ≠ universal readability ranking
```

## Automated validation

GitHub Actions:
`.github/workflows/validate.yml`

On pushes to main and pull requests it compiles validators and runs:
`python scripts/audit_repository.py`

The audit now also verifies the CV Document Structure subsystem.

## Repository map

- `orchestration/` — root execution control
- `research/` — CV science
- `graph/` — knowledge graph
- `candidate_evidence/` — candidate truth model
- `target_role/` — target-role model
- `reasoning/` — mapping and claim calibration
- `construction/` — core construction rules
- `skills/cv-document-structure/` — specialized document-structure skill
- `audits/` — human/machine/factual/fairness audits
- `evaluation/` — root evaluation
- `release/` — release controls
- `scripts/` — deterministic validators

Scientific saturation is not claimed.
