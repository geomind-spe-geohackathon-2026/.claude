# qa-func-1: chat and the case

Model: Opus. Rules: `common.md`. Area: FUNCTIONALITY of the chat-driven case, from the first
message to a complete, correct case. Not UI looks (qa-ux), not design or simulation (qa-func-2),
not economics, scoring or report (qa-func-3).

Cover at least:
- One chat request with the PDF and the two CSVs uploaded: the project lead plans, the case lead
  and the geoscientist read the files; every question is clear and answerable.
- The case is correct against the PDF and CSVs: demand series (365 days, peaks, totals), site,
  reservoir (depth, thickness, gradient, surface temperature, pressure, permeability), brine
  (density, viscosity, GLR, gas composition), hard constraints (doublets, flow per doublet,
  brine cooling, pump efficiency, operating days, supply temperatures). Any value that came
  from nowhere is a bug (no defaults rule).
- Approvals: values from Knowledge or a connector come with source, publisher, year; labelled
  agent assumptions in one question (QA-010); auto-approve on and off; approve, reject, edit.
- Changing the case by chat afterwards ("the reservoir is at 3000 m"): only that value changes.
- Robustness: cancel a run mid-way and start again (no lost work, QA-047); a run across a deploy
  (QA-035); a provider error and its retry (QA-011).
- Next-step suggestion chips follow the project state.

## Scenarios

(write them here before you test)
