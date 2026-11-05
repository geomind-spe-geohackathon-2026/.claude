exec(open('s1b.py').read().split("p = req(")[0])
p = req('/workspace/projects', {'name': 'GeoMind results (no agent, gemini 0.6.32): superstructure, candidates, uncertainty'})
pid = p['id']; print('project', pid)
case = json.load(open(SRC + 'hackathon_2026/case.json')); case['economics'] = json.load(open(SRC + 'hackathon_2026/economics.json'))
for d in ('heating', 'cooling'): case['demand'][d]['power']['file'] = 'demand.csv'
c = req('/design/case', {'project': pid, 'base': None, 'note': "gemini's hackathon sample case (examples/hackathon_2026), set without an agent", 'content': case})
multipart('/design/case/files', {'project': pid, 'name': 'demand.csv', 'base': c['version']}, 'demand.csv', open(SRC + 'hackathon_2026/data/demand.csv', 'rb').read())
LR = '/tmp/claude-1000/-home-fatemec-geomind-spe-hackathon-2026/8ec5dad2-c357-58b5-87a7-b4044b660bf6/scratchpad/liverun/'
for n in ['GEMINI_Hackathon_Challenge_Requirements.pdf', 'GEMINI_Heating_Demand_Daily_2027.csv', 'GEMINI_Cooling_Demand_Daily_2027.csv']:
    multipart('/workspace/rag', {'project': pid}, n, open(LR + n, 'rb').read())
spec = json.load(open(SRC + 'hackathon_superstructure/plants/HackathonSuperstructure.json'))
f = req('/plant/flowsheet', {'project': pid, 'base': None, 'note': 'Hackathon superstructure: every candidate structure in one plant (32 valid structures)', 'spec': spec})
base = f['version']; out = {'project': pid}
s = req('/design/study', {'project': pid, 'kind': 'evolve', 'name': 'Superstructure search on LCTS and CO2', 'plant_version': base,
    'settings': {'prepare': ['size'], 'objectives': ['lcts', 'co2'], 'evaluations': 192, 'population': 16, 'seed': 0, 'polish': 0}})
out['evolve'] = s['id']
for n in ['HeatingFullCoolingPlant', 'HeatingHeatPumpCoolingPlant', 'HeatingCoolingPlant', 'HackathonPlant', 'HeatingAbsorptionCoolingPlant']:
    f = req('/plant/flowsheet', {'project': pid, 'base': base, 'note': f'Candidate {n}', 'spec': json.load(open(SRC + f'hackathon_2026/plants/{n}.json'))})
    base = f['version']
    out[n] = req('/design/study', {'project': pid, 'kind': 'minimize', 'name': f'{n}: sized and searched on LCTS', 'plant_version': base,
        'settings': {'prepare': ['size'], 'objective': 'lcts', 'evaluations': 40, 'seed': 0}})['id']
json.dump(out, open('clean.json', 'w')); print(out)
