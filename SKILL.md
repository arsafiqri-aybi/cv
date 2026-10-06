---
name: cv
description: Build, tailor, audit, or improve CVs/resumes from real candidate evidence and a target role. Use when the user asks to create, rewrite, tailor, evaluate, diagnose, or structure a CV/resume, or to analyze the evidence and role requirements behind one. Preserve facts, calibrate claims, distinguish human from machine screening, and do not invent achievements, metrics, skills, credentials, dates, or ATS scores.
---

# CV

Build CVs as evidence-constrained representations inside a recruitment and selection system.

## 1. Identify the job

Classify the request:
- create a CV;
- tailor a CV to a role;
- improve/rewrite supplied CV content;
- audit a CV;
- diagnose weak evidence;
- analyze a target role;
- compare CV variants;
- design/audit document structure;
- explain why a CV choice is or is not defensible.

If the user only wants the finished CV, keep visible explanation concise. Do the necessary evidence and role reasoning before drafting.

## 2. Ground candidate reality

Use `candidate_evidence/MODEL.md`.

Separate supplied facts, verified facts, inferences, and unknowns.

Never invent metrics, scope, ownership, responsibilities, tools, outcomes, credentials, or dates.

If evidence is missing, narrow the claim, omit it, use a placeholder only when a template was requested, or ask for the missing fact only when it materially blocks the requested output.

## 3. Model the target role

Use `target_role/MODEL.md`.

Do not treat a job description as complete truth. Extract tasks, outputs, KSAOs, tools/domain, credentials, constraints, seniority/context. Estimate importance and hardness separately.

If no target role is supplied, create a general evidence-led CV only when requested and avoid strong tailoring claims.

## 4. Map evidence to requirements

Use `reasoning/EVIDENCE_ROLE_MAPPING.md`.

Classify matches as direct, adjacent, transferable, credential-only, weak, or none. Do not force a match.

Prioritize strong, relevant, credible evidence. Record meaningful gaps rather than hiding them.

## 5. Calibrate claims

Use `reasoning/CLAIM_CALIBRATION.md`.

A stronger verb is a stronger claim. Do not silently turn helped→led, participated→owned, supported→transformed, or used→mastered.

Team results require accurate attribution. Metrics require real support.

## 6. Construct the document

For ordinary construction use:
- `construction/CV_CONSTRUCTION.md`
- `construction/DOCUMENT_RULES.md`

For full document architecture, layout hierarchy, section ordering, page structure, typography, PDF reading order, or parser-safe structural design, load:

- `skills/cv-document-structure/SKILL.md`

The document-structure subsystem is authoritative for those tasks.

Do not force a universal one-page rule, one fixed bullet formula, one section order, one visual template, one font category, or quantified bullets when metrics do not exist.

## 7. Audit human interpretation

Use `audits/HUMAN_SCREENING.md`.

Check relevance visibility, clarity, attribution, credibility, cognitive load, inference errors, and perceived fit versus actual evidence.

Do not treat recruiter perception as objective truth.

## 8. Audit machine interpretation

Use `audits/MACHINE_SCREENING.md`.

Keep parsing, section detection, entity extraction, normalization, search/retrieval, ranking, knockout rules, and LLM evaluation separate.

If the actual ATS/platform is unknown, perform a general parseability audit; do not generate a fake ATS score or claim guaranteed ranking.

## 9. Factual integrity, fairness, privacy

Use `audits/FACTUAL_INTEGRITY.md` and `audits/FAIRNESS_PRIVACY.md`.

No final CV may contain a critical factual-integrity failure.

Treat jurisdiction-specific legal/convention claims as current external facts that may need verification.

## 10. Scientific discipline

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
one column ≠ universal requirement
serif/sans-serif category ≠ universal readability ranking
```

Use current external research when the user asks for scientific justification, a current ATS/AI/platform behavior matters, legal/cultural conventions matter, or a rule is contested/time-sensitive.

## 11. Output modes

### Draft mode
Return the finished CV content directly.

### Audit mode
Return critical issues, high-impact improvements, evidence gaps, machine/human risks, and recommended changes.

### Tailor mode
Return target-role interpretation, evidence mapping, tailored CV, and unresolved gaps only when material.

### Structure mode
Use the document-structure subsystem and return:
- section architecture;
- page architecture;
- hierarchy spec;
- entry structure;
- typography/layout spec;
- machine/PDF spec;
- QA gates.

### Research mode
Return supported conclusion, evidence, contradictions, uncertainty, and operational consequence.

## 12. Completion checks

Before finalizing a CV:
- material claims trace to candidate evidence;
- target relevance is explicit where possible;
- no metric was fabricated;
- ownership is accurate;
- chronology is internally consistent;
- unsupported skills are absent;
- human hierarchy is readable;
- machine assumptions are scoped;
- final artifact reading order is checked when an artifact exists;
- sensitive-data risks are reviewed;
- unresolved critical contradictions are surfaced.

A polished document that fails factual integrity or structural integrity is not complete.
