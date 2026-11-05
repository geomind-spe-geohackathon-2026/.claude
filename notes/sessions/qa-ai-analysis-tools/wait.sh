#!/bin/bash
# wait.sh <run>: poll until the run is not queued/running
cd /home/fatemec/geomind-spe-hackathon-2026/backend
Q=/tmp/claude-1000/-home-fatemec-geomind-spe-hackathon-2026/e2ed2f1c-e48b-5e9a-9ce5-cd56999d42fb/scratchpad/qa
for i in $(seq 1 360); do
  out=$(nice .venv/bin/python $Q/qa_ai.py status $1 2>&1)
  s=$(echo "$out" | python3 -c "import sys,json;print(json.load(sys.stdin)['status'])" 2>/dev/null)
  if [ -n "$s" ] && [ "$s" != "queued" ] && [ "$s" != "running" ]; then date -u +%T; echo "$out"; exit 0; fi
  sleep 20
done
echo timeout
