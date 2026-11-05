"""drive.py <run>: poll; approve every approval card (logged), stop at a question or the end."""
import sys, json, time
sys.argv = [sys.argv[0], "noop"] + sys.argv[1:]
run = sys.argv[2]
exec(open(__file__.replace("drive.py", "qa_ai.py")).read().split("cmd = sys.argv[1]")[0])
def _api():
    while True:
        try: return api()
        except SystemExit: time.sleep(20)
a = _api(); log = open(__file__.replace("drive.py", f"cards-{run[:8]}.log"), "a")
t0 = time.time(); n = 0
while time.time() - t0 < 7000:
    try:
        r = a.call("GET", f"/assistant/runs/{run}")
    except SystemExit as e:
        time.sleep(20)
        try: a = api()
        except SystemExit: pass
        continue
    st = r["status"]
    if st == "waiting":
        q = r["request"]
        if q["kind"] == "approval":
            n += 1
            log.write(f"{time.strftime('%H:%M:%S', time.gmtime())} {q['request']} {q['agent']}: {q['message'][:400]!r}\n"); log.flush()
            try: a.call("POST", f"/assistant/runs/{run}/answer", json={"request": q["request"], "answer": {"approved": True}})
            except SystemExit as e: print("answer failed", e)
            continue
        print(time.strftime('%H:%M:%S', time.gmtime()), "QUESTION", json.dumps(q)[:3000], "approved", n); sys.exit(0)
    if st not in ("queued", "running"):
        print(time.strftime('%H:%M:%S', time.gmtime()), st, json.dumps(r.get("usage")), json.dumps(r.get("error"))[:500], "approved", n); sys.exit(0)
    time.sleep(15)
print("timeout")
