exec(open('s1.py').read().split("p = req(")[0])
o = json.load(open('clean.json')); pid = o['project']
_req = req
def req(path, data=None):
    for i in range(60):
        try: return _req(path, data)
        except urllib.error.HTTPError as e:
            if e.code not in (502, 503, 504, 401): raise
        except Exception: pass
        time.sleep(10)
        try: api.login()
        except Exception: pass
while True:
    try: s = api.req(f"/design/study/{o['evolve']}")
    except Exception: time.sleep(15); api.login(); continue
    if s['status'] not in ('queued', 'running'): break
    time.sleep(15)
print('evolve', s['status'], s.get('result'))
sv = req(f"/design/study/{o['evolve']}/structures/1/plant", {}); v = sv['plant_version']; print('best plant version', v)
for kind, name, st in [('sensitivity', 'Chosen design: one-at-a-time sensitivity', {'metrics': ['lcts', 'co2']}),
                       ('sample', 'Chosen design: Monte Carlo uncertainty (50 draws)', {'metrics': ['lcts', 'co2', 'lcoh', 'lcoc'], 'samples': 50, 'seed': 1}),
                       ('run', 'Chosen design: full-year run and verdict', {})]:
    o[kind] = req('/design/study', {'project': pid, 'kind': kind, 'name': name, 'plant_version': v, 'settings': st})['id']
json.dump(o, open('clean.json', 'w'))
while True:
    try: items = api.req(f'/design/study?project={pid}')['items']
    except Exception: time.sleep(20); api.login(); continue
    if not [x for x in items if x['status'] in ('queued', 'running')]: break
    time.sleep(20)
for x in items: print(x['kind'], x['name'][:45], x['status'], x.get('result'), json.dumps(x.get('error'))[:150])
