---
name: gemini-workspace
description: "Where gemini library work happens on the NTNU Dell, and how it relates to the app's checkout"
metadata:
  node_type: memory
  type: project
  originSessionId: 7fbc507a-e070-59e2-997c-57769fc75858
  modified: 2026-11-04T01:26:59.737Z
---

Since 2026-11-04 (evening): `gemini/` in the project root is the one gemini clone, on `dev`, gemini's default branch; hotfixes push to `dev` only. No worktrees. Before that, gemini work ran in `gemini-work/` beside the app's checkout `gemini/`. The Mac is retired.

**Why:** the coordinator said to keep gemini work out of the app's checkout. The two share one git object store, so a fetch in either is visible to both, and one branch cannot be checked out in both at once.

Sahand's rule (2026-11-02): the gemini thread changes no other repo. What another repo needs goes to that repo's thread as a note, and only once Sahand says to send it.

**How to apply:** as of 2026-11-03 the worktree is detached at origin/dev (55235d7, 0.5.5, tag v0.5.5) and local `dev` matches it. Full fast suite baseline: 8229 passed. `gh` is not installed and anonymous GitHub API calls are limited to 60 an hour; the public run page shows annotations, and job logs need a login. To read a CI failure, emit `::error::` lines on a throwaway branch. `examples/hackathon.py` makes no LLM calls, so rerunning it uses no tokens.

Sahand's rule (2026-11-03): gemini is the source of truth. Nobody asks gemini for anything without his permission; a missing gemini feature goes on a list for him to review and approve, never directly to gemini.

As of 2026-11-03 night: local dev is f81eefc2 (0.5.6 merged, 4 ahead of origin, tag not made). `git push` to dev and any branch carrying that merge is refused by the auto-mode permission check; Sahand must push or add a rule. Waiting locally: fix/stale-tests 5c600859, feature/faster-trials 3e2bd5e1 (stacked on it), docs/repo-layout aa5b2cb8 (on dev). Origin still holds throwaway fix/ci-debug-lowest. Moving this worktree under gemini/.tmp was refused too. Test identifiers: a green Test run can land on runners without AVX-512; check `numpy.show_runtime` output per job before trusting it.

2026-11-03 (Sahand): speed has its own lasting branch `feature/speed`, rebased on dev each time work starts; each measured, CI-green gain merges to dev at once as a 0.5.x patch release; more important tasks go on dev and speed resumes after. Released by then: 0.5.6 to 0.5.10, main = dev = 373e27a6. Pushes to dev/main work since Sahand said "push it yourself".

2026-11-03 noon: gemini frozen after 0.5.13 (time_zone) except bug fixes and critical items. Urgent fixes: fast tier + lint locally, merge straight to dev; the Release workflow's tests are the gate. CI tests Python 3.12 only during the hackathon (others commented out). Open after the hackathon: the Test run on main for 0.5.13 failed only on Python 3.11 lowest-direct, cause unknown (logs need a login).

2026-11-04 ~02:30 local: gemini 0.6.2 released (main = dev = 70fa57e5): evolve tuned to an acceptance bar (scripts/validate_evolve.py), set_bypass, gm.plants.union, app requests 13-21, ice_storage. Handover for the next session: gemini-work/.tmp/handover/GEMINI_III.md.

2026-11-03 19:10 UTC: gemini 0.6.1 released (structure optimisation: Plant.set_optional/set_choice/structures/with_structure, gm.study.evolve GA/NSGA-II, study.json method evolve, examples/evolve.py + examples/hackathon_superstructure/); main = dev = 63bdf4c8. The e2e example tests run examples without PYTHONPATH, so in a worktree they import the shared .venv's gemini (gemini-work): verify a new example in a scratch venv with the build installed. Installing a wheel straight from a URL with pip was refused by the permission check; download with curl, then pip install the file.

2026-11-03 (Sahand): ranking port suggestions by learning or usage statistics belongs in geomind, not gemini; gemini keeps only the rule-based Plant.suggest (0.6.0).
