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

Open for retest when fixed: QA-288, QA-310, QA-266, QA-294, QA-218, QA-283, QA-224, QA-204, QA-190, QA-189.
