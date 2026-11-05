# Coordinator, generation 2 (Coordinator-II): state at handover (2026-11-05 ~09:55 UTC)

Read first: `.claude/AGENTS.md`, `STATUS.md`, `session-refresh.md`, `memory/MEMORY.md` (new since
gen 1: feedback-session-models, feedback-qa-round-2, feedback-usage-limit-pause,
feedback-commit-often, feedback-times-trondheim, competition-judging-criteria,
feature-agent-tools). Mode: hotfix (decided; do not ask). Chat with Sahand in Persian, short; times
in Trondheim time (CET, UTC+1); files in English. Coordinator runs on Opus.

## Role

Run the QA and hotfix round on the Dell bridge (env_016GdNnRFgDJDikcqrVDEN8i): start, message,
pause, archive sessions; route bugs to the hotfix session of their area; keep STATUS.md current;
report to Sahand; make small decisions yourself and tell him.

## Standing duties

- Usage: one pending send_later "Usage-window check" at resetsAt + 1 min (rule in
  `memory/feedback-usage-limit-pause.md`). Mine (trig_01UdS66pQWurr2D3ms9rgFSe, 14:11 UTC) dies
  with my session: recreate yours at once (resetsAt now 14:10 UTC) and write its id in STATUS.md.
- Handover at 300,000 used tokens (new rule, all sessions).
- Deploys only at :00/:30 UTC; every session commits small and often.

## Sessions now

| Name | Id | Model | State |
|---|---|---|---|
| hotfix-front | session_01J2V3UYxh6obK4VSajGwZvk | Opus | deploying frontend 1.1.78-1.1.80 at 10:00 UTC, then hands over to hotfix-front-II (told) |
| hotfix-back | session_01J2V3UWh6RugyR1DAxrkNhH | Opus | seeding five "QA3 <stage>" projects via the public API (task below), then hands over to hotfix-back-II (told) |
| hotfix-python-II | session_01J2V3UXSA2mo8MG4igf5y4n | Opus | deploys the held batch at 10:00 UTC (backend 1.1.81, geomind 0.4.78, gemini 0.6.12), then QA-090/091 (decision below), hands over to hotfix-python-III (told) |
| functional-qa-I | session_01J2V3UWQ5zYo1TfCiAKXF4d | Sonnet | told to stop at the next checkpoint and wait; archive after it reports |
| functional-qa-2 | session_01J2V3UYx2foVYxpZKRTvMhq | Sonnet | same |
| functional-qa-3 | session_01J2V3UVgJnF99ApUaSbM43F | Sonnet | stopped (final status in its file; QA-092, QA-093 filed): archive |
| Fatemeh QA | session_01J2V3UX7XrrTa9jKv7ZTh9a | - | Fatemeh's own session; it sent QA-091; not ours to control |

## Next steps, in order

1. When hotfix-back replies with the five seeded project ids, start five Sonnet sessions
   (create_session, env above, model claude-sonnet-5-5, tags ["geomind-qa","qa"]):
   functional-qa-case-I, -plant-I, -simulation-I, -study-I, -report-I, each with prompt: "You are
   the QA session <title> of GeoMind, started by the coordinator (<your id>). Read
   ~/geomind-spe-hackathon-2026/.claude/notes/qa-round-3/README.md and <title>.md and
   ../qa-round-2/common.md and follow them; your project is "QA3 <stage>" (id <id>). Check your
   own rate_limit_info at every step; hand over at 300,000 tokens. Start now: scenarios first, tell
   the coordinator, then test." Put the ids in STATUS.md. Study: no evolve for now (Sahand).
2. Archive functional-qa-I/2/3 once each has reported its stop.
3. Route: QA-090/091 to hotfix-python (decision: case lead writes supply-temperature rules with
   when "running" AND adds heat/cold delivered, unmet share <= 1 %, as gemini's sample; design
   lead stops chasing one failing rule after a few rounds and reports it). QA-092 (major: agents'
   simulated design never reaches the project Plant/Results; studies wait for 4 values) and
   QA-093 (minor, New project Create closes silently): look at areas and route.
4. Record successors' ids in STATUS.md as they report; archive the old sessions.

## Product state (09:55 UTC)

Prod: backend 1.1.79 (1.1.81 deploying 10:00), frontend 1.1.77 (1.1.78-1.1.80 at 10:00). Big
fixes today: QA-076/078/080/082/083 (design loop now builds, sizes and simulates), QA-088 (agent
study results in the Results tab, with 0.4.77/1.1.81), agent tools feature (skills folder,
calculate with constants pi/e/g and plain numbers needing one sourced operand, run_python
sandbox, web_search via SearXNG English-only max 6 per agent per run), evolve "Compare
structures" page. Open problem: the design loop does not converge (QA-090/091 above). No run has
yet reached economics and report: that is why QA round 3 seeds later stages.

## Sahand's decisions this session (all in memory/ or STATUS.md)

Times in Trondheim time; usage pause/resume cycle; commit often; QA on Sonnet, hotfix and
coordinator on Opus; agent-browser only for QA; competition inputs only; three agent tools and
skills folder; calculate: power exponent, constants (not sourced), plain numbers need one
sourced operand; QA round 3 per stage on seeded projects, no evolve study for now; handover at
300k tokens.
