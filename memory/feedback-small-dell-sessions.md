---
name: feedback-small-dell-sessions
description: Sahand 2026-11-03 23:50 UTC: do work in fresh small Claude Code sessions on the NTNU Dell to keep token use low; threads only coordinate
metadata:
  type: feedback
  modified: 2026-11-03T23:51:21.994Z
---

Sahand (2026-11-03 23:50 UTC, gemini thread, relayed to all threads): as far as possible, do the work in fresh, small Claude Code sessions on the NTNU Dell (Remote Control), not in the long cloud thread sessions, so token use stays low.

**Why:** long thread sessions carry big contexts and cost many tokens per turn.

**How to apply:**
- Keep the thread session for coordination, merges and releases.
- Start each piece of work in a fresh Dell session with a short brief.
- After each piece, write a short handoff note to /mnt/project-files/<area>/ and start the next piece fresh.
- The frontend repo on the Dell is under /home/fatemec/geomind-spe-hackathon-2026.
- Related: [[feedback-no-pull-requests]], [[hosting]].
- gemini: handover file gemini-work/.tmp/handover/GEMINI_II.md; RC session ended after each release, new one started.
- CPU CAP (Sahand 2026-11-04 00:14 UTC): never take the whole Dell; use ~75-80% of CPU max (limit worker processes/pytest -n/pools, run heavy jobs one at a time, nice long runs); leave the rest for other threads.
