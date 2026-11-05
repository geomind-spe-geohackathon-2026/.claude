import sys, json, os, httpx
sys.path.insert(0, "/home/fatemec/geomind-spe-hackathon-2026/backend")
from pathlib import Path
from scripts.seed_qa_projects import credentials
BASE="https://api.geomind.team/api/v1"; TOK="/tmp/claude-1000/qa-study/.tok"
def login():
    e, p = credentials(Path("/home/fatemec/geomind-spe-hackathon-2026/backend/.env"))
    t = httpx.post(BASE+"/identity/authn/login", json={"email": e, "password": p}, timeout=60).json()["access_token"]
    fd=os.open(TOK, os.O_WRONLY|os.O_CREAT|os.O_TRUNC, 0o600); os.write(fd,t.encode()); os.close(fd); return t
t = open(TOK).read() if os.path.exists(TOK) else login()
m, path = sys.argv[1], sys.argv[2]
kw = {"params": json.loads(sys.argv[3])} if len(sys.argv) > 3 else {}
r = httpx.request(m, BASE+path, headers={"Authorization": "Bearer "+t}, timeout=120, **kw)
if r.status_code == 401:
    t = login(); r = httpx.request(m, BASE+path, headers={"Authorization": "Bearer "+t}, timeout=120, **kw)
if r.status_code >= 400: sys.exit(f"{m} {path}: {r.status_code} {r.text[:300]}")
print(json.dumps(r.json(), indent=1))
