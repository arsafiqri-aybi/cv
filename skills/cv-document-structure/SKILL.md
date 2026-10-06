---
name: cv-document-structure
description: Design, audit, or repair the document structure of a CV/resume. Use for section selection/order, page architecture, information hierarchy, typography, spacing, one-vs-two page decisions, one-vs-two column decisions, experience/project/education entry structure, PDF reading order, parsing robustness, accessibility structure, or final document QA. Treat structure as semantic encoding; preserve upstream candidate facts and claim calibration.
---

# CV Document Structure

Design the CV as a semantic document system.

## 1. Load context

Resolve:
- candidate stage;
- target role;
- industry;
- region/jurisdiction;
- document type (industry resume vs academic CV);
- evidence volume;
- known submission platform;
- output medium.

Do not assume a universal structure.

## 2. Preserve upstream truth

Structure may:
- reorder;
- group;
- emphasize;
- compress.

Structure may not:
- invent;
- strengthen unsupported claims;
- hide hard gaps;
- detach outcomes from attribution.

Use the root CV skill for evidence and claim calibration.

## 3. Build semantic sections

Read:
- `references/STRUCTURE_ARCHITECTURE.md`
- `references/SECTION_SYSTEM.md`

Include a section only when it has a clear purpose and useful evidence.

Prefer conventional semantic headings where they accurately describe content.

## 4. Determine information order

Order by:
- role relevance;
- evidence strength;
- recency;
- differentiation;
- reader expectations;
- chronology/auditability.

Do not use a fixed section sequence for every candidate.

## 5. Build entry microstructure

Keep:
- title;
- organization;
- dates;
- evidence bullets

as coherent semantic units.

Do not visually separate metadata so far that human or machine association becomes ambiguous.

## 6. Define typography and spatial hierarchy

Read:
- `references/TYPOGRAPHY_LAYOUT.md`

Typography must make levels recognizable.

Do not claim serif or sans-serif is universally superior.

Use engineering defaults only as starting points.

## 7. Resolve page architecture

Read:
- `references/DECISION_MATRIX.md`

Do not force one page.

Use relevance density and evidence sufficiency.

If space is tight, edit content before shrinking typography.

## 8. Resolve machine/PDF structure

Read:
- `references/PDF_MACHINE_COMPATIBILITY.md`

Keep parsing, entity extraction, ranking, and selection separate.

When platform is unknown:
- prefer a simple linear reading order;
- use conventional section semantics;
- keep critical text selectable;
- test final extraction.

Two columns are conditional, not automatically forbidden.

## 9. Verify artifact

If final PDF/DOCX exists:
- inspect human hierarchy;
- extract text;
- inspect reading order;
- verify employer/title/date associations;
- verify links;
- inspect page breaks;
- check clipping/overflow;
- inspect critical section headings.

Do not call a document machine-safe solely from a screenshot.

## 10. Evidence discipline

Read:
- `references/SCIENCE_BASE.md`

Distinguish:
- CV-specific research;
- adjacent document science;
- technical standards;
- parser research;
- technical benchmark;
- engineering default;
- contextual heuristic.

Never turn a heuristic into a universal scientific rule.

## 11. Output

Follow:
- `references/OUTPUT_CONTRACT.md`

For small edits, use the minimal path.
For full CV generation, return a complete structure specification before rendering the final artifact.

## Protected non-rules

Never state as universal:
- exactly one page;
- exactly two pages;
- one column only;
- two columns always break ATS;
- sans-serif only;
- serif only;
- every CV needs a summary;
- one fixed section order;
- visual polish guarantees screening success.
