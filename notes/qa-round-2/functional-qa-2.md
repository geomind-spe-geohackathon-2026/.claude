# functional-qa-2: economics, verdict, explainer, report, agent log

Model: Sonnet. Rules: `common.md` (inputs: ONLY the competition PDF and the two CSVs; agent-browser
only; bugs with qa.py, reporter functional-qa-2). Judging criteria: `memory/competition-judging-criteria.md`.

Own project "QA2 functional-qa-2 economics", competition files, auto-approve ON; one chat
request for the full design and its economics; get to a simulated design fast (do not test the
case step: functional-qa-1's area). Then test:
- Economics: every cost from a sourced catalogue row or an approved value; keys with no row asked,
  never invented; CAPEX, OPEX, LCOH/LCOC, NPV consistent and plausible; a chat change ("discount
  rate 6 %") changes only that.
- Verdict and scoring: each PDF hard cap listed with value, limit, pass/fail; KPIs explained.
- Explainer: "why this number of doublets", "how much heat from geothermal vs backup", "peak heating
  demand and when" answered right (30.0 MW, 28 Jan; 111.67 / 23.74 GWh).
- Report: generate, read, download; every number matches the results pages; it covers the
  deliverable (geothermal assessment, system design, heating and cooling capacities, agent
  architecture).
- Evidence (judging point 7): the agent log with prompts, answers and token usage exportable;
  Runs and logs usage panel (names, tool-call counts, totals) correct.
Not yours: the case (functional-qa-1), design loop and configurations (functional-qa-1),
studies, evolve, the new tools and robustness (functional-qa-3).

## Scenarios

All use project "QA2 functional-qa-2 economics" (competition files only, auto-approve ON). Checked
against the PDF caps and CSVs (peak heating 30.0 MW on 28 Jan; heating 111.67 GWh, cooling 23.74 GWh).

- **functional-qa-2-S1 Economics from sources.** Goal: one chat request for the full design and its
  economics. Steps: upload PDF and CSVs, ask for design + economics, approve prompts. Correct: every
  cost from a sourced catalogue row or a value I approve; keys with no row (e.g. opex.per_energy of
  chillers) are asked, never invented; CAPEX, OPEX, LCOH/LCOC, NPV consistent and plausible by hand.
- **functional-qa-2-S2 Chat change.** Goal: "discount rate 6 %" changes only the discount rate. Correct:
  NPV/LCOH move, CAPEX/OPEX and the design stay; the change is shown with its source "user".
- **functional-qa-2-S3 Verdict and scoring.** Goal: results/verdict page lists each PDF hard cap with
  value, limit, pass/fail; KPIs explained in plain words; values match the simulation page.
- **functional-qa-2-S4 Explainer.** Ask: "why this number of doublets", "how much heat comes from
  geothermal vs backup", "what is the peak heating demand and when". Correct: 30.0 MW on 28 Jan;
  111.67 / 23.74 GWh; geothermal/backup split equals the results page; reasoning refers to the run.
- **functional-qa-2-S5 Report.** Generate, read in the app, download. Correct: each number equals the
  results pages; it covers geothermal assessment, system design, heating/cooling capacities, agent
  architecture; no placeholders; download opens.
- **functional-qa-2-S6 Agent log (judging point 7).** Export the log: prompts, answers, token usage per
  agent; Runs and logs usage panel (agent names, tool-call counts, totals) matches the export and the
  run JSON.

Status:
- S1-S6: not started
