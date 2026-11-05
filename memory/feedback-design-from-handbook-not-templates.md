---
name: feedback-design-from-handbook-not-templates
description: IMP-023 decided: no gemini sample plants as templates; agents design from handbook-plant-design in Knowledge (2026-11-05)
metadata:
  type: feedback
---

User, Coordinator-IV's chat, 2026-11-05 14:20 UTC: IMP-023 parts (a)-(c) rejected. The agents do
NOT start from gemini's six hackathon plant files as templates. The failing design path (QA-129,
IMP-023 measurements) is solved with `handbook-plant-design.md` in the global Knowledge: the
design lead and engineers read it by section (read_rag outline/section) and build, size,
simulate, check and optimize from it.

**Why:** the product is general; a sample-plant template would only fit the competition case.

**How to apply:** prompts and skills point to the handbook's sections (chapter 11 "Designing in
gemini", chapter 10 sizing/optimisation); never ship sample plant files as starting points.
Same day: QA-122 approved (read-only `project_designs`: backend part hotfix-back, geomind part
hotfix-python).
