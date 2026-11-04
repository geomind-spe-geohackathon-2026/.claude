---
name: gemini-remaining-work
description: State on 2026-10-31 23:05 after thread Gemini III: what is pushed, which prompts are pending, and the open gemini/geomind work list to discuss next
metadata:
  type: project
---

State (2026-10-31 23:05):
- gemini `refactor` at 2453af1 (pushed): new tree (no core/base/testing; run/ holds Problem, Constraint, Assumptions, schedule, simulate, call...; compiler optional; data/optim/evaluate/analysis), every call (plant, problem)[, results], cost-based dispatch, from_*/to_* naming. Sample problems inputs/examples/{hackathon_2027 (2 problem files), shallow_district} as problem.json + CSV + plant.json. Numbers unchanged except plant_with_treatment (float residue fix). See [[gemini-target-structure]].
- geomind main still 2964c69 (old gemini API, Brief with hackathon preset in code). Prompt for Fatemeh written, NOT yet confirmed run: /mnt/project-files/phases/geomind/follow-gemini-problem.md.
- backend not adapted (backend/src/core/gemini/plant.py uses plant_type, HackathonPlant).

Open gemini work (next prompt, not written yet; wait for «go»):
- build stubs: optim.size (doublet capacity at depth/flow, count for peak, unit capacities), optim.sensitivity, evaluate.capacities, report, compare (Pareto), data.synthesize (profile from peak/annual, cited shape), plants.capabilities.
- move fluids (density, viscosity, GLR, gas comp) from plant dict into Problem (site); Problem has no place for doublet-count range or return-temperature assumptions (geomind will report these as requests).
- results_to_frame in data/legacy breaks from_*/to_* rule (-> Results.to_frame).
- capex on all ~70 modules (only 9 have it); ambient temperature profile; multiple units per kind in schedule; storage/ATES in schedule; multi-year runs; failure diagnostics; discrete optim variables; multi-objective. Full list: /mnt/project-files/notes/gemini-gaps-general.md.
- sources: hackathon prices are placeholders (need cited prices before report); Arpagaus 10-80 K lift claim unverified; lorenz_fraction 0.5 is an assumption.
- eager vs compiled speed numbers from the structure prompt were not reported to me.
Deliverables still to plan: Challenge 2 design + report (≤5 pages/≤10 slides), video ≤5 min, agent log.
Related: [[feedback-io-naming]], [[feedback-general-not-competition]], [[prompt-writing-rules]].
Discussion of usage API / units / Problem design (2026-10-31 23:15+): [[gemini-problem-design]].
2026-11-01 10:57 Sahand: gemini-case pushed (807205e), cleanup pushed, origin/refactor = ab9e754; 7 sample runs identical. Cleanup only -293 lines, 15 bugs fixed, guards in. e2e: hackathon.py timed out 900 s on python backend -> removed from parity. Open: 8 module defaults remain (circ pump eff, well U-value, Fluid.salinity; ~130 tests); bare SI still accepted in set_params, gm.call, Stream, Fluid; size+minimize gives dearer design than stored plant (67 vs 54 EUR/MWh) and minimize ignores case constraints; injection pump unpriced; hackathon.py ~400 s; test_doublets/test_size near 1 s. speed branch NOT on origin (only local worktrees gemini-speed*), touches ops that cleanup changed -> conflict risk. Reports in gemini/.tmp/case/report.md, .tmp/cleanup/report.md.
11:10 speed session paused on a question (unknown, asked Sahand to paste). Gave a rebase update: commit WIP, rebase speed onto origin/refactor ab9e754 keeping cleanup code, redo baseline with case.json, report hackathon.py runtime. Fixes prompt (hackathon ranking, 8 defaults, units in set_params/call/Stream/Fluid, injection pump capex) waits for speed status.
11:16 speed question: keep 2 exceptions outside its folders (plants/_utils/loops.py array loop solver, modules/module.py output-validation fix) -> told Sahand "Both still stand" (hackathon daily year 8 s -> 0.143 s eager, 1e-9 equal). Fixes prompt must NOT touch those two files.
