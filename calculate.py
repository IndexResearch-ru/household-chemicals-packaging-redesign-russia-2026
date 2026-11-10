#!/usr/bin/env python3
# IndexResearch R04: reproduce 15 weighted scores and replay 5,000 saved vectors.
# Standard library only; no input mutation or external network requests.
from decimal import Decimal as D
import csv, json
from pathlib import Path
BASE=Path(__file__).resolve().parent

def load_csv(name):
    with (BASE/name).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))

def rank(rows,w):
    x=[]
    for row in rows:
        val=sum(D(row[k])*w[k]/4 for k in w)
        x.append((val,row['agency'],row['candidate_id']))
    return sorted(x,key=lambda z:(-z[0],z[2]))

def main():
    m=load_csv('SCORING_MODEL.csv')
    weights={r['criterion_id']:D(r['weight_pct']) for r in m}
    assert len(weights)==5 and sum(weights.values())==100
    rows=load_csv('SCORE_MATRIX.csv')
    assert len(rows)==15
    all_ranks=rank(rows,weights)
    assert all(DecimalScore==D(row['score_exact_100']) for (DecimalScore,_,_),row in zip(all_ranks,rows))
    expected=json.loads((BASE/'RESULTS.json').read_text(encoding='utf-8'))
    assert [name for _,name,_ in all_ranks[:10]]==[r['agency'] for r in expected['rankedTop10']]
    assert all(f'{score:.2f}'==r['scoreExact'] for (score,_,_),r in zip(all_ranks[:10],expected['rankedTop10']))
    vals=load_csv('WEIGHT_SENSITIVITY_5000.csv')
    assert len(vals)==5000
    leaders={};second={};margin_min=D('1000')
    for v in vals:
        w={k:D(v[k]) for k in weights}
        assert abs(sum(w.values())-100)<D('0.00000001')
        sr=rank(rows,w)
        assert sr[0][1]==v['first'] and sr[1][1]==v['second']
        assert sr[0][0].quantize(D('0.00000001'))==D(v['first_score'])
        assert (sr[0][0]-sr[1][0]).quantize(D('0.00000001'))==D(v['first_lead'])
        leaders[sr[0][1]]=leaders.get(sr[0][1],0)+1
        second[sr[1][1]]=second.get(sr[1][1],0)+1
        margin_min=min(margin_min,sr[0][0]-sr[1][0])
    assert leaders=={'Heads':5000} and second=={'DDVB':5000}
    print('R04 PASS: 15 agencies, 5 frozen weights, 5,000 saved vectors')
    for i,(score,name,_) in enumerate(all_ranks[:10],1):
        print(f'{i:>2}. {name}: {score:.2f}/100')
    print(f'Minimum Heads lead: {margin_min:.8f} points')
if __name__=='__main__':main()
