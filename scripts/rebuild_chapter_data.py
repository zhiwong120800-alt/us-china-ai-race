#!/usr/bin/env python3
"""Rebuild Charts 3–5 from frozen Epoch source plus documented human review inputs.

Run from repository root:
    python scripts/rebuild_chapter_data.py

Manual developer attribution, organisation grouping, and access classification
were reviewed by the team; these input decisions are in data/review. The build
never infers missing classifications and checks against frozen raw records.
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/epoch_notable_ai_models_20261020.csv"
REVIEW = ROOT / "data/review"
OUT = ROOT / "data/processed"
OUT.mkdir(parents=True, exist_ok=True)

def read(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

def write(filename, rows, fields):
    with (OUT / filename).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="raise", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

def norm(country):
    return "United States" if country == "US" else country

def identity(model, country):
    return model, norm(country)

def main():
    assert RAW.exists(), f"Missing frozen input: {RAW}"
    checksums = (ROOT / "docs/source_checksums.sha256").read_text(encoding="utf-8")
    expected = next(line.split()[0] for line in checksums.splitlines() if line.endswith("data/raw/epoch_notable_ai_models_20261020.csv"))
    assert hashlib.sha256(RAW.read_bytes()).hexdigest() == expected, "Frozen source checksum has changed"

    original = read(RAW)
    assert len(original) == 1078, "Unexpected raw Epoch snapshot length"
    index = {r["Model"]: r for r in original}
    assert len(index) == len(original), "Raw model identifiers are not unique"

    models3 = read(REVIEW / "chart3_model_attribution_review.csv")
    aff3 = read(REVIEW / "chart3_affiliation_review.csv")
    manual3 = read(REVIEW / "chart3_org_mapping_review.csv")
    records4 = read(REVIEW / "chart4_developer_type_review.csv")
    records5 = read(REVIEW / "chart5_release_review.csv")
    assert len(models3) == 679 and len(aff3) == 909
    assert len(records4) == 667 and len(records5) == 667
    assert len(manual3) == 26

    s3 = {identity(r["model"], r["country"]) for r in models3 if r["country"] != "Hong Kong"}
    s4 = {identity(r["Model"], r["country"]) for r in records4}
    s5 = {identity(r["model"], r["country"]) for r in records5}
    assert s3 == s4 == s5 and len(s3) == 667, "Chapter 3–5 denominators disagree"
    assert sum(r["country"] == "United States" for r in models3) == 514
    assert sum(r["country"] == "China" for r in models3) == 153
    assert sum(r["country"] == "Hong Kong" for r in models3) == 12

    for r in records4:
        orig = index[r["Model"]]
        assert r["Organization"] == orig["Organization"], f"Organisation mismatch: {r['Model']}"
        assert r["Publication date"] == orig["Publication date"], f"Date mismatch: {r['Model']}"
        assert ("United States of America" if r["country"] == "US" else "China") in {x.strip() for x in orig["Country (of organization)"].split(",")}, f"Country mismatch: {r['Model']}"
        assert r["category"] in {"Industry","Academia","Collaboration","Other","Unknown"}

    for r in records5:
        orig = index[r["model"]]
        assert r["organisation"] == orig["Organization"] and r["publication_date"] == orig["Publication date"], f"Source mismatch: {r['model']}"
        assert ("United States of America" if r["country"] == "US" else "China") in {x.strip() for x in orig["Country (of organization)"].split(",")}, f"Country mismatch: {r['model']}"
        assert int(r["year"]) == int(orig["Publication date"][:4])
        assert r["developer_type"] == next(a["category"] for a in records4 if a["Model"] == r["model"] and a["country"] == r["country"]), f"Cross-chart developer type mismatch: {r['model']}"

    write("chart3_model_country.csv", models3, ["model","country","year","publication_date","alignment"])
    write("chart3_affiliations.csv", aff3, ["model","country","year","developer","family"])

    names = set()
    source_countries = defaultdict(set)
    for r in original:
        orgs = [x.strip() for x in r["Organization"].split(",") if x.strip()]
        countries = [x.strip() for x in r["Country (of organization)"].split(",")]
        for i, org in enumerate(orgs):
            names.add(org)
            if len(orgs) == len(countries) and countries[i]:
                source_countries[org].add(countries[i])
    reviewed = {r["org"]: r for r in manual3}
    family = {r["developer"]: r["family"] for r in aff3}
    mapping = []
    for org in sorted(names, key=lambda x: x.casefold()):
        explicit = reviewed.get(org)
        observed = source_countries[org]
        mapping.append({
            "org":org,
            "country":explicit["country"] if explicit else (next(iter(observed)) if len(observed)==1 else ""),
            "parent":explicit["parent"] if explicit else family.get(org,org),
            "evidence":explicit["evidence"] if explicit else ("Bundled Chapter 3 affiliation map" if org in family else "Original Epoch label; no audit decision"),
            "rule":explicit["rule"] if explicit else ("grouped-in-original-chapter" if org in family else "original-label"),
            "status":"explicit_review" if explicit else ("derived_from_chapter_3" if org in family else "unreviewed_original_label")
        })
    assert len(mapping)==372, "Source organisation-label audit changed"
    write("chart3_org_map.csv", mapping, ["org","country","parent","evidence","rule","status"])

    # Concentration: top-three organisation family by unique model involvement.
    for country,expected_num,expected_total in [("United States",288,514),("China",65,153)]:
        family_models = defaultdict(set)
        for r in aff3:
            if r["country"] == country and 2016 <= int(r["year"]) <= 2025:
                family_models[r["family"]].add(r["model"])
        top = sorted(family_models, key=lambda n:(-len(family_models[n]),n))[:3]
        involvement=set().union(*(family_models[n] for n in top))
        assert len(involvement)==expected_num
        assert sum(r["country"] == country for r in models3)==expected_total

    write("chart4_model_type_records.csv", records4, ["Model","Organization","Publication date","country","period","category"])
    periods=["2016–19","2020–22","2023–25"]
    categories=["Industry","Academia","Collaboration","Other","Unknown"]
    composition=[]
    for country in ["China","US"]:
        for period in periods:
            group=[r for r in records4 if r["country"] == country and r["period"] == period]
            row={"country":country,"period":period}
            row.update({c:sum(r["category"]==c for r in group) for c in categories})
            row["Total"]=len(group)
            composition.append(row)
    write("chart4_period_summary.csv", composition, ["country","period",*categories,"Total"])

    write("chart5_model_access_records.csv", records5, ["model","organisation","publication_date","year","country","period","developer_type","release_strategy","source_accessibility"])
    release=[]
    for country in ["United States","China"]:
        for year in range(2016,2026):
            group=[r for r in records5 if norm(r["country"])==country and int(r["year"])==year]
            counts=Counter(r["release_strategy"] for r in group)
            for category,n in sorted(counts.items()):
                release.append({"Year":year,"Country":country,"Release_Strategy":category,"count":n,"total":len(group),"percentage":f"{100*n/len(group):.6f}"})
    write("chart5_release_strategies.csv", release, ["Year","Country","Release_Strategy","count","total","percentage"])

    recent=[r for r in records5 if 2023 <= int(r["year"]) <= 2025]
    us=[r for r in recent if r["country"]=="US"]
    cn=[r for r in recent if r["country"]=="China"]
    assert (len(us),len(cn))==(207,89)
    assert sum(r["release_strategy"]=="API / hosted" for r in us)==94
    assert sum(r["release_strategy"]=="Open weights" for r in cn)==57
    print("PASS: 1,078 raw models; 667 matched US/China country-model records; 12 optional Hong Kong")
    print("PASS: Chart 3 top-three 288/514 US and 65/153 China")
    print("PASS: Chart 4 types + Chart 5 released records; US API 94/207, China open-weight 57/89")
    print("PASS: 372 source organisation labels, 26 explicit reviewed mapping rows")
    print("Generated: 7 processed chapter CSV tables")

if __name__=="__main__":
    main()
