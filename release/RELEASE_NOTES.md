# CV v1.2.0 — Release Notes

## New subsystem: Application Targeting

v1.2.0 adds a research-grounded application-targeting Skill.

Canonical target:

```text
TARGET APPLICATION
=
company × vacancy × role × context
```

## Shipped

- `application_targeting/MODEL.md`
- `schemas/target-application.schema.json`
- `reasoning/APPLICATION_TARGETING.md`
- `research/APPLICATION_TARGETING_RESEARCH_V1.md`
- `skills/cv-application-targeting/SKILL.md`
- Prompting/Scale/Governor orchestration
- targeting/tailoring/company-context references
- 18 adversarial targeting cases
- machine-readable application-target spec
- root CV routing integration
- static audit integration

## Scientific correction

The project does not claim:
`one company = one completely unique CV`.

Instead:
- role/vacancy relevance is the primary targeting layer;
- company context is secondary and conditional;
- company-focused tailoring has some observational association with interview outcomes, but independent causal benefit is not established strongly enough to make it a universal rule.

## Invariant

Application variants can change:
- selection;
- order;
- salience;
- detail;
- supported terminology.

They cannot change:
- candidate facts;
- evidence provenance;
- ownership;
- chronology;
- unsupported skill status;
- claim ceiling.
