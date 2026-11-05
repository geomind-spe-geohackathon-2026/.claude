---
name: gemini-repo-findings
description: What the GEMINI repo actually implements vs placeholders, example doublet numbers, and the plan doc link
metadata:
  type: project
  modified: 2026-10-27T16:43:14.093Z
---

UPDATE 2026-10-30: the 2026-10-27 notes below describe the OLD upstream code. Team fork branch `refactor` (80cd26b) now has real HeatPump, AbsorptionUnit, AdsorptionChiller, Boiler, ThermalStorage, IceStorage, Heat/CoolingConsumer and plants HeatingSubstation, CoolingSubstation, DistrictNetwork, AtesPlant, Doublet; Cost + total_cost exist (no LCOH/CO2); no module registry, plants are handwritten (files cannot wire). Declarations expose schema/unit.

Studied gemini-geothermal-suite-open on 2026-10-27.
- Real physics models only in src/gemini_model (StaticModel API: update_parameters / calculate_output(u,x) / get_output): ESP, well dP/dT (Beggs-Brill, Darcy-Weisbach), reservoir IPR/injectivity/pressure, PVT water, CO2 corrosion, erosion.
- gemini_framework units for heat exchanger, reservoir, prod well, degasser, filter, boilers, pumps are EMPTY 11-line placeholders; only ESP and injection well have calc modules. Framework is time-series monitoring (InfluxDB), so the agent should call gemini_model classes directly.
- Templates (heat pump "carnot" 70%, CHP, heat demand, electric boiler) have no code.
- Example doublet: 80°C, 220 bar, top 1800 m, PI 21 / II 20 m3/h/bar, ESP 82–178 m3/h; dataset ~150 m3/h, 80→20°C, ~10.9 MW.
- Missing for Challenge 2: HX, demand profiles, heat pump, absorption chiller, storage, aux boiler, economics, CO2.
- User's prior design (ChatGPT notes, now documents/project/design/geomind-system-design-notes.md) overstated GEMINI coverage; plan keeps that architecture, MVP core first.
- Plan doc: https://claude.ai/artifact/SSfh6RdLGiQwcKx1Wabn4g
- Open: push target repo, deadline, site/demand case, LLM choice.
- Task inputs (scenario/demand) are released 2026-10-29; team starts input-independent work before that.

- Upstream history (checked 2026-10-27): only 5 public commits; V1.0.0 was one squashed dump of 795 files, then 3 small maintainer commits (Ryvo Octaviano, Leila Hashemi; PRs #47, #48). Dev happens internally; no outside contributions or restructures. So I advised against a folder-restructure PR; contribute additively in existing src/gemini_* folders via small PRs.
