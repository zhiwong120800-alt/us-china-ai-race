#!/usr/bin/env python3
"""Reproducible, conservative audit for ECI/Notable AI Models, 2026-10-20 frozen snapshots.
Run from project root: python scripts/build_eci_audit.py
Python standard library only. Exact-model-name matching only; fuzzy hints never modify results.
"""
import csv,collections,difflib,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data/raw';OUT=ROOT/'data/processed';OUT.mkdir(parents=True,exist_ok=True)

def read(path):
 with open(path,encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(name,rows,fields):
 with open(OUT/name,'w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
def countries(row):
 s=row.get('Country (of organization)','')
 return [c for c,k in [('US','United States of America'),('China','China')] if k in set(x.strip() for x in s.split(','))]
def year(row,col):return row[col][:4]
def one_or_empty(v):return str(v).strip() not in ('','NA','N/A','nan','None')

E=read(RAW/'epoch_eci_model_scores_20261020.csv')
N=read(RAW/'epoch_notable_ai_models_20261020.csv')
assert len({r['Model'] for r in E})==len(E), 'Duplicate ECI model names'
assert len({r['Model'] for r in N})==len(N), 'Duplicate Notable model names'
NIDX={r['Model']:r for r in N}
joined=[];scatter=[];unmatched=[];date_discrep=[]
for e in E:
 n=NIDX.get(e['Model']); ec=countries(e)
 row={'Model':e['Model'],'Display name':e['Display name'],'eci_date':e['date'],'eci_year':year(e,'date'),'eci':e['eci'],'eci_ci_low':e['eci_ci_low'],'eci_ci_high':e['eci_ci_high'],'eci_country':e['Country (of organization)'],'eci_organization':e['Organization'],'eci_accessibility':e['Model accessibility'],'exact_name_match':int(n is not None),'notable_date':n['Publication date'] if n else '', 'notable_country':n['Country (of organization)'] if n else '', 'notable_domain':n['Domain'] if n else '', 'notable_training_compute_flop':n['Training compute (FLOP)'] if n else '', 'compute_available':int(n is not None and one_or_empty(n['Training compute (FLOP)'])),'notable_org':n['Organization'] if n else '', 'eci_country_tags':','.join(ec),'notable_country_tags':','.join(countries(n)) if n else ''}
 joined.append(row)
 if n:
  assert set(ec)==set(countries(n)),f'Country mismatch: {e["Model"]}'
  if e['date']!=n['Publication date']:
   date_discrep.append({'Model':e['Model'],'eci_date':e['date'],'notable_publication_date':n['Publication date'],'eci_year':year(e,'date'),'notable_year':year(n,'Publication date'),'year_differs':int(year(e,'date')!=year(n,'Publication date'))})
  if row['compute_available']:
   for c in ec:
    scatter.append({'Model':e['Model'],'country':c,'eci_release_date':e['date'],'eci_year':year(e,'date'),'eci':e['eci'],'eci_ci_low':e['eci_ci_low'],'eci_ci_high':e['eci_ci_high'],'training_compute_flop':n['Training compute (FLOP)'],'notable_publication_date':n['Publication date'],'notable_domain':n['Domain']})
 else:
  unmatched.append(e)
fields=list(joined[0].keys())
write('chart6_eci_notable_exact_join.csv',joined,fields)
write('chart6_compute_scatter_us_china_exact.csv',scatter,['Model','country','eci_release_date','eci_year','eci','eci_ci_low','eci_ci_high','training_compute_flop','notable_publication_date','notable_domain'])
write('chart6_eci_date_discrepancies.csv',date_discrep,['Model','eci_date','notable_publication_date','eci_year','notable_year','year_differs'])

# Review hints are not used as joins. Suggestions have no demonstrated equivalence.
namepool=[r['Model'] for r in N]
review=[]
for e in unmatched:
 # Only present a likely candidate when similarity is high; never automatically join.
 near=difflib.get_close_matches(e['Model'],namepool,n=2,cutoff=0.78)
 review.append({'ECI_Model':e['Model'],'ECI_date':e['date'],'ECI_country':e['Country (of organization)'],'suggested_notable_name_1':near[0] if near else '', 'suggested_notable_name_2':near[1] if len(near)>1 else '', 'review_status':'unreviewed','notes':'Suggestions only; no automatic linking'})
write('chart6_eci_unmatched_review.csv',review,['ECI_Model','ECI_date','ECI_country','suggested_notable_name_1','suggested_notable_name_2','review_status','notes'])

# Audit all ECI names by country; note it is not a census of notable-model records.
audit=[]
for c in ['US','China']:
 for y in sorted(set(r['date'][:4] for r in E)):
  es=[r for r in E if c in countries(r) and year(r,'date')==y]
  matched=[r for r in es if r['Model'] in NIDX]
  withcompute=[r for r in matched if one_or_empty(NIDX[r['Model']]['Training compute (FLOP)'])]
  ns=[r for r in N if c in countries(r) and year(r,'Publication date')==y]
  audit.append({'country':c,'eci_year':y,'eci_models':len(es),'exact_matched_eci_models':len(matched),'match_pct_of_eci':round(100*len(matched)/len(es),2) if es else '', 'matched_with_training_compute':len(withcompute),'compute_pct_of_matched':round(100*len(withcompute)/len(matched),2) if matched else '', 'notable_models_same_calendar_year':len(ns),'matched_div_notable_same_year_pct_DESCRIPTIVE_ONLY':round(100*len(matched)/len(ns),2) if ns else '', 'date_mismatch_with_notable':sum(r['date']!=NIDX[r['Model']]['Publication date'] for r in matched)})
write('chart6_eci_country_year_coverage.csv',audit,list(audit[0].keys()))

# Full ECI country-series input for trend; no joining required.
series=[]
for e in E:
 for c in countries(e):
  series.append({'Model':e['Model'],'country':c,'release_date':e['date'],'year':e['date'][:4],'eci':e['eci'],'eci_ci_low':e['eci_ci_low'],'eci_ci_high':e['eci_ci_high'],'accessibility':e['Model accessibility']})
write('chart6_eci_us_china_full_country_scores.csv',series,list(series[0].keys()))

assert len(joined)==len(E)
assert sum(r['exact_name_match'] for r in joined)+len(unmatched)==len(E)
assert len(scatter)==sum(r['compute_available'] for r in joined if r['eci_country_tags'])
assert len(series)==sum(bool(countries(r)) for r in E) # ECI country is singular here
for c in ['US','China']:
 a=[x for x in audit if x['country']==c]
 assert sum(x['eci_models'] for x in a)==sum(c in countries(e) for e in E)
print('ECI total',len(E),'notable total',len(N),'exact matched',sum(r['exact_name_match'] for r in joined),'unmatched',len(unmatched))
for c in ['US','China']:
 group=[r for r in E if c in countries(r)]; matched=[r for r in group if r['Model'] in NIDX]; comp=[r for r in matched if one_or_empty(NIDX[r['Model']]['Training compute (FLOP)'])]
 print(c,'ECI',len(group),'exact matched',len(matched),'with compute',len(comp))
print('date discrepancies',len(date_discrep),'across calendar year',sum(x['year_differs'] for x in date_discrep))
