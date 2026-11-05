---
name: feedback-general-not-competition
description: Sahand (2026-10-31, 2026-11-05): gemini, geomind and the Knowledge handbooks must be fully general; the hackathon is only one sample problem, never baked into code or handbooks
metadata:
  type: feedback
---

2026-10-31 18:30 and 18:48 Sahand, stressed as "very important": nothing in the design may be specific to the competition inputs; everything general so changed inputs cause no problem. The hackathon is just one sample input.
**Why:** organisers may change inputs; the solution must work for any brief/site/demand.
**How to apply:** in every prompt/design: no competition numbers, names (HackathonPlant, challenge_rules, hackathon profiles) or defaults in gemini/ or geomind code; the competition lives as a data file (e.g. inputs/examples/hackathon_2027/problem.json + CSVs) used by examples/tests only; case-dependent values passed via one Problem/brief object, missing -> clear error not hidden default; physical defaults only universal/cited; test on at least two different problems; quality test greps for hackathon/challenge. Related: [[gemini-api-rules]].
18:52 wrote notes/gemini-generality-audit.md (violations in refactor 33c7f52): challenge_rules, optim default, HackathonPlant, built-in hackathon profiles + paths.hackathon, ground.py 12C/30K/km defaults, physics docstrings citing challenge, daily-only schedule, template example sizes tuned to hackathon, site data mixed with design in inputs/plants, fixed injection pump setpoint, single-problem e2e; fixes: Problem object, design.size, problem.json, 2nd problem variant, quality grep test. backend/frontend not audited.
18:51 Sahand refined: competition data is ONLY for testing the code, not the basis of implementation, and not even the basis of gemini's design/structure. Only ensure what this input needs is supported. We design gemini ourselves. => e.g. Requirements must be generic constraints (path + aggregate + min/max), not fields mirroring the competition (operating_days, pump_efficiency...); competition = one test instance + a coverage test.
18:55 gave prompts/gemini-general-not-competition.md (only the generality fix; 9 sections): competition -> inputs/examples/hackathon_2027 (plant.json, rules.json, limits.json); remove challenge_rules, HackathonPlant, template competition example values, optim profile=None default (rules arg); no built-in profiles, add profiles.from_csv/from_values (any step); schedule any time step, operating_days -> operating_time + checks.operating_time; no competition defaults (gradient, surface temp, injection pump setpoint...); rewrite citations; quality grep test, competition e2e same numbers, coverage test, second problem (hourly, colder, 1 doublet). Generic Constraint design deferred to API discussion.
18:53 Sahand: gemini is the SOURCE OF TRUTH; inputs adapt to gemini (converted into gemini shapes outside gemini), never gemini to inputs; our design must be the best possible general form. Added to prompt section 0.
19:35 Generality prompt DONE on refactor (af803e4..ca04dea, unpushed): no hackathon/challenge in gemini/, quality test; examples inputs/examples/hackathon_2027 (plant.json, plant_with_treatment.json, rules, limits) + shallow_district (hourly, 1 doublet); coverage test 13 cases; operating_time; profiles.from_csv/from_values; template examples raise NotImplementedYet. Open: DEFAULT_INJECTION_PUMP_EFFICIENCY 0.7 unsourced -> told to make required, then push. Report again wrongly said geomind has no break: geomind main 2964c69 uses gm.profiles.get/names (cli.py:109-112, runs.py:62,95), spec_schema, from_template, operating_days, HackathonPlant in prompts -> geomind adaptation needed.

Handbooks (Sahand, 2026-11-05 17:06 UTC): the Knowledge handbooks (handbook-case, -design,
-economics, -report) are general textbooks on design and on how to do it in gemini, never
competition files. No competition numbers, limits or worked hackathon example inside them; every
competition fact or assumption goes in its own file (`hackathon-2026-assumptions.md`, case inputs).
Whatever the competition needs is taught as a real, general chapter or lesson, so the same books
solve similar problems. Do not overfit them to the hackathon.

Sahand, 2026-11-05 21:40 Trondheim: help the agents much more with GENERAL knowledge in the
handbooks (every lesson that helps them, as real general lessons), never with competition answers.
Everything a full run needs (case -> economics -> design -> simulate -> report) that the inputs do
not give must be in hackathon-2026-assumptions.md (known facts, organisers' answers, team
assumptions with sources), so agents never search for missing data. Agents read Knowledge by
section (outline first, then only the sections they need; QA-351), never whole handbooks.
