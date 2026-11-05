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

## Status

(one line per scenario)
- S0 .. S12: not started

