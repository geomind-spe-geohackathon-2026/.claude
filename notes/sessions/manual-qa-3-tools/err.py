import json,gzip,glob,collections,re,sys
since=sys.argv[1] if len(sys.argv)>1 else ''
C=collections.Counter(); EX={}
for f in glob.glob('logs/*.json.gz'):
    L=json.load(gzip.open(f))
    if L['run']['started']<since: continue
    for s in L['steps']:
        for t in s.get('tool_calls',[]):
            if not t.get('error'): continue
            o=t.get('output'); o=o if isinstance(o,str) else json.dumps(o)
            m=re.sub(r"[0-9a-f]{8,}|\d+(\.\d+)?","#",o)[:150]
            k=(t['tool'],m); C[k]+=1; EX.setdefault(k,(L['run']['id'][:8],o[:400]))
for (tool,m),v in C.most_common(int(sys.argv[2]) if len(sys.argv)>2 else 60):
    print(f'{v:4} {tool}: {m}')
