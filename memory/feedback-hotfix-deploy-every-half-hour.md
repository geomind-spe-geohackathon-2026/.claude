---
name: feedback-hotfix-deploy-every-half-hour
description: Hotfix sessions deploy at every :00 and :30 UTC window on their own, with no hold by the coordinator (2026-11-05)
metadata:
  type: feedback
---

User, in Coordinator-III's chat, 2026-11-05 ~09:45 UTC: let the hotfix sessions deploy every half
hour. Each hotfix session deploys its finished, committed fixes at the next :00 or :30 UTC window
on its own; the coordinator does not hold a batch back (for example, waiting for a QA run to
finish). One deploy at a time (`/tmp/geomind-backend.lock`); a blocker may still go at once.

Extended by the user, 2026-11-05 ~10:00 UTC: deploy EVERYTHING that is ready at every half-hour
window: frontend, backend, and geomind/gemini releases too (local wheels), without waiting for a
separate release approval during this QA round. Knowledge data changes (cost-sources) are uploaded
with the deploy as well.

**Why:** fixes should reach production quickly; holding them slowed the round.
**How to apply:** never tell a hotfix session to hold a ready deploy; a running agent run resumes
after a deploy (QA-035).
