import json,gzip,glob,collections,re,sys
since,tool,n=sys.argv[1],sys.argv[2],int(sys.argv[3])
C=collections.Counter()
for f in glob.glob('logs/*.json.gz'):
    L=json.load(gzip.open(f))
    if L['run']['started']<since: continue
    for s in L['steps']:
        for t in s.get('tool_calls',[]):
            if t['tool']!=tool or not t.get('error'): continue
            o=t.get('output'); o=o if isinstance(o,str) else json.dumps(o)
            try: m=json.loads(o)['error']; m=m['code']+': '+m['message']
            except Exception: m=o
            m=re.sub(r"\b[0-9a-f]{8,}\b|\d+(\.\d+)?","#",m)
            m=re.sub(r"\b(d#|[a-z_]+_(?:pump|chiller|boiler|exchanger|consumer|grid|pipe))\b","X",m)
            C[m[:int(sys.argv[4]) if len(sys.argv)>4 else 160]]+=1
for m,v in C.most_common(n): print(f'{v:4} {m}')
