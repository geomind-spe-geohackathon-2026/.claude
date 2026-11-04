# Handover: qa-func-1 (generation 1) to qa-func-1-II

Old session: qa-func-1, session_01J2V3UWzfrtoJbvYqwfh6XD. Handed over on the coordinator's order
(Coordinator-II, 2026-11-05), not for context.

## Role

QA session qa-func-1 of QA round 2: FUNCTIONALITY of the chat-driven case (first message to a
complete, correct case). Mode: hotfix round, test and report only. Full rules:
`.claude/notes/qa-round-2/common.md`; brief, reference values from the PDF/CSVs and the scenarios
S1..S10 with their status: `.claude/notes/qa-round-2/qa-func-1.md`. Read both first, then the
files common.md lists.

## State

- Scenarios written and pushed (commit fc7e898); the coordinator was told.
- S1 in progress: project "QA2 qa-func-1 S1 full case"
  (https://geomind.team/projects/a0947848-b958-4ee9-8927-56ec0a9cff03/assistant/chat), shared
  memory Off (the dialog says keep it off for a competition run), auto-approve OFF, the PDF and the
  two CSVs attached in New project. First message sent 23:39 UTC: "We want to design a deep
  geothermal plant for heating and cooling. The challenge requirements and the two daily demand
  profiles for 2027 are attached. Please set up the case from these files first, then we go on to
  the design." The agent run is ACTIVE and left running (Geoscientist was listing files); its
  run id is in the project's Runs and logs.
- No bug reported yet.

## Tips learned

- agent-browser: `--session qa-func-1` (keep the name). Log in by reading FIRST_ADMIN_EMAIL /
  FIRST_ADMIN_PASSWORD from `backend/.env` into shell vars (`set -a; . backend/.env; set +a`),
  never print them. Auth state was saved to /tmp/qa-func-1/auth.json (`--state` to reuse).
- Set `agent-browser --session qa-func-1 set viewport 1440 1000` first: at the default 1280x577
  the New project dialog's Create button is below the fold and the click closes the dialog with
  no request sent (not reported; UI area of qa-ux).
- PDF text: no pdftotext/pypdf on the Dell; the Read tool reads the PDF.

## Next steps

1. Open the S1 chat, follow the run: answer questions as a real engineer from the PDF/CSVs only;
   note every question asked; with auto-approve off, test approve / reject with a reason / edit
   (S3).
2. S2: check every case value against the reference values in qa-func-1.md.
3. Then S4..S10 in order; one-line status per scenario in qa-func-1.md; bugs through qa.py;
   one line to the coordinator per new blocker/major, a short report every hour.
