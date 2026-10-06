#!/usr/bin/env python3
"""Static and cross-file consistency audit for the CV repository."""
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCRIPTS=ROOT/"scripts"
sys.path.insert(0,str(SCRIPTS))
import validate_models

RELEASE_VERSION="1.2.0"

REQUIRED=[
 "README.md","PROJECT_CONTRACT.md","SKILL.md","EXECUTION_STATUS.md","ROADMAP.md",
 "standards/CONSISTENCY_STANDARD.md","standards/DATE_STANDARD.md",
 "orchestration/MASTER_PROMPT.md","orchestration/SCALE.md","orchestration/GOVERNOR.md",
 "science/CONSTRUCT_TAXONOMY_V1.md","graph/nodes.json","graph/edges.json","graph/non_edges.json",
 "schemas/candidate-evidence.schema.json","candidate_evidence/MODEL.md",
 "reasoning/ENGINE.md","construction/CV_CONSTRUCTION.md","construction/DOCUMENT_RULES.md",
 "audits/HUMAN_SCREENING.md","audits/MACHINE_SCREENING.md","audits/FAIRNESS_PRIVACY.md",
 "evaluation/rubric.json","evaluation/cases.json","evaluation/STATUS.md",
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
 "application_targeting/MODEL.md",
 "schemas/target-application.schema.json",
 "reasoning/APPLICATION_TARGETING.md",
 "research/APPLICATION_TARGETING_RESEARCH_V1.md",
 "skills/cv-application-targeting/SKILL.md",
 "skills/cv-application-targeting/orchestration/MASTER_PROMPT.md",
 "skills/cv-application-targeting/orchestration/SCALE.md",
 "skills/cv-application-targeting/orchestration/GOVERNOR.md",
 "skills/cv-application-targeting/references/RESEARCH_BASE.md",
 "skills/cv-application-targeting/references/TARGET_APPLICATION_MODEL.md",
 "skills/cv-application-targeting/references/TAILORING_RULES.md",
 "skills/cv-application-targeting/references/COMPANY_CONTEXT.md",
 "skills/cv-application-targeting/references/OUTPUT_CONTRACT.md",
 "skills/cv-application-targeting/evaluation/cases.json",
 "skills/cv-application-targeting/application-target-spec.json",
 "skills/cv-application-targeting/references/README.md",
 "skills/cv-application-targeting/agents/openai.yaml",
 "release/RELEASE_MANIFEST.json","release/RELEASE_NOTES.md",
 "release/KNOWN_LIMITATIONS.md","release/QUALITY_GATES.md",
]

def fail(msg,errors):
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

    # Critical root rubric
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
        for rel in [
            "README.md","EXECUTION_STATUS.md","ROADMAP.md","evaluation/STATUS.md",
            "release/RELEASE_NOTES.md","release/KNOWN_LIMITATIONS.md","release/QUALITY_GATES.md"
        ]:
            if RELEASE_VERSION not in read(rel):
                fail(f"{rel} must mention release version {RELEASE_VERSION}",errors)
        for component in ["document_structure_skill","consistency_standard","date_standard","application_targeting_skill","target_application_model","application_target_schema"]:
            if not manifest.get("components",{}).get(component):
                fail(f"manifest must declare {component}",errors)
    except Exception as exc:
        fail(f"release consistency error: {exc}",errors)

    # Runtime snapshots must not drift from canonical standards.
    if read("standards/CONSISTENCY_STANDARD.md")!=read("skills/cv-document-structure/references/CONSISTENCY_STANDARD.md"):
        fail("runtime CONSISTENCY_STANDARD snapshot drift",errors)
    if read("standards/DATE_STANDARD.md")!=read("skills/cv-document-structure/references/DATE_STANDARD.md"):
        fail("runtime DATE_STANDARD snapshot drift",errors)

    # Document structure spec
    try:
        spec=json.loads(read("skills/cv-document-structure/structure-spec.json"))
        expected_sections=["contact","summary","experience","projects","education","skills","certifications","publications_research","awards","leadership_volunteering","portfolio"]
        if [s["id"] for s in spec["canonical_sections"]]!=expected_sections:
            fail("canonical section IDs/order drift",errors)
        if [h["id"] for h in spec["hierarchy_levels"]]!=["H0","H1","H2","M1","M2","B1","B2"]:
            fail("hierarchy ID drift",errors)
        if "margin_in_range" in json.dumps(spec):
            fail("ambiguous margin_in_range field prohibited",errors)
        if "margin_inch_range" not in spec.get("defaults",{}):
            fail("margin_inch_range required",errors)
        for test in ["reading_order","entity_association","date_association","editorial_consistency"]:
            if test not in spec.get("required_artifact_tests",[]):
                fail(f"required artifact test missing: {test}",errors)
        if spec.get("date_standard",{}).get("range_separator")!="en_dash":
            fail("date range separator must be en_dash",errors)
    except Exception as exc:
        fail(f"document-structure spec error: {exc}",errors)

    # Document-structure adversarial coverage
    try:
        ds=json.loads(read("skills/cv-document-structure/evaluation/cases.json"))
        case_ids=[c["id"] for c in ds.get("cases",[])]
        if len(case_ids)<23:
            fail("document-structure skill needs >=23 adversarial cases",errors)
        for needed in [f"DS{i:02d}" for i in range(17,24)]:
            if needed not in case_ids:
                fail(f"missing consistency case {needed}",errors)
    except Exception as exc:
        fail(f"document-structure evaluation error: {exc}",errors)

    # Application-targeting subsystem
    try:
        ats=json.loads(read("skills/cv-application-targeting/application-target-spec.json"))
        if ats.get("target_unit")!=["company","vacancy","target_role","context"]:
            fail("application target unit drift",errors)
        required_actions={"SELECT","OMIT","REORDER","EMPHASIZE","TERMINOLOGY_ALIGN","CONTEXTUALIZE","SECTION_PRIORITY"}
        if set(ats.get("allowed_tailoring_actions",[]))!=required_actions:
            fail("application tailoring action set drift",errors)
        at_cases=json.loads(read("skills/cv-application-targeting/evaluation/cases.json"))
        if len(at_cases.get("cases",[]))<18:
            fail("application-targeting skill needs >=18 adversarial cases",errors)
        app_schema=json.loads(read("schemas/target-application.schema.json"))
        props=app_schema.get("properties",{})
        for key in ["application_id","targeting_level","company_name","vacancy_title","target_role_id","sources"]:
            if key not in props:
                fail(f"target-application schema missing {key}",errors)
    except Exception as exc:
        fail(f"application-targeting validation error: {exc}",errors)

    # Target-application runtime validator self-test
    try:
        app_good={
            "application_id":"A1",
            "targeting_level":"T2_vacancy",
            "company_name":"Example Co",
            "vacancy_title":"Software Engineer",
            "target_role_id":"R1",
            "work_arrangement":"unknown",
            "sources":[{"source_type":"job_posting","description":"active posting","observed_date":"2026-10-06"}],
            "generated_date":"2026-10-06"
        }
        if validate_models.validate_application(app_good):
            fail("valid T2 target application rejected",errors)

        app_bad_skillless_context={
            "application_id":"A2",
            "targeting_level":"T3_vacancy_company_context",
            "company_name":"Example Co",
            "vacancy_title":"Software Engineer",
            "target_role_id":"R1",
            "work_arrangement":"unknown",
            "sources":[{"source_type":"job_posting","description":"posting","observed_date":"2026-10-06"}],
            "company_context":{},
            "generated_date":"2026-10-06"
        }
        if not validate_models.validate_application(app_bad_skillless_context):
            fail("T3 without material company context incorrectly accepted",errors)

        app_bad_date={
            "application_id":"A3",
            "targeting_level":"T2_vacancy",
            "company_name":"Example Co",
            "vacancy_title":"Software Engineer",
            "target_role_id":"R1",
            "work_arrangement":"unknown",
            "sources":[{"source_type":"job_posting","description":"posting","observed_date":"2026-99-99"}],
            "generated_date":"2026-10-06"
        }
        if not validate_models.validate_application(app_bad_date):
            fail("invalid target-application source date incorrectly accepted",errors)
    except Exception as exc:
        fail(f"target-application runtime validation error: {exc}",errors)

    # Candidate date schema + runtime self-test
    try:
        schema=json.loads(read("schemas/candidate-evidence.schema.json"))
        props=schema["properties"]["evidence_items"]["items"]["properties"]
        for key in ["start_date","end_date","is_current","date_source_text"]:
            if key not in props:
                fail(f"candidate schema missing {key}",errors)

        base={
            "id":"E1","episode_type":"employment","fact":"test",
            "provenance":[{"source_type":"user_report","description":"test"}],
            "ownership":"primary","confidence":"high",
            "allowed_claim_strength":"direct"
        }
        good={"candidate_id":"C1","evidence_items":[{**base,"start_date":"2024-02","end_date":None,"is_current":True}]}
        if validate_models.validate_candidate(good):
            fail("valid normalized ongoing date rejected by runtime validator",errors)

        bad_present={"candidate_id":"C1","evidence_items":[{**base,"start_date":"2024-02","end_date":"Present","is_current":False}]}
        if not validate_models.validate_candidate(bad_present):
            fail("display token Present incorrectly accepted as normalized end_date",errors)

        bad_month={"candidate_id":"C1","evidence_items":[{**base,"start_date":"2024-99","end_date":None,"is_current":True}]}
        if not validate_models.validate_candidate(bad_month):
            fail("invalid month incorrectly accepted",errors)

        bad_day={"candidate_id":"C1","evidence_items":[{**base,"start_date":"2024-02-31","end_date":None,"is_current":True}]}
        if not validate_models.validate_candidate(bad_day):
            fail("invalid calendar day incorrectly accepted",errors)
    except Exception as exc:
        fail(f"candidate date validation self-test error: {exc}",errors)

    if errors:
        for e in errors:
            print("ERROR:",e)
        return 1

    print("PASS: static repository and consistency audit")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
