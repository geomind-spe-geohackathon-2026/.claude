---
name: frontend-design
description: Frontend design thread (2026-10-30) state: proposal file, key recommendations, pending user answers
metadata:
  type: project
  modified: 2026-10-30T10:45:56.216Z
---

Thread "Design new React frontend" (2026-10-30). Brief: /mnt/project-files/frontend/brief.md. Proposal draft 1: /mnt/project-files/frontend/design.md (not yet agreed by Sahand; section 9 tracks contracts v18).
Key recommendations: shadcn/ui + own role-named tokens (incl. stream colours). Agent package is geomind (`import geomind as gd`); never write the old name in docs; Assistant first in sidebar; open project in URL prefix `/projects/{id}/<domain>/<feature>`; assistant as own page (side panel later); 3-column chat with run panel; flowsheet = generated diagram from gemini plant templates (free drawing in F3 on gemini JSON spec format 2, contracts v17; `layout` beside spec in v18), shared `PlantDiagram`; forms from JSON schema with react-hook-form + ajv; fetch-based SSE (EventSource can't send bearer); contract additions listed in design.md section 9.
F1 prompt is written only after Sahand says «go». Related: [[swarmax-architecture]], [[prompt-writing-rules]].
2026-10-30 12:45 Sahand rule: frontend prompts develop, commit and push directly on `main` (all repos except gemini); no feature branch, no PR.
