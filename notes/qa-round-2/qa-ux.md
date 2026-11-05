# qa-ux: UI and UX only

Model: Sonnet. Rules: `common.md`. Area: how the app LOOKS and FEELS, across the whole flow:
layout, clarity of text and labels, empty, loading and error states, chat rendering (streamed
text, approval cards, tool output, errors), navigation between chat, case, design, study,
results and report, charts readable, tables not cut, consistent names, keyboard use. Desktop
first; mobile is low priority. Not functional correctness of numbers or agents (qa-func-1..3);
not login.

Use one project of your own for anything you click through; you may LOOK at the QA2 projects
of the functional sessions to see later stages, but never send messages or approve there.
Report UI bugs as frontend with severity cosmetic or minor unless the flow is blocked. Retest
frontend bugs set fixed (QA-048, QA-053, QA-031 and new ones).

## Scenarios

Checked against the PDF (2 pages: reservoir 2500 m, 100 m, 30 C/km, 12 C, 250 bar(g), 200 mD; brine 1030 kg/m3,
0.40 mPa.s, GLR 0.8, 80/20 CH4/CO2; 1-3 doublets, 50-300 m3/h, 40 C cooling, 70 % pump, 330 days, 100 C / 20 C
supply) and the CSVs (365 rows each; heating peak 30 MW on 28 Jan, 111.67 GWh; cooling peak 10 MW on 19 Jul, 23.74 GWh).
Project for all clicking: "QA2 qa-ux flow". Evidence in `/tmp/qa-ux/`, bugs through qa.py.

- qa-ux-S1 Navigation and first screens: log in, projects list (empty/loaded state), create the project, open it; every
  top-level nav item (chat, case, design, study, results, report) opens, has a title, the active item is marked, back/forward
  and reload keep the place; no console errors. Correct: consistent names, no dead links, no blank page.
- qa-ux-S2 Chat input and upload: upload the PDF and the two CSVs by button (and drag if possible), file chips readable,
  long message typed by a user (Enter sends, Shift+Enter newline), send disabled while empty/streaming, stop button.
  Correct: clear feedback of upload progress and errors, no lost text.
- qa-ux-S3 Chat rendering while an agent run streams: streamed text, markdown/tables/code, tool-output blocks, agent names,
  thinking/progress indicators, auto-scroll (and stop of it when the user scrolls up), long lines not cut, timestamps.
- qa-ux-S4 Approval cards: sourced values (source, publisher, year shown), approve / reject / edit, labelled-assumption
  question, auto-approve toggle; buttons clear, state after the choice visible, tab/Enter/Esc keyboard use.
- qa-ux-S5 Error, empty and loading states: a provider error, cancelled run, reload during a run (state restored), page
  with no data yet (case/design/study/results/report before their stage), offline/slow API; messages say what to do next.
- qa-ux-S6 Case page: reservoir, brine, constraints and demand fields vs PDF; units shown, labels consistent with chat names,
  tables not cut, demand chart readable (365 days, axis units MW/MWh, peak marks), edit validation messages.
- qa-ux-S7 Design, study, results pages (look at the functional sessions' QA2 projects, no messages there): tables not cut,
  charts readable (labels, units, legend, colours, tooltips), numbers formatted (thousands, decimals, units), sort/filter.
- qa-ux-S8 Report page: sections, charts and tables render, export/download works, print/overflow, names match the pages.
- qa-ux-S9 Keyboard, focus and accessibility basics: tab order, visible focus, dialogs trap focus and close on Esc,
  buttons have names (snapshot), contrast of text on dark/light if a theme switch exists.
- qa-ux-S10 Layout at desktop widths 1920/1440/1280 and one mobile 390 px (low priority): no overlap, side panels
  collapse, long project names truncated with title.
- qa-ux-S11 Retests of frontend bugs set fixed: QA-048, QA-053, QA-031 and any new one.

## Status (final, stopped 2026-11-05 ~00:30 UTC on the coordinator's word: UI/UX is not a priority)

Own project "QA2 qa-ux flow" (4cfeab2d-73e3-4299-a1f8-afec3d7e4bae); its first chat run (159de1e5-...) was left RUNNING
(case lead / process engineer stage, Auto-approve on). Frontend 1.1.5x, backend 1.1.55 at the end.

- S1 done: login, projects list, new-project dialog, nav links, project sub-pages. Bugs: QA-060 (bare 404 in a deploy window).
- S2 done: attach PDF + 2 CSVs (chips "ready", names truncated), Enter sends.
- S3 done: streaming, steps list, tables render; tool rows vague ("Search rag 1+ matches" x15). QA-062 (chat opens at top while a card waits).
- S4 done: QA-057 (approval JSON indentation), QA-058 (approve/deny/answer leave no trace), QA-059 (15-value question, one-line input), QA-061 (leaked "Already answered ... request-530" note). Chips approve all / change some / stop work; Enter submits an answer; Deny with reason is honoured by the agent.
- S5 partial: empty states of Plant/Study/Results fine (QA-064 cosmetic). NOT done: provider error, cancel, offline, reload-during-run beyond QA-062.
- S6 partial: Case demand chart matches the CSV (cooling peak 10 MW on 19 Jul, 23.7 GWh, 365 points). NOT done: heating chart, Site/Utilities/Economics/Time tabs checked only by screenshot (not read), edit validation.
- S7, S8 not started (no plant/results/report existed in any QA2 project yet).
- S9 partial: Esc closes the dialog, Enter submits; tab order and focus rings not checked.
- S10 partial: New project dialog fits at 1440x900 and 390x844, not at 1280x577 (QA-066). Chat and design at 390 px not checked.
- S11 retests: QA-048 is already `verified` by someone else. QA-053: streamed texts in my run were complete (no mid-word stop seen), not formally verified. QA-031: started (closed the browser for 7 min with Auto-approve on) but the agent-browser session lost its login on close, so the result was not read; run 159de1e5 can be inspected under Runs and logs to see whether it waited for an approval. Both still `fixed`.

Bugs filed by qa-ux: QA-057, 058, 059, 060, 061, 062, 064, 066 (QA-063, 065 are other sessions').
