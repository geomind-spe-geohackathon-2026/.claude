"""log.py <run>: dump the run log."""
import api, json, sys
run=sys.argv[1]
L=api.req(f'/assistant/runs/{run}/log')
json.dump(L, open(f'runs/{run}.log.json','w'), indent=1)
print('keys', list(L.keys()))
