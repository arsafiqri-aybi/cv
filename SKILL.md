---
name: cv
description: Build, tailor, audit, or improve CVs/resumes from real candidate evidence and a target role. Use when the user asks to create, rewrite, tailor, evaluate, diagnose, structure, or consistency-check a CV/resume. Preserve facts, calibrate claims, distinguish human from machine screening, and do not invent achievements, metrics, skills, credentials, dates, or ATS scores.
---

# CV

Build CVs as evidence-constrained representations inside a recruitment and selection system.

## 1. Identify the job

Classify the request:
- create;
- tailor;
- rewrite;
- audit;
- diagnose evidence;
- analyze target role;
- compare variants;
- design/audit document structure;
- audit editorial/date consistency.

## 2. Ground candidate reality

Use `candidate_evidence/MODEL.md`.

Never invent:
- metrics;
- scope;
- ownership;
- responsibilities;
- tools;
- outcomes;
- credentials;
- dates or date precision.

## 3. Model the target role

Use `target_role/MODEL.md`.

Do not treat the job description as complete truth.

## 4. Map evidence to requirements

Use `reasoning/EVIDENCE_ROLE_MAPPING.md`.

Do not force a match.

## 5. Calibrate claims

Use `reasoning/CLAIM_CALIBRATION.md`.

Claim strength must not exceed evidence strength.

## 6. Apply consistency authority

For all final CV/document work, use:
- `standards/CONSISTENCY_STANDARD.md`
- `standards/DATE_STANDARD.md`

These are authoritative for dates, section identity, hierarchy IDs, units, terminology, metadata, metrics, links, and editorial consistency.

## 7. Construct the document

Use:
- `construction/CV_CONSTRUCTION.md`
- `construction/DOCUMENT_RULES.md`

For full document architecture, load:
- `skills/cv-document-structure/SKILL.md`

Do not force a universal one-page rule, one fixed bullet formula, one section order, one visual template, one font category, or unsupported quantification.

## 8. Audit human interpretation

Use `audits/HUMAN_SCREENING.md`.

## 9. Audit machine interpretation

Use `audits/MACHINE_SCREENING.md`.

Keep parsing, section detection, extraction, retrieval, ranking, knockout rules, and LLM evaluation separate.

## 10. Factual integrity, fairness, privacy

Use:
- `audits/FACTUAL_INTEGRITY.md`
- `audits/FAIRNESS_PRIVACY.md`

No final CV may contain a critical integrity failure.

## 11. Scientific discipline

Protect:

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
serif/sans-serif category ≠ universal readability ranking
display precision ≠ factual precision
```

## 12. Output modes

### Draft
Finished CV content.

### Audit
Critical issues, improvements, evidence gaps, human/machine risks.

### Tailor
Target-role interpretation, mapping, tailored CV, material gaps.

### Structure
Use document-structure subsystem.

### Consistency
Audit:
- versions;
- dates;
- section identity/labels;
- hierarchy IDs;
- locations;
- technology casing;
- numbers/metrics;
- bullet grammar/punctuation;
- links;
- page units;
- column terminology;
- artifact extraction consistency.

### Research
Supported conclusion, evidence, contradictions, uncertainty, operational consequence.

## 13. Completion checks

Before finalizing:
- claims trace to evidence;
- no invented metric/date precision;
- ownership accurate;
- chronology internally consistent;
- canonical date standard applied;
- canonical section identities stable;
- unsupported skills absent;
- hierarchy readable;
- machine assumptions scoped;
- final artifact reading order checked when available;
- editorial consistency checked;
- sensitive-data risks reviewed.

A polished CV that fails factual, structural, or editorial consistency is not complete.
