---
name: gemini-domain-folder-mapping
description: 2026-10-31 18:50 Gemini IV thread: mapping of current gemini refactor folders (33c7f52) onto the 6 domains, and the 5 open questions
metadata:
  type: project
---

Thread "Gemini IV" (discussion only, nothing changed). refactor at 33c7f52 has all 18 geomind gaps done.
Mapping given: core.base = modules/module.py, plant.py, container.py, modules/_utils, plants/_utils; core.engine = engine+graph+backends+ops; core.units = physics/units.py; library.<cat> = modules/<cat>; library.plants; library.catalogue = registry + plants catalogue; library.testing = testing + engine/evaluate.py; design.plan = analysis/schedule+roles+physics/dispatch; design.sizing = physics/doublet + plants/_utils/doublets; design.search = optim/search; evaluate.run = simulate; evaluate.kpi = analysis/kpi+series; twin.operate = replay/live/resume; twin.calibrate = optim/calibrate + analysis/fits; twin.wells = analysis/wells+solves; twin.integrity = analysis/integrity.
Fact: core already imports no analysis/checks/economics/optim/profiles. Cooler uses physics.dispatch.
Open (asked 18:50): 1 utils/ -> core._utils, Dataset -> data.datasets, legacy -> data.legacy; 2 Problem class in design.problem, data.problems = saved problems; 3 split engine/run.py between evaluate and twin; 4 keep Cooler's dispatch functions in physics; 5 remove challenge_rules, HackathonPlant, hackathon profiles, Doublet challenge defaults. Recommended starting with 2.
Related: [[gemini-api-rules]], [[gemini-decisions-2026-10-31]].
