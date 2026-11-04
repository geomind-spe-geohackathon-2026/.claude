---
name: qa-keep-test-projects
description: "On geomind.team QA passes, keep the QA-TEST projects; don't delete them at the end"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5b1d23f8-3a1e-5b89-93fc-460f0dbc02cd
  modified: 2026-11-03T11:45:32.824Z
---

On production QA of geomind.team, Sahand wants the QA-TEST projects left in place, not deleted during cleanup ("no, don't delete the project, leave it", 2026-11-03). On 2026-11-03 "QA-TEST chat" (f8cf4b68…) was kept; QA-TEST case and QA-TEST import had already been deleted.

**Why:** he wants to look at what the agents produced himself.
**How to apply:** skip project deletion in cleanup unless he asks for it. Still delete nothing that isn't a QA-TEST entity. See [[shared-clones-and-production]].
