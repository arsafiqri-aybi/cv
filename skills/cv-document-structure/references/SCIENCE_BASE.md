# CV Document Structure Research v1.0

Date: 2026-10-06

## Scope

This research isolates the **document-structure problem** inside CV/resume construction.

It does not ask only:
- which template looks good?
- how many pages?
- which font?
- one column or two?

It asks:

> How should candidate evidence be encoded into a document whose semantic hierarchy, information priority, visual organization, reading order, and export structure support accurate human and machine interpretation?

## Evidence classes

Every rule in the subsystem must be labeled as one of:

1. **CV_SPECIFIC_RESEARCH** — directly studies resumes/CVs or recruiter screening.
2. **ADJACENT_DOCUMENT_RESEARCH** — typography, reading, headings, visual search, information design.
3. **TECHNICAL_STANDARD** — PDF/WCAG/PDF-UA or comparable formal specification.
4. **PARSER_RESEARCH** — academic information extraction / resume parsing.
5. **TECHNICAL_BENCHMARK** — transparent but non-peer-reviewed parser testing.
6. **ENGINEERING_DEFAULT** — practical starting value, explicitly not a scientific law.
7. **CONTEXTUAL_HEURISTIC** — local convention requiring context validation.

Do not promote engineering defaults into scientific rules.

---

## R1 — Layout affects screening, but no universal visual style exists

Arnulf, Tegner, & Larssen (2010) experimentally varied resume layout while holding candidate information constant. Formal layouts were preferred over more creative treatments in their study.

**Implication**
- visual structure can influence shortlisting;
- visual design is consequential;
- "creative" is not automatically advantageous.

**Boundary**
- one historical study;
- one vacancy/context;
- does not prove a universal preferred template.

Classification: CV_SPECIFIC_RESEARCH

DOI: 10.1080/13594320902903613

---

## R2 — Recruiter attention is distributed unevenly across document regions

Pina et al. (2023) used eye tracking during resume screening. Total viewing time and time on Experience/Education contributed to predicting advancement decisions.

**Implication**
- section placement and salience matter;
- Experience and Education can be high-value attention regions in relevant contexts;
- hierarchy should make high-priority evidence easy to locate.

**Do not infer**
- a universal "6-second rule";
- a universal section order;
- attention automatically means validity.

Classification: CV_SPECIFIC_RESEARCH

DOI: 10.3390/make5030038

---

## R3 — Detail, clarity, and structure can matter to job-search outcomes

Wingate, Robie, Powell, & Bourdage (2025) found that more detailed, clear, and structured resumes/cover letters were associated with more interview success and shorter time-to-job in a Canadian early-career/co-op sample after controls.

**Implication**
- document structure and clarity are not cosmetic;
- information organization is a consequential communication layer.

**Boundary**
- resume + cover letter composition considered together;
- early-career context;
- does not establish job-performance validity.

Classification: CV_SPECIFIC_RESEARCH

DOI: 10.1111/ijsa.70022

---

## R4 — Resume length is context-dependent; one-page rules are not universal

Blackburn-Brockman & Belanger (2001) experimentally compared one- and two-page resumes for similarly qualified entry-level accounting candidates. Recruiters favored two-page versions in that context.

**Implication**
- "one page always wins" is empirically false as a universal statement;
- length must be controlled by relevance density, context, and information sufficiency.

**Boundary**
- old study;
- highly specific occupation and candidate group.

Classification: CV_SPECIFIC_RESEARCH

DOI: 10.1177/002194360103800104

---

## R5 — Recruiters value content differently; applied evidence can be interpreted more strongly

Stout & Olson-Buchanan (2019) found recruiters rated applied experiences such as internships more favorably than several extracurricular categories on employability/skill impressions.

Older content-preference studies also show preferences change over time and that recruiters historically shifted toward less personal information and more evidence of achievement/accomplishment.

**Implication**
- section inclusion should follow evidence value rather than template completeness;
- contextual explanation can be necessary when labels/organizations are not self-explanatory.

Classification: CV_SPECIFIC_RESEARCH

DOIs:
- 10.1177/0894845318757916
- 10.1177/002194368902600206
- 10.1177/108056999706000206

---

## R6 — Headings are structural signals, not decoration

General document research has repeatedly shown that headings support organization, recall, and navigation.

Recent information-design research also finds stronger typographic differentiation makes headings easier to identify in print and screen contexts.

**Implication**
- section headings should be semantically clear;
- hierarchy levels should be visually distinguishable;
- headings must be consistently formatted.

Classification: ADJACENT_DOCUMENT_RESEARCH

Selected sources:
- Lorch et al., headings/outlines and recall, DOI: 10.1016/0361-476X(89)90029-5
- Effects of Headings on Text Processing Strategies, DOI: 10.1006/ceps.2000.1056
- Timpany (2026), DOI: 10.1075/idj.25001.tim

---

## R7 — Serif vs sans-serif is not a meaningful universal CV rule

Modern typography research does not support a simple "serif is more readable" or "sans-serif is more readable" universal rule.

A 2026 experimental study found no systematic comprehension/cognitive-load advantage for Verdana versus Times New Roman across paper/screen conditions. Controlled legibility work similarly shows minimal or inconsistent serif effects.

**Implication**
Choose fonts for:
- legibility;
- glyph clarity;
- weight range;
- PDF embedding;
- familiarity;
- availability;
- consistent metrics.

Do not choose only because of serif category.

Classification: ADJACENT_DOCUMENT_RESEARCH

Selected sources:
- DOI: 10.1080/0144929X.2026.2678378
- DOI: 10.1016/j.visres.2005.06.013
- DOI: 10.1111/opo.13039

---

## R8 — Line length and text geometry affect scanning/readability, but exact optimum varies

Research on line length shows effects on scanning, reading speed, comprehension, and preference. Reviews commonly reject both extremely short and extremely long lines.

**Implication**
- avoid very wide full-page text blocks at small size;
- avoid narrow columns that cause excessive wrapping;
- optimize line length together with font size and spacing.

**Boundary**
CV bullets are short information units, not continuous prose. General reading findings must be adapted rather than copied as hard numbers.

Classification: ADJACENT_DOCUMENT_RESEARCH

Selected sources:
- Nanavati & Bias (2005), Visible Language
- Ling & van Schaik (2006), DOI: 10.1016/j.ijhcs.2005.08.015

---

## R9 — Machine interpretation depends on section structure and reading order

Academic resume-parsing research consistently treats resumes as heterogeneous semi-structured documents.

Werner & Laber (2024) specifically address:
- correct reading order;
- section/subsection extraction;
- PDF resume structure reconstruction.

Retyk et al. (2023) formulate resume parsing as hierarchical line/token sequence labeling across multiple languages.

Gaur et al. (2021) show that even a single section such as Education requires specialized named-entity extraction.

**Implication**
The document should make these entities structurally recoverable:
- identity/contact;
- section boundaries;
- employer;
- role title;
- date interval;
- institution;
- degree;
- skills/projects.

Classification: PARSER_RESEARCH

Selected sources:
- DOI: 10.1016/j.eswa.2023.122495
- arXiv:2309.07015
- DOI: 10.1007/s00521-020-05351-2
- DOI: 10.1155/2018/5761287

---

## R10 — PDF reading order is an artifact property that should be verified

W3C PDF guidance states that logical reading order should correspond to intended sequence, and that complex layouts can convert incorrectly even when visually clear.

Multi-column layouts are not inherently invalid, but their reading order must be correct.

**Implication**
A machine-safe CV cannot be judged only from screenshots.

Verify:
- text extraction;
- logical reading order;
- heading semantics where supported;
- link order;
- Unicode;
- selectable text.

Classification: TECHNICAL_STANDARD

Sources:
- W3C WCAG Technique PDF3 — correct tab/reading order
- W3C WCAG Technique PDF9 — tagged headings

---

## R11 — Two-column CVs are a conditional design, not categorically good or bad

Academic parsing research establishes reading-order reconstruction as a real technical problem.

Recent transparent parser experiments also report that some two-column PDFs preserve words while corrupting line order.

**Implication**
Default to a simple linear reading order when platform behavior is unknown.

A two-column design is allowed only when:
1. it has a real information-design benefit;
2. reading order is intentional;
3. final PDF extraction is tested;
4. essential chronology/identity is not fragmented.

Classification:
- PARSER_RESEARCH + TECHNICAL_BENCHMARK

Do not claim:
"all ATS reject two columns."

---

## R12 — Standard section semantics are preferable to creative labels

Resume parsers commonly perform section segmentation before entity extraction. Academic work explicitly models section classes and subsections.

Thus a heading such as `Experience` carries semantic value beyond typography.

**Implication**
Prefer conventional section names where they accurately describe the content:
- Experience
- Education
- Skills
- Projects
- Certifications
- Publications
- Awards
- Leadership / Volunteer Experience

Creative labels may be used only if:
- the platform is known not to depend on section mapping;
- human clarity improves;
- the document still has accessible semantic structure.

Classification:
- PARSER_RESEARCH + ENGINEERING_DEFAULT

---

# Architecture conclusion

CV document structure is best modeled as a layered encoding system:

```text
L0 — DOCUMENT PURPOSE / TARGET CONTEXT
↓
L1 — SEMANTIC SECTION ARCHITECTURE
↓
L2 — INFORMATION PRIORITY + ORDER
↓
L3 — ENTRY / EVIDENCE MICROSTRUCTURE
↓
L4 — TYPOGRAPHIC + SPATIAL HIERARCHY
↓
L5 — PAGE FLOW / LENGTH / BREAKS
↓
L6 — MACHINE + ACCESSIBILITY STRUCTURE
↓
L7 — FINAL ARTIFACT VERIFICATION
```

These are operational layers, not claims of separate scientific disciplines.

# Protected non-rules

Do not encode any of these as universal:

- exactly one page;
- exactly two pages;
- sans-serif only;
- serif only;
- one column always;
- two columns always fail ATS;
- every CV needs a summary;
- Skills must always precede Experience;
- Education must always be last;
- quantified bullet = stronger bullet;
- graphical novelty = stronger first impression;
- attractive PDF = parseable PDF.
