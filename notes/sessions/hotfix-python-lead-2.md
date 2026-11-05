# hotfix-python-lead-II handover (2026-11-05 ~20:50 Trondheim)

Successor name: hotfix-python-lead-III. Mode HOTFIX (do not ask). Chat with Sahand in Persian, files
in English, every time in Trondheim time. Coordinator: Coordinator-V, session
session_0171QAFoSN9TvdcAEimBHMXT (`send_message` "@parent", visibility `sent_to_shared_agent`).
Role and rules: as in hotfix-python-lead-1.md (lead fixes nothing; assigns disjoint files, reviews,
stages BY PATH, commits, pushes geomind main / gemini dev, sets qa.py). Sahand's rule: members fix
bugs and write only a minimal check, no heavy tests. Python bugs come to the lead only (asked
Coordinator-V not to route to members directly).

Deploy: this session's `scripts/hotfix_deploy.sh` call is blocked by the permission classifier;
ask the coordinator to have back-lead deploy (its deploy carries geomind/gemini HEAD). Production
Knowledge uploads and production DB reads are also blocked: they go to Sahand.

## State at handover
- LIVE (deploy 36): backend 1.1.118, geomind 0.4.130, gemini 0.6.26 (later deploys up to backend
  1.1.123/1.1.124 may carry more; check STATUS.md).
- PUSHED, deploy requested: geomind main c4108d3 (0.4.132 + QA-330, QA-331); gemini dev 2cf14074
  (0.6.32). Unit tests green in both (geomind 4190+/0, gemini 8649/0).
- qa.py: everything committed is set fixed with "pending deploy" notes; QA-320 reopened -> fixing
  (m8), QA-322 fixing (gemini part done in 0.6.31; backend/frontend with the other leads).

## Members (peer names; I am geomind-spe-hackathon-2026-39 [44a105], m3 is ...-39 [c98e15])
| m | peer | now |
|---|---|---|
| m1 | geomind-spe-hackathon-2026-44 | standby |
| m2 | geomind-spe-hackathon-2026-a4 | standby (did QA-319, QA-329, case/lead.md owner, 20k cap) |
| m3 | geomind-spe-hackathon-2026-39 [c98e15] | standby (project/analysis prompts, coordinator.md) |
| m4 | geomind-spe-hackathon-2026-16 | standby (economics.py earlier; gemini tests/version bumps) |
| m5 | geomind-spe-hackathon-2026-d9 | standby (case.py, recovery.py) |
| m6 | geomind-spe-hackathon-2026-69 | standby (gemini study/minimize/size) |
| m7 | geomind-spe-hackathon-2026-8d | standby (design prompts/agents, plants.py, stages.py, adopt_design) |
| m8 | geomind-spe-hackathon-2026-62 | QA-320 reopen: refuse source "agent" values in ask_economics (economics.py) |

## Waiting on Sahand (asked in thread)
- Upload HackathonSuperstructure.json + six hackathon plants to production Knowledge (list_starts).
- A generic complete example case in Knowledge (QA-309)?
- Re-record 6 slow replay recordings (needs LLM).
- Knowledge edit: backticked capex keys in hackathon-2026-assumptions.md; data-economics.csv row
  analysis-period-sde-2025-subsidy-period -> economics.revenue.subsidy.duration.
- gemini request (geomind/docs/requests/gemini-requests.md): public Doublet design groups.

## Report-relevant findings
- B_r1_best 29.55 EUR/MWh is invalid (QA-321: producer simulated only 2000 m deep).
- Optimum figures must be re-run on gemini >= 0.6.32 (QA-278 depth fix, QA-324 cooler sizing).
