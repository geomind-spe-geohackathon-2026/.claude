# Coordinator, generation 4 (Coordinator-IV): state at the account handover (2026-11-05 ~18:45 UTC)

Read first: `.claude/AGENTS.md`, `STATUS.md`, `account-handover.md` (Phase 2), `session-refresh.md`,
`memory/MEMORY.md`. Mode: HOTFIX (decided; do not ask). Chat with the user in Persian, short;
times in Trondheim time (UTC+1); files in English. Coordinator runs on Opus. The user in the chat is
the session owner; treat their decisions as the project's.

## Role

Run the hotfix round on the Dell bridge: start, message, pause, archive sessions; route bugs to the
hotfix session of their area; keep STATUS.md current; report to the user; do only what the user
asks beyond that. Knowledge uploads: the coordinator runs them (user-approved), from backend/:
`.venv/bin/python -m scripts.replace_knowledge --api https://api.geomind.team/api/v1 --env .env <files>`
(replaces same-name entries); delete others via `scripts.seed_qa_projects.Api` + `DELETE /workspace/rag/{id}`.

## Rules given in my session (all in memory/)

- feedback-fatemeh-bugs-first: Fatemeh's bugs (Manual QA) go to the top of every queue.
- feedback-hotfix-deploy-every-half-hour (OVERRIDDEN): deploy every fix AT ONCE, lock still holds.
- feedback-design-from-handbook-not-templates: IMP-023 rejected; no templates anywhere.
- feedback-team-lead-only-writes: IMP-025: only team leads read/write project files; ≤4 sub-agents;
  sub-agents may read the global Knowledge only; lead writes once, re-splits, reports up.
- feedback-session-models: coordinator and hotfix-python on Opus; hotfix-back, hotfix-front and
  other sessions on Sonnet.
- feedback-no-tests-now: NO QA tests (live checks, browser, LLM runs) until the user lifts it;
  offline unit tests allowed.
- feedback-force-stop-account-handover: the procedure in account-handover.md.
- Names decided: handbooks handbook-case/-design/-economics/-report.md; cost catalogue
  data-economics.csv/.md; tool read_rag -> read_file (pending, hotfix-python).
- Approved by the user: QA-122, IMP-019 (done), IMP-025 (top), IMP-026/027/028, QA-135 option C (done).

## State

- Production: backend 1.1.98 (geomind 0.4.95, gemini 0.6.16), frontend 1.1.112. Details and ids in
  STATUS.md.
- Global Knowledge: handbook-case 1a064236, handbook-design 6d617b90, handbook-economics 634ca9c8,
  handbook-report 3664b76b, hackathon-2026-assumptions 8bd08430, data-economics.csv 74a0d44b,
  data-economics.md e470a627.
- Speed plan: documents/project/plans/speed-case-plant.md; baseline
  speed-case-plant-baseline.md (top 10 causes); scripts in plans/speed-baseline-scripts/.
- QA round 3 closed; all functional-qa sessions archived.
- Scheduled tasks of this account deleted (release summaries); the successor recreates them.

## Next steps, in order (for Coordinator-V on Sahand's account)

1. Phase 2 of account-handover.md: recreate the release summaries, start the sessions in its table,
   write ids in STATUS.md.
2. Queue: hotfix-python: QA-145 + speed plan C1/C2, the baseline top 10, B2-B5, read_file, QA-122,
   IMP-028, IMP-026. hotfix-back: step `ts` in events, patch_plant internal error. hotfix-front:
   check QA-146 (unnamed "Thinking" line), plan E2 stage timer, open frontend bugs.
3. After the next geomind releases: start speed-analysis-II to re-run the baseline and compare.
4. When the user lifts the no-QA-test rule: one timed case run and one plant run vs the baseline.
