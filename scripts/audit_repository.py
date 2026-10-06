#!/usr/bin/env python3
"""Static and cross-file consistency audit for the CV repository."""
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RELEASE_VERSION="1.1.0"

REQUIRED=[
 "README.md","PROJECT_CONTRACT.md","SKILL.md",
 "standards/CONSISTENCY_STANDARD.md","standards/DATE_STANDARD.md",
 "orchestration/MASTER_PROMPT.md","orchestration/SCALE.md","orchestration/GOVERNOR.md",
 "science/CONSTRUCT_TAXONOMY_V1.md","graph/nodes.json","graph/edges.json","graph/non_edges.json",
 "schemas/candidate-evidence.schema.json","candidate_evidence/MODEL.md",
 "reasoning/ENGINE.md","construction/CV_CONSTRUCTION.md","construction/DOCUMENT_RULES.md",
 "audits/HUMAN_SCREENING.md","audits/MACHINE_SCREENING.md","audits/FAIRNESS_PRIVACY.md",
 "evaluation/rubric.json","evaluation/cases.json",
 "skills/cv-document-structure/SKILL.md",
 "skills/cv-document-structure/references/CONSISTENCY_STANDARD.md",
 "skills/cv-document-structure/references/DATE_STANDARD.md",
 "skills/cv-document-structure/references/SCIENCE_BASE.md",
 "skills/cv-document-structure/references/STRUCTURE_ARCHITECTURE.md",
 "skills/cv-document-structure/references/SECTION_SYSTEM.md",
 "skills/cv-document-structure/references/TYPOGRAPHY_LAYOUT.md",
 "skills/cv-document-structure/references/PDF_MACHINE_COMPATIBILITY.md",
 "skills/cv-document-structure/references/DECISION_MATRIX.md",
 "skills/cv-document-structure/references/OUTPUT_CONTRACT.md",
 "skills/cv-document-structure/evaluation/cases.json",
 "skills/cv-document-structure/structure-spec.json",
 "release/RELEASE_MANIFEST.json","release/RELEASE_NOTES.md",
 "release/KNOWN_LIMITATIONS.md","release/QUALITY_GATES.md",
]

def fail(msg, errors):
    errors.append(msg)

def read(rel):
    return (ROOT/rel).read_text(encoding="utf-8")

def main():
    errors=[]
    for rel in REQUIRED:
        if not (ROOT/rel).exists():
            fail(f"missing required file: {rel}",errors)

    if errors:
        for e in errors:
            print("ERROR:",e)
        return 1

    # Graph integrity
    try:
        nodes=json.loads(read("graph/nodes.json"))["nodes"]
        edges=json.loads(read("graph/edges.json"))["edges"]
        non=json.loads(read("graph/non_edges.json"))["non_edges"]
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

    # Root rubric
    try:
        rubric=json.loads(read("evaluation/rubric.json"))
        if not any(d.get("id")=="factual_fidelity" and d.get("critical") for d in rubric["dimensions"]):
            fail("factual_fidelity must be critical",errors)
    except Exception as exc:
        fail(f"rubric validation error: {exc}",errors)

    # Release version consistency
    try:
        manifest=json.loads(read("release/RELEASE_MANIFEST.json"))
        if manifest.get("version")!=RELEASE_VERSION:
            fail(f"manifest version must be {RELEASE_VERSION}",errors)
        for rel in ["README.md","release/RELEASE_NOTES.md","release/KNOWN_LIMITATIONS.md","release/QUALITY_GATES.md"]:
            if RELEASE_VERSION not in read(rel):
                fail(f"{rel} must mention release version {RELEASE_VERSION}",errors)
        if not manifest.get("components",{}).get("document_structure_skill"):
            fail("manifest must declare document_structure_skill",errors)
        if not manifest.get("components",{}).get("consistency_standard"):
            fail("manifest must declare consistency_standard",errors)
        if not manifest.get("components",{}).get("date_standard"):
            fail("manifest must declare date_standard",errors)
    except Exception as exc:
        fail(f"release consistency error: {exc}",errors)

    # Consistency standard runtime snapshot must not drift.
    if read("standards/CONSISTENCY_STANDARD.md") != read("skills/cv-document-structure/references/CONSISTENCY_STANDARD.md"):
        fail("runtime CONSISTENCY_STANDARD snapshot drift",errors)
    if read("standards/DATE_STANDARD.md") != read("skills/cv-document-structure/references/DATE_STANDARD.md"):
        fail("runtime DATE_STANDARD snapshot drift",errors)

    # Document-structure spec
    try:
        spec=json.loads(read("skills/cv-document-structure/structure-spec.json"))
        section_ids=[s["id"] for s in spec["canonical_sections"]]
        expected=["contact","summary","experience","projects","education","skills","certifications","publications_research","awards","leadership_volunteering","portfolio"]
        if section_ids!=expected:
            fail("canonical section IDs/order drift",errors)
        hierarchy=[h["id"] for h in spec["hierarchy_levels"]]
        if hierarchy!=["H0","H1","H2","M1","M2","B1","B2"]:
            fail("hierarchy ID drift",errors)
        if "margin_in_range" in json.dumps(spec):
            fail("ambiguous margin_in_range field prohibited",errors)
        if "margin_inch_range" not in spec.get("defaults",{}):
            fail("margin_inch_range required",errors)
        if "date_association" not in spec.get("required_artifact_tests",[]):
            fail("date_association artifact test required",errors)
        if spec.get("date_standard",{}).get("range_separator")!="en_dash":
            fail("date range separator must be en_dash",errors)
    except Exception as exc:
        fail(f"document-structure spec error: {exc}",errors)

    # Document-structure eval coverage
    try:
        ds=json.loads(read("skills/cv-document-structure/evaluation/cases.json"))
        ids=[c["id"] for c in ds.get("cases",[])]
        if len(ids)<23:
            fail("document-structure skill needs >=23 adversarial cases",errors)
        for needed in ["DS17","DS18","DS19","DS20","DS21","DS22","DS23"]:
            if needed not in ids:
                fail(f"missing consistency case {needed}",errors)
    except Exception as exc:
        fail(f"document-structure evaluation error: {exc}",errors)

    # Candidate date schema alignment
    try:
        schema=json.loads(read("schemas/candidate-evidence.schema.json"))
        props=schema["properties"]["evidence_items"]["items"]["properties"]
        for k in ["start_date","end_date","is_current","date_source_text"]:
            if k not in props:
                fail(f"candidate schema missing {k}",errors)
        if "Present" in json.dumps(props.get("end_date",{})):
            fail("candidate schema must not encode Present as normalized end_date",errors)
    except Exception as exc:
        fail(f"candidate schema consistency error: {exc}",errors)

    if errors:
        for e in errors:
            print("ERROR:",e)
        return 1
    print("PASS: static repository and consistency audit")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
