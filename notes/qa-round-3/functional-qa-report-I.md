# functional-qa-report-I

Read `README.md` here (your row) and `../qa-round-2/common.md`. Your project: "QA3 report" (id in
STATUS.md once seeded). Test only your stage; report bugs with qa.py (reporter
functional-qa-report-I). Check every number against the PDF and CSVs.

## Scenarios

Reference facts (competition files, `memory/competition-inputs.md`): heat 365 daily values, peak
30.0 MWth, min 2.673, sum 4652.82 MW-days = 111.67 GWh/yr; cool peak 10.0 MWcool, sum 989.27 MW-days
= 23.74 GWh/yr, >0 on 219 days; 1-3 doublets, 50-300 m3/h each, brine cooling <= 40 K, pump eff 70 %,
supply 100 C heating / 20 C cooling. Judging: `memory/competition-judging-criteria.md` (agent log with
prompts, answers, tokens; explained extra calculations; realised heating/cooling capacities; techno-economics).

Common to all: log in with the admin account (agent-browser, session functional-qa-report-I), open
"QA3 report", one short request at a time, read the numbers in the UI and compare with the run JSON
(Runs and logs). Wrong numbers, unsourced assumptions, defaults the user never approved, a Claude
model name anywhere, and stage-crossing gaps are bugs.

- functional-qa-report-I-S1 Economics: ask the chat for CAPEX, OPEX, LCOH/LCOC (or LCOE of heat and
  cold) and payback of the finished run. Correct: every cost item has a source or a labelled,
  user-approved assumption; totals equal the sum of items; units consistent (EUR, EUR/MWh); energy
  basis matches the CSVs (111.67 GWh heat, 23.74 GWh cool, minus any unmet demand shown by the run).
- S2 Economics what-if: change one assumption (electricity price, then discount rate) and ask for
  the new LCOH. Correct: only that figure moves, direction makes sense, the change is recorded.
- S3 Verdict: ask "does the design meet the requirements?". Correct: each hard cap is listed with
  its value and pass/fail (1-3 doublets, 50-300 m3/h per active doublet, brine cooling <= 40 K, pump
  eff 70 %, supply 100 C / 20 C); verdict agrees with the simulation violations; any unmet-demand
  hours/days are named.
- S4 Realised capacities: ask for realised heating and cooling capacity and annual delivered energy.
  Correct: peak delivered <= 30 MWth / 10 MWcool, annual energy within the CSV totals, coverage % consistent.
- S5 Explainer: ask why this configuration and what alternatives were compared. Correct: reasoning
  refers to real run/study results of this project (no invented numbers), names alternatives with
  their figures, states the geothermal-driven cooling path (absorption/adsorption) and its basis.
- S6 Gaps and extra calculations: ask what the twin could not model and how it was handled. Correct:
  missing models named, calculate/run_python/web_search results shown with sources, explained why appropriate.
- S7 Uncertainty/bonus: ask for a short sensitivity or uncertainty statement on the economics.
  Correct: ranges come from a real study; no fabricated percentiles.
- S8 Report: generate the technical report (max 5 pages target). Correct: opens/downloads, sections
  cover assessment, design, capacities, economics, agent architecture; every number equals the chat
  and run JSON; figures render; no placeholders, no secrets, English.
- S9 Agent log export: export the interaction log. Correct: contains prompts, answers and token
  counts per agent and in total; totals match the Runs view; model is deepseek (never Claude); file
  opens, valid format, no secrets.
- S10 Re-ask consistency: ask the same economics question twice and after a page reload. Correct:
  same numbers, no duplicate runs without notice, chat state survives reload.
- S11 Bad input: ask for a report of a figure that does not exist (e.g. LCOH with a negative
  discount rate -150 %). Correct: refused or asked back, no crash, no silent default.

## Status

- 2026-11-05: scenarios written; waiting for the QA3 report project id from the coordinator.
