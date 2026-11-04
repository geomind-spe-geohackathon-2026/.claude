# Status: read first, keep current

The short, current state every session needs. Read it at the start of every session. When any of
it changes, change it here at once (one line, with the UTC time), before you go on.

Last updated: 2026-11-04 20:22 UTC.

## Production (geomind.team, api.geomind.team, on the NTNU Dell)

- Backend 1.1.22 (main a35d668, deployed by the coordinator 2026-11-04 20:20 UTC): geomind 0.4.29 as a
  LOCAL wheel (QA-009 and QA-004 shipped; backend/.tmp/hotfix-wheels; requirements.txt still pins
  0.4.26), gemini 0.6.4, alembic 0014. Prod `.env` backups: `~/env.backend.before-*.bak`.
- Frontend 1.1.33 deployed; main has 1.1.37 (QA-008, QA-001, QA-005, QA-003) waiting for a deploy:
  the sessions' permission check refuses `scripts/hotfix_deploy.sh` for hotfix-front and hotfix-python.
- Agents: every role on `deepseek/deepseek-v4.1-flash-1017`, OpenRouter provider `morph/fp8` first
  (`GEOMIND_PROVIDER=morph/fp8`), since 2026-11-04 20:20 UTC; `GEOMIND_CONTEXT_WINDOW=200000`.
  Never a Claude model.

## Clones (project root, one clone each, no worktrees)

- `.claude` (this, agents) and `documents` (people) are repos too, on `main`; set up a machine with `.claude/setup.md`.

- backend, frontend, geomind, infrastructure on `main`; gemini on `dev` (its default branch).
- No worktrees anywhere (removed 2026-11-04 20:30 UTC). Old local files: `~/geomind-archive/`
  (screenshots, QA screenshots of 2026-11-03, the old root git); DB backups `~/geomind-backups/`.

## How we work now

- Mode: ask the user at the start of every session (development, production, hotfix);
  `documents/project/ops/development-modes.md`. Current mode of the last session: hotfix.
- QA: testing the live app; every bug in `documents/project/quality-assurance/BUGS.md` (QA-001 to QA-019; statuses there,
  QA-007 blocker: ask_economics fails again and again); ideas in `IMPROVEMENTS.md` (IMP-001 to IMP-011,
  QA-010 and IMP-006 need Sahand's decision). Run a61cfb19 was left `waiting` with no process after the 20:02 UTC deploy (QA-017).
- No file holds Persian text; chat with the user in Persian.
- Commit and push everything when a piece of work ends.

## QA round (started 2026-11-04 20:00 UTC)

- PAUSED (Fatemeh, 2026-11-04 20:30 UTC): the hotfix sessions wait for the coordinator's "resume";
  they claim, fix and deploy nothing until then.

- Coordinator: session_01J2V3UXGweG4JrR4wkEWtg9 (opens and closes the sessions, sends reports).
- Hotfix sessions (who fixes what: `documents/project/quality-assurance/README.md`):
  hotfix-front (session_01J2V3UYxh6obK4VSajGwZvk, area frontend, frontend clone),
  hotfix-back (session_01J2V3UWh6RugyR1DAxrkNhH, areas backend, data, infra, backend clone),
  hotfix-python (session_01J2V3UVLj3VrnUPsEatss4J, areas geomind, gemini; local wheels).
  They claim with `qa.py next`, take `/tmp/geomind-backend.lock` before editing the backend, and
  deploy with `scripts/hotfix_deploy.sh` (one deploy at a time).
- QA sessions (started 2026-11-04 20:11 UTC; instructions in `notes/qa-round-2026-11-04/`):
  qa-1 session_01J2V3UXnAof6WqpiA2JPxxG, qa-2 session_01J2V3UYuCFrxrXdWLCwzWro,
  qa-3 session_01J2V3UWmkUwP3g42jGxxz9g, qa-4 session_01J2V3UZkFGKUyXLCP3gYmk4,
  qa-5 session_01J2V3UVCHoDxQNsjwpBxtzH, qa-6 session_01J2V3UXM3DCMhq41Hx27eqV,
  qa-7 session_01J2V3UVMbdhwimT6VJxfNMq, qa-8 session_01J2V3UW8MS1wyUTdvJmh8UC.

## Open decisions (waiting for the user)

- None.
