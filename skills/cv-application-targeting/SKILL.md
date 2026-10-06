---
name: cv-application-targeting
description: Build or audit an application-specific CV variant for a concrete vacancy, company, or target role. Use when the user wants to tailor/personalize a CV, compare CV variants for different jobs, map candidate evidence to a job posting, decide what to emphasize/omit/reorder, or determine how much company-specific context belongs in a CV. Treat the target unit as company × vacancy × role × context; preserve the master candidate evidence base and never fabricate fit.
---

# CV Application Targeting

Create a truthful application-specific projection of the candidate evidence base.

## 1. Define the target application

Read:
- `references/TARGET_APPLICATION_MODEL.md`

Use:

```text
company
× vacancy
× target role
× context
```

Do not target "the company" in isolation when a specific vacancy exists.

## 2. Ground the candidate

Candidate master evidence is upstream authority.

Do not mutate evidence to match the target.

## 3. Build the requirement model

Use the root:
- `target_role/MODEL.md`

Separate:
- task/output/KSAO;
- hard constraints;
- preferences;
- employer-specific wording;
- legitimate company context.

## 4. Map evidence

Use:
- `reasoning/EVIDENCE_ROLE_MAPPING.md`

Allow:
- direct;
- adjacent;
- transferable;
- credential-only;
- weak;
- none.

Never force a match.

## 5. Tailor

Read:
- `references/TAILORING_RULES.md`
- `references/COMPANY_CONTEXT.md`

Allowed:
- select;
- omit;
- reorder;
- emphasize;
- terminology align;
- contextualize;
- change section priority.

Forbidden:
- fabricate;
- inflate title/ownership;
- add unsupported skills;
- mimic culture;
- keyword stuff;
- hide hard constraints.

## 6. Calibrate company specificity

Company context is secondary to role/vacancy relevance.

Use T0–T3 targeting levels from the model.

Do not assume T3 is automatically superior to T2.

## 7. Construct the CV variant

Use root:
- `reasoning/CLAIM_CALIBRATION.md`
- `construction/CV_CONSTRUCTION.md`
- `standards/CONSISTENCY_STANDARD.md`
- `standards/DATE_STANDARD.md`

For full structure/layout:
- `skills/cv-document-structure/SKILL.md`

## 8. Audit

Check:
- every emphasized requirement has evidence;
- no unsupported terminology implies unsupported capability;
- company context materially justifies its presence;
- chronology/claim strength remain stable across variants;
- hard gaps are not disguised.

## 9. Research discipline

Read:
- `references/RESEARCH_BASE.md`

Protect:

```text
role relevance ≠ company flattery
tailoring ≠ fabrication
terminology alignment ≠ keyword stuffing
company context ≠ culture mimicry
one application variant ≠ total rewrite from zero
association ≠ causal proof
```

## 10. Output

Follow:
- `references/OUTPUT_CONTRACT.md`

For a small tailoring request, use the minimal path.
For a serious application, construct the Target Application + evidence map before finalizing.

## Completion

A targeted CV is complete when the variant is materially specific to the application while candidate truth remains invariant.
