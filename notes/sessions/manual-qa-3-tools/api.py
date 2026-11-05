import json, os, sys, urllib.request, time
ENV = os.path.expanduser('~/geomind-spe-hackathon-2026/backend/.env')
env = {}
for l in open(ENV):
    if '=' in l and not l.startswith('#'):
        k, v = l.strip().split('=', 1); env[k] = v.strip('"\'')
BASE = 'https://api.geomind.team/api/v1'
UA = {'User-Agent': 'geomind-qa/1.0', 'Content-Type': 'application/json'}
_tok = None
def req(path, data=None):
    global _tok
    h = dict(UA)
    if _tok: h['Authorization'] = 'Bearer ' + _tok
    r = urllib.request.Request(BASE + path, data=json.dumps(data).encode() if data is not None else None, headers=h)
    with urllib.request.urlopen(r, timeout=120) as f:
        b = f.read()
        return json.loads(b) if b else None
def login():
    global _tok
    r = req('/identity/authn/login', {'email': env['FIRST_ADMIN_EMAIL'], 'password': env['FIRST_ADMIN_PASSWORD']})
    _tok = r.get('access_token') or r.get('token') or r
    return _tok
