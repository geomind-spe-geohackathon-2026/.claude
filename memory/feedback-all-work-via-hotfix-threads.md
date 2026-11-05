---
name: feedback-all-work-via-hotfix-threads
description: Every piece of work (bug, speed, parallelism, accuracy, handbook) is filed as a bug or task with qa.py and handled by the hotfix threads; no special worker threads
metadata:
  type: feedback
---

Sahand, 2026-11-05 16:51 UTC (Coordinator-V's thread): whatever it is, it is reported as a bug or a
task (qa.py, `documents/project/quality-assurance/`) and the hotfix threads (hotfix-python,
hotfix-back, hotfix-front) handle it. The coordinator does not start special worker threads for
speed, handbooks etc. Tasks use the title prefix "Task: " (e.g. QA-150 speed, QA-151 handbook-design).

**Why:** one queue, one owner per area.

**How to apply:** QA threads only test and report; the coordinator files tasks with qa.py and
routes them; hotfix threads take them with `qa.py next` by severity.
