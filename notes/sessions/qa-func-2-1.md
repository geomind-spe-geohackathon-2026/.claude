# Handover: qa-func-2 (generation 1) -> qa-func-2-II

Predecessor: qa-func-2, session_01J2V3UVVo1KkYNZFZvsvmoe (Opus). Handed over 2026-11-05 on
Coordinator-II's order (Sahand): successor runs on Sonnet.

## Role and rules

QA session for the FUNCTIONALITY of design and simulation, QA round 2 (HOTFIX round; you only
test and report; do not ask the user for the mode). Read and follow exactly:
`.claude/notes/qa-round-2/common.md` and `.claude/notes/qa-round-2/qa-func-2.md` (your brief,
the reference figures from the PDF/CSVs and scenarios qa-func-2-S1..S8, already written and
pushed in commit 3f843a4; the coordinator was told). Coordinator id: read `.claude/STATUS.md`.

## State

- No bug reported yet. Scenario status: none tested yet (the "## Status" section of
  qa-func-2.md is empty; fill it).
- Project created: "QA2 qa-func-2 base", id 4b318ee0-b410-4e37-8cf6-c835bc76d8c2, shared memory
  On, with the PDF and both CSVs as context files, chat:
  https://geomind.team/projects/4b318ee0-b410-4e37-8cf6-c835bc76d8c2/assistant/chat
  The first request is only drafted in the chat input (the New project goal); it was NOT sent.
  No agent run is running.
- Backend 1.1.53 at the time (read /api/v1/system/health again for every bug).

## agent-browser lessons (cost me time; not app bugs)

- Use `--session qa-func-2-II` (or reuse `qa-func-2`) and `set viewport 1440 1000` first; the
  default viewport is small.
- Login: read FIRST_ADMIN_EMAIL/PASSWORD from backend/.env into shell variables, fill
  `find label "Email"` / `"Password"`; never print them.
- Refs from `snapshot -i` go stale quickly; in dialogs prefer selectors: `#project-name`,
  `#project-memory` (values on/off), `#project-goal`, and upload to
  `"[role=dialog] input[type=file]"`. Plain `input[type=file]` hits the page's "Import zip"
  input (it gives "Request validation failed").

## Next steps

1. Open the chat above, turn auto-approve on, send the drafted request (S1), follow the run;
   answer agent questions as a user would from the PDF/CSVs only; note what is asked.
2. Test S2-S8 in order as written in qa-func-2.md; keep one status line per scenario there,
   commit and push (stage that file only).
3. Bugs via qa.py only; blockers/majors to the coordinator at once; an hourly short report.
4. At 75 % context hand over again (`.claude/session-refresh.md`), to qa-func-2-III.
