"""QA-AI-analysis-I driver for api.geomind.team (no secrets printed)."""
import sys, json, time
from pathlib import Path
sys.path.insert(0, "/home/fatemec/geomind-spe-hackathon-2026/backend")
from scripts.seed_qa_projects import Api, credentials, upload_documents, set_case
ROOT = Path("/home/fatemec/geomind-spe-hackathon-2026")
SAMPLE = ROOT / "gemini/examples/hackathon_2026"
STATE = Path(__file__).with_name("state.json")
def api():
    e, p = credentials(ROOT / "backend/.env")
    return Api("https://api.geomind.team/api/v1", e, p)
def st(): return json.loads(STATE.read_text()) if STATE.exists() else {}
def save(s): STATE.write_text(json.dumps(s, indent=1))
cmd = sys.argv[1]; a = api(); s = st()
if cmd == "setup":  # setup <n> <plant>
    n, plant = sys.argv[2], sys.argv[3]
    name = f"QA-TEST QA-AI-analysis-I {n}"
    pid = a.call("POST", "/workspace/projects", json={"name": name})["id"]
    upload_documents(a, pid, SAMPLE)
    if len(sys.argv) > 4 and sys.argv[4] == "noecon":
        content = json.loads((SAMPLE / "case.json").read_text()); content.pop("economics")
        a.call("POST", "/design/case", json={"project": pid, "base": None, "note": "Reference case without economics (QA-AI-analysis-I)", "content": content})
        with open(SAMPLE / "data/demand.csv", "rb") as h:
            a.call("POST", "/design/case/files", data={"project": pid, "base": "1", "name": "data/demand.csv"}, files={"file": ("demand.csv", h)})
        cv = 2
    else:
        cv = set_case(a, pid, SAMPLE)
    spec = json.loads((SAMPLE / "plants" / f"{plant}.json").read_text())
    a.call("POST", "/plant/flowsheet", json={"project": pid, "base": None, "note": f"{plant} (QA-AI-analysis-I seed)", "spec": spec})
    chat = a.call("POST", "/assistant/chat", json={"project": pid, "title": f"analysis {n}"})["id"]
    s[n] = {"project": pid, "chat": chat, "case_version": cv, "runs": []}; save(s); print(json.dumps(s[n]))
elif cmd == "chat":  # chat <n> <title>  (new chat in project)
    n = sys.argv[2]
    s[n]["chat"] = a.call("POST", "/assistant/chat", json={"project": s[n]["project"], "title": sys.argv[3]})["id"]; save(s); print(s[n]["chat"])
elif cmd == "send":  # send <n> <text>
    n = sys.argv[2]
    r = a.call("POST", f"/assistant/chat/{s[n]['chat']}/messages", json={"content": sys.argv[3]})
    s[n]["runs"].append(r["run"]["id"]); save(s); print(r["run"]["id"], r["run"]["status"])
elif cmd == "status":  # status <run>
    r = a.call("GET", f"/assistant/runs/{sys.argv[2]}")
    print(json.dumps({k: r[k] for k in ("status", "started", "ended", "usage", "request", "error")}, indent=1))
elif cmd == "answer":  # answer <run> <request> approve|deny|text:...
    v = sys.argv[4]
    ans = {"approved": True} if v == "approve" else {"approved": False, "reason": v[5:]} if v.startswith("deny:") else {"text": v[5:]}
    r = a.call("POST", f"/assistant/runs/{sys.argv[2]}/answer", json={"request": sys.argv[3], "answer": ans}); print(r["status"])
elif cmd == "get":  # get <path> [out]
    r = a.call("GET", sys.argv[2])
    if len(sys.argv) > 3: Path(sys.argv[3]).write_text(json.dumps(r, indent=1)); print("saved")
    else: print(json.dumps(r, indent=1)[:20000])
elif cmd == "post":
    print(json.dumps(a.call("POST", sys.argv[2], json=json.loads(sys.argv[3])), indent=1)[:5000])
elif cmd == "export":  # export <run> <out>
    resp = a.http.get(f"/assistant/runs/{sys.argv[2]}/log/export", params={"format": "json"})
    Path(sys.argv[3]).write_bytes(resp.content); print(resp.status_code, len(resp.content))
