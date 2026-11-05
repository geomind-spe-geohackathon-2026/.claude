# QA-E2E-case-I handover (2026-11-05 ~20:00 UTC)

Role: plan documents/project/plans/qa-round-e2e-ai.md, row QA-E2E-case-I (chat to a complete case, S1/S3/S6).
Hotfix mode, no code changes; live runs, browser and LLM allowed for this thread (memory/feedback-no-tests-now.md).
Chat with Sahand in Persian, times in Trondheim time (CET) in chat, UTC in files. Never stop after a bug:
file it and go on (coordinator rule). Poll runs at most every 5 s (QA-217), cache the login token.

## State

- Report: documents/project/quality-assurance/reports/QA-E2E-case-I-2026-11-05.md (rounds 1 and 2), SCENARIOS.md row E2E-case.
- Projects QA-TEST QA-E2E-case-I 1-12 on geomind.team, all kept (ids in the report).
- Project 12 (331bf443) run 3152a411 is stuck on QA-336 (economics question not shown). Leave it as evidence.
- Filed: QA-196, 197, 198, 199, 200, 203, 230, 243, 255, 286, 301, 304, 306, 318, 336. Reopened QA-085.
  Open/reopened at handover: QA-200, QA-301, QA-318, QA-336, QA-085; verified: 197, 198, 199, 230, 255, 286, 304.

## Tools (scratch, recreate if gone)

- agent-browser sessions named qa-e2e-case-<n> (one per project), viewport 1440x900; log in with
  FIRST_ADMIN_EMAIL/PASSWORD from backend/.env at run time (never write them down).
- A New project now asks "Turn on auto-approve for this chat?": answer No.
- Approve buttons sit inside a scroll box: scrollintoview the ref before click.
- The accessibility value of a number input is the raw number; check the screenshot before reporting display bugs.
- Run state: GET /assistant/runs?project=<id> (status, request), /assistant/runs/<id>/log, /design/case?project=<id>.

## Next

Retest QA-336, QA-318, QA-301, QA-200, QA-085 when fixed; then new inputs: hourly file with an offset, a file
with a stated time zone, a PDF only (no CSVs), and the economics answer of project 12 after QA-336.

## Update 20:33 UTC

- Projects 13 (PDF only, OK), 14 (QA-301 verified, 7 min), 15 (QA-318 reopened, cancelled) added; report has rows 10-13.
- Open now: QA-336 (stuck run 3152a411 still shows no card), QA-318 (repair_series gaps), QA-200, QA-085 fixed-not-retested.
- Waiting for the coordinator's word that Knowledge is cleaned (QA-340: hackathon brief removed, assumptions file cleaned);
  then rerun the competition case from the 3 organiser files and check case AND design are sound; put that clean run in the report.
- Driver: /tmp/claude-1000/qae2ecase/drive2.sh <session> <project> [free answer] acts on run.request (no stale page text).

## Closed 2026-11-05 20:57 UTC (Sahand: close the QA-E2E threads, may reopen later)

- Final: verified QA-085, 197, 198, 230, 255, 286, 301, 304, 318, 336 (199 verified by me, later set to fixed by its fixer);
  fixed not retested QA-196, 199, 203, 243; QA-200 fixing; QA-306 wont-fix.
- Runs of projects 16 and 17 cancelled at the close; projects 1-17 kept. The QA-351 knowledge-usage run was dropped
  (it needs Sahand's OK for LLM spend before it starts).
- On reopen: retest QA-200 (files-alone set_case refusals, still 4 in run 5c0ad032), QA-196, QA-203, QA-243, QA-199.
