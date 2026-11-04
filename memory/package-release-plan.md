---
name: package-release-plan
description: "Sahand's decision to install gemini and geomind from published versions instead of sibling folders"
metadata:
  node_type: memory
  type: project
  originSessionId: 7fbc507a-e070-59e2-997c-57769fc75858
  modified: 2026-11-02T21:17:23.764Z
---

Project-wide rule from Sahand (2026-11-02): nobody installs another project with `-e`, not even locally. Whoever builds a package publishes it, and whoever uses it installs the published version; every thread migrates at the first chance. Versions must be real everywhere. gemini releases from `dev`. geomind releases from `main` and uses `dev` to hold changes on their way to `main`. A repo may keep `-e .` for its own tests.

**Why:** today what a project runs depends on which commit its sibling folder happens to be on.

**How to apply:** GitHub Packages has no Python registry, so wheels go on GitHub Releases and the sandbox image on `ghcr.io`. gemini 0.5.5 is published (tag v0.5.5, 2026-11-03); install URL pattern is in gemini VERSIONING.md. CI runs NumPy without AVX-512 because a few winter days split heat between heat pump and boiler non-uniquely, a known bug to fix in 0.5.6. Publish only when the version in `pyproject.toml` is new, after tests pass. Backend pins exact versions; geomind keeps a range because it is a library. Sahand will make geomind public, which is needed for an untokened install from Releases. Sahand's scope for the geomind thread (2026-11-02): tell it only how to install gemini correctly from now on, once a version is published, and nothing about CI or its own releases yet. Changes outside gemini go to their own threads only with Sahand's OK ([[gemini-workspace]]).
