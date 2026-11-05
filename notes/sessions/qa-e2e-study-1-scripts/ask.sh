#!/bin/bash
# ask.sh "message"  (on current chat page)
A="nice agent-browser --session qa-e2e-study-I"
for i in 1 2 3 4 5 6; do S=$($A snapshot -i); echo "$S" | grep -q "textbox \"Message\"" && break; sleep 3; done
R=$(echo "$S" | grep 'textbox "Message"' | grep -o 'ref=e[0-9]*' | cut -d= -f2)
$A fill @$R "$1" >/dev/null
for i in 1 2 3 4 5 6; do S=$($A snapshot -i); echo "$S" | grep -q "textbox \"Message\"" && break; sleep 3; done
B=$(echo "$S" | grep 'button "Send"' | grep -o 'ref=e[0-9]*' | cut -d= -f2)
$A click @$B >/dev/null; date -u +%H:%M:%S
