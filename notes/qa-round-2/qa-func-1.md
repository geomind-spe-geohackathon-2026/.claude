# qa-func-1: chat and the case

Model: Sonnet (Sahand 2026-11-04 23:45 UTC). Rules: `common.md`. Area: FUNCTIONALITY of the chat-driven case, from the first
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

Reference values (from the PDF and the CSVs, checked 2026-11-04 by qa-func-1):
- Heating CSV: columns `date, heating_demand_MWth`, 365 rows 2027-01-01..2027-12-31, max 30.0 MW
  on 2027-01-28, min 2.673 MW, 111.668 GWh/year. Cooling CSV: `date, cooling_demand_MWcool`, 365
  rows, max 10.0 MW on 2027-07-19, 146 days at 0, 23.743 GWh/year.
- Reservoir: midpoint 2500 m TVD, gross thickness 100 m, gradient 30 C/km, surface 12 C (so
  87 C at 2500 m), pressure 250 bar(g), permeability 200 mD. Brine: 1030 kg/m3, 0.40 mPa s,
  GLR 0.8 Nm3/m3 (Nm3 at 0 C, 1.01325 bar(a)), gas 80 mol% CH4, 20 mol% CO2.
- Constraints: 1-3 doublets, max 300 and min 50 m3/h per doublet, max brine cooling 40 C,
  pump hydraulic efficiency 70 %, equal production/injection volumes, 330 operating days,
  supply 100 C heating, 20 C cooling.
- The PDF gives no site location, no weather, no prices, no return temperatures: anything the
  agents put there must be asked, sourced (Knowledge/connector with source, publisher, year) or a
  labelled assumption the user approved.

### qa-func-1-S1: one chat request with the three files (auto-approve off)
Goal: the first message builds the plan and the case. Steps: New project "QA2 qa-func-1 S1
full case"; upload the PDF and both CSVs; write "Design a geothermal heating and cooling plant
for this challenge; the files hold the demand and the requirements." Watch: the project lead
plans; the case lead and the geoscientist read the files (read/list_files steps); questions are
clear, one at a time or grouped, answerable from what a user knows. Correct: no question about a
value the files already give; no tool error loops; the run ends waiting for the user or done.

### qa-func-1-S2: the case against the PDF and the CSVs
Goal: every case value matches the reference above. Steps: after S1, open the Case page and read
the case through the chat ("show me the case"). Correct: demand series 365 days, peaks 30.0 and
10.0 MW on the right dates, totals 111.67 and 23.74 GWh; reservoir, brine, constraints exactly as
the PDF, with the right units (bar(g) vs bar(a), mol%, Nm3); supply temperatures 100 C and
20 C. Any value no file gave and no user approved is a bug (no defaults rule).

### qa-func-1-S3: approvals (approve, reject, edit; sources)
Goal: approval cards are complete and act right. Steps: in S1's chat with auto-approve off,
approve one set_case, reject one with a reason, edit one value before approving. Correct: the
card shows values, units and sources; a Knowledge or connector value carries source, publisher,
year; agent assumptions come labelled in one question (QA-010); reject makes the agent change
its proposal, not repeat it (QA-042); an edited value is the one stored.

### qa-func-1-S4: auto-approve on
Goal: the same request with auto-approve on runs without stopping on tool approvals. Steps: new
project "QA2 qa-func-1 S4 auto"; auto-approve on; same files and request. Correct: no approval
card waits; questions to the user still appear; the case ends complete; values same as S2.

### qa-func-1-S5: change the case by chat
Goal: one value changes, nothing else. Steps: in a project with a complete case, write "The
reservoir is at 3000 m TVD"; then "the permeability is 150 mD". Correct: only depth changes (the
agent may ask whether temperature should follow the gradient, 102 C, and pressure hydrostatic,
as the PDF allows; it must ask, not silently change); a new case version; the Case page shows it;
other values unchanged (compare versions).

### qa-func-1-S6: cancel mid-run and start again
Goal: no lost work (QA-047, QA-022). Steps: start a case run, cancel while the case lead is
working, send "go on". Correct: cancelled messages and steps stay in the chat; the next run
reuses the stored case and saved work, does not start from zero or re-ask answered questions.

### qa-func-1-S7: a run across a deploy (QA-035)
Goal: a run that spans :00 or :30 UTC resumes. Steps: start a long run a few minutes before a
deploy window; watch after. Correct: the run resumes, the chat keeps streaming or says what
happened; no run stuck waiting with no process (QA-017).

### qa-func-1-S8: provider error and retry (QA-011, QA-030)
Goal: a provider error is retried and shown. Steps: observe during all runs (cannot be forced).
Correct: the chat shows the retry; the nested run goes on; one bug per error kind.

### qa-func-1-S9: next-step chips follow the state
Goal: chips match the project state. Steps: read the chips on an empty project, after the files
are uploaded, with a complete case, after a case change. Correct: no "build the case" chip when a
case is complete; chips name the next real step (design) (QA-023).

### qa-func-1-S10: a user who does not know
Goal: questions the files cannot answer are handled. Steps: when asked for a value the files do
not give (location, weather, return temperatures), answer "I do not know; propose a sourced
value" or "use your assumption". Correct: a sourced proposal with source/publisher/year, or a
labelled assumption in one question; never silently invented.

## Status

- S1: in progress (2026-11-04 23:39 UTC). Project "QA2 qa-func-1 S1 full case"
  (a0947848-b958-4ee9-8927-56ec0a9cff03), shared memory Off, auto-approve off, three files
  attached in New project; first message sent; run active (Geoscientist listing files). No bug yet.
- S9 note: empty project with files attached shows chips "Build the case from my files", "Build
  the case by questions", "Which files do you need?" (fine for an empty case; recheck later).
- S2..S10: not started.

### Update by qa-func-1-II (2026-11-05 ~00:00 UTC / 01:00 local)
- Backend went 1.1.53 -> 1.1.54 during S1; the run resumed. A case_lead step shows "interrupted by a
  crash; it may have run in part" (QA-025 area), then the run continued (QA-035 OK).
- S1/S3 reject: first set_case card proposed time_zone UTC, text "the user's instruction is that the
  times are UTC" (user never said so). Denied with a reason; the agent then asked the time zone,
  I answered "do not know, use UTC as labelled assumption"; the new proposal labelled it UNCONFIRMED
  (reject works, QA-042 OK). Approved; case values (site, fluid, demand, supply temps) match the
  reference. Requirements card (flow 300/50, cooling 40, pump 0.7, reinjection 1, 330 d, 100/20 C)
  matches; no 1-3 doublets entry seen yet. Approval card has only Approve / Deny / Reason: no edit control.
- To do: file the "invented user instruction" bug, check doublets, edit test, S2.
