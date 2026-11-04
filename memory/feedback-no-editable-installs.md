---
name: feedback-no-editable-installs
description: Sahand project-wide rule 2026-11-02 22:44: no `-e`/editable/path installs; owners build+push packages to a registry, consumers pin released versions; geomind main=releases, dev=work
metadata:
  type: feedback
  modified: 2026-11-02T21:45:14.316Z
---

Sahand (2026-11-02 22:44 local): nobody may install packages with -e; everyone migrates ASAP. Each package owner builds and pushes to a registry; every consumer installs released versions. geomind: branch `main` = releases, branch `dev` = changes headed to main. gemini: always branch `dev`.
**Why:** editable path deps (e.g. geomind pyproject `[tool.uv.sources] gemini-geothermal-suite-open = { path = "../gemini", editable = true }`) make builds depend on local checkouts.
**How to apply:** every prompt: no editable/path sources; pin `gemini-geothermal-suite-open>=X,<Y` from the registry; geomind work on `dev`, release = merge dev->main + tag + publish; backend pins geomind/gemini versions. Registry name/URL: ask (unknown on 2026-11-02). Supersedes "geomind works on main" ([[gemini-branch-rule]]).
