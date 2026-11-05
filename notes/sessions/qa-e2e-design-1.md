# QA-E2E-design-I handover (2026-11-05 19:40 UTC)

Role: QA-E2E-design-I, row "QA-E2E-design-I" of `documents/project/plans/qa-round-e2e-ai.md`.
Mode: hotfix; change NO code, only test and report with `documents/project/quality-assurance/qa.py`
(README there). Live runs, browser and LLM use allowed for this thread (memory/feedback-no-tests-now.md).
Chat with Sahand in Persian, times in Trondheim time (CET) in chat, UTC in files. Never stop after
a bug: file it and go on (plan "Never stop"). Poll run state at most every 5 s (QA-217); I used 15 s.
Projects: name `QA-TEST QA-E2E-design-I <n>`, keep them, never touch other threads' projects.

Tools: agent-browser `--session qa-e2e-design-I` (logged in as the admin from backend/.env; never
print the password). Approve a card with a DOM click:
`agent-browser --session qa-e2e-design-I eval "(()=>{const b=[...document.querySelectorAll('button')].find(x=>x.textContent.trim()==='Approve'); if(!b) return 'none'; b.click(); return 'clicked'})()"`.
API helper scripts were in the old session's scratchpad (setup.py login, load.py loads
`gemini/examples/hackathon_2026/case.json` + `data/demand.csv` + `economics.json` into a project:
POST /design/case first, then POST /design/case/files twice).

## Done

- Projects: 1 f1704a61-f1b8-4b63-84d3-20bd30beaed7, 2 72df9c82-e577-4605-8743-ffcee53c3a73,
  3 d555740a-1054-4642-b905-4919d36702a7 (reference case v3 in each).
- Rounds 1-5 (runs 76d19df6, dca5ed1a, 365bcbd3, 06fd16f0, e3c10ff9); report
  `documents/project/quality-assurance/reports/QA-E2E-design-I-2026-11-05.md` (rounds 1-4 written;
  add round 5) and the SCENARIOS.md row "E2E-design".
- Filed: QA-169, 171, 172, 223, 225, 226, 229, 231, 241, 246, 260, 329. Evidence added to QA-230,
  QA-254, QA-287, QA-250, QA-212.
- Verified: QA-169, 172, 246, 247, 251, 253, 287. Reopened: QA-223 (what-if stored as its own
  design still becomes the Results row), QA-250 (first full-year simulate fails until the well
  segments are set), QA-212 (5 patches), QA-260 (patch size.doublets stays 1; size_plant ignores
  range 3-3).
- Round 5 (run e3c10ff9, 19:15-19:31 UTC, 4.43 M input tokens, 0.097 USD): 1/2/3 doublets
  compared, all feasible, LCTS 37.49 / 37.82 / 42.48 EUR/MWh; third doublet ran at 50 m3/h while
  the answer says "each at 300 m3/h"; no approval cards at all (QA-329).

## Next, in order

1. Add round 5 to the report and SCENARIOS row; commit and push documents.
2. Coordinator's list (19:34 UTC): retest QA-221 (verified by others) only if a new run shows it;
   new scenarios from the browser: "design a plant with 3 doublets and no heat pump" (new project 4),
   then a cooling-only case (copy case.json, remove demand.heating, load it by the API).
3. Retest QA-329, QA-223, QA-260, QA-250, QA-241, QA-171 when they are set fixed.
