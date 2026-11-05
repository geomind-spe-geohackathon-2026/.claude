# functional-qa-simulation-I

Read `README.md` here (your row) and `../qa-round-2/common.md`. Your project: "QA3 simulation" (id in
STATUS.md once seeded). Test only your stage; report bugs with qa.py (reporter
functional-qa-simulation-I). Check every number against the PDF and CSVs.

## Scenarios

Reference numbers (from the CSVs and PDF): heating 365 daily means, peak 30.0 MWth (28 Jan), min
2.673, 111.67 GWh/yr (sum x 24 = 111,667.7 MWh); cooling peak 10.0 MWcool (19 Jul), 23.74 GWh/yr
(23,742.5 MWh), >0 on 219 days; reservoir 2500 m, 87 C (12 + 30 x 2.5), 250 bar(g), 200 mD; 1-3
doublets, 50-300 m3/h per doublet while active, brine cooling <= 40 K, pump 70 %, 330 daily steps
of doublet operation, supply 100 C heating, 20 C cooling. One doublet at 300 m3/h and 40 K cooling:
about 300/3600 x 1030 x ~4.0 kJ/kg/K x 40 = about 14 MWth (so three doublets give at most ~42 MWth).
Every scenario starts on the seeded "QA3 simulation" project (case + sized plants); one run at a
time; short requests; no earlier stage redone (a gap is reported, not repaired).

- **functional-qa-simulation-I-S1: simulate a sized plant for the whole year.** Steps: open the
  project, ask the chat to simulate the stored plant design over 2027. Correct: a run starts without
  more questions than the case needs; result covers 365 daily steps (doublet active at most 330);
  yearly heat delivered vs 111.67 GWh and cold vs 23.74 GWh shown with units; delivered <= demand
  on every day; no silent defaults (a missing value is asked for).
- **S2: results against the CSVs.** Steps: ask for yearly delivered heat, cold, unmet demand, peak
  delivered and the day of the peak. Correct: demand totals equal the CSV sums; peak days 28 Jan and
  19 Jul; delivered + unmet = demand per day; each number has a unit; figures in chat equal the
  Results page and the charts (daily series, 365 points).
- **S3: constraints and violations.** Steps: ask which hard constraints hold. Correct: per doublet
  flow within 50-300 m3/h whenever active (or flagged); brine cooling <= 40 K; pump efficiency 70 %;
  production = injection volume; supply 100 C / 20 C met or the shortfall reported per day; the count
  of active days <= 330; violations listed by day, with the amount.
- **S4: physics sanity.** Steps: ask for the producer temperature, thermal power per doublet at peak,
  pump power, gas rate and its use. Correct: producer ~87 C at 2500 m (or the chosen depth with
  12 + 30 x depth); thermal power per doublet <= ~14 MW at 40 K; gas = 0.8 Nm3/m3 x flow (300 m3/h
  gives 240 Nm3/h); CO2 share 20 mol %; pump power = flow x dp / 0.7 plausible; energy balance
  closes (heat out = flow x cp x dT).
- **S5: iterate on a violation.** Steps: ask to change one thing (for example 2 doublets instead of
  3, or a smaller peak flow), re-simulate, compare. Correct: the new plant version is saved, the
  result is new, the old result stays; the comparison names what changed and the effect on unmet
  demand; the agent explains why (checked against S2 numbers).
- **S6: honest limits.** Steps: ask a question the data cannot answer (for example hourly peak, or a
  year other than 2027). Correct: the agent says the files give daily means only / 2027 only, does
  not invent data, and offers what it can do.
- **S7: persistence and display.** Steps: reload the page, reopen the project, open Results and Runs
  and logs. Correct: results, chat, plant version and run record survive; token use of the run is
  shown; no console errors; a deploy at :00/:30 does not lose the run (QA-035).
- **S8 (variation): cooling-heavy and heating-only checks.** Steps: ask for the result for the
  summer only (Jun-Aug) and for the winter peak week. Correct: sums match the CSV for that window.

## Method (user rule, memory/feedback-qa-through-chat.md)

Every action is a chat request written like a user (S1 "simulate the plant for the whole year",
S5 "change to 2 doublets and simulate again", S8 "give me the summer result"); I answer the agents'
questions and approvals in the chat. Tabs (Results, Runs and logs, plant view) are used only to
check what the chat produced (S2, S7); a step the chat cannot do is filed as a gap bug. No form is
used for an action in any scenario.

## Status

- Scenarios written 2026-11-05 ~10:00 UTC; waiting for the coordinator's "go" with the project id (Knowledge guides first).
- 2026-11-05 11:20 UTC (PAUSED by coordinator): project ef87f914-3aaa-4f58-be60-2d54c7687511, one chat. S1 done: totals equal the CSV sums (heat 111,667.68 MWh, cold 23,742.528 MWh, unmet none, 0 failed steps). S2 mostly done: peaks 30.0 MW 2027-01-28 and 10.0 MW 2027-07-19 right; geothermal 34,837.7 MWh vs boiler 76,829.96 MWh; active-days count not delivered (QA-125). S3 (constraints, question sent 12:10 chat time) was running at 65 steps when paused; read its answer first on resume. S4-S8 not started. Bugs: QA-125.
- 2026-11-05 ~11:45 UTC (round closed by Coordinator-IV): S3 finished, no run active or waiting, nothing to cancel. S3 result: heating supply 100 C always; d0 flow 341 m3/h on 2027-01-01 (> 300 cap) with verdict feasible = QA-132; brine cooling and active days not checkable (QA-125, 84 steps). S4-S8 not run. Bugs: QA-125, QA-132.
