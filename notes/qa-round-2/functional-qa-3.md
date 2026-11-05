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

(write them here before you test)
