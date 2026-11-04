# Status: read first, keep current

The short, current state every session needs. Read it at the start of every session. When any of
it changes, change it here at once (one line, with the UTC time), before you go on.

Last updated: 2026-11-04 20:05 UTC.

## Production (geomind.team, api.geomind.team, on the NTNU Dell)

- Backend 1.1.16 (main 3f40ef2, deployed 2026-11-04 19:56 UTC): geomind 0.4.26, gemini 0.6.4,
  alembic 0014. Rollback image `geomind-backend:prev` = 1.1.15. Prod `.env` backup before the model
  switch: `~/env.backend.before-nemotron-*.bak`.
- Frontend 1.1.33 (main 27c3a21 deployed; main now 351902d, test-only changes, not deployed).
- Agents: every role on `nvidia/nemotron-3.5-super-vl:free` via OpenRouter since 2026-11-04 19:56 UTC
  (was DeepSeek); `GEOMIND_PROVIDER` empty, `GEOMIND_CONTEXT_WINDOW=200000`. Free tier: about 20
  requests a minute and 1000 a day. Never a Claude model.

## Clones (project root, one clone each, no worktrees)

- `.claude` (this, agents) and `documents` (people) are repos too, on `main`; set up a machine with `.claude/setup.md`.

- backend, frontend, geomind, infrastructure on `main`; gemini on `dev` (its default branch).
- No worktrees anywhere (removed 2026-11-04 20:30 UTC). Old local files: `~/geomind-archive/`
  (screenshots, QA screenshots of 2026-11-03, the old root git); DB backups `~/geomind-backups/`.

## How we work now

- Mode: ask the user at the start of every session (development, production, hotfix);
  `documents/project/ops/development-modes.md`. Current mode of the last session: hotfix.
- QA: testing the live app; every bug in `documents/project/quality-assurance/BUGS.md` (QA-001 to QA-014 open,
  QA-007 blocker: ask_economics fails again and again); ideas in `IMPROVEMENTS.md` (IMP-001 to IMP-009,
  QA-010 and IMP-006 need Sahand's decision).
- No file holds Persian text; chat with the user in Persian.
- Commit and push everything when a piece of work ends.

## QA round (started 2026-11-04 20:00 UTC)

- Coordinator: session_01J2V3UXGweG4JrR4wkEWtg9 (opens and closes the sessions, sends reports).
- Hotfix sessions: hotfix-front (session_01J2V3UYxh6obK4VSajGwZvk, frontend clone only) and
  hotfix-back (session_01J2V3UWh6RugyR1DAxrkNhH, backend, geomind, gemini). They claim bugs with
  `qa.py next` and deploy with `scripts/hotfix_deploy.sh` (one deploy at a time, a shared lock).
- QA sessions qa-1 to qa-8: one scenario each (`documents/project/quality-assurance/SCENARIOS.md`);
  they start once the Playwright system libraries are installed on the Dell.

## Open decisions (waiting for the user)

- None.
