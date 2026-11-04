---
name: gemini-topology-optimization-idea
description: Parked idea (Sahand 2026-11-03 17:40 +0100): optimize which gemini modules exist and how they connect, not just sizes; discuss later
metadata:
  type: project
  modified: 2026-11-03T16:40:39.238Z
---

Sahand wants study to optimize every module and connection (topology), not only parameter values. Today minimize keeps plant structure fixed (only range/options leaves vary; doublet count = separate searches); study compares listed plant files.
Proposed plan (not started, no doc written): (1) superstructure plant with all candidate units, each with present/absent switch (bypass, zero capex, dispatch skips it); (2) optional connections as option variables (series/parallel, routing); (3) two-level search: outer GA over valid structures (invalid combos rejected before simulation), inner current minimize on sizes. ~1 week; trial count grows a lot, so parallelism matters there. Additive API only.
Status: PARKED by Sahand ("keep it, talk later"); after app works end to end. Related: [[gemini-status-2026-11-03]].
Cheaper alternative (no gemini change): app/agent builds several structural variants (with/without peak boiler, heat pump...) from the plant catalog and passes them all in one study; gemini optimizes + ranks each (parallel since 0.5.14). In-gemini structure search = new feature (needs Sahand; version rule says stay 0.5.x).
Estimates (RC): 5 optional modules = 32 structures x ~40 trials ~100 s CPU (~15-20 s with 8 procs); 10 optional = 1024 -> outer search (GA) needed. Only engineer-sensible connection options, no free wiring. Effort 2-4 days; additive key in plant file ("optional"/options per module) + bypass per module.
2026-11-03 19:18 UTC: UNPARKED. 0.6.0 released + everyone told. Sahand wants GA for structure; "consult first, then start". Proposed: superstructure plant file with "optional"/"choices" (bypass when off), typed ports + plant.check reject invalid before sim, suggest repairs; mixed single-level GA (structure+capacity genes, ~40x faster than two-level), polish top 3 with minimize; objective LCTS+CO2 via NSGA-II (own small impl, no pymoo); API gm.study.evolve + study.json method "evolve", additive -> 0.6.x; budget pop 40 x 25 gen ~15-25 s on 8 cores; first superstructure = union of 6 hackathon plants; 2-3 days. Awaiting his answers; then send exact file format before coding.
2026-11-03 ~19:15 UTC: DONE in gemini 0.6.1 (thread GEMINI II). Search is within a superstructure only (optional modules + choice groups + doublets + ranges/options), no free wiring or catalog search. Peak boiler not yet optional (GasMakeup has no bypass pair).
