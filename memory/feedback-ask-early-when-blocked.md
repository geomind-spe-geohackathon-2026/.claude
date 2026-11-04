---
name: feedback-ask-early-when-blocked
description: Sahand 2026-11-03 08:54 +0100: when a device permission refuses a step he already approved, just ask him for a one-word go ("push it") in the thread; don't wait hours for him to run commands
metadata:
  type: feedback
  modified: 2026-11-03T07:55:06.956Z
---

On 2026-11-03 the Dell's auto-mode classifier refused `git push origin dev` (an approved 0.5.6 release). The thread asked Sahand to run the command himself and waited all night. Sahand: "of course push it yourself, what a silly thing to wait for".
**Why:** his explicit word in the thread is enough for the RC session to retry; waiting for him to type shell commands stalls everything.
**How to apply:** when a device step is refused, immediately ask Sahand in the thread for an explicit go (e.g. "write 'push it'"), say only that; never ask him to run commands himself first. Still never route around a refusal on our own.
