import json,gzip,glob,collections,sys
from datetime import datetime
R={x['id'].replace('-',''):x for x in json.load(open('runs.json'))}
G=collections.Counter(); GE=collections.Counter(); GEM=collections.Counter(); AG=collections.Counter()
rows=[]
for f in sorted(glob.glob('logs/*.json.gz')):
    L=json.load(gzip.open(f)); run=L['run']; rid=run['id']; meta=R.get(rid,{})
    tc=[(s['agent'],t) for s in L['steps'] for t in s.get('tool_calls',[])]
    lc=[(s['agent'],c) for s in L['steps'] for c in s.get('llm_calls',[])]
    tools=collections.Counter(t['tool'] for a,t in tc)
    errs=[(a,t) for a,t in tc if t.get('error')]
    seen=collections.Counter(json.dumps([t['tool'],t.get('input')],sort_keys=True) for a,t in tc)
    dup=sum(v-1 for v in seen.values() if v>1)
    agents=collections.Counter(s['agent'] for s in L['steps'])
    for a,t in tc:
        G[t['tool']]+=1
        if t.get('error'):
            GE[t['tool']]+=1
            m=json.dumps(t['error'])[:110]; GEM[(t['tool'],m)]+=1
    for a,c in agents.items(): AG[a]+=c
    llmt=sum(float(c.get('duration') or 0) for a,c in lc); toolt=sum(float(t.get('duration') or 0) for a,t in tc)
    rows.append((run['started'][11:16],rid[:8],run['status'][:4],(meta.get('_project') or '')[:22],len(L['steps']),len(tc),len(errs),dup,
      tools.get('simulate',0),tools.get('check',0)+tools.get('check_plant',0),tools.get('optimize',0),tools.get('patch_plant',0),round(llmt/60,1),round(toolt/60,1),dict(agents)))
print('start id stat project steps tools errs dups sim chk opt patch llm_min tool_min')
for r in sorted(rows): print(*r[:-1]); print('     agents:',r[-1])
print('\nTOOLS calls/errors:')
for k,v in G.most_common(): print(f'  {k:28} {v:5} err {GE[k]:4} ({100*GE[k]/v:.0f}%)')
print('\nTOP ERRORS:')
for (k,m),v in GEM.most_common(45): print(f'  {v:4} {k}: {m}')
