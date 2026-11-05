# functional-qa-case-I

Read `README.md` here (your row) and `../qa-round-2/common.md`. Your project: "QA3 case" (id in
STATUS.md once seeded). Test only your stage; report bugs with qa.py (reporter
functional-qa-case-I). Check every number against the PDF and CSVs.

## Scenarios

Rule (feedback-qa-through-chat): every action below is a chat request, every approval is answered in
the chat; tabs (case page, problem state) only check what the chat produced. A step the chat cannot
do is filed as a gap bug.

Project "QA3 case" (files only: PDF + two CSVs, nothing else). Reference values (CSVs computed by
me: 365 rows each; heating min 2.673, peak 30.0 MW, 4652.82 MWh/day-sum = 111.67 GWh/yr as daily
MW x 24; cooling peak 10.0, >0 on 219 days, 23.74 GWh/yr). PDF values from
`memory/competition-inputs.md` (the PDF has no text layer in this container; I re-check it on the
live site page and note any difference): reservoir mid depth 2500 m TVD, 100 m thick, 30 C/km,
surface 12 C, 250 barg, 200 mD; brine 1030 kg/m3, 0.40 mPa.s; GLR 0.8 Nm3/m3, gas 80 % CH4 /
20 % CO2; 1-3 doublets, 50-300 m3/h per doublet while active, brine cooling <= 40 K, pump eff
70 %, prod = inj volume, 330 daily steps, supply 100 C heating / 20 C cooling.

- **functional-qa-case-I-S1 Case from files.** Open the seeded project; in the chat ask (as a user, in my own words) to set up the
  case from the files. Correct: demand series 365 days each, peak 30.0 MW (28 Jan) and 10.0 MW
  (19 Jul), annual 111.67 / 23.74 GWh; year 2027; the case page matches the CSVs.
- **S2 Reservoir and fluid.** Correct: every PDF reservoir/brine/gas value above is in the case with
  right unit (250 barg stays gauge, 200 mD, 0.40 mPa.s); temperature at depth 87 C is derived from
  gradient, not invented.
- **S3 Requirements.** Correct: doublets 1-3, 50-300 m3/h, cooling <= 40 K, pump eff 70 %, supply
  temperatures 100 C / 20 C, 330 steps, prod = inj; each shown with its source (PDF).
- **S4 Missing values.** Values the PDF does not give (return temperatures, prices, discount rate,
  grid CO2, well cost): the agent asks or proposes a sourced value for approval; no silent default.
  I answer as a user (approve a labelled assumption, or "I do not know"); I note what was asked.
- **S5 Change by chat.** "Set the supply temperature to 95 C" / "make the year 2028": only that
  field changes, the rest is untouched, source "user"; revert it by chat.
- **S6 Wrong or odd input.** Ask for 4 doublets, depth in feet, negative flow: the agent explains
  the conflict with the PDF caps or converts units correctly, never sets it silently.
- **S7 Case page vs chat.** Read-only check: the case page, the problem state and the agent's text give the same
  numbers; a reload keeps them; the demand chart shows the peak days.
- **S8 Check.** `check` / "what is missing for a plant?" lists real gaps (plant needs), in plain words.

## Status

Chat 37fb7886 in "QA3 case", backend 1.1.84 / geomind 0.4.80, 2026-11-05 10:30-11:05 UTC.

- S1 Case from files: PASS. Case page demand = CSVs (peak 30 MW 28 Jan, 10 MW 19 Jul, 111.7 / 23.7 GWh, means 12.75 / 2.71).
- S2 Reservoir and fluid: PASS (2500 m, 100 m, 30 C/km, 12 C, 250 bar(g), 200 mD, 1030, 0.40, GLR 0.8, 80/20 mol%; temperature at depth not set, derived).
- S3 Requirements: PASS (8 requirements, each with PDF page). Tolerances 1 % unmet and reinjection band came from the Knowledge assumptions, labelled.
- S4 Missing values: PASS after one confirmation question (16 values, each with source); "I do not know" answers kept as flagged assumptions. Found QA-112 (verified), QA-118 (open, minor).
- S5 Change by chat: PASS (95 C changes only that field, recorded as deviation from PDF; revert to 100 C exact). QA-114 (agent names case version 16, app shows 6).
- S6 Odd input (4 doublets, 400 m3/h): PASS, agent refuses with PDF page and offers keep / deliberate deviation.
- S7 Page vs chat: PASS for demand and values; version numbers differ (QA-114).
- S8 Check / what is missing: PASS in chat ("complete enough for a plant"), open items listed in plain words.
- Gap: the agent also sets the whole economics file during case set-up (one extra question, values from Knowledge); noted, not a bug.

## Variations (2026-11-05 ~11:10 UTC, paused by the coordinator)

- V1 depth 3000 m + return 55 C by chat: values changed, nothing else; QA-119 (reservoir pressure not re-derived or flagged).
- V2 reject the proposed economics, give own numbers: stopped at the Set case approval card (chat 37fb7886, NOT approved, run left waiting); QA-120 (discount_rate sent as 8 with no unit). On resume: deny or approve with "discount rate 0.08", then check the stored economics and the list of values without a source.
- Not done: V3 a user with no files, case from the PDF only (needs a new project from the coordinator); retest QA-114, QA-118 when shipped.

## Closed (Coordinator-IV, round 3 ends)

Filed: QA-112 (verified), QA-114, QA-118, QA-119, QA-120, QA-133. Run 11597465 in chat 37fb7886 could NOT be cancelled (QA-133): it stays waiting at the Set case approval card (economics with discount_rate 8). V3 and the retests of QA-114/118 not done.
