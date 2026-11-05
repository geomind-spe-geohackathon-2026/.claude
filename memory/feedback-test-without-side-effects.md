---
name: feedback-test-without-side-effects
description: Live UI checks never act on real runs or data; intercept the request in Playwright instead (2026-11-05)
metadata:
  type: feedback
---

A hotfix session tried to click Cancel run on a real waiting QA run to reproduce QA-133; the
auto-mode classifier refused it ("interfere with workloads"). The check worked without side
effects by intercepting the request in Playwright (`page.route('https://api.geomind.team/**/cancel',
r => r.fulfill({status: 200, body: '{}'}))`) and logging that the frontend sends it.

**Why:** live runs and project data belong to users and QA sessions; a test must not change them.
**How to apply:** to check a button that writes (cancel, restore, delete, approve), route the
request to a fake answer in the browser and assert that it was sent; never press it for real on
production data unless the bug's owner asks.
