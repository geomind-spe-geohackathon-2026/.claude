---
name: gemini-pure-forward-update
description: Saved task (2026-11-01 13:44, Sahand): make every gemini module a pure forward(inputs, inlets, state) + update for stateful modules; prompt to be written later on request
metadata:
  type: project
  modified: 2026-11-01T13:44:27.377Z
---

Sahand asked to keep this task and give its prompt LATER (when he asks). Agreed in discussion 2026-11-01 13:25-13:42.

Decisions:
- Plant STAYS a subclass of Module (Sahand 13:26: do not split them).
- Every module: `forward(self, inputs, inlets, state) -> (outputs, outlets)`, pure: nothing written to self, outputs returned (removes assign_outputs-style helpers, ~44 places), time-varying inputs (Control/Boundary: setpoint, measurement, frequency) come in `inputs`, not read from self.
- `self` holds only design parameters (set via set_params before a run, fixed during it).
- Stateful modules (6 on refactor ab9e754: PIDController, thermal/ice/aquifer storage, boreholefield, thermaldecline) add `update(self, inputs, inlets, outlets, state, dt) -> state` (today's private `_advance_states` made public and pure). Stateless: state = {} and no update. Initial state from `State(..., initial=...)` declarations.
- No structural None for "first step" (PID previous_error/previous_step None -> 0, previous_step=0 means no step yet) so compiler can trace; today PID is a graph break.
- Plant implements forward/update once for its graph (user never writes plant forward, like nn.Sequential); plant state = nested dict of children; nested Doublet unchanged.
- Engine/compiler: time loop as scan `state[t+1] = update(..., state[t], dt)` -> enables storage/ATES in schedule, multi-year; trials share one plant object, own state (no deepcopy).
- Remove module Parameter defaults while touching (no-defaults rule; ESP has 9, PID integral_time/derivative_time).
- Return keys checked against declarations (missing/extra key = error).
- Worked examples given in thread for PID and ESP (forward/update code + direct use + plant use).

Plan/caveats: ~70 modules + engine + compiler + health + tests; numbers equal 1e-9 before/after (like speed task); coordinator prompt with parallel workers. My advice: do after competition delivery; now only ESP depth + pipe path numeric and module defaults (in the study-speed prompt). Value: 8/10 for gemini, 2/10 for competition.
Related: [[gemini-status-2026-11-01]], [[feedback-coordinator-prompts]], [[feedback-no-defaults]].
