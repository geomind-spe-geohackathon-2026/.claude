---
name: docker-via-sg
description: "On the Dell, docker commands need sg docker because agent shells miss the docker group"
metadata:
  node_type: memory
  type: reference
  originSessionId: 3db29973-7824-5bbd-8292-d9adf25ff607
  modified: 2026-11-03T01:08:29.351Z
---

The user `fatemec` is in the docker group, but agent shells do not have it active, so plain `docker` gets permission denied. Run `sg docker -c '<command>'`. `gh` is not installed on this machine, and the geomind repo is private, so workflow runs and release assets cannot be checked from here.
