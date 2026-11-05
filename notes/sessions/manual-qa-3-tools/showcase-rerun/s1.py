import sys, json, uuid, urllib.request, time
sys.path.insert(0, '/home/fatemec/geomind-spe-hackathon-2026/.claude/notes/sessions/manual-qa-3-tools')
import api
SRC = '/tmp/claude-1000/-home-fatemec-geomind-spe-hackathon-2026/8ec5dad2-c357-58b5-87a7-b4044b660bf6/scratchpad/norun/src/examples/'
api.login()
def multipart(path, fields, fname, content):
    b = uuid.uuid4().hex; body = b''
    for k, v in fields.items():
        body += f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
    body += f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="{fname}"\r\nContent-Type: text/csv\r\n\r\n'.encode() + content + f'\r\n--{b}--\r\n'.encode()
    h = dict(api.UA); h['Content-Type'] = f'multipart/form-data; boundary={b}'; h['Authorization'] = 'Bearer ' + api._tok
    try:
        return json.loads(urllib.request.urlopen(urllib.request.Request(api.BASE + path, data=body, headers=h), timeout=120).read())
    except urllib.error.HTTPError as e:
        print('ERR', e.code, e.read()[:1500]); raise
def req(path, data=None):
    try: return api.req(path, data)
    except urllib.error.HTTPError as e:
        print('ERR', path, e.code, e.read()[:2000].decode()); raise
p = req('/workspace/projects', {'name': 'No-agent showcase: gemini study, superstructure and uncertainty'})
pid = p['id']; print('project', pid)
case = json.load(open(SRC + 'hackathon_2026/case.json'))
case['economics'] = json.load(open(SRC + 'hackathon_2026/economics.json'))
v = multipart('/design/case/files', {'project': pid, 'name': 'demand.csv'}, 'demand.csv', open(SRC + 'hackathon_2026/data/demand.csv', 'rb').read())
print('file', json.dumps(v)[:300])
json.dump({'project': pid, 'case': case, 'file_version': v}, open('state.json', 'w'), default=str)
