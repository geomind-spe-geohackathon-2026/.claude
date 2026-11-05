---
name: feedback-force-stop-account-handover
description: On the user's word "force stop", the coordinator runs .claude/account-handover.md: every session stops, writes its note in .claude, and the work reopens on Sahand's account (2026-11-05)
metadata:
  type: feedback
---

User, Coordinator-IV's chat, 2026-11-05 ~18:10 UTC: Fatemeh's account usage is running out. When
the user says "force stop" (or hand over to Sahand's account), the coordinator at once runs Phase 1
of `.claude/account-handover.md`: every session stops where it is, commits and pushes, writes its
handover note in `.claude/notes/sessions/`, starts no successor; the coordinator writes its own
note and the reopen table. Sahand's account then reopens the same sessions per Phase 2.

**Why:** the work must survive the account switch with nothing lost.

**How to apply:** never start Phase 1 without the user's word; keep account-handover.md current
(running sessions in STATUS.md).
