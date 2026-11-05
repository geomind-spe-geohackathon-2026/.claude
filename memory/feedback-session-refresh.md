---
name: feedback-session-refresh
description: Every session hands over to a fresh successor (<name>-II, -III) at 75% context; follow .claude/session-refresh.md
metadata:
  type: feedback
---

Fatemeh, 2026-11-04 21:10 UTC: sessions must refresh automatically. When a session's context nears 75 %, it opens a new session with the next name (Coordinator -> Coordinator-II -> Coordinator-III; hotfix-back-II; qa-3-II) and moves the important parts of its context to it. This holds for the coordinator, the hotfix sessions and the QA sessions.

**Why:** long sessions get slow, expensive and forgetful; a fresh one with a handover note keeps the work going.

**How to apply:** check `get_session` (`context_usage`) at the start of every piece of work; at 75 % follow `.claude/session-refresh.md`: commit and push, write `notes/sessions/<name>-<n>.md`, `create_session` the successor on the Dell bridge, tell the coordinator, stop. See [[feedback-write-shared-context]].


Changed by Sahand 2026-11-05 ~09:50 UTC: the threshold is 300,000 used tokens of context
(`context_usage.used_tokens >= 300000`), not 75 %; every session, the coordinator included.
