---
name: competition-inputs
description: Official hackathon inputs released 2026-10-29 (demand CSVs, reservoir, brine/gas, hard constraints) and what they imply for gemini
metadata:
  type: project
  modified: 2026-10-30T20:57:40.707Z
---

Files (Sahand uploaded 2026-10-30 in thread "Fit gemini to the competition inputs"): GEMINI_Heating_Demand_Daily_2027.csv (date,heating_demand_MWth), GEMINI_Cooling_Demand_Daily_2027.csv (date,cooling_demand_MWcool), GEMINI_Hackathon_Challenge_Requirements.docx.pdf (2 pages, dated 2026-10-28). Not yet copied into project files.
- Demand: 365 daily averages. Heat peak 30.0 MWth (28 Jan), min 2.67, 111.67 GWh/yr. Cool peak 10.0 (19 Jul), 23.74 GWh/yr, >0 on 219 days. Max heat+cool on one day = 30.
- Reservoir: mid depth 2500 m TVD, 100 m thick, 30 C/km, surface 12 C (=> 87 C at 2500 m), 250 barg, 200 mD. Depth may be chosen: hydrostatic pressure + gradient.
- Brine: 1030 kg/m3, 0.40 mPa.s constant; GLR 0.8 Nm3/m3 (0 C, 1.01325 bar), gas 80% CH4 20% CO2.
- Hard caps: 1-3 doublets; 50-300 m3/h per doublet while active; brine cooling <= 40 K; pump eff 70%; prod = inj volume; doublet runs 330 daily steps; supply 100 C heating, 20 C cooling (return temps not given).
- Upstream says agent must be built by participants; GEMINI repo ref is the development branch.
Implications: 87 C < 100 C supply, so heat pump / gas boiler top-up or deeper wells (~3000 m gives ~102 C). One doublet max ~14 MW at 40 K, so peak needs 2-3 doublets or top-up. Gas ~1.9 MW fuel per doublet at full flow.
Related: [[gemini-repo-findings]], [[native-engine-plan]].
Upstream `development` branch (checked 2026-10-30 22:30, last merge 2026-10-29): adds gemini_simulator (nodal solver, JSON project loader, kpi, well_flow), separator with gas_water_ratio -> gas flow, gas boiler + CHP burning co-produced gas with CO2 emission, heat pump, HX, compressor, mixer/splitter, docs. refactor branch has the modules but NOT the gas chain (no gas_water_ratio; boiler has no gas inlet). Organisers clearly expect co-produced gas use.
