---
title: Documentation
category: documentation
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - README.md
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/helper/documentation.py
---

- **User docs:** These are external. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`). There is no in-repo docs site, and `healthcare/docs/current` is gitignored.
- **Fork design and usage docs:** These go in `wiki/` as Markdown. Use UPPER-KEBAB names for feature docs (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`) and descriptive names for plans and reports (`insurance-parity-report.md`, `upstream-sync-version-16.md`). Screenshots sit alongside the docs.
- **Long-running work:** Record it as a ledger in `wiki/`, with method, outcomes vocabulary and baselines. Commit those updates as `docs(wiki): ...`.
- **PR docs gate:** `docs_checker.yml` fails `feat` PRs unless the PR body links a docs page on `biograph.frappe.cloud` / `biograph.io` under `/wiki`, or contains `no-docs` (or `backport`).
- The PR template asks contributors to update the necessary documentation and to reference issues with `closes #XXXX`.
