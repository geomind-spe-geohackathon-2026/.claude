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

Status (final, 2026-11-05 ~09:35 UTC; stopped by the coordinator, QA restructured by stage):

- S1 economics from sources: PARTLY. Run A (6921d00e, failed, QA-078; f59e5d2c cancelled, old code) and run B (project "QA2 functional-qa-2 economics B" df514ce2-1d5b-4681-a7e6-5592cc5eac30, run cef908d9, started 06:43 UTC, chat 138c18fa-3751-4f74-a76e-b52cbd1105ef). Questions and sources behave: region asked (QA-085 fixed in run B), no subsidy kept out (QA-084 fixed in run B), heat price 93.5115 honoured, the chiller per-energy opex never invented (offered 0 EUR/MWh as my accounting decision, set in case version 8). No simulation result ever saved, so CAPEX, OPEX, LCOH/LCOC, NPV were never seen.
- S2 chat change (discount rate 6 %): NOT RUN. S3 verdict, S4 explainer, S5 report, S6 agent log: NOT RUN (all need a finished simulation; QA-090: the design loop did not converge in 2 h 40).
- Run B is still running; I cancel it at 10:00 UTC (coordinator) and close the browser. Project QA2 functional-qa-2 economics (aa8023ca...) holds runs A (failed) and f59e5d2c (cancelled).

Bugs filed: QA-078 blocker (calculate state, fixed 0.4.68; retest partial: calculate used once in run B; the same validator fired for `questions` ids ['Q-indoor'] twice, recovered), QA-079 major (same questions asked again; real in geomind), QA-084 major (subsidy kept; ok in run B), QA-085 major (NL rows unlabelled; ok in run B), QA-086 minor (continue every 30 steps), QA-090 major (design loop does not converge). QA-084 and QA-085 need a Retest note by the next economics session: both behave right in run B.

Unfiled findings (not verified enough to file):
1. Run B case economics.json (versions 4-8) has no per-value sources (`about.sources` of run A's file is gone) and the 0 EUR/MWh chiller value is not marked as a user assumption: the user cannot see where each cost value comes from in the case. Check the Case page and the economics results for a source column before filing.
2. Run A: the UI said "Worked through 1012 steps, 294 needed another try" while the API said 150 steps and 292 tool calls; the runs list gave 4,803,456 input tokens, the agents endpoint 4,901,020; two agents stayed `running` in a failed run. Check against the Runs and logs usage panel (S6) before filing.
3. In request-461 the agent recommended a different heat price than in request-426 and did not answer my question why (the user question inside "Approve all, except ..." was ignored).
4. The case lead said the case was complete and then asked for indoor temperature/humidity, dew point margin and return pressures one at a time (same class as QA-069); the first run asked 16 values in one question, the second only 6.
5. Run A's chat repeated my three answers three times each (QA-079), run B twice for the economics list.
6. Log export: `/runs/{id}/log/export` needs `format` (json 17 MB, md 1.5 MB, csv returned 422); not tried in the UI.
7. agent-browser: the New project dialog closed without creating a project when "Create" was clicked by ref or by name; pressing Enter in the Name field created it. Possibly an agent-browser quirk (no product bug filed).
8. Observed: opex.fixed.production_pump = 20 %/yr (row opex-production-pump-ecn-2012-esp-replacement) looks high; worth a plausibility check against the OPEX result.

Next session on economics, verdict, explainer, report and agent log: start from a finished simulation (QA-088 Results tab should show agent study results), then S2-S6 as written above.
