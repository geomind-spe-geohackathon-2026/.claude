---
name: feedback-times-trondheim
description: In chat with Sahand give every time in Trondheim local time (Europe/Oslo, CET = UTC+1 in winter), not UTC
metadata:
  type: feedback
---

Sahand is in Trondheim (2026-11-05): in chat, give times in his local time, Europe/Oslo (CET,
UTC+1 until the end of March; CEST, UTC+2 in summer). Files, STATUS.md and commit messages keep
UTC as before. Deploy windows at :00 and :30 UTC are the same minutes in Trondheim.

**Why:** he reads the chat in local time; UTC made him convert.
**How to apply:** `TZ=Europe/Oslo date` before writing a time in chat.

Repeated by Sahand 2026-11-05 18:14 Trondheim ("tell everyone to give times in Trondheim time"):
EVERY thread and session, in every chat message, gives times in Trondheim time (write "Trondheim"
or "CET" after it), never UTC. Many threads still wrote UTC.
