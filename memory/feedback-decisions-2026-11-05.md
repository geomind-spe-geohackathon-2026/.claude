---
name: feedback-decisions-2026-11-05
description: Sahand's decisions of 2026-11-05 ~00:00 UTC: catalogue only sourced rows, gemini unfrozen, auto-approve in backend, features in hotfix mode, releases without his OK, rate limit stays high, automatic session handover
metadata:
  type: feedback
---

Sahand, 2026-11-05 (about 00:00 UTC), answering the coordinator's open decisions:

- Cost catalogue: rows without a source are REMOVED entirely; in their place find rows with a cited source, its year, converted to EUR (2015 prices, as the catalogue states). Applies to QA-045's three USD/FRF rows and every other unsourced row; QA-006's cited rows follow the same rule.
- gemini is NOT frozen any more: fix the gemini-side bugs (requests 33-38 in geomind `.claude/docs/plan.md`, QA-039, QA-049) in gemini itself. Replaces [[feedback-gemini-api-freeze]], [[gemini-api-freeze-0-5-x]], [[gemini-requests-need-approval]] and [[feedback-never-message-gemini-thread]] for the gemini changes the bugs need.
- QA-031: auto-approve stored per chat in the backend, so the backend approves with no tab open (option A).
- Development features (QA-011, QA-013/IMP-001, QA-047) are built now, in HOTFIX mode: there is little time.
- Releases (geomind, gemini, backend, frontend) go ahead without his approval from now on. Replaces [[geomind-release-on-sahand-word]].
- The prod API rate limit stays at 1000 for now.
- Session handover at 75 % context must be automatic, done by the sessions themselves with no help from him ([[feedback-session-refresh]]).

**How to apply:** act on these without asking again; record new state in STATUS.md.
