# qa-func-3: economics, scoring and report

Model: Opus. Rules: `common.md`. Area: FUNCTIONALITY after the simulation. Get to a simulated
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

(write them here before you test)
