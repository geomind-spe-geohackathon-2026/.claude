---
name: feedback-fatemeh-bugs-first
description: Bugs Sahand or Fatemeh report themselves (chat, screenshots, their own QA session) always come first in every hotfix queue, above bugs found by QA threads (2026-11-05)
metadata:
  type: feedback
---

User, in Coordinator-IV's chat, 2026-11-05 14:15 UTC: bugs Fatemeh reports come first.

**Why:** Fatemeh tests the live app herself; her findings decide what users see.

**How to apply:** the coordinator routes each Fatemeh bug to the hotfix session of its area at
once and puts it at the TOP of that session's queue, above every other bug and IMP item,
whatever its severity. A hotfix session finishes only the step it is in, then takes the
Fatemeh bug next. Her session: session_01J2V3UX7XrrTa9jKv7ZTh9a ("Fatemeh QA", renamed "Manual QA"); now Manual QA-II session_01J2V3UYeTzFtZEuQJvkuadd.

Extended by Sahand, 2026-11-05 17:01 UTC (Coordinator-V's chat): bugs that Sahand or Fatemeh send
themselves ALWAYS get the highest fix priority, above everything the QA threads (QA-E2E-*, QA-AI-*,
Manual QA) and tasks (QA-150 ...) file. The coordinator files them with qa.py (reporter "Sahand" or
"Fatemeh"), severity at least major, routes them to the hotfix thread at once, and tells it to take
it next.

Sahand, 2026-11-05 18:16 Trondheim (in Manual QA-IV's thread): bugs that Manual QA-IV (Fatemeh's QA
session and its successors) finds have the same top tier as bugs Sahand or Fatemeh send.
