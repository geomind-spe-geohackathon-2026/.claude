import sys, json
sys.path.insert(0, "/home/fatemec/geomind-spe-hackathon-2026/backend")
from pathlib import Path
from scripts.seed_qa_projects import Api, credentials, upload_documents, set_case, store_plants
S = Path("/home/fatemec/geomind-spe-hackathon-2026/gemini/examples/hackathon_2026")
e, p = credentials(Path("/home/fatemec/geomind-spe-hackathon-2026/backend/.env"))
api = Api("https://api.geomind.team/api/v1", e, p)
name = sys.argv[1]
pid = api.call("POST", "/workspace/projects", json={"name": name})["id"]
upload_documents(api, pid, S)
cv = set_case(api, pid, S)
pv = store_plants(api, pid, S)
print(json.dumps({"project": pid, "case_version": cv, "plants": pv}))
