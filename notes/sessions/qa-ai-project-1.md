# QA-AI-project-I (2026-11-05): handover note

Thread: QA round plan `documents/project/plans/qa-round-e2e-ai.md`, row QA-AI-project-I (project/ and
support/ agents, backend layer only). Report: `documents/project/quality-assurance/reports/QA-AI-project-I-2026-11-05.md`
(rounds 1-3, 17 runs). Hotfix mode, no code changes; live LLM runs allowed for this thread only.

Projects on geomind.team (keep, never delete):
- QA-TEST QA-AI-project-I 1: 35a70dbe-5e24-4f51-9c6f-50e06d47fe82 (reference case + HackathonPlant; case now v6, permeability 160 mD by hand)
- QA-TEST QA-AI-project-I 2: dfe5d6e1-8fdc-404f-b150-b8e7d919f2a1 (case only; compare runs, auto-approve on)
- QA-TEST QA-AI-project-I 3: 3ecb4493-3368-4bc2-b2f0-ca0b06670a86 (memory on)
- QA-TEST QA-AI-project-I 4: 588c282d-fd39-4ea1-b495-d167817739c3 (empty)

Tools: `notes/sessions/qa-ai-project-1-tools/` (api.py logs in with the backend .env admin, never
prints it; drive.py newchat/send/answer/wait, polls every 15 s (QA-217: no faster than 5 s);
log.py dumps /runs/{id}/log; trace.py prints every LLM and tool call with times and tokens;
upload.py adds a case file with the base version). Run them from a scratch copy.

State at 19:40 UTC (backend 1.1.123): rounds 1-4 done (report has 4 sections). Verified: QA-187,
189, 190, 204, 218, 224, 227, 245, 252, 283, 288, 310 (QA-266 verified by its fixer). Open: QA-294
(project results invisible to agents in a new chat). Duplicates: QA-188 (= QA-176), QA-265 (= QA-199).
Idea: IMP-032.

Rules from the user during this session (already in memory/ or STATUS by the coordinator): times in
chat in Trondheim time (CET), files UTC; a bug never ends testing: file it and go on, retest only
deployed fixes; poll run state no faster than every 5 s.

Next steps for the successor (role: same row of the plan, hotfix mode, no code changes, live LLM runs
allowed, backend layer only, chat with Sahand in Persian):
1. Retest QA-294 when fixed (project 1, new chat: "what moved in LCOH against the last result").
2. New scenarios not yet run: support lead's summarizer for a long handover (memory off), the
   `design` loop route ("only a new design round on the case as it is"), an app event message from
   a plant saved by hand, a request that mixes two goals, a third compare family named by the user.
3. Check the comparison LCTS (33.66 EUR/MWh, HP + compression) against gemini's
   examples/hackathon.py on the current gemini (README says 40.34, older version); report only a
   real gap.
4. Append each round to the report and update the SCENARIOS row.
