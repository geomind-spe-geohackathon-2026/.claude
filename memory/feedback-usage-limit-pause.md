---
name: feedback-usage-limit-pause
description: When the Claude usage limit gets close, the coordinator tells every session to finish its last step and pause, then resumes them after the reset (Sahand, 2026-11-05)
metadata:
  type: feedback
---

Sahand, 2026-11-05 ~01:45 Trondheim: when the coordinator sees the usage limit getting close
(`get_session` -> `external_metadata.rate_limit_info.status` no longer `allowed`, or a warning),
it sends every running session one line: finish the step you are in, commit and push, then pause
and wait. It writes "Usage pause: <time UTC>, sessions <names>" in STATUS.md. After the reset
(`rate_limit_info.resetsAt`, plus one minute) it tells each paused session to resume and clears the
line. A `send_later` at resetsAt + 1 min does the resume; re-schedule it when resetsAt moves.

Limits: only the coordinator's own `rate_limit_info` is visible (status and reset time, no percent,
nothing weekly); while the limit is hit no session, the coordinator included, can run a turn, so
polling every 5 minutes is not possible: the reset timer is the way back.

Standing cycle (Sahand, 2026-11-05 ~00:55 UTC): this repeats every 5-hour window until the whole
project works stably. The coordinator keeps exactly one pending `send_later` "usage-window check"
at the current resetsAt + 1 minute; each firing resumes paused sessions if allowed and schedules
the next one at the new resetsAt + 1 minute. At every piece of work the coordinator checks
`rate_limit_info`; when resetsAt has moved, it moves the check. A successor coordinator recreates
the check at once (a send_later belongs to the session that made it): note its trigger id in
STATUS.md.

**Why:** a hard stop mid-edit leaves shared clones dirty and runs half done.
**How to apply:** check `rate_limit_info` at each piece of work; act at once when it changes.
