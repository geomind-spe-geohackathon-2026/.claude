#!/bin/bash
# wait.sh RUN_ID [loops]: until status != running or a request is pending
cd /home/fatemec/geomind-spe-hackathon-2026/backend
for i in $(seq 1 ${2:-54}); do
 st=$(.venv/bin/python /tmp/claude-1000/qa-study/api.py GET /assistant/runs/$1 2>/dev/null | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['status'], 'REQ' if d.get('request') else '-', d['usage'])" 2>/dev/null)
 [ -z "$st" ] && { echo "$(date -u +%T) api unavailable"; sleep 10; continue; }
 echo "$(date -u +%T) $st"
 case "$st" in running\ -*) sleep 20;; *) break;; esac
done
