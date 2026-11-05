import json, os, urllib.request, urllib.error
ENV = os.path.expanduser('~/geomind-spe-hackathon-2026/backend/.env')
env = {}
for l in open(ENV):
    if '=' in l and not l.startswith('#'):
        k, v = l.strip().split('=', 1); env[k] = v.strip('"\'')
BASE = 'https://api.geomind.team/api/v1'
_tok = None
import time as _t
def req(path, data=None, method=None, raw=False, _try=0):
    try:
        return _req(path, data, method, raw)
    except (RuntimeError, OSError) as e:
        if str(e)[:3] in ('500','502','503','504') and _try < 40:
            _t.sleep(15); return req(path, data, method, raw, _try+1)
        raise
def _req(path, data=None, method=None, raw=False):
    h = {'User-Agent': 'geomind-qa/1.0', 'Content-Type': 'application/json'}
    if _tok: h['Authorization'] = 'Bearer ' + _tok
    r = urllib.request.Request(BASE + path, data=json.dumps(data).encode() if data is not None else None, headers=h, method=method)
    try:
        with urllib.request.urlopen(r, timeout=300) as f:
            b = f.read()
            return b if raw else (json.loads(b) if b else None)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'{e.code} {path}: {e.read()[:2000]}')
def login():
    global _tok
    r = req('/identity/authn/login', {'email': env['FIRST_ADMIN_EMAIL'], 'password': env['FIRST_ADMIN_PASSWORD']})
    _tok = r['access_token']
login()
