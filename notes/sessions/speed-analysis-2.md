# speed-analysis-II: state (2026-11-05 18:05 UTC)

Role and rules as in speed-analysis-1.md (read-only GET analysis, no live runs started by this
session; approvals now go to Coordinator-V). Chat times in Trondheim time, files in UTC.

Done: `documents/project/plans/speed-case-plant-baseline-0.4.10x.md` (first pass 9 runs on
0.4.96-0.4.98, documents 0b6a45a; second pass 3 runs on 0.4.102-0.4.106, 4b07d27). Filed QA-219,
QA-220 (linked to QA-150). New scripts `ts.py`, `gaps.py` (step `ts` gaps, model time, tokens).

Next: a pass on ended runs on 0.4.106+ with a case or a fresh design (T1/T2/T5/T6 untested). Use a
FRESH work dir (/tmp/sa3, /tmp/sa4 ...): /tmp/sa/data still holds the 41 first-baseline runs and
analyse.py globs every run in data/. Set the start filter in fetch2.py; keep only ended runs.

Update 18:15 UTC: full set done (documents 22d1e34): 50 runs, group A 0.4.96-0.4.100 (26), group B
0.4.102-0.4.118 (24). Earlier passes missed runs: /workspace/projects pages by cursor (`next`, max
50); fetch.py fixed. Filed QA-261 (read_case before a case), QA-262 (read_result 'd0').
