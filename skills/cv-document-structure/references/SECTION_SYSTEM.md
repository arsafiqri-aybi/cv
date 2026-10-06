# Section System v1.1

## Principle

A CV section is a **semantic container for evidence**, not a decorative panel.

Canonical internal section IDs are defined in:
- `CONSISTENCY_STANDARD.md`
- `../structure-spec.json`

Display labels may be localized, but IDs remain stable.

## Inclusion decision

For each candidate section reason conceptually about:

```text
role relevance
× evidence strength
× differentiation
× reader need
− space cost
− redundancy
− inference risk
```

Do not turn this into fake precise arithmetic.

## `contact` — Header/contact block

Purpose:
- uniquely identify candidate;
- enable contact;
- provide high-value professional links.

Prefer:
- full professional name;
- email;
- phone when appropriate;
- city/region when useful;
- LinkedIn/portfolio/GitHub only when valuable.

Avoid by default:
- full street address;
- irrelevant sensitive personal data;
- icon-only contact methods.

## `summary` — Professional Summary

Optional.

Include when it solves a real problem:
- career transition;
- senior-level synthesis;
- multidisciplinary identity;
- target-role positioning.

Exclude when it repeats obvious information.

## `experience` — Experience

Usually the primary evidence container for experienced industry candidates.

Entry order:
- generally reverse chronological for conventional industry applications;
- deviations require a reason.

Within each role:
1. role + organization + dates;
2. highest-relevance evidence;
3. supporting evidence;
4. routine duties only when diagnostically necessary.

Dates must follow `DATE_STANDARD.md`.

## `projects` — Projects

Use when projects carry material evidence.

Especially valuable for:
- students;
- career changers;
- technical candidates;
- builders/designers;
- freelance/open-source work.

Do not duplicate Experience bullets verbatim.

## `education` — Education

Priority increases when:
- early career;
- credential is a hard constraint;
- degree/field is highly relevant;
- academic achievement is meaningful.

Priority decreases when:
- a long professional record dominates;
- education is old and weakly diagnostic.

## `skills` — Skills

Skills are an index, not proof.

Every material skill should be supportable elsewhere or by credential/artifact.

Avoid:
- proficiency bars;
- stars;
- arbitrary percentages;
- unsupported keyword dumps.

## `certifications` — Certifications

Use when required, strongly relevant, or externally verifiable.

Include issuer and validity/expiry when material.

## `publications_research` — Publications & Research

Use structured bibliographic conventions for research-heavy candidates.

For industry CVs, select highly relevant items unless a full academic CV is required.

## `awards` — Awards

Include when selective, relevant, and understandable.

Add context for obscure awards.

## `leadership_volunteering` — Leadership & Volunteering

Include when it contributes credible evidence not already represented.

Explain obscure organizations minimally when needed.

## `portfolio` — Selected Work

Use for high-value external proof:
- portfolio;
- case study;
- GitHub repository;
- product;
- publication.

Do not use as a duplicate link dump.

## Contextual order matrix

| Candidate context | Usually high priority | Conditional | Usually lower |
|---|---|---|---|
| Experienced industry | Experience | Professional Summary, Skills, Projects, Certifications | Education |
| Student | Education, Projects/Experience | Skills, Leadership & Volunteering | Professional Summary |
| Career changer | Professional Summary, transferable Projects/Evidence, Experience | Certifications, Skills | unrelated detail |
| Technical builder | Experience/Projects | Skills, Selected Work | generic summary |
| Regulated role | Certifications/Licenses, Experience | Education | optional extras |
| Academic | Education, Research, Publications | Teaching, Awards, Service | industry-style summary |

This is an engineering decision aid, not a universal empirical ranking.
