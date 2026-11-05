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

### Status lines (qa-func-1-II, 2026-11-05 ~00:25 UTC)
- S1 done: case built from the 3 files in one chat; questions clear (time zone, air, delegated assumptions, economics). Run continued into design.
- S2 done: Case page demand 365 pts, peaks 30 MW Jan 28 / 10 MW Jul 19, 111.7 / 23.7 GWh; site, fluid, constraints match the PDF; supply 100/20 C. Bugs: QA-063 (dissolved gas shown x100 in the form), QA-065 (no 1-3 doublets rule though the design lead says the case has it). Notes: agent claimed 'the user's instruction is that the times are UTC' (never said); asked time zone though the Time tab says no offset = UTC; chemical price took proxy row (2.908) not the recommended (1.942); economics proposed Dutch subsidy/heat cap for a site-less case (QA-041 pattern; I removed them by 'change some').
- S3 done: reject with reason -> new proposal (OK); edit via 'change some' -> 8 C stored (OK); approval card has no edit control, only Approve/Deny/Reason; assumptions come labelled in one question (QA-010 OK), economics rows carry source/publisher/year.
- S5 partly: 'reservoir is at 3000 m TVD' -> set_case changed only reference_depth (+ note 'depth FIXED by the user', not said); agent then asked about pressure (did not change it silently) - OK; temperature follow not yet seen.
- S6 done: cancel then 'go on' -> reused stored case, no re-asked questions, steps collapsed into 'Worked through 125 steps'. Chat shows 'This run ended without an answer' for cancelled runs.
- S7: backend deployed 1.1.53 -> 1.1.54 (and 1.1.56) during S1; run resumed; one case_lead step 'interrupted by a crash'.
- Order now (coordinator 2026-11-05): one project through case -> design -> economics/report; qa-func-2 and qa-func-3 files for their scenarios.

## PRIORITY (Sahand, 2026-11-05 ~00:45 UTC)

The most important test is ONE start-to-end design run exactly as the challenge PDF asks
(section 1): interpret the demand profiles, generate system configurations, run engineering
checks with GEMINI, detect violations of every hard cap, iteratively improve the design, and
explain every major engineering decision, to a final feasible, explained design. For each step
record: did it happen, was it correct against the PDF and CSVs, was the decision explained.
Economics and the report come after, as far as time allows.

## Judging checklist (organisers' slides, `memory/competition-judging-criteria.md`)

Check in the start-to-end run, and file a bug when one fails:
1. Analysis: the agents read the problem themselves (PDF, CSVs) without the user filling values.
2. GEMINI: they configure and run GEMINI models (check, simulate), not only talk.
3. Gaps: they name a missing modelling capability and fill it with an explained extra
   calculation (calculate, run_python) or a sourced value (web_search), saying why it fits.
4. Alternatives: at least two configurations compared, with the reason for the final one.
5. Integrated design: geothermal for direct heating AND, where possible, for cooling (e.g. an
   absorption/sorption chiller on geothermal heat), plus heat pumps, chillers, storage or backup
   as needed; each sized.
6. Results: the realised heating and cooling capacities and energies are stated (vs 30/10 MW
   peaks, 111.67/23.74 GWh).
7. Evidence: the agent log with prompts, answers and token usage can be exported; the final
   configuration and its supporting calculations are explained.

### functional-qa-I status (2026-11-05 ~00:25 UTC)
- QA-068 (key limit) retested and verified: failed run now says "The model provider refused: key limit exceeded; an admin must raise it"; runs work. QA-065 and QA-061 retested verified in fresh project (count 1-3 present; no 'Already answered' note). QA-063 verified by hotfix-front. QA-069 filed from qa-func-3 notes. QA-070 filed (nested design_lead 'interrupted by a crash' x2, project lead shrinks scope).
- Start-to-end run: project "QA2 functional-qa-I full run" 61134432, chat 81b51db5, run 861ef137, auto-approve ON, shared memory Off. Case step: 19-item question, my answers (UTC, generic site, labelled assumptions, Ember 209.21), economics card with NL/NO/FR rows (I left subsidy and waste disposal open). Design phase running; checklist points 1 (analysis from files: yes, asked only values the files lack) done; 2-7 pending.
- Old project S1 (a0947848) abandoned with its depth changed to 3000 m and a pressure question open; S5 temperature-follow not checked.

### functional-qa-I PAUSE (usage pause, ~02:00 UTC 2026-11-05; resume after 04:10 UTC on coordinator's "go on")
- Start-to-end run left RUNNING: project "QA2 functional-qa-I full run" 61134432-45fa-48db-afef-4f930f3825da, chat 81b51db5-1a6b-402a-9223-66c8af1c6403, run 861ef137-08a2-4252-bf30-437630caf747 (auto-approve ON, shared memory Off, started on backend 1.1.62; 5.03M tokens, 0.169 USD at pause; tokens were flat for ~1 min at the last check).
- Where the design stands: case complete and stored (count 1-3 rule present, QA-065 verified). Because of QA-070 (fixed in 1.1.65 after this run began) the project lead narrowed the brief to ONE configuration: 17 modules, size.doublets = 2, compression chiller route, stored as design/geothermal_doublet_compression_conn2; equipment values still missing, the three engineers were filling them. No simulation or comparison of two configurations yet. After the reset: look at the run; if it finished with one configuration, send the full brief again (several configurations, comparison, capacities, explanation) to retest QA-070 on 1.1.65+.
- Judging checklist: 1 analysis OK; 2-7 not yet seen (absorption chiller on geothermal heat not chosen so far: cooling route is compression chiller; check why in the explanation).
- Unfiled notes: agent claimed 'user's instruction is UTC' (old project); economics cards offer NL/NO/FR rows for a site-less case (QA-041 pattern, I leave subsidy/waste open); chemical price once used non-recommended proxy row; approval card has no edit control.
- Old project S1 a0947848 (depth set to 3000 m, pressure question answered, run cancelled): abandoned; S5 temperature-follow, S9 chips, S7/S8 only observed.
- Bugs this session: QA-063 (verified), QA-065 (verified), QA-061 retest verified, QA-068 (verified), QA-069, QA-070 (to retest).
