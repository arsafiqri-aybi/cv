---
name: cv-document-structure
description: Design, audit, or repair the document structure of a CV/resume. Use for section selection/order, page architecture, information hierarchy, typography, spacing, date/metadata consistency, one-vs-two page decisions, single-vs-multi-column decisions, experience/project/education entry structure, PDF reading order, parsing robustness, accessibility structure, or final document QA. Treat structure as semantic encoding; preserve upstream candidate facts and claim calibration.
---

# CV Document Structure

Design the CV as a semantic document system.

## 1. Load context

Resolve:
- candidate stage;
- target role;
- industry;
- region/jurisdiction;
- document type;
- output language/locale;
- evidence volume;
- known submission platform;
- output medium.

Do not assume a universal structure.

## 2. Preserve upstream truth

Structure may reorder, group, emphasize, and compress.

Structure may not invent, strengthen unsupported claims, hide hard gaps, or detach outcomes from attribution.

Use the root CV skill for evidence and claim calibration.

## 3. Load consistency authority

Before structural decisions, read:
- `references/CONSISTENCY_STANDARD.md`
- `references/DATE_STANDARD.md`

These govern:
- canonical section IDs;
- date normalization/display;
- hierarchy IDs;
- units;
- terminology;
- locations;
- metrics;
- links;
- bullet editorial consistency.

## 4. Build semantic sections

Read:
- `references/STRUCTURE_ARCHITECTURE.md`
- `references/SECTION_SYSTEM.md`

Include a section only when it has a clear purpose and useful evidence.

Use canonical internal IDs even when display labels are localized.

## 5. Determine information order

Order by:
- role relevance;
- evidence strength;
- recency;
- differentiation;
- reader expectations;
- chronology/auditability.

Do not use a fixed section sequence for every candidate.

## 6. Build entry microstructure

Keep title, organization, dates, location, and evidence bullets as coherent semantic units.

Do not visually separate metadata so far that human or machine association becomes ambiguous.

## 7. Define typography and spatial hierarchy

Read:
- `references/TYPOGRAPHY_LAYOUT.md`

Typography must make canonical hierarchy levels recognizable.

Engineering defaults are starting points, not scientific laws.

## 8. Resolve page architecture

Read:
- `references/DECISION_MATRIX.md`

Do not force one page.

Use relevance density and evidence sufficiency.

If space is tight, edit content before shrinking typography.

## 9. Resolve machine/PDF structure

Read:
- `references/PDF_MACHINE_COMPATIBILITY.md`

Keep parsing, entity extraction, retrieval, ranking, and selection separate.

When platform is unknown:
- prefer a simple linear reading order;
- use conventional section semantics;
- keep critical text selectable;
- test final extraction.

Multi-column layouts are conditional, not automatically forbidden.

## 10. Verify artifact

If final PDF/DOCX exists:
- inspect human hierarchy;
- extract text;
- inspect reading order;
- verify employer/title/date associations;
- verify date display consistency;
- verify links;
- inspect page breaks;
- check clipping/overflow;
- inspect section headings;
- run editorial consistency checks.

Do not call a document machine-safe solely from a screenshot.

## 11. Evidence discipline

Read:
- `references/SCIENCE_BASE.md`

Distinguish:
- CV-specific research;
- adjacent document science;
- technical standards;
- parser research;
- technical benchmarks;
- engineering defaults;
- contextual heuristics.

Never turn a heuristic into a universal scientific rule.

## 12. Output

Follow:
- `references/OUTPUT_CONTRACT.md`

For small edits, use the minimal path.
For full CV generation, produce a complete structure specification before rendering the final artifact.

## Protected non-rules

Never state as universal:
- exactly one page;
- exactly two pages;
- single-column only;
- multi-column always breaks ATS;
- sans-serif only;
- serif only;
- every CV needs a summary;
- one fixed section order;
- visual polish guarantees screening success.
