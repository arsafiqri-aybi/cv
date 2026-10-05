# Machine Interpretation Audit v1

## Goal

Assess document robustness for likely machine-mediated application workflows without pretending all ATS systems behave the same.

## Separate functions

Never collapse:

```text
PARSING
SECTION DETECTION
ENTITY EXTRACTION
NORMALIZATION
SEARCH / RETRIEVAL
RANKING
KNOCKOUT RULES
AI / LLM EVALUATION
```

## Parseability checks

- text is selectable;
- reading order is coherent;
- headings are recognizable;
- dates are plain text;
- employer / role / education entities are not embedded only in graphics;
- multi-column layout does not scramble extraction;
- tables do not merge unrelated fields;
- icons are not the sole carrier of meaning;
- headers/footers do not contain critical content;
- export preserves Unicode and text order.

## Semantic checks

- target terminology is used only when supported;
- synonyms are not needlessly replaced by obscure phrasing;
- skills appear in context where possible;
- titles and technologies are spelled consistently;
- acronyms are expanded when ambiguity matters.

## System-specific checks

Only run when the actual platform/system is known:
- required file type;
- knockout questions;
- parser behavior;
- field mapping;
- ranking/recommendation features;
- AI disclosure requirements.

## Forbidden claims

Do not say:
- "ATS score = 92%";
- "all ATS require one column";
- "repeat keyword X times";
- "this guarantees parsing";
- "this guarantees ranking."

unless a defined system and empirical test support the statement.

## Critical failures

- extraction loses material evidence;
- dates or roles map to wrong employer;
- text order becomes incoherent;
- unsupported keyword stuffing;
- critical information only in image;
- parser-safe claim made without testing;
- ranking claim inferred from parsing success.
