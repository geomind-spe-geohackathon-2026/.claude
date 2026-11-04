---
name: cpu-budget-dell
description: "Use at most ~75-80% of the Dell's CPU; leave the rest for other threads"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 79f44894-62ce-5cab-9c31-1e512b813fd8
  modified: 2026-11-04T00:14:17.395Z
---

Sahand (2026-11-04 00:14 UTC): don't take all the Dell's resources; other threads and jobs need CPU too. Use about 75-80% and leave the rest free.

**Why:** the NTNU Dell (32 cores) is shared by several sessions and production; a validation run with 30 processes plus test runs pushed load to 138.

**How to apply:** all my jobs together at most ~24 cores: `--processes`/`-n` small (e.g. 16 for one heavy run, 6-8 for tests), never two heavy runs at once, `nice -n 10` on long jobs, tell subagents the same limit. See [[fresh-sessions-for-work]].
