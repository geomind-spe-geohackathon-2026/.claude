"""trace.py <run> [width]: compact trace of every step, LLM call and tool call."""
import json, sys
from datetime import datetime
run=sys.argv[1]; W=int(sys.argv[2]) if len(sys.argv)>2 else 300
L=json.load(open(f'runs/{run}.log.json'))
def sh(x,w=W):
    s=x if isinstance(x,str) else json.dumps(x); s=s.replace('\n',' ')
    return s if len(s)<=w else s[:w]+f'...[{len(s)}]'
tot={}
for s in L['steps']:
    a=s['agent']; ts=s.get('ts','')[11:19]
    for c in s['llm_calls']:
        t=tot.setdefault(a,[0,0,0,0.0,0.0]); t[0]+=1; t[1]+=c.get('input_tokens',0); t[2]+=c.get('output_tokens',0); t[3]+=c.get('cost',0); t[4]+=c.get('duration',0) or 0
        print(f"{ts} [{a}#{s['index']} p={s.get('parent')}] LLM {c.get('duration',0):.1f}s in={c.get('input_tokens')} out={c.get('output_tokens')} :: {sh(c.get('answer',''))}")
    for tc in s.get('tool_calls',[]):
        print(f"      TOOL {tc.get('name') or tc.get('tool')} {tc.get('duration','')} in={sh(tc.get('input'),200)} out={sh(tc.get('output'),W)}")
print('--- per agent: calls in out cost llm_s')
for a,t in tot.items(): print(f'{a:24} {t[0]:4} {t[1]:8} {t[2]:7} {t[3]:.4f} {t[4]:.0f}')
