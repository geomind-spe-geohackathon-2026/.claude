---
name: feedback-qa-round-2
description: Sahand's rules for QA round 2 (2026-11-04 ~23:50 UTC): agent-browser only, competition inputs only, functional flow first, OpenRouter spend not a limit, gemini may be edited
metadata:
  type: feedback
---

Sahand, 2026-11-04 ~23:50 UTC, to Coordinator-II:

- QA sessions write their own scenarios and test them: one session for UI/UX only, two or three
  for functionality only, with tasks that do not overlap.
- The functional flow matters most: chatting with the agents, the case, the design, the
  simulation, the economics, the scoring and the report. Not login or account basics.
- Use good models for the functional sessions; since 2026-11-04 23:45 UTC every QA session runs on
  Sonnet (claude-sonnet-5-5), Sahand's word.
- Browser tool: agent-browser (vercel-labs, `npm i -g agent-browser`, installed on the Dell) ONLY.
  No Playwright: its token cost is too high. Replaces Playwright in older QA instructions.
- Inputs: only the competition files (`gemini/examples/hackathon_2026/`: the requirements PDF and
  the two daily demand CSVs). No other data. The QA session writes the user's chat text itself.
- OpenRouter spend is not a limit: what matters is that the product becomes stable and really
  works. Replaces older spend caps for QA runs.
- gemini may and must be edited to fix its bugs (repeats [[feedback-decisions-2026-11-05]]).

**Why:** little time; the agentic pipeline end to end is what the jury scores.
**How to apply:** QA instructions in `notes/qa-round-2/`; never script Playwright for QA.
