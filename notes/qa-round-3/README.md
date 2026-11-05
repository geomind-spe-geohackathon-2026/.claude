# QA round 3: one session per product stage (Sahand, 2026-11-05 ~09:45 UTC)

Instead of start-to-end runs, each stage is tested alone and fast, on a seeded project whose
earlier stages are already done (seeded by hotfix-back through the public API from the
competition files and gemini's sample `gemini/examples/hackathon_2026/`). Rules of
`../qa-round-2/common.md` hold (agent-browser only, competition inputs only, qa.py, commit often,
check your own rate_limit_info, Sonnet). Judging criteria: `memory/competition-judging-criteria.md`.

| Session | Project | Tests only |
|---|---|---|
| functional-qa-case-I | "QA3 case" (files only) | case set-up from the files by chat |
| functional-qa-plant-I | "QA3 plant" (case set) | plant design: configurations, sizing, checks, explanations |
| functional-qa-simulation-I | "QA3 simulation" (case + sized plants) | whole-year simulation, results, violations, iteration |
| functional-qa-study-I | "QA3 study" (+ simulation results) | studies: run, size, minimize, sample, sensitivity; NOT evolve (no structure search for now) |
| functional-qa-report-I | "QA3 report" (+ finished run study, economics) | economics, verdict, explainer, report, agent log export |

All testing goes through the chat (memory/feedback-qa-through-chat.md): ask each stage in the chat like a user; tabs only to check results or when the chat cannot do it (report that gap).

Each session: write scenarios in its file here first (`<session>.md`), tell the coordinator,
then test; when a run of its stage would need an earlier stage redone, use the seeded state and
report the gap instead. One run at a time; short, focused requests.
