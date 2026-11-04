---
name: gemini-target-structure
description: Agreed target gemini package tree (2026-10-31 20:40, thread Gemini III): no core/ folder, core at top level, optional compiler, domains data/design/evaluate/analysis; not executed yet
metadata:
  type: project
---

Two concepts: domain, feature. Modelled on PyTorch (no core folder; compiler like torch.compile).

Tree (latest, 20:40):
- gemini/__init__: Module, Plant, Parameter, Inlet, Outlet, Output, Stream, Fluid, BRINE, WATER, simulate, replay, live, resume, run_once, Results, Dataset, Engine
- top-level folders (no base/): modules/ (module.py Module, declarations.py Parameter/Inlet/Outlet/Output, container.py ModuleList/Dict) {subsurface wells pumps treatment exchangers heating cooling power storage piping grids environment control} + get/names/check; plants (plant.py Plant, template classes, Doublet...; from_dict/validate/schema/get/names); physics; ops (math API, dispatcher, kernels python scalar + numpy arrays); runtime (settings(backend, precision, display_units, default_fluid), state); engine (eager runner, executor interface, chunks, checkpoint); run (Problem, Constraint, Assumptions, schedule, simulate, replay, live, resume, run_once, Results, Dataset); types, units, errors, _utils (registry.py, automatic via __init_subclass__)
- compiler (optional): graph (Tracer, Graph, passes, cache), compile, future native backends; self-registers (register_executor/register_backend); core never imports it
- data: from_csv, from_values, profile_schema, synthesize, legacy reader (read/write via from_*/to_* methods: gm.Problem.from_json, gm.Plant.from_dict/from_json, Dataset.from_<fmt>)
- optim (was design, renamed 20:53): size, minimize, sample, sensitivity; capabilities -> gm.plants.capabilities()
- evaluate: totals, capacities, report, compare, balance, constraints, capex, opex, lcoh, lcoc, lcts, co2, npv, payback
- analysis: calibrate, nodal, injectivity, pump_curve, corrosion, erosion

Rules: public gm top or gm.<folder>.<Name>; physics/ops/runtime sub-namespaces; run folders import none of compiler/data/design/evaluate/analysis (quality test); everything works eager without graph/compile; core foresees compiler; nothing problem-specific in code.
Dropped: core/base/registry/testing folders, word "core" (never say it), load_file, public register, design.apply.
API rule: every function takes only (plant, problem) [+ results]: gm.schedule(plant, problem), gm.simulate(plant, problem) (schedules inside), gm.optim.size/minimize/sample(plant, problem, ...), gm.evaluate.report(plant, problem, results). gm.Problem(demand, site, constraints=[gm.Constraint], assumptions=gm.Assumptions); gm.Problem.from_json(path). site keys = plant param paths, applied at run time without mutating plant.
Constraint: gm.Constraint(path, min, max, equals, over=each|sum|mean|max|min|duration, when); schedule enforces what it can, rest check-only; evaluate.constraints checks all. Replaces operating_time, Limits, fixed rules.
Assumptions (prices const or profile, co2_price, lifetime, discount_rate): schedule does cost merit-order per step (price/efficiency + co2_price*emission, efficiency from modules); missing price -> missing_value.

20:53 run_once -> gm.call (proposed, like torch functional_call; used in prompt). Order removed (rec used). 20:55 prompt prompts/gemini-structure-and-problem.md given; stubs size/sensitivity/capacities/report/compare/synthesize/capabilities -> next prompt. See [[feedback-io-naming]].
22:40 structure prompt done; fixes sent. Later: fluids into Problem.site; sourced prices.
23:01 fixes pushed: gemini refactor at 2453af1 (numbers same; call in modules/, legacy reader in plants/_utils). 23:10 wrote geomind prompt phases/geomind/follow-gemini-problem.md for Fatemeh (Brief -> gm.Problem, presets out of package into fixtures, tools on new API, optimize/sample wrappers). Next gemini prompt: build stubs + Results.to_frame naming + fluids into Problem.
Related: [[gemini-api-rules]], [[feedback-general-not-competition]], [[gemini-domain-folder-mapping]].
