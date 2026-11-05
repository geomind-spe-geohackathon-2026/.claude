# hotfix-python-4 handover (2026-11-05 ~15:15 UTC)

You are hotfix-python-V, the successor of hotfix-python-IV (session_01J2V3UZqdULpCLT7XEFdd6t).

## Role and mode

Mode: HOTFIX (decided; do not ask the user). You fix the QA bugs and IMP items of the Python
packages geomind and gemini (areas geomind, gemini) and build IMP-025 in geomind. The coordinator
is the one in `.claude/STATUS.md` (Coordinator-IV, session_01J2V3UYqrLbCNN9zst5WY8d); send it one
line per fix or deploy with `send_message`, and the same to Manual QA-II
(session_01J2V3UYeTzFtZEuQJvkuadd).

Read first: `notes/sessions/hotfix-python-1.md` (bug loop, deploy steps), `hotfix-python-2.md`,
`hotfix-python-3.md`, then this file.

Rules in force (new this session; most are in `memory/`):
- DEPLOY AT ONCE: every finished fix is deployed the moment it is done, no :00/:30 windows (user,
  ~14:26 UTC); the lock `/tmp/geomind-backend.lock` still holds; bump the backend patch on top of
  whatever is on backend main (hotfix-back-III deploys too).
- Fatemeh's bugs go to the TOP of the queue (`memory/feedback-fatemeh-bugs-first.md`).
- QA tests (live checks on geomind.team, browser, LLM runs) are STOPPED; offline unit tests are
  allowed. Only check that you add no new failures (many stale ones: compare with a `git archive`
  of HEAD in /tmp, as done here).
- IMP-025 rule (`memory/feedback-team-lead-only-writes.md`): only a team lead reads and writes
  project files (case, plant, studies, results, inputs); sub-agents have no tools for them, only
  Knowledge (`search_knowledge`, `read_knowledge`, user-approved); a lead splits into at most 4
  briefs, puts everything into each brief, writes ONCE when all are back, re-splits what is left.
- IMP-023 rejected: no gemini sample plants as templates; agents design from
  `knowledge/handbook-design.md` (handbooks renamed: handbook-case.md, handbook-design.md,
  handbook-economics.md, handbook-report.md).
- gemini changes need no permission; write what and why in each gemini commit; API frozen.

## State at handover

Production: backend 1.1.95 (geomind 0.4.91, gemini 0.6.15) was live at 14:55. A deploy of
geomind 0.4.95 + gemini 0.6.16 was waiting on the lock (hotfix-back-III held it since 14:53 for
QA-135 / backend 1.1.96). CHECK: health version and `docker exec geomind-celery` versions. If
0.4.95/0.6.16 are not live, deploy them: take the lock, `git pull` backend, replace both wheels
in `backend/.tmp/hotfix-wheels/` (build from ../geomind and ../gemini), bump backend patch
(src/version.py, openapi.json "version", contracts.md line 3, CHANGELOG section naming geomind
0.4.92-0.4.95 and gemini 0.6.16), commit, push, `cd backend`, `scripts/hotfix_deploy.sh`, free
the lock, tag, STATUS line, tell coordinator + Manual QA-II, then `qa.py set ... fixed` for
QA-128, QA-140, QA-143, QA-121 with notes and Fix sections (qa.py set writes "- time: note" under
## Fix; append the cause/fix text after it, then `qa.py save`).

Released this session:
- geomind 0.4.86 QA-125 (read_result series `summary`, module `operation`), QA-124, QA-123 skill;
  0.4.87 QA-129 skill, QA-132; 0.4.88 QA-131 (sensitivity `values=`); 0.4.89 handbook name;
  0.4.90 IMP-025 Team list briefs + `instance` on events, data-economics rename; 0.4.91 lead-only
  file access, max 4 briefs; 0.4.92 QA-140 (case lead always splits into 2-4 geoscientists,
  single geoscientist tool removed) + search_knowledge/read_knowledge; 0.4.93 QA-143
  (evaluate_module class name with design, inlet message, `failed_before` guard in
  engine/step.py); 0.4.94 QA-121 (approval cards start with one sentence: session.call_summary;
  skill: a size question is one ranged search); 0.4.95 IMP-019 (runs.single_choices fills
  dispatch/outages, note `filled`).
- gemini 0.6.14 QA-123 (capacities reason), 0.6.15 QA-130 (doublet flow capped at nominal_flow)
  + QA-129 (free plant takes size.doublets, resize.py `_free_resized`), 0.6.16 QA-128 (carbon
  price only on the plant's own CO2e: co2_steps.priced_steps; schedule electric() factor 0).
- Fixed and deployed: QA-123, 124, 125, 129, 130, 131, 132. Fixed, deploy pending: QA-128, 140,
  143, 121 (claimed by hotfix-python; set fixed after deploy). QA-128 judgement told to nobody
  yet: tell the coordinator that grid electricity's CO2 is no longer priced (counted in co2 only);
  an explicit case flag could be added if the user wants grid CO2 priced.
- IMPROVEMENTS.md: IMP-019 done, IMP-023 rejected (written), IMP-025 status, IMP-026/027/028
  approved (written).
- QA-122: hotfix-back-III's backend part is LIVE (backend 1.1.90): optional
  `Workspace.project_designs(project_id) -> {plants: [{version, name, note, by, created, latest}],
  studies: [{id, name, kind, status, created, plant_version, case_version, settings, result:
  None|{id, name, role, plant_version, case_version, kpis:[{name,title,value,unit,reason}],
  checks:{passed,failed,not_assessed}}}]}` and `Workspace.plant_version(project_id, version) ->
  dict|None`. The geomind part (a read-only tool for the explainer/agents, read with getattr) is
  yours.
- Backend tests that fail since geomind 0.4.89 (from hotfix-back-III): 
  `test_a_run_that_cannot_start_fails_with_geomind_message` ('geomind_refused' vs 'error') and
  `test_events_replay_and_end_at_the_root_run_finished` (replay ids): look at them.

## Next steps, in order (user order via Coordinator-IV)

1. Finish the pending deploy (above) and report.
2. IMP-025 plant stage with IMP-027: the design lead splits plant work into at most 4 engineer
   instances (Team list briefs; `geomind/agents/design/lead.py` team(), fill_parts); under the
   lead-only rule the engineers get NO patch_plant/read_plant: they return proposed changes
   (paths and values with reasons) from the plant text in the brief, and the lead applies them
   ONCE with patch_plant/merge. IMP-027: a wall-clock and round budget per sub-agent set by the
   lead (Delegate `steps` exists; add a time limit), at the limit it hands back what it has.
   Then analysis and report stages the same way. Deploy each stage when it works.
3. Rename the tool read_rag to read_file (user): tool, skill finding-sources, prompts, tests,
   evals; search_rag searches project files and Knowledge, so rename it search_files; keep the
   old names working (tools.base with_old_names); tell hotfix-back-III / hotfix-front-V
   (session_01J2V3UVNQkaiH9cMvNv911G) about any label mapping.
4. QA-122 geomind part (contract above).
5. IMP-028 (margin tests and failure scenarios, no LLM), then IMP-026 (cooling with network heat
   gain and a sourced chiller minimum part load).
6. The case lead's 5 refusals in run 9696f5d4 (QA-140 evidence): no_case x2, update_state list
   form, set_case files-only, set_case date without time zone: make each a normalised slip with
   a note or a clearer refusal.
7. `qa.py next --area geomind,gemini --fixer hotfix-python`.
