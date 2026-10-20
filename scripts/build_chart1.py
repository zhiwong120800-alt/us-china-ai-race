"""Rebuild OWID US/China and Chart 1 comparison tables from frozen source CSVs.
Run from repository root: python scripts/build_chart1.py
Python standard library only. Source files remain unmodified.
"""
from pathlib import Path
import csv
from collections import defaultdict

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data'/'raw'
OUT=ROOT/'data'/'processed'
OUT.mkdir(parents=True,exist_ok=True)
OWID=RAW/'annual-scholarly-publications-on-artificial-intelligence.csv'
EPOCH=RAW/'epoch_notable_ai_models_20261020.csv'
METRIC='AI scholarly publications - Field: All'

def load(path):
    with path.open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))

def save(path,fields,rows):
    with path.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=fields)
        wr.writeheader()
        wr.writerows(rows)

def main():
    owid=load(OWID)
    epoch=load(EPOCH)
    papers={}
    codes={'United States':'USA','China':'CHN'}
    for r in owid:
        if r['Entity'] in codes and 2016<=int(r['Year'])<=2024:
            key=(int(r['Year']),r['Entity'])
            assert key not in papers, f'Duplicate OWID year-country {key}'
            papers[key]=int(r[METRIC])
    assert len(papers)==18,'Expected 9 years each for two countries'
    normalized=[{'year':y,'country':c,'country_code':codes[c],'ai_publications':papers[(y,c)]}
                for y in range(2016,2025) for c in ['United States','China']]
    save(OUT/'owid_us_china_2016_2024.csv',list(normalized[0]),normalized)

    models=defaultdict(set)
    for r in epoch:
        d=r['Publication date'].strip()
        if not d:continue
        year=int(d[:4])
        if not 2016<=year<=2024:continue
        model=r['Model'].strip()
        assert model, 'Blank model identifier in selected range'
        nations=set(t.strip() for t in r['Country (of organization)'].split(',') if t.strip())
        if 'United States of America' in nations:models[(year,'United States')].add(model)
        if 'China' in nations:models[(year,'China')].add(model)

    merged=[]
    for y in range(2016,2025):
        papers_sum=sum(papers[(y,c)] for c in codes)
        model_sum=sum(len(models[(y,c)]) for c in codes)
        for c in ['United States','China']:
            pc=papers[(y,c)]
            mc=len(models[(y,c)])
            merged.append({'year':y,'country':c,'country_code':codes[c],
                           'ai_publications':pc,'epoch_notable_models':mc,
                           'share_of_two_country_publications_pct':round(100*pc/papers_sum,4),
                           'share_of_two_country_models_pct':round(100*mc/model_sum,4) if model_sum else ''})
    save(OUT/'chart1_papers_vs_models_2016_2024.csv',list(merged[0]),merged)
    for y in range(2016,2025):
        assert sum(r['epoch_notable_models'] for r in merged if r['year']==y)>=0
    print('Wrote',len(normalized),'OWID and',len(merged),'comparison rows')
    for r in merged:
        if r['year'] in [2016,2024]:print(r)

if __name__=='__main__':main()
