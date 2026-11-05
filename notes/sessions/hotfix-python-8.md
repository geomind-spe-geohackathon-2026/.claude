# hotfix-python-VIII / hotfix-python-lead state

## Update 19:30 Trondheim (newest; supersedes the rest)

Sahand's rule: the lead does NO fixing at all; it assigns, collects reports, stages by path,
commits, pushes, deploys (backend scripts/hotfix_deploy.sh: builds from git HEAD, dirty member
files don't block, only a dirty backend clone does) and sets qa.py status. Deploy in batches
about every 10 min. Team = 8 members; task list in `.claude/notes/python-team-tasks.md`.
Peers: m1 = -44, m2 = -a4, m3 = -39, m5 = -d9; m4/m6/m7/m8 among -69, -8d, -62 and one more
(-7e is NOT a member: bug tracker). Live: geomind 0.4.123, gemini 0.6.21 (backend 1.1.115).
Pending Sahand: deleting the wrong memory rows (QA-199) from the production DB; do not delete.

# Older state (2026-11-05 ~19:00 Trondheim)

Role since 18:38: **hotfix-python-lead** (`memory/feedback-hotfix-teams.md`). Peer name of this
session: geomind-spe-hackathon-2026-52. Members (Dell peers; SendMessage by name):
- member-1 = geomind-spe-hackathon-2026-44: QA-175 + QA-212 (reopened) + QA-171 in
  tools/gemini/plants.py (report every stage's missing values at once); then QA-221 (reopened) +
  QA-247 (start from a stored plant version without retyping; read_plant output must round-trip
  through build_plant), same file.
- member-2 = geomind-spe-hackathon-2026-a4: QA-225/226 (gemini schedule.py pipe-loss flow, work
  in progress, stashed as `stash@{0} member-2 wip` in the gemini clone during a deploy: POP IT
  after the deploy), then gemini 0.6.18 + CHANGELOG, geomind assessment.py/runs.py (QA-226
  useful vs delivered, QA-228 geothermal/backup split from coverage); then QA-238
  (evaluate/coverage.py), QA-240 (evaluate/report.py). QA-239 is backend.
- member-3 = geomind-spe-hackathon-2026-39: owns prompts/case, prompts/project/lead.md,
  agents/case, agents/project (not explainer.py/reviewer.py), skills/setting-the-case. Idle
  after QA-243.

Deploy handshake (agreed with Coordinator-V): hotfix-back-lead pings before every deploy; I pause
members, commit or stash all dirty files in geomind and gemini, reply "go"; after the deploy pop
the stash and say "resume". hotfix_deploy.sh refuses any dirty clone (backend, gemini, geomind).

Pushed geomind: 0.4.103-0.4.114 (HEAD 778970d). Live: 0.4.110 (backend 1.1.107). 0.4.111-0.4.114
go out with hotfix-back-lead's backend 1.1.110 deploy (go given ~19:00). After it lands, qa.py
set fixed: QA-230, QA-224, QA-177, QA-227, QA-197, QA-198, QA-173, QA-243 (all claimed).

Queue (mine to split): QA-205+QA-209+QA-248 (studies: run_python refuses study history,
read_stored no slice, cost metrics, uncertainty samples all six), QA-233 (false "result is
stale" on report finish), QA-234 (raw floats), QA-192+QA-216 (proxy rows with unit mismatch to
Open; uncertainty field in ask_economics), QA-199 (curator approval cards; delete wrong shared
memory lessons case-lead-dated-series-time-zone and user-fact-* after a backup file), speed
group QA-150/156/157/159/179/187/189/219/229/235/236/245, IMP-029/030, QA-160/200/203/222
(222 duplicate of 200), QA-154/155/163/190/194/204 minors, QA-220 geomind part, QA-214 (330 d
cap echo), IMP-031 (gemini economics.json about.sources).
Pre-existing failing tests: /tmp/hp5/base_fail.txt (also test_compare x3, test_no_unit_math
economics.py, test_case section_the_case_lacks).
