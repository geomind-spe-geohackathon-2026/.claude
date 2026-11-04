---
name: ux-direction-agent-first
description: "GeoMind's first screen is chat and agents, with the manual pages kept; UX work is on branch dev in ux/frontend; agents always deepseek"
metadata:
  node_type: memory
  type: project
  originSessionId: 3c4d46b1-64f9-5b25-b8ce-9b0d98de26a8
  modified: 2026-11-02T20:29:36.500Z
---

On 2026-11-02 Sahand said the app has drifted too manual. The first screen should be chat: the user gives files (for example the competition PDF and CSVs) and says what they want, and the agents do the work and ask only when needed. He likes the Case, Plant, Study and Results pages and they must keep working for users who want to add or design by hand.

**Why:** the forms became the main path, which is not the original idea of the product.

**How to apply:** UX work happens on branch `dev` in the separate clone `ux/frontend`; `ux-agent-first` is fully merged into main. Do not touch the shared `frontend` clone for this. Agents always use deepseek, never Sonnet (Sahand's rule, 2026-11-02): set it explicitly on any agent run or config. The 22-item review is in https://claude.ai/artifact/TehS6XZQ7SUsNNdEYrFby5. See [[shared-clones-and-production]].

Since 2026-11-02 21:50 Sahand has paused all live agent runs and LLM token use until he lifts it: test agent work only with fake models.

From 2026-11-02: no `-e` installs of gemini or geomind anywhere; publish to the registry and pin released versions. geomind changes go to its `dev` branch, and `main` holds releases.

Branch rule from Sahand (2026-11-03, all repos): only `dev` and `main` stay. New work goes on `dev`, test on local servers, merge `dev` into `main` when tests pass, and `main` goes to production. Delete or tag other branches once merged.
