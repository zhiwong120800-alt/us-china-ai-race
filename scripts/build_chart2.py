#!/usr/bin/env python3
"""Rebuild all reported-compute Chart 2 model records from frozen Epoch CSV."""
import csv
from pathlib import Path
from collections import defaultdict
import math
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"data/raw/epoch_notable_ai_models_20261020.csv"
OUT=ROOT/"data/processed"
OUT.mkdir(parents=True,exist_ok=True)
def read(path):
    with path.open(encoding="utf-8-sig",newline="") as fh:return list(csv.DictReader(fh))
def write(name,rows,fields):
    with (OUT/name).open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=fields,lineterminator="\n")
        w.writeheader();w.writerows(rows)
def main():
    model_rows=[];coverage=[]
    for r in read(RAW):
        date=r.get("Publication date","").strip()
        if not ("2016-01-01" <= date <= "2026-09-30"):continue
        raw_flop=r.get("Training compute (FLOP)","").strip()
        try:f=float(raw_flop)
        except (ValueError,TypeError):f=float("nan")
        known=math.isfinite(f) and f>0
        nations=set(x.strip() for x in r.get("Country (of organization)","").split(","))
        for country,source_label in [("United States","United States of America"),("China","China")]:
            if source_label not in nations:continue
            year=int(date[:4])
            coverage.append((country,year,known))
            if known:
                model_rows.append(dict(model=r["Model"],country=country,publication_date=date,
                    year=year,training_compute_flop=raw_flop,compute_available=1,
                    frontier_flag=int(r.get("Frontier model","").strip().lower() in ("true","1"))))
    assert len(model_rows)==375 and len(coverage)==745, "Unexpected Chart 2 source coverage"
    write("chart2_compute_models.csv",model_rows,["model","country","publication_date","year","training_compute_flop","compute_available","frontier_flag"])
    cover=[]
    for country in ["United States","China"]:
        for year in range(2016,2027):
            rr=[x for x in coverage if x[0]==country and x[1]==year]
            n=sum(x[2] for x in rr)
            cover.append(dict(country=country,year=year,all_notable=len(rr),
                with_compute=n,coverage_pct=f"{100*n/len(rr):.1f}"))
    write("chart2_compute_coverage.csv",cover,["country","year","all_notable","with_compute","coverage_pct"])
    us=[r for r in model_rows if r["country"]=="United States"]
    cn=[r for r in model_rows if r["country"]=="China"]
    assert len(us)==277 and len(cn)==98
    assert max(float(r["training_compute_flop"]) for r in us)==9.4e26
    assert max(float(r["training_compute_flop"]) for r in cn)==2.505e25
    print("PASS Chart 2: 745 model-country assignments, 375 with FLOP (US 277, China 98)")
if __name__=="__main__":main()
