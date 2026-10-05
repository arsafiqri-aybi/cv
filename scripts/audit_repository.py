#!/usr/bin/env python3
"""Static audit for the CV repository."""
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[
 "README.md","PROJECT_CONTRACT.md","orchestration/MASTER_PROMPT.md",
 "orchestration/SCALE.md","orchestration/GOVERNOR.md",
 "science/CONSTRUCT_TAXONOMY_V1.md","graph/nodes.json","graph/edges.json",
 "graph/non_edges.json","reasoning/ENGINE.md","construction/CV_CONSTRUCTION.md",
 "audits/HUMAN_SCREENING.md","audits/MACHINE_SCREENING.md",
 "audits/FAIRNESS_PRIVACY.md","evaluation/rubric.json","evaluation/cases.json",
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

    if errors:
        for e in errors:
            print("ERROR:",e)
        return 1
    print("PASS: static repository audit")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
