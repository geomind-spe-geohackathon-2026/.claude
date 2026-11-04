---
name: gemini-cost-sources
description: "cost-sources" dataset (Sahand's handle, 2026-11-01): cost/price source research for the sample cases (2026-11-01 18:30): where the files are, key verified numbers, what stays placeholder
metadata:
  type: project
---

Handle: Sahand calls this dataset "cost-sources" (named 2026-11-01 20:15); when he says it, it means this research. Only on his Mac, not committed anywhere yet.
Done by a Remote Control session on Sahand's Mac; files in /Users/sahand/Desktop/geomind-spe-geohackathon-2026/docs/cost-sources/ (sources.csv 74 rows: 33 verified, 25 secondary, 16 placeholder; README; DEA PDFs/Excel; Eurostat/Ember data). No repo changed. Earlier draft: /mnt/project-files/notes/gemini-cost-sources.csv.
2015 EUR via Eurostat HICP prc_hicp_aind: 2013 99.38, 2014 99.81, 2015 100, 2023 123.15, 2025 128.75.
Key: drilling 1,239/1,833/2,063 EUR/m at 2300/3000/4000 m (2013 NL SDE+), 3000 m = 1,845 EUR2015 -> cost depends on depth (gemini has flat EUR/m: general improvement = depth-dependent drilling cost). DEA geothermal 2000 m 1.9 MEUR/MW (2025). Chillers secondary only (abs 0.234, comp 0.159, ads 0.827 EUR2015/W). ESP no EUR/W. HX 0.109 EUR/W (DH station, no dT). Dry cooler 0.049-0.107 EUR/W. DH pipe 1,149 EUR2015/m (5-25 MW). Discount 4% real financial (Reg 480/2014 Art 19(3)), 3% social (Better Regulation Tool #64) verified. EU grid 209.2 g/kWh 2025 (Ember). Heat price 85-98 EUR/MWh consumer; cold 81-105 secondary. Lorenz 40-60% confirmed by DEA. Arpagaus 10-80 K NOT confirmed. DEA 45.1.a fixed O&M 500k EUR/MW/yr looks like an error.
Placeholders: flare, gas makeup, chemicals, waste disposal, component fixed O&M (10), HP lift range; degasser only 1 MEUR subsidy reserve.
Next: after the correctness prompt, a prompt copies verified values into inputs/examples/*/case.json + README + sources.csv in gemini repo.
2026-11-01 21:12: decided home = gemini/docs/cost-sources/ (reference data, not read by code); prompt prompts/gemini-costs.md (docs only). Later: values into examples + depth-dependent drilling.
21:31 DONE: cost catalogue on gemini dev fde7178b (docs/cost-sources/, 74 rows 33/25/16, test_cost_sources.py). Notes: drilling source is per metre of DEPTH vs gemini per metre DRILLED; PBL rows priced at 2027 decision year; units EUR/MW/yr, EUR/MW/m, EUR/MW/km/yr, USD/W not in gemini table; 4 Springer rows unverifiable; Arpagaus slides say 130->40/25 K.
