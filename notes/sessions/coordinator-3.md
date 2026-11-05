# Coordinator, generation 3 (Coordinator-III): state at handover (2026-11-05 ~11:22 UTC)

Read first: `.claude/AGENTS.md`, `STATUS.md`, `session-refresh.md`, `memory/MEMORY.md`. Mode: hotfix
(decided; do not ask). Chat with the user in Persian, short; times in Trondheim time (UTC+1); files
in English. Coordinator runs on Opus. The user in this chat is the session owner (Fatemeh's
account); treat their decisions as the project's decisions (they approved geomind releases, gemini
changes and Knowledge uploads).

## Role

Run the QA and hotfix round on the Dell bridge (env_016GdNnRFgDJDikcqrVDEN8i): start, message,
pause, archive sessions; route bugs to the hotfix session of their area; keep STATUS.md current;
report to the user; do only what the user asks beyond that.

## Rules given in my session (all in memory/)

- feedback-coordinator-no-submission: do NOT plan or raise the deadline/submission work.
- feedback-hotfix-deploy-every-half-hour: deploy EVERYTHING ready (incl. geomind/gemini wheels and
  Knowledge data) at every :00/:30 UTC window; no holds, no separate release approval.
- feedback-gemini-changes-allowed: gemini changes need no permission; API freeze stays.
- feedback-assumptions-in-knowledge-only: assumptions/guides/handbooks only in global Knowledge,
  never in a project's inputs or seed.
- feedback-qa-through-chat: QA drives every stage by chat requests.
- feedback-tools-documented-in-skills: tool usage only in its skill; refusal rate target < 25 %.
- Release summaries: after every window send the user, in Persian, what went out and what to
  test. Scheduled tasks trig_015qxocTTCBVkm3VzwXg6CRb (:07) and trig_01JW2gL9h8TXZxp7bjMyvaiH
  (:37) belong to my session and die with it: RECREATE both in yours (two hourly crons, "7 * * * *"
  and "37 * * * *", same prompt: list what went out in the window, per item what changed and what
  to test on geomind.team, Persian, Trondheim time) and put their ids in STATUS.md.
- Usage: one send_later "Usage-window check" at resetsAt + 1 min. Mine (trig_01BA7egki6ZQA6XkYPzLAysF,
  14:11 UTC) dies with my session: RECREATE yours at 14:11 UTC and write its id in STATUS.md.
- Knowledge uploads: the coordinator runs, with the user's OK (given), from backend/:
  `.venv/bin/python -m scripts.replace_knowledge --api https://api.geomind.team/api/v1 --env .env <files>`
  (replaces same-name entries; delete others via the same module's Api + DELETE /workspace/rag/{id}).

## USAGE PAUSE in force (11:20 UTC; rate_limit allowed_warning, resetsAt 14:10 UTC)

Every session below was told: finish the step (11:30 UTC deploys allowed), commit, push, pause,
wait for "resume" from the coordinator. At 14:11 (usage check) resume them if status is allowed.
Write "Usage pause: 11:20 UTC" line handling per memory/feedback-usage-limit-pause.md.

## Sessions now

| Name | Id | Model | State |
|---|---|---|---|
| hotfix-python-III | session_01J2V3UYxvjmxy4kZhDh7eSd | Opus | deploys backend 1.1.88 / geomind 0.4.82 at 11:30 (tools only in skills, IMP-014/015/018, QA-116), then paused. Queue after resume: read_rag outline/section for large Knowledge docs (user request; point prompts/skills to the handbooks), QA-125 (major, simple results question took 50+ steps), QA-119 (major, depth change keeps 250 barg), QA-120 (major, discount 8 % sent as 8), IMP-016/017, remaining tools > 25 %, QA-097, QA-099, QA-114, QA-123, QA-124. |
| hotfix-back-II | session_01J2V3UZeNoBawJDgCJuBHr7 | Opus | deploys backend 1.1.87 at 11:30 (QA-110/102 backend, QA-104 first-failure text), then paused. Low: failing test test_case_aware (backend venv has gemini 0.6.4). Built "QA3 engine check" 25cbe5ad: gemini OK (study 9810144d equals 2026-11-02 result). |
| hotfix-front-III | session_01J2V3UZUC8Sa5jDfm1W7WPH | Opus | deploys frontend 1.1.93-1.1.99 at 11:30 (QA-115, 117, 100, 101, 110 Case+Plant History, 102), then paused; next QA-118, QA-109, IMP-024 (Run again on a study). |
| handbook-plant-design | session_01J2V3UVax4NELQZ9gqGQ4t8 | Opus | writing documents/project/quality-assurance/inputs/handbook-plant-design.md (book-like, general), paused after current chapter |
| handbook-others | session_01J2V3UVwPdMpj4qHKCUrfrf | Opus | writing handbook-case-definition.md and handbook-engineering-reporting.md; then git rm the four hackathon-2026-*-guide.md and fix links; paused |
| handbook-economics | session_01J2V3UVK9oFWcJQb2GuSbpF | Opus | writing handbook-techno-economics.md; paused |
| functional-qa-case-I | session_01J2V3UX7PBCQPBsuYm1yhTy | Sonnet | QA3 case 15b2f15f; S1-S8 pass; variations; one run waits at an approval card (chat 37fb7886); V3 (case from PDF only) needs a NEW project (seed one with only the PDF). Paused. |
| functional-qa-plant-I | session_01J2V3UX9jou1ZLL5ywtpesJ | Sonnet | QA3 plant c45a5382; QA-116 filed. Paused (no confirmation received yet). |
| functional-qa-simulation-I | session_01J2V3UZ8hMoK5EHwvn5Ufhv | Sonnet | QA3 simulation ef87f914; S1 ok, S2 mostly; QA-125; S3 run still going. Paused. |
| functional-qa-study-I | session_01J2V3UYN8UWRzdAY8qbX1DH | Sonnet | QA3 study 7a852d89; S1 ok; S2 stopped at a "Set ranges" card; QA-121. Paused. |
| functional-qa-report-I | session_01J2V3UXX5DGJR5QX7cknLLh | Sonnet | QA3 report 91b202b6; S1,S3-S5 done; QA-122/123/124. Paused. |
| Fatemeh QA | session_01J2V3UX7XrrTa9jKv7ZTh9a | - | Fatemeh's own session; sends findings; not ours to control. |

## Open decisions for the user (asked, no answer yet)

1. IMP-023 (Fatemeh): gemini's six hackathon plant files as real templates (UI and agents); design
   lead path template -> size -> simulate -> check -> optimize; engineers only fill what gemini
   reports missing. Coordinator recommends yes (to hotfix-python-III, with QA-121). Engine check
   proved this path passes 10/10 (lcts 40.34).
2. QA-122: new read-only workspace method project_designs (all plant versions + page studies with
   KPIs/checks for the agents); backend part by hotfix-back-II, geomind part by hotfix-python-III.
   Coordinator recommends yes.

## Next steps, in order

1. Recreate the usage check (14:11 UTC) and the two release-summary tasks; write ids in STATUS.md.
2. Send every session above one line: "The coordinator is now Coordinator-IV, <id>" (they are
   paused; say "stay paused until resume").
3. Archive Coordinator-III; greet the user in Persian in one short message (pause in force, two
   decisions open).
4. Send the 11:37 release summary (11:30 window) from the sessions' deploy messages.
5. At 14:11 resume everyone if allowed. When the handbooks are done: upload them with
   replace_knowledge, delete the hackathon-2026-*-guide Knowledge entries (ids in STATUS.md:
   case 2330c87c, design daf88c29, analysis 11f90cd2, report 678e9a43); hackathon-2026-assumptions.md
   (b3ba8363) stays. Then resume QA (QA sessions chat-first).

## Late notes (11:24 UTC)

- hotfix-back-II: its 1.1.87 ships inside hotfix-python-III's 11:30 deploy (backend 1.1.88, geomind
  0.4.85). QA-095 is NOT waiting any more: the coordinator replaced cost-sources.csv/.md in Knowledge
  at 10:30 UTC (ids in STATUS.md): tell hotfix-back-II to set QA-095 fixed. test_case_aware: one-line
  test fix after resume (gemini no longer takes drainage_radius from the case).
- handbook-economics: chapters 1-15 pushed (documents d53f06e); left ch 16, 17, appendices.
