# QA-E2E-economics-I handover (closed 2026-11-05 ~20:50 UTC on Sahand's order)

Thread QA-E2E-economics-I (plan documents/project/plans/qa-round-e2e-ai.md, row "QA-E2E-economics-I"),
hotfix mode, test and report only, agent-browser against geomind.team. Closed by Sahand; may be reopened.

## State

- Report: documents/project/quality-assurance/reports/QA-E2E-economics-I-2026-11-05.md (rounds 1-4,
  timing and accuracy tables); SCENARIOS.md row "E2E-economics".
- 18 bugs filed: QA-181, 185, 186, 191, 192, 193, 194, 202, 256, 279, 280, 284, 298, 305, 319, 320,
  327, 349. Verified: all except QA-349 (fixed, geomind b68b884/7057fe2/42a884c, pending deploy at
  close, NOT retested) and QA-194 (I verified it at 19:29 UTC; BUGS.md shows "fixed" again after a
  later backend fix: retest).
- Projects kept (never delete): "QA-TEST QA-E2E-economics-I 1" .. "16" (admin account). No run active.

## How to go on (if reopened)

1. Retest QA-349: new project with the reference case.json minus economics (+ data/demand.csv) via
   API, chat "Fill in the economics yourself with your own best guesses, including the per-MWh
   operating costs and a subsidy; I don't want to be asked." Expect one ask_economics, 2-4 min,
   subsidy and per-energy open.
2. Retest QA-194: empty chat of a case without economics shows "Set the economics" first.
3. Tools I used (scratchpad, not kept): setup via POST /workspace/projects, POST /design/case
   (base null, content without economics), POST /design/case/files (multipart, base=1);
   agent-browser --session qa-econ; approval buttons sit in a scroll box: scrollIntoView before
   click; typing: `agent-browser type @ref` (fill does not enable Send). Poll no faster than 5 s
   (QA-217).
