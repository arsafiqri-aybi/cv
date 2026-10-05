# Target Role Model v1

## Purpose

Represent the target work before tailoring the CV.

The model is **not** a copy of the job description.

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

A role requirement can be classified as:

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

These are different.

Example:

A degree may be a **hard constraint** for one employer while a specific daily task is **high importance** for successful work.

Do not equate a formal gate with predictive importance.

## Target-role inference route

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

## Job-description guardrails

Do not assume:
- every bullet has equal importance;
- frequency of a keyword equals importance;
- preferred requirements are mandatory;
- employer language is technically precise;
- all responsibilities are current;
- a generic corporate template fully describes the real role.

## Role-to-evidence matching

Matching should consider:
- direct relevance;
- adjacent/transferable evidence;
- recency;
- scope;
- context similarity;
- evidence strength;
- semantic alignment.

The output is a **relevance map**, not a claim that the candidate objectively "fits" the job.
