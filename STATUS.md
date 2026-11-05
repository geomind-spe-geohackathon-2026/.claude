# Status: read first, keep current

The short, current state every session needs. Read it at the start of every session. When any of
it changes, change it here at once (one line, with the UTC time), before you go on.

Last updated: 2026-11-05 21:55 UTC.

- 21:55 UTC (Sahand): wind-down. Only the best-runs memory seed (python m3) + its import and GEOMIND_MEMORY on remain; every other hotfix thread finishes its task in hand and stops. Coordinator-V idle-check cron stopped.

- 21:48 UTC (Sahand): import real past designs into geomind experience memory (runs that passed gemini's check and gemini's own study results; origin = real run id or gemini study; nothing invented); GEOMIND_MEMORY to be turned on in prod at the next batch deploy.

- 2026-11-05 22:00 UTC (handbook-case-II round 3): handbook-case ch 18 cooling demand, 19 subsurface data, 20 produced fluid (gas, corrosion, scaling), 21 inputs as uncertain values, 22 worked example II (hourly), 23 worked example III (no files), 24 reviewing a case; 15.2 corrected to gemini CoolingGrid (latent taken when supply <= dew point - margin); 16.1 DST row count fixed; Appendix C split C.1-C.3, 39 external references (documents fffd4ce). Global Knowledge: handbook-case 7745c30a (was 8c2b10b4).
- 2026-11-05 ~22:55 CET Trondheim (handbook-economics-II, round 3): handbook-economics Global Knowledge 72710daf (replaces 45f1a2ce); documents 3cebb66. New ch 20 subsurface economics (depth, flow, doublet count, exploration risk), 21 load duration and screening curves, 22 heat pumps vs boilers (COP, cost and CO2 break-even), 23 cooling economics (compression, absorption, free cooling), 24 thermal and ice storage; outline table lists 0-24.
- 2026-11-05 22:50 Trondheim (handbook-report-II, round 3): handbook-report ch 22 method and V&V, 23 energy flows and time series, 24 presenting the economics, 25 emissions (scopes, GWP, intensity), 26 checking before release; Appendix B split B.1-B.3; 29 external sources (documents 0bf0fee). Global Knowledge: handbook-report ad1d1639 (replaces 01846b4c, 47a28eb8, 160a73d8, 5462feed).
- 2026-11-05 21:30 UTC (assumptions thread): completeness pass done (every key of gemini's sample case, economics and six plants is in the files, hackathon-2026-assumptions.md or data-equipment.md); added section 4 requirement forms (on/quantity/over/when, 330-day row, no over: sum). documents df06438. Global Knowledge: hackathon-2026-assumptions 8795ffc1 (was bcc0482b).
- 2026-11-05 ~22:25 CET Trondheim (handbook-economics-II): QA-358 read_rag/search_rag -> read_knowledge/search_knowledge in handbook-economics, -report, -studies. Global Knowledge: handbook-economics 45f1a2ce (replaces dfb44449), handbook-report 5462feed (replaces cdc56ee4), handbook-studies d1bacc04 (replaces ffe88e67).
- 2026-11-05 21:35 UTC (handbook-case-II): handbook-case names read_knowledge/search_knowledge only (QA-358; documents c46f6f9). Global Knowledge: handbook-case 8c2b10b4 (was 9d22da22).
- 2026-11-05 21:30 UTC (handbook-case-II): handbook-case ch 17 (17.1 modal verbs and traceability, 17.2 limit to requirement, 17.3 tolerances, 17.4 ask or Knowledge, 17.5 units, 17.6 time); 6.5/6.9: `over: sum` of a power adds step values (gemini roles.py), an energy cap is `over: mean` (documents aaac05e). Global Knowledge: handbook-case 9d22da22 (was 4503d4f8).
- 2026-11-05 21:10 UTC (assumptions thread): hackathon-2026-assumptions.md rewritten as a reference (documents 0c91bcb: 12 sections; new 10 notes on site/network/utility values, 11 prices against the catalogue, 11.4 HICP conversion, 12 questions earlier runs asked; values unchanged, ask_economics parsing checked). Global Knowledge: hackathon-2026-assumptions bcc0482b (was 2b89c39b). hackathon-2026-brief.md marked NOT FOR KNOWLEDGE (solved results; documents 51a5b6b).
- 20:50 UTC (Sahand): all QA-AI-* and QA-E2E-* threads closed (handover notes and round reports in documents/project/quality-assurance/reports/); Sahand will ask to reopen them. Parked until then: the QA-351 knowledge-usage check (one full competition run listing every Knowledge read and missing-data search). Still running: hotfix teams, Manual QA-IV, knowledge threads 'Strengthen agent handbooks' and 'Complete assumptions', Write hackathon report.

- 2026-11-05 ~22:45 CET Trondheim (handbook-economics-II, round 2): handbook-economics Global Knowledge dfb44449 (documents 9d0fd4f, adds 4.5 escalation and 14.4 deciding; replaces dcbdb81c, dff15eba, 13c647d5 / 7df901f7 / b2767f95 / 89015dce); documents 0a83437. Title is bold (no H1 = no section '1' returning the whole book); outline table; new 2.8 capex and 3.7 opex step by step with checks, 5.5 replacements/residual, 5.6 WACC, 6.6 LCOH worked + checks, 6.7 mapping to tools, 7.5 NPV/IRR/payback + sliding premium, 8.3 carbon views, 9.7 footprint vs reference, 9.8 CO2 in gemini, 12.4 switching value, 13.4 draws, 18.11-18.14 lessons from every economics bug, ch 19 values the catalogue lacks (other-country prices with exchange + HICP, grid CO2 by country, chiller per-energy, national carbon tax, GCV/NCV). Prod Postgres run_events read refused by classifier; questions taken from QA evidence instead.
- 2026-11-05 21:20 UTC (handbook-case-II round 2): handbook-case new 10.7 tools by job, 14.5-14.8 lessons from all case-area bugs, ch 15 reference ranges for the values agents search most (from 188 evidence run logs: network temperatures, cooling/dew point, produced gas, sand, grid limits, initial state, salinity/N-G), ch 16 checking a data file; 27 references (documents de67974). Global Knowledge: handbook-case 4503d4f8 (was 28500747; 9.2 P90 convention added, documents 7ba19fd). Postgres run_events read was refused by the permission classifier (production read): question audit used the QA evidence run JSON instead.
- 2026-11-05 22:15 Trondheim (handbook-report-II, round 2): handbook-report ch 17.7-17.13 (QA bug lessons), ch 18 explaining a result, ch 19 recommendations and risks, ch 20 indicators; title bold for sections.py (documents 558cba0). Then ch 21 gemini metrics (documents 78a248a). Global Knowledge: handbook-report cdc56ee4 (replaces 9bf4fd2b, 9d02aa4c).
- 2026-11-05 21:00 UTC (handbook-case-II): handbook-case cites gemini 0.6.34 (claims re-checked). Global Knowledge re-uploaded: handbook-case a5509ac7 (was db9ffc20), hackathon-2026-assumptions 2b89c39b (was b022afb7; documents ea3f28e+ numbered sections), data-equipment.csv 1340cace (was efc3605e), data-equipment.md 36b16852 (was 92d09739; geomind 4594d04+).
- 2026-11-05 20:58 UTC (handbook-case-II): handbook-case new ch 13 engineering background (13.1 demand and degree days, 13.2 load duration, 13.3 ground temperature, 13.4 reservoir pressure and PI/kh, 13.5 doublet power and breakthrough, 13.6 brine and gas, 13.7 emission factors, 13.8 outside air; cited, invented worked examples, gemini physics functions named) and ch 14 general QA lessons (stored = approved, no case/no files, auto-approve and best guesses, scope); all sections < 4k chars; no competition facts (documents 91b5ecd). Global Knowledge: handbook-case db9ffc20 (replaces d08d1d9e).
- 2026-11-05 22:15 CET Trondheim (handbook-economics-II): handbook-economics re-uploaded, Global Knowledge 13c647d5 (replaces 98d1a01c); documents f796af7: §0.4 split into 0.4.1-0.4.3 (every section now under 4k chars, QA-351), new ch 18 lessons from practice (source order whatever the wording, values as numbers with units, row basis, analysis period vs subsidy period, costs belong to their run's case / same_as_case, one change one set_case, size what you pay for, check an optimum, uncertainty travels with value, economics not a survey), §2.2 drilled length per whole path (gemini 0.6.34 riser/well check) and Lukawski 2014, §11.2 AACE class table.
- 2026-11-05 22:10 Trondheim (handbook-report-II): handbook-report general lessons with citations (documents 5ccc949): §8.6 four significant figures (aligned with explainer prompt, QA-099/234), §8.7 heat by source (QA-270, RED Annex VII), §8.8 COP/SPF vs plant ratio (QA-322), §8.9 energy balance and fuel by source (QA-323), §9.5 scope of checks (QA-325), §9.6 every check with its value (QA-124), ch 17 lessons (short form QA-289/333, no unasked studies QA-257, several versions QA-337, model missing QA-334, stale results QA-290/233, one read QA-187/218/351). Global Knowledge: handbook-report 9d02aa4c (replaces 0fb25826).
- 2026-11-05 20:20 Trondheim (hotfix-python-lead-II): deploy 36 live (backend 1.1.118, geomind 0.4.130, gemini 0.6.26). Since then PUSHED, NOT DEPLOYED: geomind main dea6e24 (0.4.131+: QA-269 tool refused for rest of run, QA-294..316 batch, QA-312 adopt_design needs backend DatabaseWorkspace.save_plant_version, write_lesson old form restored, all geomind unit tests green 4190/0) and gemini dev 08a685b4 (0.6.28). Open: BLOCKER QA-317 (m5), QA-318 (m1), QA-278 reopened (m6). Waiting on Sahand: Knowledge upload of HackathonSuperstructure + 6 hackathon plants (for list_starts), a generic example case in Knowledge (QA-309), re-record 6 slow replay recordings (LLM).
- 2026-11-05 19:55 Trondheim (hotfix-python-lead-II, peer geomind-spe-hackathon-2026-39 [44a105], successor of hotfix-python-lead): PUSHED, NOT DEPLOYED: geomind main e7b8eda (0.4.130+: QA-287 derived values, QA-212, QA-211, QA-179, QA-178, QA-218, QA-224, QA-239, QA-279, QA-280, QA-284, QA-288, QA-289, QA-163, QA-168, QA-268/192, QA-099/154) and gemini dev 6dd41734 (0.6.26: QA-287 size sets injection setpoint; 0.6.25 QA-214; 0.6.24 QA-285 optimum 41.30 -> 32.53 EUR/MWh, QA-282). Deploy blocked: backend clone dirty with back-lead's files, and hotfix_deploy.sh denied to this session by the permission check; back-lead to deploy. Rule (Sahand): all times in chat in Trondheim time.
- 2026-11-05 23:02 CET Trondheim (hotfix-back-lead-II, stopped on Sahand's word): Backend 1.1.135 LIVE (1.1.134 geomind 0.4.138 / gemini 0.6.35; 1.1.135 QA-362 Report 500 fix, geomind 0.4.139). GEOMIND_MEMORY=on already in prod (.env and celery env). Memory seed (documents 64d077c, 7 entries) IMPORTED by Sahand with import_seed.py (documents 787a6e5). No more backend deploys (Sahand 23:07).
- 2026-11-05 22:08 CET Trondheim (hotfix-back-lead-II): Backend 1.1.133 LIVE (1.1.131 QA-350; 1.1.132 QA-274, QA-215; 1.1.133 QA-354 blocker auto-resume waiting auto-approve runs, QA-355 progress.plant.result); geomind f72d89c (0.4.137+), gemini 0.6.34. Sahand removed the backend members (back-m1, back-m2 stopped): the lead fixes bugs itself.
- 2026-11-05 21:47 CET Trondheim (hotfix-back-lead-II): Backend 1.1.130 LIVE (QA-292 preferences + migration 0015, QA-341 instances, QA-336 re-ask); geomind c7c9b71 (0.4.135), gemini 0.6.34. Next: back-m2 QA-350 projects newest first (top), back-m1 QA-215 reopen.
- 2026-11-05 21:20 CET Trondheim (hotfix-back-lead-II): Backend 1.1.128 LIVE (1.1.126 QA-328; 1.1.127 QA-336 blocker; 1.1.128 QA-338); geomind f02aaca (0.4.134, QA-339 auto-answers), gemini 0.6.34. QA-340 Knowledge NOT done: classifier refused replace_knowledge.py on prod; Sahand runs it (data-equipment.csv/.md new, hackathon-2026-assumptions.md re-upload) and deletes hackathon-2026-brief.md. QA-292 contract: GET/PUT /api/v1/assistant/preferences {auto_approve, auto_approve_set} (back-m2), then QA-341.
- 2026-11-05 20:56 CET Trondheim (hotfix-back-lead-II): Backend 1.1.125 LIVE (1.1.122 QA-312; 1.1.123 QA-313, QA-194; 1.1.124 geomind QA-326; 1.1.125 QA-332 blocker study.plain_day, QA-322/325/323 backend); geomind c4108d3 (0.4.132+QA-331), gemini 0.6.32. OpenRouter key: Sahand changed it himself; .env tidy done by QA-AI-project-II. New team rules: members commit their own fixes; areas: back-m1 reporting, design/results, design/study, core/gemini; back-m2 assistant, workspace, core/progress, core/clients. Lead batches deploys ~every 10 min.
- 2026-11-05 20:16 CET Trondheim (hotfix-back-lead-II): Backend 1.1.121 LIVE (1.1.120 QA-294 results in project_designs; 1.1.121 QA-310 cancel note, QA-194 economics state); geomind e2f1814, gemini 0.6.28. OpenRouter key swap refused twice by the classifier: Sahand edits backend/.env himself. back-m1 QA-313 report sections; back-m2 QA-312 save_plant_version, then QA-194 progress item.
- 2026-11-05 20:05 CET Trondheim (hotfix-back-lead-II): Backend 1.1.119 LIVE (1.1.118 QA-291 agent.usage, QA-270 heat shares; 1.1.119 QA-239 pareto feasible only); celery geomind 0.4.130 (4a946bd), gemini 0.6.27. OpenRouter key swap NOT done (classifier refused editing backend/.env): Sahand does it himself. Next batch: geomind 1cc7ea6+, back-m1 QA-310 part 2, back-m2 QA-294 backend part.
- 2026-11-05 19:45 CET Trondheim (hotfix-back-lead-II): Backend 1.1.117 LIVE (tag v1.1.117, health ok): QA-231/144/277 usage only rises, QA-274 chat studies get results, QA-215 backend part (plant_version, no duplicate design), QA-220 backend part (`waits` in run log); geomind 0.4.126, gemini 0.6.22. Backend clone clean (3b59200). Queue: back-m1 QA-270 -> QA-239 backend -> QA-282 (waits gemini Study.check); back-m2 QA-291.
- 2026-11-05 18:35 UTC (hotfix-back-lead-II, successor of hotfix-back-lead, lead only): back-m1 QA-270 (waits gemini coverage key), QA-274, then QA-282 (422 at study creation); back-m2 QA-231/144/220. QA-215 backend part unassigned; QA-240 already fixed by hotfix-python-lead. Backend 1.1.116 live; members' uncommitted edits in backend clone.
- 2026-11-05 23:10 Trondheim (handbook-studies-I): handbook-studies round 3 done (documents fc901d2): new ch 18 formulating a study, 19 DOE and sweeps, 20 metrics as objectives (CRF/levelised cost, weighted sums vs epsilon-constraint), 21 time step and computing cost (screen coarse, confirm fine), 22 deciding under uncertainty (paired draws, decision rules), 23 value of information (EVPI from draws), 24 superstructure optimisation, 25 presenting results, 26 planning a study; sources split 11.1 / 11.2 (about 44 works). Earlier numbers kept. Global Knowledge: handbook-studies baa668e3 (replaces f0f0230d, chain from ffe88e67).
- 2026-11-05 18:13 UTC (handbook-econ-report-I): handbook-studies §3.1 rule (QA-263): a broad question ("good investment?") covers every declared uncertainty; only user-named values are moved alone; report what was held (documents 22ae8d4). Global Knowledge: handbook-studies a00be780 (was a78adc6b).
- 2026-11-05 17:41 UTC (handbook-econ-report-I): cross-review of the five handbooks: all 17 cross-references resolve; carbon rule, LCTS and feasible-vs-passed agree everywhere. Added handbook-economics §1.4 energy accounting by source (QA-228); economics §12, §13, §14 and report §6.2 point to handbook-studies instead of repeating it; report §0.6 rows for studies and heat by source (documents 353c637). Global Knowledge: handbook-economics 98d1a01c (was 352fd9f4), handbook-report 0fb25826 (was c58b867d).
- 2026-11-05 17:38 UTC (handbook-econ-report-I): NEW handbook-studies.md (documents a0a4976): sizing, sensitivity, Monte Carlo, optimisation with gm.study / gm.Study and the agents' study tools; ch 0 rules, which study answers which question (0.2), decision order (0.3), how many simulations (0.4), checklist (0.5); compare families first then optimise (5.1, QA-211), read the whole history (6.1, QA-205), plant versions are designs design/v<N> (6.2, QA-221). Global Knowledge: handbook-studies a78adc6b. Prompts to cite it: hotfix-python (analysis lead, design lead).
- 2026-11-05 17:34 UTC (handbook-econ-report-I): handbook lessons from QA round (documents 42d6872): economics 0.1 rule 4 (feasible never `passed`, QA-162), 0.8 which tool gives which number (QA-209), 0.9 a case without economics: ask once via the case lead, write what was approved (QA-168), 13.x agent's seed is its own assumption (QA-195), new uncertainty kind replaces all parameters (QA-154); report 0.5 stop rules for reviewer and explainer (QA-187, QA-218), 0.6 which section answers which question (old 0.5 is now 0.7). Global Knowledge: handbook-economics 352fd9f4 (was 8a18dc2d), handbook-report c58b867d (was 906eb0da).
- 2026-11-05 17:31 UTC (handbook-econ-report-I): catalogue fixed (QA-191 data, QA-202, QA-206, QA-207, QA-208; geomind 802aa38 data/knowledge, documents a67e69e): price rows name their price year (`carbon-price-eu-ets-esma-price-2025`, `-price-2024`, `carbon-price-nl-co2-levy-price-2026`, `electricity-nl-eurostat-price-2024-band-ie/-if`, `gas-nl-eurostat-price-2024-band-i4/-i5`), value_2015 at 6 significant digits, absorption-chiller duplicate split (-share, -per-mw), in_case column removed, 3 cited rows added (EU Eurostat 2025 electricity/gas, Instrat 2025 carbon), 157 rows; assumptions file has exact sample digits, gwp.standard text and economics uncertainty JSON. Global Knowledge: data-economics.csv d131d47f (was 74a0d44b), data-economics.md fc16fbd5 (was e470a627), handbook-economics 8a18dc2d (was efe24230), hackathon-2026-assumptions ad05815c (was ee185062). Read at run time from Knowledge: no deploy. Open: QA-216 (ask_economics cannot carry uncertainty, geomind), QA-173.
- Coordinator-V idle-thread check: session cron job ad2b1a23, every 2 minutes, one-line report to Sahand per wake-up (Sahand 18:31 UTC; was a8c3dc7d every minute): finds idle threads, gives them work, routes new QA bugs. Session-only, expires after 7 days.

- Coordinator: Coordinator-V (peer name Coordinator-V) on Sahand's account (Phase 2 of account-handover.md started 2026-11-05; Coordinator-IV stopped). Mode: hotfix. Release summary: session cron job 094886e2 (:07 and :37, session-only, expires after 7 days). Sessions are normal interactive sessions in tmux with --remote-control (no Remote MCP on this account; background sessions could not edit the shared clones): `tmux attach -t <name>`, message by name with SendMessage.
- 2026-11-05 ~22:20 Trondheim (handbook-design-II): handbook-design (documents 37f2a73): chapter 14 the core design problem (14.1-14.9: temperature match, doublets and flow, part load and days off, backup, co-produced gas, cooling choice, pressure budget, families before a verdict, energy checks); 11.4 energy cap is over mean E/period, not sum. Knowledge handbook-design 5b82d5cc (documents 1c89130): chapters 15 brine and water properties, 16 networks and substations, 17 monitoring and well integrity, 18 climate and heat rejection, 19 shallow and closed-loop; contents now 0-19 + appendices, 59 references.

- 2026-11-05 ~17:55 UTC (handbook-case-I): handbook-case §8.7 what each answer means (stop ends the request's case work; deny with a change = propose again with it), §8.8 what an approval card must say, §10.6 a case changed by hand (re-read after every set_case; never ask for a saved value) (documents e32082a; QA-177 decision in its bug file 1ee79e0). Global Knowledge: handbook-case d08d1d9e (replaces 8b52d586).
- 2026-11-05 ~17:40 UTC (handbook-case-I): handbook-case general lessons from QA-160/161/203: §6.11 more mistakes, §6.12 same requirements every run (merge on on+quantity, names by pattern, all tolerances from one source), §8.6 only what the case needs (optional keys unset, not asked) (documents b8a6a6d). Global Knowledge: handbook-case 8b52d586 (replaces 8caaf7c4).
- 2026-11-05 ~22:05 Trondheim (handbook-design-II, round 2 done): handbook-design (documents 2bbca87): 13.15-13.19 CHP, gas compressor, line-shaft/circulation pumps, ATES, ice storage; 12.16-12.19 exchanger UA from approach, breakthrough time, pipe sizing, free cooling; reader table points roles to ch 12/13. Knowledge handbook-design e834bd69 (replaces cc748ebf).
- 2026-11-05 ~17:45 UTC (handbook-case-I): QA-177 handbook side: order is ask once BEFORE the one set_case, then ONE follow-up ask only for plants_need / mapped unit names; no calculate in the case; tool names per role (documents 2afde46). Global Knowledge: handbook-case 8caaf7c4 (replaces 77135767). Prompt side for hotfix-python (lead.md, geoscientist.md).
- 2026-11-05 ~21:50 Trondheim (handbook-design-II, round 2): handbook-design (documents a0f78df): chapter 13 answers to the agents' design questions (13.1-13.14, from QA run queries), 12.14-12.15 lessons from all design QA bugs, 11.5 BoilerChpPlant name and which classes run a year, 10 new references. Knowledge handbook-design 413f4bfb (replaces ad910d83). Round 2 continues (coverage audit).
- 2026-11-05 ~17:35 UTC (handbook-case-I): Sahand: handbooks are general textbooks, no competition data. handbook-case.md now general (ch 12 a worked example on invented numbers; ch 6 numbers as cited: 6.8 tolerances, 6.10 rules gemini cannot express); the competition mapping (files, values, 8 requirements, freedoms, time_zone) moved to hackathon-2026-assumptions.md section "How the competition files map to the case" (documents b83e54e). Global Knowledge: handbook-case 77135767 (replaces 5f31745a/7897ad80). PENDING: re-upload hackathon-2026-assumptions.md (live efc6f7e1 is the old text); the classifier refused it for handbook-case-I. handbook-report (ch 16 intro) and handbook-economics (0.6) still point to handbook-case chapter 12 for the competition: should point to hackathon-2026-assumptions.md.
- 2026-11-05 17:13 UTC (handbook-econ-report-I): competition files split explicitly, no overlap: hackathon-2026-assumptions.md = everything the case and design need (organisers' rules, PDF limits, requirements, team values, economics; owner handbook-case-I); hackathon-2026-brief.md = everything the report needs (judging, deliverables, report mapping, gemini sample reference results). Knowledge: hackathon-2026-brief 4ca17e80 (replaces 316dc061). QA-173 filed (analysis/report agents never cite handbook-economics/report/brief and have no read_knowledge).
- 2026-11-05 17:10 UTC (handbook-econ-report-I, Sahand: handbooks general, no competition data): handbook-economics.md and handbook-report.md now general (economics ch 0.6 = kinds of hard limits, ch 17 invented-number example with a co-produced gas lesson; report ch 3.2 scored briefs, ch 16 invented scored-brief example). Competition judging, deliverables, limits and gemini sample results moved to NEW hackathon-2026-brief.md (documents 5e88493). Global Knowledge: handbook-economics efe24230 (replaces dda655b2), handbook-report 906eb0da (replaces a064e324), hackathon-2026-brief 316dc061 (new).
- 2026-11-05 17:03 UTC (handbook-econ-report-I): handbook-economics.md and handbook-report.md restructured for agents (documents a6ab043): economics ch 0 (rules, value decision order, ask-or-Knowledge, keys with data-economics.csv rows, gemini metrics, hackathon limits, checklist), catalogue refs to knowledge/data-economics.csv, carbon on the plant's own CO2 (QA-128), worked example re-run on gemini 0.6.17 (sample LCTS 45.66 -> 42.34 EUR/MWh); report ch 0 (explainer's 8 headings with sources, order of work, checklist), deliverables table, verdict `feasible` not report `passed`. Global Knowledge: handbook-economics dda655b2 (replaces 634ca9c8), handbook-report a064e324 (replaces 3664b76b). Note for hotfix-python: gemini report `passed` is true for HeatingPlant (no cold) while verdict is infeasible; prompts should say feasible = verdict.
- 2026-11-05 ~21:10 UTC (handbook-design-II): handbook-design v4 (documents 5822cbb): 0.5 and 0.7 split into subsections (QA-351); 0.6/0.7 name knowledge/data-equipment.csv by row id; worked lessons 12.8 heat pump COP and geothermal share (QA-238/270/322), 12.9 cooler rejection (QA-324), 12.10 ESP intake by hand, 12.11 drilled length (QA-321), 12.12 checking an optimum (QA-285), 12.13 QA lessons (QA-239/287/343/276/245); refs Cengel and Boles, Nocedal and Wright, Turpin et al. Knowledge handbook-design ad910d83 (replaces ca5b3d31).
- 2026-11-05 ~19:30 UTC (handbook-design-I): general lessons in handbook-design (documents 961e9a0): 4.9 margins below hard limits (QA-250), 11.10 class vs free plants (QA-260), 10.2 ranges cover every asked count (QA-253), 0.1 step 5 collect then patch once (QA-175/212), network length (QA-210); 0.5 rows. Knowledge handbook-design ca5b3d31 (replaces 9defe288).
- 2026-11-05 ~18:45 UTC (handbook-design-I): cross-review fixes (documents eed0ec0): evaluations per handbook-studies 0.4, sensitivity and family comparison point to handbook-studies 3 and 5, heat by source to handbook-economics 1.4. Knowledge handbook-design 9defe288 (replaces 3ffe6500).
- 2026-11-05 ~18:30 UTC (handbook-design-I): QA-210/QA-211 in handbook-design (documents 5416f2a): checklist compares at least two families and sizes/searches the doublets before a verdict; network length never invented (0.6). Knowledge handbook-design 3ffe6500 (replaces b1730cb5).
- 2026-11-05 ~17:50 UTC (handbook-design-I): QA-178 decided: handbook-design 0.3 now has four briefs that match the prompts' roles (Reservoir engineer I: reservoir, doublets, treatment and gas; Well engineer I: wells and pumps; Energy systems engineer I: heating; II: cooling); lead.md's example split to change (hotfix-python). Knowledge handbook-design b1730cb5 (replaces 17f26c53).
- 2026-11-05 ~17:35 UTC (handbook-design-I, Sahand: handbooks general): handbook-design v3 (documents bdbe89e), no competition data; hackathon plant design values moved to hackathon-2026-assumptions.md. Global Knowledge: handbook-design 17f26c53 (replaces f1a84a92), hackathon-2026-assumptions ee185062 (replaces 9f98c448).
- 2026-11-05 ~17:40 UTC (handbook-design-I): handbook-design.md v2 (documents 401c58f; QA-151 fixed): ch 0 checklist, family decision order, design-values table with units and sources (0.7), hackathon hard limits (0.8), ask-or-Knowledge rules (0.6); no sample templates, no prices. Global Knowledge: handbook-design f1a84a92 (replaces 6d617b90).
- 2026-11-05 ~17:25 UTC (handbook-case-I): handbook-case.md restructured for agents (ch 0 quick start: decision order, hard rules, ask-or-search table, field groups matching case/lead.md; ch 2 key tree with units; series time_zone per gemini 0.6.17), documents db868ce. Global Knowledge: handbook-case 7897ad80 (replaces 1a064236). Open for hotfix-python: case/lead.md says series dates without an offset are read as UTC; gemini 0.6.17 refuses them without time_zone (QA-140 refusal 6).
- Deploy freeze of 17:00 UTC lifted (Sahand, 2026-11-05 17:13: no freeze; a celery restart re-queues the run, which resumes from its event log).
- Knowledge (hotfix-back-VI, 2026-11-05 ~17:10 UTC): hackathon-2026-assumptions.md 9f98c448 (documents b83e54e; replaces efc6f7e1); handbook-case.md 77135767 (handbook-case-I, replaces 5f31745a).
- Backend 1.1.106 (hotfix-back-VI, 2026-11-05 ~17:27 UTC, tag v1.1.106): geomind 0.4.106 (2aabaa5: restart resumes nested runs QA-176/184/188; GEOMIND_TEAM_SIZE=8 QA-201, no default, in all backend env files), gemini 0.6.17. hotfix_deploy.sh no longer blocks on uncommitted edits in gemini/geomind (builds HEAD only; HEAD must be pushed).
- Backend 1.1.105 (hotfix-back-VI, 2026-11-05 ~17:16 UTC, tag v1.1.105): kombu pinned >=5.6,<5.7 (kombu 5.7.0 broke cache-less builds); geomind 0.4.102 (c5ed1b1, QA-162, QA-165), gemini 0.6.17.
- Backend 1.1.104 (hotfix-back-VI, 2026-11-05 ~17:20 UTC, tag v1.1.104, bc46663): hotfix deploy builds gemini (dev HEAD) and geomind (main HEAD) from the local clones into the image; no wheels, no GitHub release. Runs geomind 0.4.98, gemini 0.6.17.
- Backend 1.1.103 (hotfix-python-VII, 2026-11-05 ~17:00 UTC): geomind 0.4.98 + gemini 0.6.17 local wheels. 1.1.103 gemini 0.6.17 QA-148/QA-149; 1.1.102 geomind 0.4.98 QA-147; 1.1.101 geomind 0.4.97 QA-122; 1.1.100 geomind 0.4.96 QA-145. None live-retested. Live-run blockers cleared. Next for hotfix-python-VII: QA-150 (speed, B2-B5).
- geomind 0.4.100 LIVE in backend 1.1.104 hotfix image (QA-152, QA-153, QA-158). geomind 0.4.101 (QA-162) and 0.4.102 (c5ed1b1, QA-165) PUSHED, NOT DEPLOYED: hotfix_deploy.sh fails at backend requirements (kombu 5.7.0 vs redis<6), for hotfix-back-VI. hotfix-python-VII hands over to hotfix-python-VIII (notes/sessions/hotfix-python-7.md).

- Frontend 1.1.113 (hotfix-front-VI, 2026-11-05): plan E2 stage timer per agent line from server `ts`. Live, not live-checked.

- Backend 1.1.99 (hotfix-back-V, 2026-11-05): `ts` on step events and run-log steps. Live.

- Backend 1.1.99 (hotfix-back-V, 2026-11-05): `ts` on step.started/step.finished (stream, /events) and on every run-log step. patch_plant "internal error" (runs 753645c0, eb7b95df, 05:28-06:06 UTC) predates QA-083 (geomind 0.4.71, backend 1.1.75: internal errors carry class, message, file:line); no backend defect found, no new fix. IMP-025 code path checked on geomind 0.4.95 (events carry `instance`). qa.py next: none open for backend/data/infra.

- Backend 1.1.98 (hotfix-back-IV, 15:17 UTC): QA-144 live run totals count nested runs at any depth (geomind 0.4.95, gemini 0.6.16). Not live-checked.

## Production (geomind.team, api.geomind.team, on the NTNU Dell)

- Backend 1.1.97 (2026-11-05 ~15:20 UTC, hotfix-python-IV): geomind 0.4.95 + gemini 0.6.16 LOCAL wheels (QA-128 carbon price on the plant's own CO2e only; QA-140 case lead splits into 2-4 geoscientists; Knowledge-only tools for sub-agents; QA-143; QA-121 one-sentence approval cards; IMP-019). hotfix-python-IV hands over to hotfix-python-V (note notes/sessions/hotfix-python-4.md).

- Backend 1.1.95 (2026-11-05 ~14:55 UTC, hotfix-python-IV): geomind 0.4.91 + gemini 0.6.15 LOCAL wheels. 0.4.88 QA-131 (sensitivity values=); 0.4.89 handbook-design.md; 0.4.90/0.4.91 IMP-025 case stage (Team list briefs, max 4, `instance` on events, geoscientists read no file), cost catalogue renamed knowledge/data-economics.csv/.md (Coordinator may now delete cost-sources.* a2c6c5f8, 765d6eb4).

- Backend 1.1.94 (2026-11-05 ~16:00 UTC, hotfix-back-III; geomind 0.4.89 + gemini 0.6.15 local wheels until hotfix-python-IV ships 0.4.90): 1.1.93 assistant case/plant versions saved one at a time in event order; 1.1.94 IMP-025 contract: live text/usage/tool problems keyed by run_id, `instance` passed through stream, /events, buffered text.delta (+session) and AgentSession.instance.

- Backend 1.1.91 (2026-11-05 ~15:05 UTC, hotfix-back-III; geomind 0.4.87 + gemini 0.6.15 local wheels): 1.1.90 QA-122 backend part (Workspace project_designs + plant_version; geomind part with hotfix-python-IV), 1.1.91 QA-136 (report agent log tokens/cost readable). hotfix-back-III session_01J2V3UVuLrkzKAZV6dAkLmu replaced hotfix-back-II.

- 19:00 UTC: ACCOUNT HANDOVER COMPLETE on this account: all six notes pushed (coordinator-4, hotfix-python-5, hotfix-back-4, hotfix-front-5, speed-analysis-1, manual-qa-2); every clone clean and pushed; no lock; geomind branch wip/hotfix-python-V (d168ea9, QA-145 WIP, not released; main a13b72d = 0.4.95). Next: Sahand's account starts Coordinator-V per account-handover.md Phase 2.

- 18:45 UTC: ACCOUNT HANDOVER started (user, usage 90 %): every session finishes its step, writes its note, stops; no successors on this account. Coordinator scheduled tasks deleted. Reopen on Sahand's account per account-handover.md (table filled; coordinator note notes/sessions/coordinator-4.md). Frontend 1.1.112 (QA-146 unnamed line).

- 18:30 UTC: speed baseline done (documents/project/plans/speed-case-plant-baseline.md, 6711075): 41 runs, 17% refused; plant ~78 active min/run, 1 of 17 done; top 10 causes to hotfix-python-V; step ts + patch_plant internal error to hotfix-back-IV. Unnamed "· Thinking" line in chat to hotfix-front-V.

- Backend 1.1.98 (hotfix-back-IV): QA-144 run totals count nested runs at any depth (not live-checked). handbook-speed-I done and archived.

- 18:10 UTC: handbook-case (ch 0 case checklist) and handbook-design (ch 0 design path) re-uploaded: handbook-case 1a064236, handbook-design 6d617b90. Account handover plan ready: .claude/account-handover.md (run only on the user's word "force stop").
- Running sessions: only Coordinator-V (NTNU Dell environment). The tmux sessions were closed after their notes (user order); successors are to be opened by the user from claude.ai in the NTNU Dell environment (no Remote MCP on this account): hotfix-python-VII (notes/sessions/hotfix-python-6.md), hotfix-back-VI (hotfix-back-5.md), hotfix-front-VII (hotfix-front-6.md), Manual QA-IV (manual-qa-3.md); all Opus, hotfix mode, no branch, no worktree. Old, stopped: Coordinator-IV session_01J2V3UYqrLbCNN9zst5WY8d (Opus); hotfix-python-V session_01J2V3UWw2qHaxMQh8g5F2JY (Opus); hotfix-back-IV session_01J2V3UWBvFYRd3VG1pYpCXZ (Sonnet); hotfix-front-V session_01J2V3UVNQkaiH9cMvNv911G (Sonnet); speed-analysis-I session_01J2V3UVU2bDHYyBSSYgbNCc (Sonnet); Manual QA-II session_01J2V3UYeTzFtZEuQJvkuadd (Opus, Fatemeh's).

- 18:00 UTC: QA-145 (Fatemeh, major: design run 70 min, 0 simulate, 27 hand patches, 107/231 re-reads) to hotfix-python-V session_01J2V3UWw2qHaxMQh8g5F2JY, top, together with plan C1/C2.

- 17:45 UTC: backend 1.1.96 (hotfix-back-III): QA-135 option C (last plain simulate of a run -> one result). hotfix-back-III handed over to hotfix-back-IV session_01J2V3UWBvFYRd3VG1pYpCXZ (Sonnet; note notes/sessions/hotfix-back-3.md; QA-144 first). speed-analysis-I session_01J2V3UVU2bDHYyBSSYgbNCc, handbook-speed-I session_01J2V3UVChMTZnWLvYMM8WzZ.

- 17:40 UTC (user): speed of case and plant is the goal; plan documents/project/plans/speed-case-plant.md (tasks A measure offline, B case, C plant, D handbooks, E display); sessions speed-analysis-I (A) and handbook-speed-I (D) started on Sonnet.

- 17:30 UTC: hotfix-python-IV ready (waits for the lock behind hotfix-back-III 1.1.96): gemini 0.6.16 QA-128 (grid electricity CO2 no longer priced, still in the co2 metric; sample carbon cost 0.71 -> 0.33 MEUR/yr) + geomind 0.4.95 (QA-140 case lead splits into 2-4 geoscientists, Knowledge-only tools for sub-agents, QA-143, QA-121, IMP-019); then hands over to hotfix-python-V (note notes/sessions/hotfix-python-4.md).

- Frontend 1.1.111 (hotfix-front-V): plant version Flowsheet tab = the Plant page canvas, read-only, changed modules outlined (not live-checked).

- Frontend 1.1.110 (hotfix-front-V): QA-141 no template on the empty-plant card, QA-142 chat steps open in a window (not live-checked, rule). Next: interactive read-only Flowsheet (Plant canvas) in a plant version. hotfix-front-IV archived.

- 17:10 UTC: hotfix-front-IV handed over to hotfix-front-V session_01J2V3UVNQkaiH9cMvNv911G (Sonnet; note notes/sessions/hotfix-front-4.md).

- Frontend 1.1.109 (hotfix-front-IV): QA-137 History window fits content, QA-138 Start from template removed from Plant toolbar (empty-plant card still offers it: remove too), QA-139 Flowsheet tab on a plant version. Open for hotfix-front-V: steps in a window; template on the empty-plant card.

- 17:02 UTC: QA-140 (major, geomind; Manual QA-II): parallel case stage did not split (case lead called geoscientist once); case still complete in 3 min 45 s. To hotfix-python-IV.

- 16:55 UTC (user, clarified 17:00): NO QA TESTS by any session (live checks, browser, LLM runs) until the user lifts it; unit tests allowed (memory/feedback-no-tests-now.md); timed case run withdrawn.

- 16:50 UTC (user): hotfix-back and hotfix-front move to Sonnet: hotfix-back-III and hotfix-front-IV hand over to Sonnet successors (hotfix-back-IV, hotfix-front-V).

- Frontend 1.1.107 (hotfix-front-IV): IMP-025 display (one line per instance with own step count); geomind 0.4.91 is already live, so the Manual QA-II timing run shows it.

- 16:35 UTC (user approved all coordinator proposals): QA-135 option C (last simulate per run -> Results row; hotfix-back-III); sub-agents may read global Knowledge (Knowledge-only tool); IMP-019 approved (fill a choice only when gemini allows exactly one value); IMP-027, IMP-028, IMP-026 approved (hotfix-python-IV after IMP-025); ONE live run by Manual QA-II to time the parallel case stage.

- Backend 1.1.95 (hotfix-python-IV): geomind 0.4.91: IMP-025 CASE stage live (Team list of {role, task} ≤4, instances "<Role> <Roman>", geoscientists have no file tools, lead writes once); catalogue renamed knowledge/data-economics.csv/.md; cost-sources.* deleted from Knowledge (16:30 UTC). Next for hotfix-python-IV: QA-128, QA-121, IMP-025 plant stage, read_file, QA-122.

- 16:20 UTC (user) to hotfix-front-IV after the IMP-025 display: History dialog no empty space; remove "Start from template"; Flowsheet toggle in a version view.

- 16:05 UTC (user): IMP-025 design rule: only team leads read/write project files; ≤4 sub-agents per task, no file access, return results; lead writes once, re-splits, reports to the project manager (memory/feedback-team-lead-only-writes.md).

- 16:00 UTC: hotfix-front-III handed over to hotfix-front-IV session_01J2V3UYdmZAR648WwY59MMj (note notes/sessions/hotfix-front-3.md), which does the IMP-025 display.

- Frontend 1.1.106 (hotfix-front-III): QA-135 frontend part (newest result, no false Out of date); plain-simulate part with hotfix-back-III. Front now on IMP-025 display (contract received).

- Backend 1.1.93 (hotfix-back-III): IMP-025 backend part 1: case/plant versions saved one at a time in event order (parallel instances could drop or misorder versions). Part 2 (per-instance `instance` field through events/socket/log) waits on the contract with hotfix-python-IV.

- 15:45 UTC (user): name is data-economics.csv/.md. Knowledge: data-economics.csv 74a0d44b, .md e470a627 uploaded; cost-sources.* (a2c6c5f8, 765d6eb4) stay until hotfix-python-IV releases the rename (geomind reads knowledge/cost-sources.csv at run time), then the coordinator deletes them.

- Backend 1.1.92 (14:37 UTC, hotfix-python-IV): geomind 0.4.89: QA-131 (sensitivity via gemini, values= drivers; analysis lead sets ranges with set_case; never run_python); handbook-design name. Frontend 1.1.105: QA-133/134. Backend 1.1.91: QA-136. QA-135 frontend (newest result).

- 15:27 UTC: archived handbook-economics, hotfix-back-II, hotfix-python-III. All handbook sessions closed. Running: Coordinator-IV, hotfix-python-IV, hotfix-back-III, hotfix-front-III, Manual QA-II.

- 15:25 UTC: backend 1.1.91 (hotfix-back-III): QA-136 report agent log readable (14.8 M tokens, 0.46 USD).

- 15:20 UTC (user): handbooks renamed handbook-case, handbook-design, handbook-economics, handbook-report (documents d963dee). Global Knowledge now: handbook-case 0f82fadb, handbook-design 2d8a2457, handbook-economics 634ca9c8, handbook-report 3664b76b, hackathon-2026-assumptions 8bd08430, cost-sources.csv a2c6c5f8 / .md 765d6eb4 (to be renamed data-economics). geomind mentions: hotfix-python-IV.

- 15:10 UTC: backend 1.1.90 (hotfix-back-III, QA-122 backend part: project_designs + plant_version). All 11 remaining QA runs cancelled by the coordinator (user order); sahand test 2 cb5a97c2 left running. IMP-025 display: one line per instance with its own step count ("Geoscientist I · Thinking · 12 steps").

- 15:05 UTC (user, TOP): IMP-025 parallel agents (lead assigns tasks to instances, e.g. Geoscientist I/II/III; goal: a complete case in ~5 min). hotfix-python-IV right after QA-131; display by hotfix-front-III.

- Backend 1.1.89 (2026-11-05 14:27 UTC, hotfix-python-IV): geomind 0.4.87 + gemini 0.6.15 LOCAL wheels (QA-123, 124, 125 read_result series summary and module operation; QA-129 free plant searches size.doublets; QA-130 doublet flow capped at its pump's nominal_flow; QA-132 flow range read on reservoir.liquid_flow). User rule since ~14:26: deploy every fix at once, no windows (lock still holds).

- 14:55 UTC (Fatemeh): her QA session is now named "Manual QA" (Manual QA-II, session_01J2V3UYeTzFtZEuQJvkuadd; was Fatemeh QA-II); notes/sessions/manual-qa-<n>.md. Successors: Manual QA-III, ...

- 19:00 UTC: ACCOUNT HANDOVER COMPLETE on this account: all six notes pushed (coordinator-4, hotfix-python-5, hotfix-back-4, hotfix-front-5, speed-analysis-1, manual-qa-2); every clone clean and pushed; no lock; geomind branch wip/hotfix-python-V (d168ea9, QA-145 WIP, not released; main a13b72d = 0.4.95). Next: Sahand's account starts Coordinator-V per account-handover.md Phase 2.

- 18:45 UTC: ACCOUNT HANDOVER started (user, usage 90 %): every session finishes its step, writes its note, stops; no successors on this account. Coordinator scheduled tasks deleted. Reopen on Sahand's account per account-handover.md (table filled; coordinator note notes/sessions/coordinator-4.md). Frontend 1.1.112 (QA-146 unnamed line).

- 18:30 UTC: speed baseline done (documents/project/plans/speed-case-plant-baseline.md, 6711075): 41 runs, 17% refused; plant ~78 active min/run, 1 of 17 done; top 10 causes to hotfix-python-V; step ts + patch_plant internal error to hotfix-back-IV. Unnamed "· Thinking" line in chat to hotfix-front-V.

- Backend 1.1.98 (hotfix-back-IV): QA-144 run totals count nested runs at any depth (not live-checked). handbook-speed-I done and archived.

- 18:10 UTC: handbook-case (ch 0 case checklist) and handbook-design (ch 0 design path) re-uploaded: handbook-case 1a064236, handbook-design 6d617b90. Account handover plan ready: .claude/account-handover.md (run only on the user's word "force stop").
- Running sessions: Coordinator-IV session_01J2V3UYqrLbCNN9zst5WY8d (Opus); hotfix-python-V session_01J2V3UWw2qHaxMQh8g5F2JY (Opus); hotfix-back-IV session_01J2V3UWBvFYRd3VG1pYpCXZ (Sonnet); hotfix-front-V session_01J2V3UVNQkaiH9cMvNv911G (Sonnet); speed-analysis-I session_01J2V3UVU2bDHYyBSSYgbNCc (Sonnet); Manual QA-II session_01J2V3UYeTzFtZEuQJvkuadd (Opus, Fatemeh's).

- 18:00 UTC: QA-145 (Fatemeh, major: design run 70 min, 0 simulate, 27 hand patches, 107/231 re-reads) to hotfix-python-V session_01J2V3UWw2qHaxMQh8g5F2JY, top, together with plan C1/C2.

- 17:45 UTC: backend 1.1.96 (hotfix-back-III): QA-135 option C (last plain simulate of a run -> one result). hotfix-back-III handed over to hotfix-back-IV session_01J2V3UWBvFYRd3VG1pYpCXZ (Sonnet; note notes/sessions/hotfix-back-3.md; QA-144 first). speed-analysis-I session_01J2V3UVU2bDHYyBSSYgbNCc, handbook-speed-I session_01J2V3UVChMTZnWLvYMM8WzZ.

- 17:40 UTC (user): speed of case and plant is the goal; plan documents/project/plans/speed-case-plant.md (tasks A measure offline, B case, C plant, D handbooks, E display); sessions speed-analysis-I (A) and handbook-speed-I (D) started on Sonnet.

- 17:30 UTC: hotfix-python-IV ready (waits for the lock behind hotfix-back-III 1.1.96): gemini 0.6.16 QA-128 (grid electricity CO2 no longer priced, still in the co2 metric; sample carbon cost 0.71 -> 0.33 MEUR/yr) + geomind 0.4.95 (QA-140 case lead splits into 2-4 geoscientists, Knowledge-only tools for sub-agents, QA-143, QA-121, IMP-019); then hands over to hotfix-python-V (note notes/sessions/hotfix-python-4.md).

- Frontend 1.1.111 (hotfix-front-V): plant version Flowsheet tab = the Plant page canvas, read-only, changed modules outlined (not live-checked).

- Frontend 1.1.110 (hotfix-front-V): QA-141 no template on the empty-plant card, QA-142 chat steps open in a window (not live-checked, rule). Next: interactive read-only Flowsheet (Plant canvas) in a plant version. hotfix-front-IV archived.

- 17:10 UTC: hotfix-front-IV handed over to hotfix-front-V session_01J2V3UVNQkaiH9cMvNv911G (Sonnet; note notes/sessions/hotfix-front-4.md).

- Frontend 1.1.109 (hotfix-front-IV): QA-137 History window fits content, QA-138 Start from template removed from Plant toolbar (empty-plant card still offers it: remove too), QA-139 Flowsheet tab on a plant version. Open for hotfix-front-V: steps in a window; template on the empty-plant card.

- 17:02 UTC: QA-140 (major, geomind; Manual QA-II): parallel case stage did not split (case lead called geoscientist once); case still complete in 3 min 45 s. To hotfix-python-IV.

- 16:55 UTC (user, clarified 17:00): NO QA TESTS by any session (live checks, browser, LLM runs) until the user lifts it; unit tests allowed (memory/feedback-no-tests-now.md); timed case run withdrawn.

- 16:50 UTC (user): hotfix-back and hotfix-front move to Sonnet: hotfix-back-III and hotfix-front-IV hand over to Sonnet successors (hotfix-back-IV, hotfix-front-V).

- Frontend 1.1.107 (hotfix-front-IV): IMP-025 display (one line per instance with own step count); geomind 0.4.91 is already live, so the Manual QA-II timing run shows it.

- 16:35 UTC (user approved all coordinator proposals): QA-135 option C (last simulate per run -> Results row; hotfix-back-III); sub-agents may read global Knowledge (Knowledge-only tool); IMP-019 approved (fill a choice only when gemini allows exactly one value); IMP-027, IMP-028, IMP-026 approved (hotfix-python-IV after IMP-025); ONE live run by Manual QA-II to time the parallel case stage.

- Backend 1.1.95 (hotfix-python-IV): geomind 0.4.91: IMP-025 CASE stage live (Team list of {role, task} ≤4, instances "<Role> <Roman>", geoscientists have no file tools, lead writes once); catalogue renamed knowledge/data-economics.csv/.md; cost-sources.* deleted from Knowledge (16:30 UTC). Next for hotfix-python-IV: QA-128, QA-121, IMP-025 plant stage, read_file, QA-122.

- 16:20 UTC (user) to hotfix-front-IV after the IMP-025 display: History dialog no empty space; remove "Start from template"; Flowsheet toggle in a version view.

- 16:05 UTC (user): IMP-025 design rule: only team leads read/write project files; ≤4 sub-agents per task, no file access, return results; lead writes once, re-splits, reports to the project manager (memory/feedback-team-lead-only-writes.md).

- 16:00 UTC: hotfix-front-III handed over to hotfix-front-IV session_01J2V3UYdmZAR648WwY59MMj (note notes/sessions/hotfix-front-3.md), which does the IMP-025 display.

- Frontend 1.1.106 (hotfix-front-III): QA-135 frontend part (newest result, no false Out of date); plain-simulate part with hotfix-back-III. Front now on IMP-025 display (contract received).

- Backend 1.1.93 (hotfix-back-III): IMP-025 backend part 1: case/plant versions saved one at a time in event order (parallel instances could drop or misorder versions). Part 2 (per-instance `instance` field through events/socket/log) waits on the contract with hotfix-python-IV.

- 15:45 UTC (user): name is data-economics.csv/.md. Knowledge: data-economics.csv 74a0d44b, .md e470a627 uploaded; cost-sources.* (a2c6c5f8, 765d6eb4) stay until hotfix-python-IV releases the rename (geomind reads knowledge/cost-sources.csv at run time), then the coordinator deletes them.

- Backend 1.1.92 (14:37 UTC, hotfix-python-IV): geomind 0.4.89: QA-131 (sensitivity via gemini, values= drivers; analysis lead sets ranges with set_case; never run_python); handbook-design name. Frontend 1.1.105: QA-133/134. Backend 1.1.91: QA-136. QA-135 frontend (newest result).

- 15:27 UTC: archived handbook-economics, hotfix-back-II, hotfix-python-III. All handbook sessions closed. Running: Coordinator-IV, hotfix-python-IV, hotfix-back-III, hotfix-front-III, Manual QA-II.

- 15:25 UTC: backend 1.1.91 (hotfix-back-III): QA-136 report agent log readable (14.8 M tokens, 0.46 USD).

- 15:20 UTC (user): handbooks renamed handbook-case, handbook-design, handbook-economics, handbook-report (documents d963dee). Global Knowledge now: handbook-case 0f82fadb, handbook-design 2d8a2457, handbook-economics 634ca9c8, handbook-report 3664b76b, hackathon-2026-assumptions 8bd08430, cost-sources.csv a2c6c5f8 / .md 765d6eb4 (to be renamed data-economics). geomind mentions: hotfix-python-IV.

- 15:10 UTC: backend 1.1.90 (hotfix-back-III, QA-122 backend part: project_designs + plant_version). All 11 remaining QA runs cancelled by the coordinator (user order); sahand test 2 cb5a97c2 left running. IMP-025 display: one line per instance with its own step count ("Geoscientist I · Thinking · 12 steps").

- 15:05 UTC (user, TOP): IMP-025 parallel agents (lead assigns tasks to instances, e.g. Geoscientist I/II/III; goal: a complete case in ~5 min). hotfix-python-IV right after QA-131; display by hotfix-front-III.

- Backend 1.1.89 (2026-11-05 14:27 UTC, hotfix-python-IV): geomind 0.4.87 + gemini 0.6.15 (QA-129 doublets searchable on a free plant, QA-130 doublet flow capped at pump nominal_flow, QA-132 not a breach (ESP intake volume with free gas), QA-125 result summaries, QA-123, QA-124; QA-128 filed). 15:00 UTC (user): rename tool read_rag to read_file (hotfix-python-IV, after QA-131). QA run 11597465 cancelled by the coordinator. QA-133/134/135 to hotfix-front-III; QA-136 to hotfix-back-III; QA-121 to hotfix-python-IV.

- Frontend 1.1.104 (2026-11-05 14:27 UTC, hotfix-front-III): QA-127+109 (report opens on best feasible result + its run log), QA-126+107 (Days covered: geothermal only / topped up / backup only), QA-118 (no rounding in approval cards), IMP-024 (Run again on studies).

- 14:55 UTC (user): DEPLOY AT ONCE: every finished fix goes out immediately (no :00/:30 windows) until the user says otherwise; lock still holds.

- 14:50 UTC (user): rename cost-sources.csv/.md to data-economics.csv/.md (hotfix-python-IV, after Fatemeh's bugs); the coordinator then swaps them in Knowledge (delete a2c6c5f8, 765d6eb4).

- 14:45 UTC: functional-qa-plant-I (QA-116, QA-134) and functional-qa-case-I (QA-133; run 11597465 still waiting, Cancel broken) closed and archived. QA-133+134 to hotfix-back-III, which then cancels run 11597465. functional-qa-study-I closed and archived (run 1461ca81 cancelled; QA-121, QA-135). ALL five functional-qa sessions closed. Fatemeh's session is now "Manual QA-II".

- 14:40 UTC (user-approved, coordinator): global Knowledge now holds the four handbooks: handbook-case 2355088c, handbook-report bc8b41e4, handbook-design 61619cce, handbook-economics b019b649; hackathon-2026-assumptions.md re-uploaded c3510844 (was b3ba8363); the four hackathon-2026-*-guide entries deleted; cost-sources.csv a2c6c5f8 / .md 765d6eb4 unchanged.

- 14:30 UTC: Fatemeh QA handed over to Fatemeh QA-II session_01J2V3UYeTzFtZEuQJvkuadd (note notes/sessions/manual-qa-1.md); send Fatemeh findings there. functional-qa-simulation-I closed and archived (QA-125, QA-132; QA-132 with QA-130 to hotfix-python-IV). QA-107 with QA-126 to hotfix-front-III.

- 14:25 UTC: functional-qa-report-I closed and archived (filed QA-099, 122, 123, 124; S2, S6-S11 untested). User: archive each QA session once it reports stopped.

- 14:20 UTC (user): IMP-023 REJECTED (no sample-plant templates; design from handbook-design, memory/feedback-design-from-handbook-not-templates.md); QA-122 APPROVED. QA sessions: cancel every QA run, complete their reports, then close (functional-qa-* stop for now).

- 14:17 UTC usage check: five-hour window reset; now seven_day allowed_warning (resetsAt 2026-11-11 23:00 UTC). Hotfix sessions work through it (user, 13:40 UTC); QA sessions stay paused by the user's word, not by usage. No further usage check scheduled.

- 14:45 UTC (Fatemeh): QA-129, QA-130, QA-131 routed to hotfix-python-IV, top of queue. hotfix-back-III idle (QA-126/118 are frontend-only; QA-122 backend part waits for the user).

- 14:35 UTC (user): Fatemeh QA (session_01J2V3UX7XrrTa9jKv7ZTh9a, 525k context) is under the 300k refresh rule too; asked to hand over to "Fatemeh QA-II".

- 14:20 UTC: hotfix-back-II handed over to hotfix-back-III session_01J2V3UVuLrkzKAZV6dAkLmu (note notes/sessions/hotfix-back-2.md); QA-095 fixed; test_case_aware fixed (backend 931cac5, no deploy). handbook-others archived (guides git rm'd, documents a0854de). ALL FOUR handbooks COMPLETE (plant-design 995bd35, techno-economics a1ab0cb; handbook-economics session_01J2V3UVK9oFWcJQb2GuSbpF done, archive refused by classifier: user archives). Frontend 1.1.99 live 14:10 UTC (hotfix-front-III). Knowledge swap (upload the four handbook-*.md, re-upload hackathon-2026-assumptions; delete guides 2330c87c, daf88c29, 11f90cd2, 678e9a43) PENDING: auto-mode classifier refused scripts.replace_knowledge for the coordinator; the user runs it. Rule: Fatemeh's bugs first (memory/feedback-fatemeh-bugs-first.md).

- 13:40 UTC (user): the five functional-qa sessions STAY PAUSED until the user says otherwise; every other session (hotfix, handbooks) resumed now. hotfix-python-III (context full) handed over to hotfix-python-IV session_01J2V3UZqdULpCLT7XEFdd6t (note notes/sessions/hotfix-python-3.md).

- Backend 1.1.88 (2026-11-05 11:30 UTC, hotfix-python-III; includes hotfix-back-II 1.1.87 QA-110/102 backend, QA-104): geomind 0.4.85 + gemini 0.6.13 LOCAL wheels (every tool in exactly one skill, IMP-014/015/016/017 part 1/018, QA-097/099/114/116/119/120, read_rag outline/section). Frontend 1.1.93-1.1.99 (11:30, hotfix-front-III: QA-115, 117, 100, 101, 110, 102).

- Backend 1.1.88 (2026-11-05 11:30 UTC, hotfix-python-III; includes hotfix-back-II 1.1.87): geomind 0.4.85 + gemini 0.6.13 LOCAL wheels (tools documented only in skills, IMP-014..018, QA-097/099/114/116/119/120, read_rag by section). hotfix-python-III paused for the usage limit; handover note notes/sessions/hotfix-python-3.md (successor hotfix-python-IV on resume).

- Backend 1.1.86 (2026-11-05 11:00 UTC, hotfix-python-III; includes hotfix-back-II 1.1.85 QA-106): geomind 0.4.81 + gemini 0.6.13 LOCAL wheels (QA-104, QA-105, QA-107a gemini part, IMP-012/013 evaluate_module and set_case slips, skills sent with a tool's first result).

- Backend 1.1.84 (2026-11-05 10:30 UTC, hotfix-python-III): geomind 0.4.80 + gemini 0.6.12 LOCAL wheels (QA-090 stop rule, QA-091 supply temperatures running + heat/cold delivered, QA-094 return temperatures a design choice, QA-095 row co2-grid-organisers-2026 shipped (Knowledge re-upload of cost-sources.csv/.md still for Sahand), economics from an assumptions document in Knowledge first).

- 2026-11-05 (handbook-others): the four hackathon-2026-*-guide.md files were removed from `documents/project/quality-assurance/inputs/` and replaced by the general handbooks handbook-case.md, handbook-design.md, handbook-economics.md and handbook-report.md (the hackathon is their worked-example chapter). hackathon-2026-assumptions.md stays. Knowledge: the old guide entries are still there (case 2330c87c, design daf88c29, analysis 11f90cd2, report 678e9a43); replacing them with the handbooks is for the coordinator and the user.

- 10:55 UTC (hackathon-guides): documents 07085fc: `documents/project/quality-assurance/inputs/` holds hackathon-2026-assumptions.md (renamed from assumptions.md; the rename itself landed in debeb20) and hackathon-2026-case-guide.md, -design-guide.md, -analysis-guide.md, -report-guide.md. Global Knowledge upload PENDING: the auto-mode classifier refused `scripts.replace_knowledge`; the user runs it (command in the report to Coordinator-III), then deletes the old global entry assumptions.md (eb95027a). New Knowledge ids: (pending). Never in a project's files.

- Backend 1.1.83 (2026-11-05 10:00 UTC, hotfix-python-II; includes hotfix-back-II's 1.1.80-1.1.82, QA-088 and QA-092): geomind 0.4.78 + gemini 0.6.12 LOCAL wheels (QA-074, 079, 084, 085, 086, 088 full runs, request 35).

- 11:26 UTC (Fatemeh): QA-127 + QA-109 (report default result and agent log) routed to hotfix-front-III, first after resume in one deploy; then QA-126 (Days covered backup class).

- 11:23 UTC: handbook-case.md and handbook-report.md COMPLETE (documents b3b2199; unverified items marked); handbook-others left: git rm hackathon-2026-*-guide.md + links. handbook-design ch 1-11 done (documents fd81b3a; left ch 12, appendices A-D); handbook-economics ch 1-15 (d53f06e).

- 11:15 UTC (user): QA round 3 PAUSED (all five sessions finish their step and wait for the coordinator's resume). Handbooks replacing the hackathon-2026-*-guide files (general, book-like, read by section): handbook-design (session_01J2V3UVax4NELQZ9gqGQ4t8), handbook-case + handbook-report (session_01J2V3UVwPdMpj4qHKCUrfrf), handbook-economics (session_01J2V3UVK9oFWcJQb2GuSbpF); hotfix-python-III adds read_rag outline/section. Knowledge upload by the coordinator when done; hackathon-2026-assumptions.md keeps its name.

- 10:30 UTC (Coordinator-III, user-approved): global Knowledge now holds hackathon-2026-assumptions.md b3ba8363 (QA-112 fix, 11:05 UTC; was ad184278), -case-guide 2330c87c, -design-guide daf88c29, -analysis-guide 11f90cd2, -report-guide 678e9a43, cost-sources.csv a2c6c5f8 and cost-sources.md 765d6eb4 (with the QA-095 organisers' row); old assumptions.md eb95027a deleted. All ready. QA3 testing released.

- 09:55 UTC: the user approved a geomind release (QA-091, QA-094, QA-095 row); hotfix-python-II releases and deploys at the next window. assumptions.md (documents/project/quality-assurance/inputs/, b2846fd) is in the global Knowledge (eb95027a); NOT in any project's inputs (user, 10:00 UTC).

- 09:40 UTC (hotfix-back-II): QA-092 fixed in backend 1.1.82 (9da4bbf; plant-changing tools and simulate on a stored design save the next plant version; a plain simulate still writes no Results row), goes out with hotfix-python-II's held batch. QA-095 row co2-grid-organisers-2026 (300 g/kWh) on geomind main 3a5027d: live only after a geomind release (Sahand's word) and a Knowledge re-seed by Sahand. QA3 seed runs after the batch deploy.


- Backend 1.1.78 (2026-11-05 07:30 UTC, hotfix-python-II): geomind 0.4.73 + gemini 0.6.10 LOCAL wheels (QA-081 gd.errors.AlreadyAnsweredError, backend must treat it as no-op; QA-087 six web searches per agent and run).

- Backend 1.1.76 (2026-11-05 07:00 UTC, hotfix-python-II): geomind 0.4.72 + gemini 0.6.10 LOCAL wheels (QA-082 root: simulate summary no longer fails on an ESP failure group).

- Backend 1.1.75 (2026-11-05 06:30 UTC, hotfix-python-II): gemini 0.6.10 + geomind 0.4.71 LOCAL wheels (QA-082 depth named first, simulate changes set plant options; QA-083 internal errors carry their cause, bare inlet names coded).

- Backend 1.1.73 (2026-11-05 05:30 UTC, hotfix-python-II): gemini 0.6.8 + geomind 0.4.69 LOCAL wheels (QA-080: flow range over several requirements; case lead writes one min+max rule).

- Backend 1.1.72 (2026-11-05 05:00 UTC, hotfix-python-II): geomind 0.4.68 + gemini 0.6.7 LOCAL wheels (QA-076 gm.check no longer raises on incomplete plants, engineers own their parts; QA-078 random calculation ids C+6hex). 1.1.71 (04:30): geomind 0.4.66 (QA-072).

- Backend 1.1.69 (2026-11-05 02:00 UTC, hotfix-python-II): geomind 0.4.65 + gemini 0.6.6 LOCAL wheels (QA-071 English-only short web queries; gm.study.structure_plant for the evolve structures view). Sandbox image stays gemini-sandbox:0.6.5. Includes the structures view endpoints (1.1.66-1.1.68). Frontend 1.1.71 (Compare structures).

- Backend 1.1.65 (2026-11-05 01:30 UTC, hotfix-python-II): geomind 0.4.64 LOCAL wheel (QA-047 findings in problem state; QA-070 nested agents rerun after a restart).

- Backend 1.1.64 (2026-11-05 01:06 UTC, hotfix-python-II): geomind 0.4.62 LOCAL wheel (QA-069: set_case returns plants_need).

- Backend 1.1.63 (2026-11-05 01:02 UTC, hotfix-python-II): geomind 0.4.61 LOCAL wheel (skills connectors, economics, report, comparing-designs; prompt-to-skills step done as agreed: only sometimes-needed how-to moved).

- Backend 1.1.61 (2026-11-05 00:22 UTC, hotfix-python-II): geomind 0.4.60 LOCAL wheel (QA-065 doublet-count requirement, QA-061 no internal note on question cards).

- Backend 1.1.58 (2026-11-05 00:16 UTC, hotfix-python-II): geomind 0.4.58 LOCAL wheel (web_search/read_web_page over SearXNG live; calculate takes plain numbers/pi/e beside one sourced operand); 1.1.57: geomind 0.4.57 (run_python live in gemini-sandbox:0.6.5, checked from geomind-celery); 1.1.56: geomind 0.4.56 (skills folder
  `geomind/skills/<name>/SKILL.md` with roles; `calculate` tool, results in problem state `calculations`),
  gemini 0.6.5, alembic 0014. 1.1.55 gave the worker the run_python sandbox (docker socket) and SearXNG.
  Deploys resume running runs (QA-035).
- Frontend 1.1.57 (2026-11-05 00:00 UTC: busy indicator and activity line by the agent name, QA-048). Hotfix sessions deploy themselves with two calls:
  `cd <repo>`, then exactly `scripts/hotfix_deploy.sh`.
- Agents: every role on `deepseek/deepseek-v4.1-flash-1017`, OpenRouter provider `morph/fp8` first
  (`GEOMIND_PROVIDER=morph/fp8`), since 2026-11-04 20:20 UTC; `GEOMIND_CONTEXT_WINDOW=200000`.
  Never a Claude model.

## Clones (project root, one clone each, no worktrees)

- `.claude` (this, agents) and `documents` (people) are repos too, on `main`; set up a machine with `.claude/setup.md`.

- backend, frontend, geomind, infrastructure on `main`; gemini on `dev` (its default branch).
- No worktrees anywhere (removed 2026-11-04 20:30 UTC). Old local files: `~/geomind-archive/`
  (screenshots, QA screenshots of 2026-11-03, the old root git); DB backups `~/geomind-backups/`.

- Knowledge re-seeded by Sahand 2026-11-04 ~23:35 UTC with geomind 0.4.52 cost-sources (153 sourced
  rows). No row yet for opex.per_energy of the three chillers and opex.fixed.adsorption_chiller.

- Release summaries to the user (Persian, what to test) after every deploy window: scheduled tasks trig_01DPzkqZPcFQx6PsQ8e53i52 (:07) and trig_01KxsFUkVb8Vo5beKrQiX3xS (:37) in Coordinator-IV; a successor recreates them.
- Usage-window check: trig_01PDidq5qh4bL1zp9ZzQVTik fired 14:17 UTC; none pending (seven-day warning until 2026-11-11 23:00 UTC)
  (resetsAt 14:10 UTC + 1 min). Last pause 01:50-04:12 UTC, resumed; pauses and resumes per `memory/feedback-usage-limit-pause.md`.

## How we work now

- Mode: ask the user at the start of every session (development, production, hotfix);
  `documents/project/ops/development-modes.md`. Current mode of the last session: hotfix.
- QA: testing the live app; every bug in `documents/project/quality-assurance/BUGS.md` (QA-001 to QA-019; statuses there,
  QA-007 blocker: ask_economics fails again and again); ideas in `IMPROVEMENTS.md` (IMP-001 to IMP-011,
  QA-010 and IMP-006 need Sahand's decision). Run a61cfb19 was left `waiting` with no process after the 20:02 UTC deploy (QA-017).
- No file holds Persian text; chat with the user in Persian.
- Commit and push everything when a piece of work ends.

- QA round 3 (since 2026-11-05 09:41 UTC, Sonnet, briefs `notes/qa-round-3/`; writing scenarios until the QA3 projects are seeded after the 10:00 UTC deploy): functional-qa-case-I session_01J2V3UX7PBCQPBsuYm1yhTy, functional-qa-plant-I session_01J2V3UX9jou1ZLL5ywtpesJ, functional-qa-simulation-I session_01J2V3UZ8hMoK5EHwvn5Ufhv, functional-qa-study-I session_01J2V3UYN8UWRzdAY8qbX1DH, functional-qa-report-I session_01J2V3UXX5DGJR5QX7cknLLh. Project ids (seeded 10:10 UTC on 1.1.83, competition files only): QA3 case 15b2f15f-46d0-4b09-a44b-0f849127c1f0, QA3 plant c45a5382-af55-43fc-9340-dd1ab1245533, QA3 simulation ef87f914-3aaa-4f58-be60-2d54c7687511, QA3 study 7a852d89-dfe5-423c-980a-a4ca231353bc, QA3 report 91b202b6-6236-45e7-8860-a58437d6eb98. Released 10:30 UTC (was: testing starts only after hackathon-guides (session_01J2V3UWWyDq7eZprEhSK2r4) has put the four hackathon-2026 guides and hackathon-2026-assumptions.md in Knowledge; then the coordinator sends each "go" with its id.

## QA round (started 2026-11-04 20:00 UTC)

- Hotfix sessions resumed 2026-11-04 20:25 UTC (paused 20:10-20:25). Deploy windows at :00 and :30 UTC
  only (a blocker may go at once); every deploy still ends running agent runs until QA-035.

- Coordinator: Coordinator-III, session_01J2V3UWsUm5z442CiXM5MZU (since 2026-11-05 09:30 UTC; opens and
  closes the sessions, sends reports). Coordinator-II (session_01J2V3UXD6UT73meeapsG2MS) archived; its
  handover note is `notes/sessions/coordinator-2.md`. Generation 1 (session_01J2V3UXGweG4JrR4wkEWtg9) archived;
  its handover note is `notes/sessions/coordinator-1.md`.
- Hotfix sessions (who fixes what: `documents/project/quality-assurance/README.md`):
  hotfix-front-III (session_01J2V3UZUC8Sa5jDfm1W7WPH since 2026-11-05 11:05 UTC, successor of hotfix-front-II; note notes/sessions/hotfix-front-2.md; area frontend; QA-115, QA-110/102 frontend parts, QA-109, QA-100, QA-101),
  hotfix-back-II (session_01J2V3UZeNoBawJDgCJuBHr7, since 2026-11-05 09:30 UTC, successor of hotfix-back session_01J2V3UWh6RugyR1DAxrkNhH; note notes/sessions/hotfix-back-1.md; areas backend, data, infra, backend clone; QA3 seeding, QA-095, QA-092 triage),
  hotfix-python-III (session_01J2V3UYxvjmxy4kZhDh7eSd since 2026-11-05 10:05 UTC, successor of hotfix-python-II; note notes/sessions/hotfix-python-2.md; areas geomind, gemini; local wheels; QA-090/091/094, QA-095 case-lead part, the user-approved geomind release).
  Archived by Coordinator-III: hotfix-front-II (11:06 UTC), hotfix-python-II (10:06 UTC), hotfix-front, hotfix-back, functional-qa-I, -2, -3 (run B cef908d9 cancelled).
  They claim with `qa.py next`, take `/tmp/geomind-backend.lock` before editing the backend, and
  deploy with `scripts/hotfix_deploy.sh` (one deploy at a time).
- QA sessions qa-1, qa-4, qa-5 paused by Sahand 2026-11-04 23:25 UTC and ARCHIVED ~23:30 UTC;
  their state is in `notes/sessions/qa-paused-2026-11-04.md`. QA round 2 started 2026-11-04 23:36 UTC (briefs `notes/qa-round-2/`, agent-browser only):
  all on Sonnet since 23:45 UTC. Since 2026-11-05 00:25 UTC (Sahand, usage) only
  functional-qa-I (was qa-func-1-II) session_01J2V3UWQ5zYo1TfCiAKXF4d runs QA: one project through the whole pipeline, owning
  qa-func-1/2/3 scenarios. qa-func-2-II, qa-func-3-II and qa-ux archived (00:20-00:40 UTC); their state is in
  their files in `notes/qa-round-2/`. QA-031 and QA-053 retests are still open (qa-ux did not finish).
  Since 2026-11-05 04:12 UTC three functional QA sessions (Sonnet, competition files only):
  functional-qa-I session_01J2V3UWQ5zYo1TfCiAKXF4d (case + start-to-end design loop),
  functional-qa-2 session_01J2V3UYx2foVYxpZKRTvMhq (economics, verdict, explainer, report, agent log),
  functional-qa-3 session_01J2V3UVgJnF99ApUaSbM43F (studies, evolve, compare structures, agent tools, robustness). (Started 2026-11-04 20:11 UTC; instructions in `notes/qa-round-2026-11-04/`):
  qa-1 session_01J2V3UXnAof6WqpiA2JPxxG, qa-2 session_01J2V3UYuCFrxrXdWLCwzWro,
  qa-3 session_01J2V3UWmkUwP3g42jGxxz9g, qa-4 session_01J2V3UZkFGKUyXLCP3gYmk4,
  qa-5 session_01J2V3UVCHoDxQNsjwpBxtzH, qa-6 session_01J2V3UXM3DCMhq41Hx27eqV,
  qa-7 session_01J2V3UVMbdhwimT6VJxfNMq, qa-8 session_01J2V3UW8MS1wyUTdvJmh8UC.

- TEMPORARY for the QA round: prod backend `.env` has `RATE_LIMIT_REQUESTS=1000` (was 100; all QA
  sessions share the admin account, QA-024). Set it back to 100 after the round (Fatemeh runs it;
  backup `~/env.backend.before-ratelimit.bak`).
- `~/.claude/settings.json` allows `scripts/hotfix_deploy.sh` (added by Fatemeh 2026-11-04 20:35 UTC).

## Feature in progress (hotfix mode)

- DONE 2026-11-05 01:02 UTC: skills folder + calculate, run_python, web_search/read_web_page (SearXNG) live
  (geomind 0.4.58-0.4.61), chat views live (frontend 1.1.67), sometimes-needed how-to moved into skills;
  spec `notes/features/agent-tools-2026-11-05.md`; hotfix-python, hotfix-back, hotfix-front.
- 2026-11-05 ~00:15 UTC (Sahand): SearXNG up (geomind-searxng, geomind network only), image
  gemini-sandbox:0.6.5 built, prod backend `.env` has GEOMIND_SEARCH_URL, DOCKER_GID, ASSISTANT_SANDBOX,
  GEOMIND_SANDBOX_* (backup `~/env.backend.before-sandbox.bak`). Worker change deploys next (hotfix-back).

## To do in development mode after the QA round

- Backend `requirements.txt` still pins geomind 0.4.26; production runs local wheels (geomind up to
  0.4.41) from `backend/.tmp/hotfix-wheels`: pin the released version, empty the folder.
- Frontend `src/api/schema.d.ts` was patched by hand for QA-040 (1.1.49): run `npm run gen:api` and
  review the ~1100-line diff.
- Set the prod backend `RATE_LIMIT_REQUESTS` back to 100 (QA round only).
- Run every automated test that needs no LLM in every repo; the hotfixes ran none.
- QA-011 (resume a nested run after a provider failure), QA-013 (IMP-001) and QA-047's record of
  half-done engineer work are development work.
- QA-045's data part: three catalogue rows need a person-approved price year, then a Knowledge
  re-seed.

## Open decisions (waiting for Sahand)

- SUBMISSION DEADLINE (organisers, Discord #technical-q-and-a, 2026-11-04): Thursday 2026-11-05 23:59 CET
  = 22:59 UTC. A pull request is enough (to GEMINI's development branch); for the gemini bugs we fixed,
  explain what and where in it, no separate PR. Sahand decides what goes in. Organiser rules found by
  Fatemeh's QA session: return temperatures are the team's choice within the constraints (QA-094); grid CO2
  reference 0.3 kg/kWh (QA-095); 330 d is the doublet's availability, the full system must meet the demand
  all 365 days (QA-091); depth may change; gas is CO2+CH4, several handling options allowed.

Decided 2026-11-04 21:40 UTC: QA-010 option A (agent proposes labelled assumptions in one question,
user approves; hotfix-python), QA-006 option A (research cited rows, Sahand approves, then re-seed;
hotfix-back writes proposed rows to evidence/QA-006/).

Still open (Sahand answers later; the full write-up is in the coordinator's chat of 21:35 UTC):
3. QA-045 data: three rows in USD/FRF with no price year. Proposed: leave them (the tool skips
   them now), convert after the hackathon.
4. gemini requests 33-38 (geomind `.claude/docs/plan.md`, none sent). Proposed: approve 36
   (check names params.backup), 38 (dimensionless % accepted), 33 (check vs simulate); the rest later.
5. QA-031: auto-approve with no tab open needs a backend setting per chat. Proposed: build it.
6. A development round after QA for QA-011, QA-013 (IMP-001), QA-047.
7. geomind tags v0.4.27-v0.4.45 were pushed and released by CI during the hotfix round (the rule
   was "release only on Sahand's word"); prod runs the local 0.4.45 wheel; pin it in development.
8. Set prod `RATE_LIMIT_REQUESTS` back to 100 after QA (now counted per browser since QA-024).
9. Done 2026-11-05 00:20 UTC: Coordinator-II is running (handover was automatic).
