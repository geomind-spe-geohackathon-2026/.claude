---
name: gemini-branch-rule
description: Branch naming for gemini agreed 2026-11-01 13:56 (refactor -> dev, feature/fix/docs prefixes); geomind/backend stay on main
metadata:
  type: project
---

Sahand 2026-11-01 13:54-13:56: `refactor` is a bad name; rename all gemini branches.
Agreed scheme (gemini only; geomind and backend keep working on main, "not important"):
- main = stable (competition delivery, releases); dev = development line (replaces refactor).
- feature/<name>, fix/<name>, docs/<name> branched from dev, merged into dev, then deleted. No dev/<name> (git cannot hold dev and dev/x).
- Coordinator worker branches/worktrees local only, never pushed.
- speed deleted after merge, tag archive/speed.
Prompt: /mnt/project-files/prompts/gemini-branches.md, run AFTER the blockers session pushes. GitHub default branch -> dev must be set by hand.
**How to apply:** after the rename, every new gemini prompt uses dev and a feature/fix/docs branch, not refactor. Supersedes the "gemini keeps its branch (refactor)" note in MEMORY.md.
15:03 DONE: origin has only dev (b8d0282) + main; tag archive/speed=8fbe403; AGENTS.md Branching rewritten (a28a93e); inputs/examples/hackathon_2027 -> hackathon_2026 (data files + case time still 2027). Repo moved: git@github.com:geomind-spe-geohackathon-2026/gemini.git (origin URL on Mac still old). CONTRIBUTING.md:23,25 still says branch from main (fix in next prompt). hackathon.py 529 s; 11 one-second budget tests fail under load.
15:07 Sahand wanted study work on dev/study (impossible: dev exists) -> wrote prompts/gemini-study-fixes.md on feature/study: 1 ESP out-of-curve fails / injection negative head = 0 power; 2 size backup policy arg no default; 3 Comparison Quantity; 4 uncertainty in case + sample/sensitivity read it; 5 fast study (no pandas lcts, apply_case once, ESP depth/pipe numeric, parallel trials via runtime.settings); 6 CPU-time budget tests + CONTRIBUTING; 7 examples/docs.
15:20 Sahand: geomind needs must be met by OUR general gemini design first. Extended prompts/gemini-study-fixes.md: size pump rating (share<=1) + feasible start with notes (3 mK cooling miss), report.to_dict(units), gm.evaluate.failures, to_dict on every result, remove plants.example stub, parameter descriptions + missing_parameters for agents. geomind old->new API table: notes/geomind-to-gemini-dev-mapping.md (geomind main 2964c69 broken on dev).
17:26 STUDY DONE: dev 3cec98b. size(backup=peak|none), pumps rated full duty, last chiller rated whole peak (3 mK cause: adsorption map), uncertainty in case (6 values), trial 0.155 s, simulate 0.10 s, hackathon.py 158 s (procs=8), failures(), to_dict everywhere, 370 descriptions, stubs removed. Open: slow golden replay.csv.gz stale; leftovers Plant.from_legacy+legacy folder, gemini/data/legacy, Plant.validate vs gm.plants.validate; ESP low suction -> gas volume blowup (needs general intake-pressure constraint).
17:41 leftovers done: dev cca153b (from_legacy, legacy folders removed ~1400 lines, scripts/legacy/ for tests; Plant.validate removed -> gm.plants.validate(plant.to_dict(structure=True)); golden regenerated). Sahand's .venv on Mac points at old crust-team path -> recreate.
17:52 wrote prompts/gemini-correctness.md (feature/correctness): 1 Quantity in set_params/call/Stream/Fluid (phase 2), 2 remove ~70 module defaults (constants allow-list, None switches), 3 roles heat_output/cold_output/plant, 4 ESP intake_pressure + gas fraction as doublet role quantities (limits in case data), 5 report parts display units + validate(Plant), 6 examples/docs. Next after it: prices (DEA files), scan/state, multi units, multi-objective.
