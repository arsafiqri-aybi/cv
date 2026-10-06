# CV

**Release: v1.3.0 — PROJECT_COMPLETE_V1 release line**

Research-grounded CV system spanning candidate evidence acquisition, application targeting, document construction, and auditing.

## End-to-end architecture

```text
CANDIDATE DISCOVERY INTERVIEW
        ↓
MASTER CANDIDATE EVIDENCE BASE
        ↓
TARGET APPLICATION
(company × vacancy × role × context)
        ↓
EVIDENCE SCREENING / MAPPING
        ↓
APPLICATION-SPECIFIC CV VARIANT
        ↓
DOCUMENT STRUCTURE
        ↓
HUMAN + MACHINE + INTEGRITY AUDITS
```

## Candidate Discovery Skill

`skills/cv-candidate-discovery/SKILL.md`

Design:
- structured coverage;
- adaptive probing;
- stateful memory;
- bounded sufficiency;
- semantic repeat prevention;
- target-delta follow-up instead of re-interviewing from zero.

The goal is minimum sufficient questioning, not maximum depth.

## Application Targeting Skill

`skills/cv-application-targeting/SKILL.md`

Target unit:
`company × vacancy × target role × context`.

## Document Structure Skill

`skills/cv-document-structure/SKILL.md`

Handles section/page architecture, typography, PDF reading order, extraction robustness, and artifact QA.

## Canonical standards

- `standards/CONSISTENCY_STANDARD.md`
- `standards/DATE_STANDARD.md`

## Automated validation

`.github/workflows/validate.yml`

The static audit covers:
- root architecture;
- Candidate Discovery;
- Application Targeting;
- Document Structure;
- schemas/specs;
- consistency/date rules;
- adversarial case coverage.

Scientific saturation is not claimed.
