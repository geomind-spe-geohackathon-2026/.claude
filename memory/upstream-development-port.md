---
name: upstream-development-port
description: Prompt for porting upstream GEMINI `development` into our `refactor` branch, and first-review findings
metadata:
  type: project
---

2026-10-29: user wants upstream `development` (simulator, DDT models) ported into `refactor`.
User said: only give a prompt (for local Claude Code), do not do the work here.
Prompt: /mnt/project-files/prompts/port-upstream-development.md (plan goes to .tmp/porting-plan.md).
First-review findings: refactor already has almost every upstream model (better ones). Missing/partial:
nodal well solve, CO2 emissions helper, heat-pump Lorenz COP + source-outlet floor, parallel-HX and
boiler/CHP examples. Upstream compressor power low by factor k.
Related: [[prompt-writing-rules]], [[project-status-handoff]].
2026-10-29 22:45: local Claude Code finished the analysis (.tmp/porting-plan.md, matched my findings). I advised: confirm; C4 (injector needs no pump) return None documented, zero pump power; Q1 nodal functions only via gemini.core.modules.plants.nodal; keep refactor models for conflicts; no tuning for well-model gap (135.93 m3/h ref). Local gemini/ was re-cloned at c2e4b9f (no venv); upstream clone at crust-team/gemini-legacy.
2026-10-29 23:31: port done locally, 7 commits on refactor (13ab520 Lorenz, 2b2300b min source outlet, fb2ec6a nodal, 03e335f emissions, 9ecad67/e852848 examples, 352f909 docs), not pushed. 5 pre-existing >1 s timing test failures. I asked for 2 checks before push: example 02 injection wellhead pressure 54.86 vs ~44 bar upstream; DNV erosion constant (code 3.15576e10 likely right).
2026-10-29 23:47: checks done (beca09e, a482155, 5813ac8): upstream injector friction sign is wrong (adds friction; gap 2x5.197 bar). Upstream injectivity 2.3 m3/h/bar was fitted with that error; correct refit from 44.47 bar at 125.1 m3/h is about 2.84 m3/h/bar. DNV doc constant is a typo. Told user to push and recalibrate injectivity in example 02.
