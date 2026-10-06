# CV

**Release: v1.2.0 — PROJECT_COMPLETE_V1 release line**

Research-grounded system for evidence-grounded CV construction, application targeting, document structure, and auditing.

## Central model

```text
CANDIDATE MASTER EVIDENCE
        +
TARGET APPLICATION
(company × vacancy × role × context)
        ↓
REQUIREMENT / EVIDENCE MAP
        ↓
CLAIM-CALIBRATED TAILORING
        ↓
APPLICATION-SPECIFIC CV VARIANT
        ↓
DOCUMENT STRUCTURE + AUDITS
```

Candidate truth remains stable across variants.

## Runtime systems

### Root CV Skill
`SKILL.md`

### Application Targeting Skill
`skills/cv-application-targeting/SKILL.md`

Use for:
- tailoring to a specific vacancy;
- company/role targeting;
- comparing variants;
- evidence-to-JD mapping;
- deciding what to select/omit/reorder/emphasize;
- controlling legitimate company context.

### Document Structure Skill
`skills/cv-document-structure/SKILL.md`

Use for:
- section/page architecture;
- typography/layout;
- PDF reading order;
- machine extraction;
- artifact QA.

## Targeting principle

Do not encode:

```text
one company = one totally unique CV
```

Use:

```text
one master evidence base
→ one serious target application
→ one application-specific CV variant
```

The strongest targeting unit is:

```text
company × vacancy × target role × context
```

Company-specific context is secondary to vacancy/role relevance and only used when it materially changes a CV decision.

## Canonical standards

- `standards/CONSISTENCY_STANDARD.md`
- `standards/DATE_STANDARD.md`

## Research boundaries

Protect:
- tailoring ≠ fabrication;
- role relevance ≠ company flattery;
- terminology alignment ≠ keyword stuffing;
- company context ≠ culture mimicry;
- company-focused tailoring association ≠ proven independent causal advantage.

## Automated validation

`.github/workflows/validate.yml`

The static audit covers:
- root architecture;
- document structure;
- consistency/date standards;
- application targeting;
- schemas/evaluation coverage.

Scientific saturation is not claimed.
