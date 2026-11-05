# functional-qa-3: studies, optimisation, uncertainty, agent tools, robustness

Model: Sonnet. Rules: `common.md` (inputs: ONLY the competition PDF and the two CSVs; agent-browser
only; bugs with qa.py, reporter functional-qa-3). Judging criteria: `memory/competition-judging-criteria.md`.

Own project "QA2 functional-qa-3 studies", competition files, auto-approve ON; get to a design
fast (do not test the case: functional-qa-1's area). Then test:
- Studies (page and chat): run, size, minimize ("Find the best design"), evolve ("Find the best
  structure"), sample ("Test the uncertainty"), sensitivity ("Rank what matters most"); results
  plausible against the PDF caps; progress, cancel, results pages.
- Compare structures (new, frontend 1.1.70/1.1.71, backend 1.1.66-1.1.68): from a done evolve
  study, the new tab lists up to 10 unique structures ranked; compare 2-3; Open and Save on every row.
- Agent tools (judging point 3, "missing models are part of the challenge"): calculate (sourced
  operands, constants, plain numbers need one sourced operand), run_python (sandbox, approval,
  outputs), web_search/read_web_page (English, short one-value queries, QA-071; values approved
  with source); each gap the agents fill is explained.
- Robustness: a run across a deploy (:00/:30 UTC) and a cancel, then "go on" (QA-070, QA-074,
  QA-047): no lost work, no silent narrowing of the brief, no run stuck at 0 tokens.
Not yours: the case and the main design loop (functional-qa-1), economics, report and logs
(functional-qa-2).

## Scenarios

Source of truth: PDF caps (1-3 doublets; max 300 m3/h, min stable 50 m3/h per doublet; brine cooling
<= 40 C; pump eff 70 %; heat 100 C, cool 20 C; reservoir 2500 m, 100 m, 30 C/km, 12 C, 250 bar(g),
200 mD) and CSVs (heat max 30.0 MWth on 28 Jan, 111.67 GWh; cool max 10.0 MWcool on 19 Jul, 23.74 GWh).
Project "QA2 functional-qa-3 studies", auto-approve ON. Status per scenario is kept one line each below.

- functional-qa-3-S0 Setup: upload both CSVs, one chat message with the PDF's brief (design a heating and cooling
  plant, 1-3 doublets), reach a simulated design. Correct: demand peaks 30.0/10.0 MW found, caps stated.
- functional-qa-3-S1 Study run + size ("size" study page and chat): sizes within caps, result plausible,
  progress shown, results page opens.
- functional-qa-3-S2 Minimize ("Find the best design"): objective shown, best design obeys all caps
  (doublets 1-3, flow 50-300 m3/h, dT<=40 C); progress and results consistent between page and chat.
- functional-qa-3-S3 Evolve ("Find the best structure"): finishes, structures ranked; progress/cancel work.
- functional-qa-3-S4 Compare structures tab (frontend 1.1.70/71, backend 1.1.66-68): up to 10 unique structures
  ranked; compare 2-3; Open and Save work on every row.
  Extra (Coordinator-II): Open AND Save a structure that is NOT rank 1 and not on the front (backend 1.1.69,
  gemini 0.6.6 structure_plant); report the result to the coordinator in one line.
- functional-qa-3-S5 Sample ("Test the uncertainty"): distribution, percentiles plausible, all samples within caps or
  violations flagged.
- functional-qa-3-S6 Sensitivity ("Rank what matters most"): ranking sensible (heat demand/flow/depth ...), stated in chat.
- functional-qa-3-S7 Cancel + progress: cancel a running study from the page and from chat; state clean; go-on works.
- functional-qa-3-S8 Agent tool calculate: ask for a derived value (e.g. reservoir temperature = 12 + 0.03*2500 = 87 C;
  hydrostatic pressure); operands sourced, plain numbers need one sourced operand, result in problem state.
- functional-qa-3-S9 run_python: ask for a missing model (e.g. thermal-storage or absorption chiller COP estimate);
  sandbox, approval asked, outputs shown, gap explained.
- functional-qa-3-S10 web_search/read_web_page: ask for a value not in files (e.g. absorption chiller COP); English
  short one-value query (QA-071), value approved with source.
- functional-qa-3-S11 Robustness: a run across a deploy (:00/:30 UTC) then cancel, then "go on": no lost work, no
  silent narrowing of the brief, no run stuck at 0 tokens (QA-070, QA-074, QA-047).
- functional-qa-3-S12 Variations: repeat S1-S6 with other wording / a changed brief (e.g. 2 doublets fixed).

## Status (final, 2026-11-05 ~09:30 UTC, backend 1.1.79, geomind 0.4.73; stopped by the coordinator, no new run)

Project "QA2 functional-qa-3 studies" 932b318c-f285-4827-aefe-c8fa3327735b, chat 510ab94f-c4f7-4019-9f75-cb40229b374e.
A design run (b01f2tbfn, started 08:27 UTC) is left as it is: it waits on a question card ("At least 100 C while
delivering" / keep exactly 100 C / adiabatic main).

- S0 setup: done with detours. Case built from the PDF and CSVs after about 8 question cards (time zone, air, return
  temperatures, economics, requirements change, dew point margin asked 4 times, CO2 intensity, indoor temperature and
  humidity, limits). The agents then reach a simulating plant (365 steps) meeting 6 of the 8 PDF caps; the two failing
  caps (heating exactly 100 C at the consumer, cooling exactly 20 C on 146 zero-demand days) are a requirement-semantics
  question the agent put to the user (good) - gemini should perhaps treat the supply caps as 'while delivering'.
- S1-S9, S12 (studies): BLOCKED by QA-092 (agent design never reaches the project Plant; Study 'Run the design'
  waits for 4 values, Results 'No results'). Not tested: size, find best design, test uncertainty, rank, evolve,
  compare structures (including the coordinator's non-rank-1 / off-front Open and Save check), cancel.
  Study UI seen: kinds Run the design / Find the best design / Test the uncertainty / Rank what matters most /
  Find the best structure; 'size' is a checkbox on Run; the study list loads, but once 'Loading studies' hung 30+ s.
- S8 calculate: not exercised. S9 run_python: works (sandbox, named inputs; two refused attempts: data literals and
  non-number JSON; then ESP head/power curve estimate stored). S10 web_search: guard works but QA-087 (39 searches for one
  value; fixed in 1.1.79, retest open).
- S11 robustness: run bd7aa40e failed after a deploy cut, 'go on' kept the case (QA-081, fixed 1.1.74/1.1.79, retest
  open); run 753645c0 failed with 'resume: request-1124 ... already answered' (QA-081 reopened, fixed 1.1.79, retest open);
  run eb7b95df cancelled after gemini 'internal' loops (QA-083).

Bugs filed: QA-081 (major), QA-083 (blocker), QA-087 (minor), QA-092 (major), QA-093 (minor). Also seen, not filed
separately: the same question asked again after the user said 'unknown' (dew point 4 times; QA-079 family).
Retests still to do: QA-081 and QA-087 on 1.1.79, QA-083 (1.1.75+).
