# CV

**Release: v1.0.0 — PROJECT_COMPLETE_V1**

Research-grounded architecture and runtime system for understanding, constructing, tailoring, and auditing CVs/résumés.

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

## Release snapshot

- 77 operational constructs
- 70 typed graph edges
- 12 protected non-edges
- 18 adversarial evaluation cases
- 10 evaluation dimensions
- candidate evidence JSON Schema
- target-role JSON Schema
- reasoning + claim-calibration engine
- CV construction system
- human/machine/factual/fairness audits
- root runtime `SKILL.md`
- static release audit: **PASS**

Scientific saturation is **not claimed**.

## Orchestration

```text
MASTER PROMPT
↓
SCALE
↓
GOVERNOR
↓
DOMAIN SCIENCE
↓
REASONING
↓
CONSTRUCTION
↓
AUDIT
↓
EVALUATION
```

Files:
- `orchestration/MASTER_PROMPT.md`
- `orchestration/SCALE.md`
- `orchestration/GOVERNOR.md`

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
```

## Runtime

Use `SKILL.md`.

The runtime:
1. models target role;
2. structures candidate evidence;
3. maps evidence to requirements;
4. diagnoses gaps;
5. calibrates claims;
6. selects signals;
7. constructs the document;
8. audits human interpretation;
9. audits machine interpretation;
10. verifies factual integrity and fairness/privacy risk.

## Repository map

- `PROJECT_CONTRACT.md` — scope and invariants
- `docs/ARCHITECTURE.md` — process architecture
- `research/` — evidence, claims, contradictions, uncertainty
- `science/` — taxonomy
- `graph/` — nodes, edges, protected non-edges
- `candidate_evidence/` — candidate truth model
- `target_role/` — target-role model
- `schemas/` — machine-readable schemas
- `reasoning/` — mapping and claim calibration
- `construction/` — CV/document construction
- `audits/` — human, machine, factual, fairness/privacy audits
- `evaluation/` — rubric, adversarial cases, evaluation status
- `references/` — runtime progressive-disclosure references
- `release/` — manifest, gates, limitations, notes
- `scripts/` — deterministic validators

## Important limitation

PROJECT_COMPLETE_V1 means the defined operational v1 scope is complete and statically verified.

It does not mean every scientific question about CVs is settled or that interviews/offers can be guaranteed.

See `release/KNOWN_LIMITATIONS.md`.
