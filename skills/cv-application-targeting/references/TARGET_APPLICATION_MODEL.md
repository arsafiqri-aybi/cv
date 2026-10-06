# Target Application Model v1.0

## Purpose

Represent the exact application context that a CV variant is targeting.

A `Target Role` models the work.

A `Target Application` models the concrete application instance.

## Canonical identity

```text
target_application
=
company
+ vacancy
+ target_role
+ context
```

## Fields

### Application identity
- application_id
- company_name
- vacancy_title
- vacancy_id or source reference when available
- target_role_id
- location / work arrangement when material
- language / locale
- application_channel
- source freshness

### Vacancy evidence
- job posting
- recruiter message
- company careers page
- role-specific documentation
- user-provided context

### Company context
Only collect context that can materially affect relevance:
- industry/domain;
- product/service;
- customer/user type;
- technology environment;
- regulatory environment;
- business model where job-relevant;
- role-specific organization context.

Do not collect company facts merely to decorate the CV.

### Constraints
- required credentials;
- work authorization;
- location;
- language;
- schedule;
- security clearance;
- portfolio/work-sample requirement;
- other explicit gates.

## Targeting levels

### T0 — General
No concrete vacancy.

Use:
- broad evidence-led CV.

Do not claim application-specific optimization.

### T1 — Role-family targeted
Known role family, no concrete employer/vacancy.

Use:
- role-family requirements;
- conservative terminology alignment.

### T2 — Vacancy targeted
Concrete job posting / vacancy.

Use:
- requirement-level evidence mapping;
- evidence selection/reordering;
- supported terminology alignment.

### T3 — Vacancy + legitimate company context
Concrete vacancy plus verified company context that changes interpretation.

Use company context only where it:
- changes relevance;
- clarifies domain transfer;
- changes terminology;
- affects constraints;
- provides a meaningful reason to foreground specific evidence.

T3 is not "more personalized = automatically better."

## Variant identity

A CV variant should record:
- candidate evidence snapshot/version;
- target application ID;
- target role model version;
- date generated;
- tailoring decisions;
- unresolved gaps.

This enables comparison without rewriting candidate truth.
