"""trace.py <log.json> [width]: one line per step and tool call."""
import json, sys
r = json.load(open(sys.argv[1])); W = int(sys.argv[2]) if len(sys.argv) > 2 else 300
print(json.dumps(r["run"])[:600])
for s in r["steps"]:
    lc = s["llm_calls"]
    tin = sum(c.get("input_tokens") or 0 for c in lc); dur = sum(c.get("duration") or 0 for c in lc)
    ans = " | ".join((c.get("answer") or "")[:W] for c in lc if c.get("answer"))
    print(f"#{s['index']} {s['ts'][11:19]} {s['agent']}{'/'+str(s.get('instance')) if s.get('instance') else ''} llm={len(lc)} in={tin} {dur:.1f}s {('ANS: '+ans) if ans else ''}")
    for t in s["tool_calls"]:
        o = json.dumps(t.get("output"))
        err = t.get("error") or ("error" in o[:40])
        print(f"   - {t['tool']}{' ERR' if err else ''} {t.get('duration') and round(t['duration'],2)}s in={json.dumps(t.get('input'))[:W]}\n       out={o[:W]}")
