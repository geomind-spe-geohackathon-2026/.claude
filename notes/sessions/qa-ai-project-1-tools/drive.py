"""usage: drive.py send <chat> <text> | answer <run> <request> <json-answer> | wait <run> | newchat <pid> <title>"""
import api, json, sys, time
def wait(run, limit=5400):
    t0=time.time(); last=None
    while time.time()-t0<limit:
        r=api.req(f'/assistant/runs/{run}')
        if r['status']!=last:
            print(time.strftime('%H:%M:%S'), r['status'], r.get('loop'), flush=True); last=r['status']
        if r['status'] in ('waiting','succeeded','failed','cancelled','done','completed','finished','stopped'):
            json.dump(r, open(f'runs/{run}.run.json','w'), indent=1)
            print(json.dumps({k:r.get(k) for k in ('status','loop','request','error','input_tokens','output_tokens','cost','started','ended')})[:4000])
            return r
        time.sleep(15)
cmd=sys.argv[1]
import os; os.makedirs('runs',exist_ok=True)
if cmd=='newchat':
    c=api.req('/assistant/chat',{'project':sys.argv[2],'title':sys.argv[3]}); print(c['id'])
elif cmd=='send':
    m=api.req(f'/assistant/chat/{sys.argv[2]}/messages',{'content':sys.argv[3]})
    print(json.dumps(m)[:600]); run=m['run']['id']; print('RUN', run, flush=True); wait(run)
elif cmd=='answer':
    r=api.req(f'/assistant/runs/{sys.argv[2]}/answer',{'request':sys.argv[3],'answer':json.loads(sys.argv[4])})
    wait(sys.argv[2])
elif cmd=='wait':
    wait(sys.argv[2])
