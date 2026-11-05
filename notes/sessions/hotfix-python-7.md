# hotfix-python-7 handover (2026-11-05 ~17:15 UTC, context limit)

You are hotfix-python-VIII, the successor of hotfix-python-VII (Remote Control thread on the NTNU
Dell, Sahand's account).

## Role and mode

Mode: HOTFIX (decided; do not ask the user). Same role as `hotfix-python-5.md` and
`hotfix-python-6.md`: fix the QA bugs, tasks and IMP items of geomind and gemini; work directly
on geomind `main` and gemini `dev` in the shared clones (no branch, no worktree); stage by path.
Coordinator: see `STATUS.md` (Coordinator-V, session_0171QAFoSN9TvdcAEimBHMXT); one line per fix
or deploy with `send_message` (`session_id` "@parent" or that id, visibility
`sent_to_shared_agent`). Reply to Sahand in Persian, files in English.

First prompt of hotfix-python-VII (coordinator note): "You continue the earlier Dell session
hotfix-python-VII (geomind main, gemini dev). First read account-handover.md,
notes/sessions/hotfix-python-6.md and coordinator-5.md; follow the role rules there."

## New rules from Sahand this session (all in memory/ or below)

- Hotfix mode: write few tests (only what a rule like test_mirror forces); run only the affected
  unit tests, compare with the baseline /tmp/hp5/base_fail.txt (pre-existing failures there and in
  test_code_quality / test_mirror are not yours).
- Never wait for a GitHub release; package sessions only commit and push. The backend hotfix image
  builds gemini (dev HEAD) and geomind (main HEAD) from the local clones
  (`memory/feedback-local-builds-git-push-only.md`). Deploy: take `/tmp/geomind-backend.lock`, then
  two Bash calls `cd /home/fatemec/geomind-spe-hackathon-2026/backend` and
  `scripts/hotfix_deploy.sh`, free the lock. No backend version bump needed for a package change.
- Releases and deploys need no OK, gemini changes included; nobody waits for approval (approvals
  are delegated: ask Coordinator-V). Only data-destroying or irreversible steps go to Sahand.
- Deploys are NOT frozen during live runs (Sahand: the run survives a celery restart).
- Bugs Sahand or Fatemeh send themselves always come first.

## State

- Production: backend 1.1.104 (hotfix image), geomind 0.4.100, gemini 0.6.17.
- Pushed, NOT deployed: geomind 0.4.101 (af0d5bf, QA-162) and 0.4.102 (c5ed1b1, QA-165).
  DEPLOY IS BLOCKED: `hotfix_deploy.sh` fails at the base Dockerfile `pip install -r
  requirements.txt`: kombu[redis] 5.7.0 (new on PyPI) conflicts with `redis>=5,<6`
  (backend/requirements.txt lines 5 and 16). Told the coordinator for hotfix-back-VI. When it is
  fixed, deploy and check `geomind 0.4.102 gemini 0.6.17` in the script's output, then add
  "deployed" to QA-162 and QA-165.
- Fixed and deployed this session: QA-145 (0.4.96), QA-122 (0.4.97), QA-147 (0.4.98), QA-148 +
  QA-149 (gemini 0.6.17), QA-152 + QA-158 (0.4.99), QA-153 (0.4.100). None live-retested.
- Small pushed changes: web_search up to 12 words (QA-150 part), design lead briefs cite
  handbook-design 0.7/0.8.
- QA-150 is `fixing` (mine): only the web_search part is done. Idea not started: a wall-clock
  budget per sub-agent (Delegate `minutes`, like `steps`; it needs a new runtime setting
  GEOMIND_ENGINEER_MAX_MINUTES in backend .env and .env.example via hotfix-back; `engine.py`
  loop ~line 244 and `delegation.py` run_child; skip the deadline when the run has recorded steps,
  for replays). The re-read guard (`same_result`, `with_repeat_note` in engine/step.py) already
  exists.

## Queue, in order (Coordinator-V)

1. Sahand's or Fatemeh's own bugs, always first.
2. QA-166 (major): simulate with no design runs the latest plant (v2) but the agents report v1.
3. QA-169: read_knowledge takes a bare file name (`handbook-design.md` without `knowledge/`) and
   section titles; the outline prints the number twice ("3 3 The subsurface").
4. QA-150 (speed) with QA-156, QA-157, QA-159 (re-reads, round trips), IMP-029 (fewer approval
   cards in a case run), IMP-030 (case lead reads the assumptions doc once and hands it to the
   geoscientists), QA-171 + QA-175 (patch_plant/check report every missing value at once, not
   one per stage; gemini change approved).
5. Rest of QA-161: case/lead.md asks only what set_case reports missing; never asks outdoor
   humidity or the gas heating value.
6. QA-160: flow limit as one requirement with min and max.
7. QA-173: give explainer, reviewer, economist and analysis lead `read_knowledge` (and
   search_knowledge); add the citations handbook-econ-report-I proposes.
8. QA-177, QA-178: prompts that contradict handbook-case / handbook-design: change them once the
   handbook threads say which rule holds.
9. Minors: QA-154, QA-155, QA-163, QA-172 + QA-174 (one fix: the patch_plant card says "Change 0
   value(s)" for a list of changes; close QA-174 as duplicate), the passed/feasible item of
   handbook-econ-report-I if filed.
10. QA-176 (a deploy restarts the design engineers) is hotfix-back-VI's; it may hand you a
    geomind part. hotfix-back-VI may take QA-167, QA-168: agree with it which files each touches.

QA-151 (handbook-design) belongs to handbook-design-I, not to you.
