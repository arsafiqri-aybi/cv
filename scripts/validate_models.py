#!/usr/bin/env python3
"""Lightweight structural validator for CV project JSON instances.

This validator intentionally uses only the Python standard library.
It performs project-specific checks; it is not a full JSON Schema engine.
"""
import json
import sys
from pathlib import Path

ALLOWED_OWNERSHIP = {"sole","primary","shared","supporting","unknown"}
ALLOWED_CONFIDENCE = {"high","medium","low"}
ALLOWED_CLAIM = {"direct","bounded","descriptive_only","do_not_use"}
ALLOWED_IMPORTANCE = {"critical","high","medium","low","unknown"}

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def validate_candidate(data):
    errors=[]
    if not isinstance(data.get("candidate_id"), str) or not data["candidate_id"]:
        errors.append("candidate_id must be a non-empty string")
    items=data.get("evidence_items")
    if not isinstance(items, list):
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

def main():
    if len(sys.argv)!=3 or sys.argv[1] not in {"candidate","role"}:
        print("usage: validate_models.py candidate|role FILE.json", file=sys.stderr)
        return 2
    data=load(sys.argv[2])
    errors=validate_candidate(data) if sys.argv[1]=="candidate" else validate_role(data)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print("PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
