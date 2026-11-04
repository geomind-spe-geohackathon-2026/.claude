---
name: geomind-release-on-sahand-word
description: geomind releases only when Sahand says so; work collects on dev meanwhile
metadata:
  node_type: memory
  type: feedback
  originSessionId: 3aea9698-789f-59b6-93b1-7cd4178ef35d
  modified: 2026-11-04T12:59:48.195Z
---

Release geomind only when Sahand himself says so (2026-11-04: "don't release until I say; there may be more changes on the new version"). Collect work on dev as 0.4.24.devN, tests and the release profile green, and push dev; never tag or move main on my own or on a coordinator's word alone.

**Why:** more changes may come for the new gemini version; also the Dell's permission check refuses production steps (main, tags) unless Sahand asks in his own thread.

**How to apply:** after each piece: merge, push dev, report. A release needs Sahand's message in the thread; then main is fast-forwarded (--ff-only) to dev and tagged. See [[fresh-sessions-for-work]], [[package-release-plan]].
