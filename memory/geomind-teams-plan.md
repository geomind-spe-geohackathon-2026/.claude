---
name: geomind-teams-plan
description: "Agreed GEOMIND II team layout (2026-11-03); not started until Sahand says \"start\""
metadata:
  node_type: memory
  type: project
  originSessionId: 3db29973-7824-5bbd-8292-d9adf25ff607
  modified: 2026-11-03T16:08:28.129Z
---

Agreed with Sahand on 2026-11-03 in the geomind thread (moving to a new thread "GEOMIND II"). Do not start until he says "start".

- Teams, each with a lead; folders `geomind/agents/<team>/<one-word>/{agent.py,prompt.md}`, tests mirrored; class names stay full (ProjectLead, CaseLead, ...); import stays `gd.agents`.
- project/: lead (ProjectLead, a model, code guards kept), coordinator, reviewer (Verifier renamed, knowledge only), explainer (knowledge only).
- case/: lead (CaseLead = Formulator renamed), geoscientist (new).
- design/: lead (DesignLead = Designer renamed, the reviewer of its team), process, integration, reservoir, well, energy; the last three fill params in parallel via patch_plant.
- analysis/: lead (AnalysisLead = Analyst renamed), economist. support/: summarizer.
- Removed: Assistant, CodeAssistant, FamilyDesigner, run_python, sandbox, write_module, test_module ("we don't write code").
- Every model agent has its own required GEOMIND_<NAME>_MODEL, no fallback.
- Order: renames/removals/folders → geoscientist → design team → ProjectLead → live test with replay → MCP → full run, release.

**Why:** Sahand wants the agents modelled on a real geothermal engineering team.
**How to apply:** follow this layout exactly; see [[gemini-api-freeze-0-5-x]] and [[package-release-plan]].
