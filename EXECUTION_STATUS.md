# Execution Status

Last updated: 2026-10-06

## Release

**v1.2.0 — PROJECT_COMPLETE_V1 release line**

## Root CV system
COMPLETE for v1.x operational scope.

## Application Targeting subsystem
COMPLETE v1:
- research base;
- Target Application model;
- JSON Schema;
- targeting levels T0–T3;
- Tailoring Rules;
- Company Context policy;
- Prompting / Scale / Governor;
- runtime Skill;
- reasoning integration;
- 18 adversarial cases;
- static audit coverage.

## Core targeting rule

```text
candidate master evidence
→ target application
→ requirement/evidence mapping
→ calibrated tailoring
→ application-specific CV variant
```

Target application:
`company × vacancy × target role × context`.

## Non-claim

The system does not claim that a fully unique company-specific CV has a proven independent causal advantage.

## Automated validation

GitHub Actions runs repository validation on pushes and pull requests.
