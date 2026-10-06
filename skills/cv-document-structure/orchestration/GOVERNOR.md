# Document Structure Governor

Optimize document resources without lowering semantic integrity.

## Resource hierarchy

When space is constrained, change in this order:

1. remove irrelevant evidence;
2. remove redundancy;
3. shorten weakly diagnostic prose;
4. simplify low-value section metadata;
5. tighten excess spacing modestly;
6. adjust typography within legibility range;
7. add a page if high-value evidence still requires space.

Do **not** start by shrinking font.

## Escalate research when
- user requests a contested rule;
- occupation/context is unusual;
- parser behavior is platform-specific;
- regional/legal convention matters;
- scientific evidence conflicts.

## Stop optimization when
- all high-value evidence is represented;
- hierarchy is clear;
- artifact extraction is coherent;
- further compression would reduce readability or evidence quality.

## Failure diagnoses

- SECTION_OVERLOAD
- WEAK_PRIORITY
- DENSITY_EXCESS
- HIERARCHY_AMBIGUITY
- READING_ORDER_FAILURE
- ENTITY_ASSOCIATION_FAILURE
- EXPORT_CORRUPTION
- LEGIBILITY_FAILURE
