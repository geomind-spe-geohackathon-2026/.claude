# hotfix-python-lead handover (2026-11-05 19:45 Trondheim, context limit)

You are **hotfix-python-lead-II**, successor of hotfix-python-lead (hotfix-python-VIII, peer
name geomind-spe-hackathon-2026-52, thread cmsg_016VUmQoW7nUde2xdqUWA2Po98A4zYiWNQakrBuTJwyBp3).
Mode HOTFIX (do not ask). Chat with Sahand in Persian, files in English, times in Trondheim time.
Coordinator: Coordinator-V, session_0171QAFoSN9TvdcAEimBHMXT (`send_message` "@parent" or that
id, visibility `sent_to_shared_agent`).

## Role (Sahand, 18:37 and 19:27)
Read `.claude/memory/feedback-hotfix-teams.md`. The lead works on NO task itself: it only assigns
bugs to members (each with a disjoint file list), collects their reports, reviews quickly, stages
BY PATH, commits, pushes (geomind main, gemini dev), deploys, and sets qa.py status. Deploy in
batches about every 10 min. Approvals are delegated to Coordinator-V; only data-destroying steps
go to Sahand.

Deploy: `cd /home/fatemec/geomind-spe-hackathon-2026/backend` then `scripts/hotfix_deploy.sh`
(two Bash calls). It builds gemini/geomind from git HEAD (git archive), so members' dirty files do
not matter; it refuses only when the BACKEND clone is dirty (back-lead's files): then ask the
coordinator to have back-lead commit and deploy (its deploy carries geomind HEAD).
Commit pattern: bump `pyproject.toml` + `geomind/__init__.py` version and add a CHANGELOG entry
(`docs/CHANGELOG.md`, under `## [Unreleased]`), commit with
`Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. gemini: version in pyproject +
gemini/__init__.py, docs/CHANGELOG.md. Unit tests: `.venv/bin/python -m pytest -q -n 8 <paths>`
in geomind; pre-existing failures in /tmp/hp5/base_fail.txt (also: loops/test_compare x3,
test_no_unit_math economics.py, test_case section_the_case_lacks, test_reviewer it_is_complete,
test_economics x2). qa.py: `python3 documents/project/quality-assurance/qa.py claim|set ...`
(slow, run in background with timeout).

## State
- LIVE: backend 1.1.116, geomind 0.4.124, gemini 0.6.21 (19:30 CET).
- PUSHED, NOT DEPLOYED (deploy blocked at 19:38 by back-lead's dirty backend files
  src/api/v1/assistant/runs/adapters/simulated.py + test; coordinator asked to have back-lead
  deploy): geomind 0.4.125 (ced01b3: QA-271, 219, 159, 266, 268, 189, 278, 276, 194, 204),
  da67c9a (QA-199/265 one write_lesson card, QA-196, QA-168 part 3), 01c4beb (QA-283),
  32fcda0 (QA-156 part). After the deploy: qa.py set fixed for those ids.
- Marked fixed up to 0.4.123 (see BUGS.md). Duplicates set: QA-174, QA-222, QA-265.
- Pending Sahand: deleting wrong memory rows of QA-199 in the production DB (my read was denied;
  coordinator asked Sahand). IMP-029 is an idea, not approved.

## Members (SendMessage to the peer name; they reply to the lead's peer name: TELL EACH ONE
your new peer name first)
| member | peer | working on | files |
|---|---|---|---|
| m1 | geomind-spe-hackathon-2026-44 | QA-235/236 + stored versions in ONE run_study (QA-278 fix 3) | tools/calculate.py, agents/project/comparison.py |
| m2 | geomind-spe-hackathon-2026-a4 | QA-272 (search_rag snippets), QA-273 (skills.py first_call_skill), QA-270 answer (coverage key for HP electricity, for backend member-1), QA-282 (gemini Study.check population for polish) | tools/gemini/results.py search_rag part, context/skills.py, prompts/case/lead.md (owner; collects case prompt lines from m3/m5), gemini study/evolve check |
| m3 | geomind-spe-hackathon-2026-39 | IMP-030, QA-197/198 follow-ups | agents/case/lead.py, agents/project/*, prompts/project/*.md (not explainer.md) |
| m4 | unknown peer (thread cmsg_016VUmQoW7nUde2xdqUWA2Po6cwrvUy9zjpKxqHdynF5fv; coordinator relayed) | QA-275, QA-168 parts 2/4, QA-192 part 2, QA-279, QA-280 | tools/gemini/assessment.py, economics.py, unit_bridge.py, skills/economics |
| m5 | geomind-spe-hackathon-2026-d9 | QA-200/222/157 DONE in the tree (case.py, skills/setting-the-case, test_case.py; two integration tests test_live_regressions.py/_h.py being updated): commit when m5 says they pass; then QA-163, QA-203, QA-160, QA-284 | tools/gemini/case.py, origin.py, skills/setting-the-case, those tests |
| m6 | geomind-spe-hackathon-2026-69 | QA-285 (gemini optimizer never moves HP capacity), .claude/docs tools.md/memory.md write_lesson form | gemini/gemini/study/* (coordinate with m2), .claude/docs |
| m7 | geomind-spe-hackathon-2026-8d | QA-212 reopened (all values in the first patch: flow, ready, setpoints, ESP stage_count, injection pressure_setpoint), plants.py build_plant warns vs project version, QA-211, QA-263 | tools/gemini/plants.py, stages.py, prompts/design/*, agents/design/*, tools/gemini/study.py, studies.py, skills designing/comparing |
| m8 | geomind-spe-hackathon-2026-62 | QA-234 (explainer.md 4 significant figures), QA-155 (tools/state.py, context/state.py), QA-190 (run.py), QA-156 Team part (tools/delegate.py Team, tools/dispatch.py _bounded), QA-154/155/190 | tools/stored.py, gemini/results.py (non-search part), references.py, suggestions.py, knowledge_only.py, explainer.md, state, run.py, delegate, dispatch |
geomind-spe-hackathon-2026-7e is NOT a member (bug tracker).
Full task text for the new members: `.claude/notes/python-team-tasks.md`.

## Routed to back-lead via coordinator
QA-194 backend (project_state economics), QA-196 /calls/{id}, QA-156 delegate (taken back: m8).

## Next steps
1. Tell all 8 members your peer name. 2. Once back-lead deploys (or the backend is clean), deploy
and mark the pending batch fixed. 3. Commit m5's batch when its tests pass. 4. Keep members fed
from BUGS.md (open geomind/gemini bugs) with disjoint files; never fix yourself.
