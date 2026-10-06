#!/usr/bin/env python3
"""Lightweight structural validators for CV project JSON instances."""
import calendar
import json
import re
import sys
from pathlib import Path

ALLOWED_OWNERSHIP={"sole","primary","shared","supporting","unknown"}
ALLOWED_CONFIDENCE={"high","medium","low"}
ALLOWED_CLAIM={"direct","bounded","descriptive_only","do_not_use"}
ALLOWED_IMPORTANCE={"critical","high","medium","low","unknown"}
ALLOWED_TARGETING={"T0_general","T1_role_family","T2_vacancy","T3_vacancy_company_context"}
ALLOWED_WORK_ARRANGEMENT={"onsite","hybrid","remote","unknown"}
DATE_RE=re.compile(r"^(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?$")

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def valid_date(value):
    if value is None:
        return True
    if not isinstance(value,str):
        return False
    m=DATE_RE.fullmatch(value)
    if not m:
        return False
    year=int(m.group(1))
    month=int(m.group(2)) if m.group(2) else None
    day=int(m.group(3)) if m.group(3) else None
    if year < 1:
        return False
    if month is not None and not 1 <= month <= 12:
        return False
    if day is not None:
        if month is None:
            return False
        if not 1 <= day <= calendar.monthrange(year,month)[1]:
            return False
    return True

def validate_candidate(data):
    errors=[]
    if not isinstance(data.get("candidate_id"),str) or not data["candidate_id"]:
        errors.append("candidate_id must be a non-empty string")
    items=data.get("evidence_items")
    if not isinstance(items,list):
        errors.append("evidence_items must be a list")
        return errors
    ids=set()
    for i,item in enumerate(items):
        p=f"evidence_items[{i}]"
        eid=item.get("id")
        if not eid:
            errors.append(f"{p}.id missing")
        elif eid in ids:
            errors.append(f"{p}.id duplicate: {eid}")
        else:
            ids.add(eid)
        if not item.get("fact"):
            errors.append(f"{p}.fact missing")
        if not item.get("provenance"):
            errors.append(f"{p}.provenance must contain at least one source")
        if item.get("ownership") not in ALLOWED_OWNERSHIP:
            errors.append(f"{p}.ownership invalid")
        if item.get("confidence") not in ALLOWED_CONFIDENCE:
            errors.append(f"{p}.confidence invalid")
        if item.get("allowed_claim_strength") not in ALLOWED_CLAIM:
            errors.append(f"{p}.allowed_claim_strength invalid")
        for field in ("start_date","end_date"):
            if not valid_date(item.get(field)):
                errors.append(f"{p}.{field} must be a real YYYY, YYYY-MM, YYYY-MM-DD date, or null")
        if item.get("is_current") is True and item.get("end_date") is not None:
            errors.append(f"{p}.end_date must be null when is_current=true")
    return errors

def validate_role(data):
    errors=[]
    if not data.get("role_id"):
        errors.append("role_id missing")
    if not data.get("title"):
        errors.append("title missing")
    reqs=data.get("requirements")
    if not isinstance(reqs,list):
        errors.append("requirements must be a list")
        return errors
    ids=set()
    for i,r in enumerate(reqs):
        p=f"requirements[{i}]"
        rid=r.get("id")
        if not rid:
            errors.append(f"{p}.id missing")
        elif rid in ids:
            errors.append(f"{p}.id duplicate: {rid}")
        else:
            ids.add(rid)
        if not r.get("statement"):
            errors.append(f"{p}.statement missing")
        if r.get("importance") not in ALLOWED_IMPORTANCE:
            errors.append(f"{p}.importance invalid")
        if not r.get("evidence_basis"):
            errors.append(f"{p}.evidence_basis must not be empty")
    return errors

def validate_application(data):
    errors=[]
    if not isinstance(data.get("application_id"),str) or not data["application_id"]:
        errors.append("application_id must be a non-empty string")
    level=data.get("targeting_level")
    if level not in ALLOWED_TARGETING:
        errors.append("targeting_level invalid")
    if not isinstance(data.get("target_role_id"),str) or not data["target_role_id"]:
        errors.append("target_role_id must be a non-empty string")

    # Concrete application levels require concrete vacancy/company identity.
    if level in {"T2_vacancy","T3_vacancy_company_context"}:
        if not data.get("company_name"):
            errors.append("company_name required for T2/T3")
        if not data.get("vacancy_title"):
            errors.append("vacancy_title required for T2/T3")

    # T3 must contain material company context rather than only a label.
    if level=="T3_vacancy_company_context":
        ctx=data.get("company_context") or {}
        material=sum(len(ctx.get(k,[]) or []) for k in (
            "industry_domain","products_services","customer_types",
            "technology_context","regulatory_context","material_notes"
        ))
        if material == 0:
            errors.append("T3 requires material company_context")

    sources=data.get("sources")
    if not isinstance(sources,list) or not sources:
        errors.append("sources must contain at least one source")
    else:
        for i,source in enumerate(sources):
            p=f"sources[{i}]"
            if not source.get("source_type"):
                errors.append(f"{p}.source_type missing")
            if not source.get("description"):
                errors.append(f"{p}.description missing")
            if not valid_date(source.get("observed_date")):
                errors.append(f"{p}.observed_date invalid")

    if data.get("work_arrangement") not in ALLOWED_WORK_ARRANGEMENT:
        errors.append("work_arrangement invalid")

    generated=data.get("generated_date")
    if generated is not None:
        if not valid_date(generated) or len(generated)!=10:
            errors.append("generated_date must be a real YYYY-MM-DD date")

    return errors

def main():
    if len(sys.argv)!=3 or sys.argv[1] not in {"candidate","role","application"}:
        print("usage: validate_models.py candidate|role|application FILE.json",file=sys.stderr)
        return 2
    data=load(sys.argv[2])
    mode=sys.argv[1]
    if mode=="candidate":
        errors=validate_candidate(data)
    elif mode=="role":
        errors=validate_role(data)
    else:
        errors=validate_application(data)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print("PASS")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
