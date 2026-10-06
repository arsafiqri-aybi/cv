# Target Role Model v1.1

## Purpose

Represent the target work before tailoring the CV.

The model is not a copy of the job description and is distinct from the Target Application.

Use:
- `application_targeting/MODEL.md` for company/vacancy/application context.

## Inputs

Possible sources:
- job posting;
- organization website;
- recruiter message;
- occupational database;
- role-family knowledge;
- industry references;
- user-supplied context.

Each source is evidence, not automatic ground truth.

## Requirement decomposition

A role requirement can be:
- task;
- output;
- knowledge;
- skill;
- ability;
- credential;
- experience;
- tool;
- domain;
- constraint;
- context;
- behavioral.

Each requirement receives:
- importance;
- hardness;
- evidence basis;
- aliases;
- confidence.

## Importance vs hardness

A hard eligibility gate is not automatically the most predictive or important work requirement.

## Inference route

```text
SOURCE MATERIAL
→ REQUIREMENT EXTRACTION
→ DUPLICATE / ALIAS RESOLUTION
→ TASK / OUTPUT / KSAO MAPPING
→ IMPORTANCE ESTIMATE
→ HARD-CONSTRAINT IDENTIFICATION
→ CONTEXT + SENIORITY ADJUSTMENT
→ OPEN QUESTIONS
```

## Guardrails

Do not assume:
- every JD bullet is equally important;
- keyword frequency equals importance;
- preferred means mandatory;
- employer language is technically precise;
- generic company role pages equal the active vacancy.

## Role-to-evidence matching

Consider:
- direct relevance;
- adjacent/transferable evidence;
- recency;
- scope;
- context similarity;
- evidence strength;
- semantic alignment.

The output is a relevance map, not objective fit.

## Boundary

```text
TARGET ROLE
≠
TARGET APPLICATION

role model = work reality
application model = company × vacancy × role × context
```
