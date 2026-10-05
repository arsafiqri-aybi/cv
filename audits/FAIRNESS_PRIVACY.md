# Fairness, Privacy & Sensitive-Data Audit v1

## Goal

Reduce irrelevant exposure and discriminatory risk without erasing legitimate identity or inventing "neutrality."

## Principles

1. Fairness is cross-cutting.
2. Candidate-side formatting cannot eliminate structural discrimination.
3. Legal requirements vary by jurisdiction.
4. Sensitive data is not automatically harmful or automatically removable.
5. The user's identity should not be rewritten to imitate an employer.

## Review classes

### Demographic / sensitive cues
Examples may include:
- age/date of birth;
- gender/sex markers;
- photo;
- marital/family status;
- religion;
- ethnicity/race;
- disability/health information;
- nationality/citizenship;
- political or union information.

Handle only with:
- relevance;
- jurisdiction;
- explicit user context;
- privacy necessity.

### Indirect cues
Examples:
- graduation year;
- organization affiliation;
- location;
- names;
- language;
- interests.

Do not assume they are removable or legally protected everywhere; flag context.

### Machine fairness
If an algorithmic screening system is known:
- identify protected/sensitive attributes;
- identify proxy variables;
- separate performance from fairness metrics;
- document comparison baseline;
- avoid assuming AI is automatically fairer than humans.

## CV construction default

For conventional industry applications, exclude irrelevant sensitive personal data by default unless:
- customary/legal requirements clearly justify it;
- the user explicitly requests inclusion with awareness of tradeoffs;
- role-specific necessity exists.

## Critical failures

- unnecessary highly sensitive data exposure;
- advice presented as universal law despite jurisdiction dependence;
- identity manipulation or misrepresentation;
- fairness claim without comparison baseline;
- demographic cue used as a fabricated "culture fit" strategy.
