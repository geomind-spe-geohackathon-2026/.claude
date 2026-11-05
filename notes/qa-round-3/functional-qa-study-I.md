# functional-qa-study-I

Read `README.md` here (your row) and `../qa-round-2/common.md`. Your project: "QA3 study" (id in
STATUS.md once seeded). Test only your stage; report bugs with qa.py (reporter
functional-qa-study-I). Check every number against the PDF and CSVs.

## Scenarios

All actions are chat requests like a user would write them (answer the agents' questions and approvals in the chat); tabs only check what the chat produced, and a step the chat cannot do is filed as a gap.
Project "QA3 study" (case + plant + simulation results seeded). One run at a time, short requests, no evolve.
Reference numbers (CSVs): heating peak 30.0 MWth (28 Jan), 111.67 GWh/yr; cooling peak 10.0 MWcool (19 Jul), 23.74 GWh/yr. PDF caps: 1-3 doublets, 50-300 m3/h per doublet, brine cooling <= 40 K, pump efficiency 70 %, supply 100 C heating / 20 C cooling.

- functional-qa-study-I-S1 Plain study run. Goal: ask "run a study of the current plant over the year". Correct: the agent states which study kind and which plant version it uses, the run finishes, realised heating/cooling per day never exceeds the CSV demand, annual totals <= 111.67 / 23.74 GWh, hard caps respected, tokens shown in the agent log.
- functional-qa-study-I-S2 Size study. Goal: "size the doublet count and flow rate to cover the heating demand". Correct: doublets in 1..3, flow per doublet in 50..300 m3/h, brine cooling <= 40 K; peak 30 MWth covered or the shortfall named; result differs from the seed and says why; plant gets a new version.
- functional-qa-study-I-S3 Minimize study. Goal: "minimize the cost (or gas use) while meeting at least 95 % of the heat demand". Correct: objective and constraint echoed back, optimiser history/iterations visible, final value better than or equal to the start, constraint satisfied; a missing cost value is asked or sourced, never defaulted.
- functional-qa-study-I-S4 Sample (uncertainty) study. Goal: "sample reservoir permeability 100-300 mD and 20 % demand uncertainty, 20 samples, show P10/P50/P90 of delivered heat". Correct: sample count 20, P10<=P50<=P90, ranges as asked, no run beyond the asked count.
- functional-qa-study-I-S5 Sensitivity study. Goal: "which inputs matter most for delivered heat: depth, flow, supply temperature, heat pump COP". Correct: one-at-a-time or ranked result, sign and size of effects match physics (more flow and depth give more heat; delivered heat capped by demand), ranking explained.
- functional-qa-study-I-S6 Bad requests. Goal: ask outside the caps (4 doublets, 400 m3/h, 60 K cooling) and an evolve/structure search. Correct: the agent refuses or clarifies with the PDF limits and states evolve is not available; nothing silently clamped.
- functional-qa-study-I-S7 Study management. Goal: ask in the chat to stop and then continue a running study, restart after a deploy, ask the chat for the finished study's results again; then check the Runs tab only to compare. Correct: statuses true, results survive, no duplicate runs, Runs and logs match the chat.
- functional-qa-study-I-S8 Follow-up. Goal: after S2 change the case (e.g. new supply temperature) and ask for the next step. Correct: the agent warns that the study is outdated (case_changed_after_study) and suggests rerunning.

## Status

Project id 7a852d89-dfe5-423c-980a-a4ca231353bc. Browser session `functional-qa-study-I` (logged in). Paused by the coordinator at 11:17 UTC.

- S1 done (backend 1.1.84): chat run, heat 111,667.68 MWh, cold 23,742.53 MWh delivered = CSV demand, 365 steps, 0 failed. Notes: Overview keeps Study and Results "Out of date" after the run (seeded state too; not filed yet, check whether by design, QA-092); KPI "cop 12.2" is heat/electricity, not a COP; gas_bought 65,189 MWh < boiler_heat 76,830 MWh (co-produced gas?) unverified.
- S2 in progress, stopped: chat "Now run a sizing study ..." in the first chat; ~20 approval cards (QA-121). Agent found study/sized2 = 3 doublets x 300 m3/h feasible; a pending "Set ranges" card (design/ranged3 -> ranged_2d, doublets 1-2) is waiting for my approval. On resume: approve it, wait for the final answer, check it against 30 MW peak and caps.
- S3-S8 not started.
- Side task for the coordinator (LCTS rerun in SPE GeoHackathon 2026): failed at creation, 'plant has no doublet' for plant v3; reported, moved to hotfix-back-II.
