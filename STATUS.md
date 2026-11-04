# Status: read first, keep current

The short, current state every session needs. Read it at the start of every session. When any of
it changes, change it here at once (one line, with the UTC time), before you go on.

Last updated: 2026-11-04 20:15 UTC.

## Production (geomind.team, api.geomind.team, on the NTNU Dell)

- Backend 1.1.15 (deployed from 1d4da82; main now has docs-only commits after it): geomind 0.4.26, gemini 0.6.4, alembic 0014. Rollback image
  `geomind-backend:prev` = 1.1.14. Latest DB backup `~/geomind-backups/geomind-prod-20261104T192107Z.dump`.
- Frontend 1.1.33 (main 27c3a21 deployed; main now 351902d, test-only changes, not deployed).
- Agents: DeepSeek only, never a Claude model.

## Clones (project root, one clone each, no worktrees)

- `.claude` (this, agents) and `documents` (people) are repos too, on `main`; set up a machine with `.claude/setup.md`.

- backend, frontend, geomind, infrastructure on `main`; gemini on `dev` (its default branch).
- geomind still has 10 old worktrees under `geomind/.tmp/`, all synced; Fatemeh removes them.

## How we work now

- Mode: ask the user at the start of every session (development, production, hotfix);
  `documents/project/ops/development-modes.md`. Current mode of the last session: hotfix.
- QA: testing the live app; every bug in `documents/project/quality-assurance/BUGS.md` (QA-001 to QA-008 open,
  QA-007 blocker: ask_economics fails again and again).
- No file holds Persian text; chat with the user in Persian.
- Commit and push everything when a piece of work ends.

## Open decisions (waiting for the user)

- None.
