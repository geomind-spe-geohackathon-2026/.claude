#!/bin/bash
# drive.sh RUN_ID : wait; approve every approval card in the UI (logs each); stop on done/question
A="nice agent-browser --session qa-e2e-study-I"
for n in $(seq 1 40); do
  out=$(./wait.sh $1 50 | tail -1); echo "$out"
  case "$out" in *"waiting REQ"*) ;; *) break;; esac
  cd /home/fatemec/geomind-spe-hackathon-2026/backend
  .venv/bin/python /tmp/claude-1000/qa-study/api.py GET /assistant/runs/$1 | python3 -c "import sys,json;r=json.load(sys.stdin)['request'];print('REQ',r.get('kind'),r.get('agent'),r.get('message','')[:160].replace(chr(10),' '))" | tee -a /tmp/claude-1000/qa-study/requests-$1.txt
  cd /tmp/claude-1000/qa-study
  kind=$(tail -1 requests-$1.txt | awk '{print $2}')
  [ "$kind" != "approval" ] && break
  B=$($A snapshot -i | grep 'button "Approve"' | head -1 | grep -o 'ref=e[0-9]*' | cut -d= -f2)
  [ -z "$B" ] && { $A reload >/dev/null; sleep 4; B=$($A snapshot -i | grep 'button "Approve"' | head -1 | grep -o 'ref=e[0-9]*' | cut -d= -f2); }
  $A scrollintoview @$B >/dev/null; $A click @$B >/dev/null; sleep 5
done
