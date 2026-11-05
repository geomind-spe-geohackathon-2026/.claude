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

(write them here before you test)
