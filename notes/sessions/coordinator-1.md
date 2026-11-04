# Coordinator, generation 1: state at handover (2026-11-05 ~00:10 UTC)

Facts for the next coordinator session. The rules themselves are in `.claude/AGENTS.md`,
`.claude/session-refresh.md`, `.claude/memory/` and `documents/project/ops/development-modes.md`;
the live state is in `.claude/STATUS.md`.

## Role (as Sahand set it on 2026-11-04 and 2026-11-05)

- The coordinator runs the QA and hotfix round on the NTNU Dell: it starts, messages, pauses and
  archives sessions with the Claude Code Remote MCP tools on the Dell bridge
  (`env_016GdNnRFgDJDikcqrVDEN8i`), routes new bugs to the hotfix session of their area, keeps
  `STATUS.md` current and reports to the user.
- The user is Sahand (he also writes as Fatemeh's account). Chat in Persian; files in English;
  short replies.
- Mode of the round: hotfix (decided; not asked again).
- Usage runs out fast: few sessions, no polling, one-line messages, archive stopped sessions.
- Sahand's decisions of 2026-11-05 are in `memory/feedback-decisions-2026-11-05.md`.
- He wants to discuss new features with the coordinator next.

## Sessions (2026-11-05 00:10 UTC)

| Name | Id | State |
|---|---|---|
| hotfix-front | session_01J2V3UYxh6obK4VSajGwZvk | frontend bugs QA-053, QA-048, QA-051; then QA-031's frontend part |
| hotfix-back | session_01J2V3UWh6RugyR1DAxrkNhH | QA-056 root cause (run row keeps a stale request), then catalogue clean-up (sourced rows only), QA-031 backend part |
| hotfix-python | session_01J2V3UVLj3VrnUPsEatss4J | QA-055, QA-050, QA-009, gemini requests 33-38 in gemini, then QA-011, QA-013, QA-047 |
| qa-1 | session_01J2V3UXnAof6WqpiA2JPxxG | S1 + S2, QA-037 live test |
| qa-4 | session_01J2V3UZkFGKUyXLCP3gYmk4 | S4 + S8 |
| qa-5 | session_01J2V3UVCHoDxQNsjwpBxtzH | S5 + S3, QA-010 live test |
| Coordinator (generation 1) | session_01J2V3UXGweG4JrR4wkEWtg9 | handed over; to be archived |
| qa-2, qa-3, qa-6, qa-7, qa-8 | archived | final reports in their bug and scenario lines |

Hotfix sessions deploy themselves with two calls (`cd <repo>`, then `scripts/hotfix_deploy.sh`).
Runs survive deploys (QA-035). New bugs: `qa.py list --status open`.

## Production (2026-11-05 00:10 UTC)

Backend 1.1.47 (geomind 0.4.48 local wheel, gemini 0.6.4), frontend 1.1.50. Models:
`deepseek/deepseek-v4.1-flash-1017`, provider `morph/fp8`. Prod `RATE_LIMIT_REQUESTS=1000` stays.

## Open with the user

- QA-006 proposed rows (`documents/project/quality-assurance/evidence/QA-006/proposed-rows.md`)
  now fall under his catalogue rule (cited rows only); hotfix-back adds them.
- New features: he will describe them in the chat.
