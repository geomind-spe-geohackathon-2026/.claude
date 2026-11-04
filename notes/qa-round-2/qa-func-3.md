# qa-func-3: economics, scoring and report

Model: Sonnet (Sahand 2026-11-04 23:45 UTC). Rules: `common.md`. Area: FUNCTIONALITY after the simulation. Get to a simulated
design quickly with your own project (competition files, auto-approve on); do not test the case,
design or simulation steps (qa-func-1, qa-func-2) unless they block you.

Cover at least:
- Economics: every cost comes from a sourced catalogue row (Knowledge, 153 rows since geomind
  0.4.52) or an approved value; keys with no row (opex.per_energy of the chillers,
  opex.fixed.adsorption_chiller, subsidy.capacity) are asked, never invented; ask_economics
  answers complete (QA-013); results (CAPEX, OPEX, LCOH/LCOC, NPV) are consistent and plausible.
- Scoring: KPIs, the verdict against the PDF's requirements, each score explained.
- The explainer: questions about the design and the numbers get correct answers.
- The report: generate, read and download it; every number matches the results pages; it covers
  what the PDF asks for; the agent log is exportable (a hackathon deliverable).
- Runs and logs: run JSON, per-agent usage (context, tokens, cost, tool calls) and totals.
- Economics changes by chat ("discount rate 6 %"): only that changes; results update.

## Scenarios

Reference numbers (from the CSVs, matching the PDF): heating 365 days, peak 30.0 MWth on
2027-01-28, 111.67 GWh/yr; cooling 365 days (219 non-zero), peak 10.0 MWcool on 2027-07-19,
23.74 GWh/yr. Hard caps: 1-3 doublets, 50-300 m3/h per doublet, brine cooling <= 40 C,
pump efficiency 70 %, 330 operating days, supply 100 C heating / 20 C cooling.

- qa-func-3-S1 Setup: project "QA2 qa-func-3 economics", auto-approve on, upload the PDF and the
  two CSVs, one chat request to build the case, design and simulate. Correct: a simulated design
  exists; only blockers in qa-func-1/2 areas are reported.
- qa-func-3-S2 Economics sourcing: ask for the economics. Correct: every cost key shows a
  catalogue row (source, publisher, year) or a value the user approved; keys with no row
  (opex.per_energy of the chillers, opex.fixed.adsorption_chiller, subsidy.capacity) are asked
  with a labelled assumption, never filled silently; ask_economics completes in one question
  (QA-007, QA-013, QA-045); no foreign tariffs (QA-041).
- qa-func-3-S3 Economic results: CAPEX, OPEX, LCOH/LCOC, NPV are shown. Correct: CAPEX per
  doublet and per MW plausible (wells at ~2.5 km), OPEX consistent with energy used, LCOH within
  a sane range for deep geothermal (tens of EUR/MWh), LCOH*heat ~ annualised cost; same numbers
  on every page and in chat.
- qa-func-3-S4 Scoring and verdict: KPIs and verdict against each PDF requirement (doublets,
  flow caps, brine cooling, supply temperatures, 330 days, demand covered). Correct: each
  requirement is listed with value, limit and pass/fail; each score is explained; delivered heat
  and cooling vs 111.67 / 23.74 GWh.
- qa-func-3-S5 Explainer: ask in chat "why this number of doublets", "what is the LCOH and how
  is it computed", "how much heat comes from geothermal vs backup", "what is the peak heating
  demand and when". Correct: answers match the results pages and the CSVs (30.0 MW, 28 Jan).
- qa-func-3-S6 Economics change by chat: "use a discount rate of 6 %". Correct: only the
  discount rate changes (case version diff); LCOH/NPV update, CAPEX and energy stay the same.
- qa-func-3-S7 Report: generate, read, download. Correct: every number matches the results
  pages; it covers what the PDF asks (demand, constraints, configuration, checks, violations,
  iterations, explanation of decisions); download works; the agent log is exportable.
- qa-func-3-S8 Runs and logs: run JSON download; per-agent context, tokens, cost, tool calls and
  totals. Correct: totals equal the sum of agents; nothing flat or missing (QA-046).
- qa-func-3-S9 Variations (after all above): a second plant family (e.g. with heat pump) and
  the comparison of economics; a change of a price ("electricity 0.12 EUR/kWh").

## Status

- S1: running (chat 63c70b89-4c1e-496b-b908-2f9220c73457, sent 2026-11-05 ~01:00 UTC). Note: Auto-approve toggle does not switch on before the first message is sent (aria-pressed stays false); works inside the chat. Not yet reported (qa-ux area).
