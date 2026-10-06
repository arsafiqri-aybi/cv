#!/usr/bin/env python3
"""Static audit for the CV repository."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[
 "README.md","PROJECT_CONTRACT.md","orchestration/MASTER_PROMPT.md",
 "orchestration/SCALE.md","orchestration/GOVERNOR.md",
 "science/CONSTRUCT_TAXONOMY_V1.md","graph/nodes.json","graph/edges.json",
 "graph/non_edges.json","reasoning/ENGINE.md","construction/CV_CONSTRUCTION.md",
 "audits/HUMAN_SCREENING.md","audits/MACHINE_SCREENING.md",
 "audits/FAIRNESS_PRIVACY.md","evaluation/rubric.json","evaluation/cases.json",
 "skills/cv-document-structure/SKILL.md",
 "skills/cv-document-structure/orchestration/MASTER_PROMPT.md",
 "skills/cv-document-structure/orchestration/SCALE.md",
 "skills/cv-document-structure/orchestration/GOVERNOR.md",
 "skills/cv-document-structure/references/SCIENCE_BASE.md",
 "skills/cv-document-structure/references/STRUCTURE_ARCHITECTURE.md",
 "skills/cv-document-structure/references/SECTION_SYSTEM.md",
 "skills/cv-document-structure/references/TYPOGRAPHY_LAYOUT.md",
 "skills/cv-document-structure/references/PDF_MACHINE_COMPATIBILITY.md",
 "skills/cv-document-structure/references/DECISION_MATRIX.md",
 "skills/cv-document-structure/references/OUTPUT_CONTRACT.md",
 "skills/cv-document-structure/evaluation/cases.json",
 "skills/cv-document-structure/structure-spec.json",
]

def fail(msg, errors):
    errors.append(msg)

def main():
    errors=[]
    for rel in REQUIRED:
        if not (ROOT/rel).exists():
            fail(f"missing required file: {rel}",errors)

    try:
        nodes=json.loads((ROOT/"graph/nodes.json").read_text())["nodes"]
        edges=json.loads((ROOT/"graph/edges.json").read_text())["edges"]
        non=json.loads((ROOT/"graph/non_edges.json").read_text())["non_edges"]
        ids={n["id"] for n in nodes}
        if len(ids)!=len(nodes):
            fail("duplicate node IDs",errors)
        for collection,label in [(edges,"edge"),(non,"non-edge")]:
            for i,e in enumerate(collection):
                if e["source"] not in ids:
                    fail(f"{label} {i} unknown source {e['source']}",errors)
                if e["target"] not in ids:
                    fail(f"{label} {i} unknown target {e['target']}",errors)
    except Exception as exc:
        fail(f"graph validation error: {exc}",errors)

    try:
        rubric=json.loads((ROOT/"evaluation/rubric.json").read_text())
        if not any(d.get("id")=="factual_fidelity" and d.get("critical") for d in rubric["dimensions"]):
            fail("factual_fidelity must be critical",errors)
    except Exception as exc:
        fail(f"rubric validation error: {exc}",errors)

    try:
        ds_cases=json.loads((ROOT/"skills/cv-document-structure/evaluation/cases.json").read_text())
        if len(ds_cases.get("cases",[])) < 12:
            fail("document-structure skill needs >=12 adversarial cases",errors)
        spec=json.loads((ROOT/"skills/cv-document-structure/structure-spec.json").read_text())
        if "reading_order" not in spec.get("required_artifact_tests",[]):
            fail("document-structure spec must require reading_order test",errors)
        if not spec.get("defaults",{}).get("note"):
            fail("engineering defaults must be explicitly labeled",errors)
    except Exception as exc:
        fail(f"document-structure validation error: {exc}",errors)

    if errors:
        for e in errors:
            print("ERROR:",e)
        return 1
    print("PASS: static repository audit")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
