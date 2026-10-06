---
name: cv
description: Build, tailor, audit, or improve CVs/resumes from real candidate evidence and a target application. Use when the user asks to create, rewrite, tailor, personalize, evaluate, diagnose, structure, compare variants, or consistency-check a CV/resume. Preserve facts, calibrate claims, and do not invent achievements, metrics, skills, credentials, dates, fit, or ATS scores.
---

# CV

Build CVs as evidence-constrained representations inside a recruitment and selection system.

## 1. Classify the request

Modes include:
- create;
- tailor/personalize;
- rewrite;
- audit;
- diagnose evidence;
- analyze target role;
- analyze target application;
- compare variants;
- structure;
- consistency audit.

## 2. Ground candidate reality

Use `candidate_evidence/MODEL.md`.

Candidate evidence is the master source of truth.

Never invent metrics, scope, ownership, responsibilities, tools, outcomes, credentials, dates/date precision, or employer fit.

## 3. Model the target

### Target Role
Use `target_role/MODEL.md`.

### Target Application
For a concrete application, use:
- `application_targeting/MODEL.md`
- `skills/cv-application-targeting/SKILL.md`

Target unit:

```text
company × vacancy × target role × context
```

Do not treat "one company = one CV" as a scientific law.

## 4. Map evidence

Use:
- `reasoning/EVIDENCE_ROLE_MAPPING.md`
- `reasoning/APPLICATION_TARGETING.md`

Do not force matches.

## 5. Calibrate claims

Use `reasoning/CLAIM_CALIBRATION.md`.

Across CV variants, facts and claim ceilings stay stable unless candidate evidence changes.

## 6. Apply consistency authority

Use:
- `standards/CONSISTENCY_STANDARD.md`
- `standards/DATE_STANDARD.md`

## 7. Construct the document

Use:
- `construction/CV_CONSTRUCTION.md`
- `construction/DOCUMENT_RULES.md`

For document structure:
- `skills/cv-document-structure/SKILL.md`

For application-specific tailoring:
- `skills/cv-application-targeting/SKILL.md`

## 8. Audit

Use:
- `audits/HUMAN_SCREENING.md`
- `audits/MACHINE_SCREENING.md`
- `audits/FACTUAL_INTEGRITY.md`
- `audits/FAIRNESS_PRIVACY.md`

## 9. Scientific discipline

Protect:

```text
interview success ≠ job-performance validity
role relevance ≠ company flattery
tailoring ≠ fabrication
company context ≠ culture mimicry
terminology alignment ≠ keyword stuffing
company-specific tailoring association ≠ proven independent causal advantage
one application-specific variant ≠ total rewrite from zero
```

## 10. Output modes

### Draft
Finished CV.

### Tailor
Use application-targeting subsystem.

### Audit
Critical issues, gaps, human/machine risks.

### Structure
Use document-structure subsystem.

### Consistency
Use canonical standards.

### Research
Evidence, contradictions, uncertainty, operational consequence.

## 11. Completion

Before finalizing:
- candidate facts are stable;
- target application is explicit when a concrete vacancy exists;
- high-priority requirements are mapped;
- unsupported matches are absent;
- hard gaps are not hidden;
- company context is used only when material;
- claim calibration is preserved;
- document/consistency audits pass.

A CV that is highly personalized but factually distorted is a failed CV.
