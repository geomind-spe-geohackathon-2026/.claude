---
name: competition-judging-criteria
description: The organisers' slides (SPE Europe Energy GeoHackathon Express): Challenge 1 and 2 (50 % each), bonus, deliverables and the evidence the jury wants
metadata:
  type: project
---

From the organisers' kick-off slides (Pejman Shoeibi Omrani), shared by Sahand 2026-11-05:

**Challenge 1 (50 %): Agentic AI engineering workflow.** The workflow autonomously analyses the
problem, interacts with the GEMINI digital twin, selects and executes appropriate models,
identifies missing modelling capabilities and integrates additional calculations or tools where
necessary, compares alternatives, and explains the reasoning behind the final configuration.

**Challenge 2 (50 %): Integrated heating and cooling system design.** Deep geothermal energy for
direct heating and, where possible, to support cooling production. Select and size technologies
such as heat exchangers, heat pumps, sorption/absorption cooling, chillers, thermal storage or
auxiliary systems. Provide the realised heating and cooling capacities, the designed system, and
the interaction with the agent (prompts, answers, number of tokens used).

**Bonus:** multi-agent collaboration, automated optimisation, uncertainty analysis,
techno-economic assessment, automatic model generation, autonomous verification of the solution.

**GEMINI environment slide:** the agent accesses geothermal information and configures
simulations through GEMINI, runs calculations, compares configurations and operating strategies,
and identifies gaps and connects additional models, datasets or tools. "Missing models are part
of the challenge": teams may add simplified models or external tools and explain why they are
appropriate.

**Deliverables:** a technical report (max 5 pages) or presentation (max 10 slides) summarising the
geothermal assessment, system design and heating/cooling capacities, and documenting the agent
architecture, models and libraries; a video pitch (max 5 min) with the solution, key findings,
design choices, novelty and the main technical and/or economic results. Commit and push all
contributions to GitHub (merging into main not required). Evidence: provide the agentic system
and record the interactions (prompts, answers, token usage); explain the final configuration and
supporting calculations.

**How to apply:** QA and features are judged against this list; the agent log with tokens, the
calculate/run_python/web_search tools (gaps filled with explained extra calculations) and
geothermal-driven cooling are scored items. Inputs: [[competition-inputs]].
