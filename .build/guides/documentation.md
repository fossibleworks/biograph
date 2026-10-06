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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - context7.json
---

- **User/product docs** live outside the repo. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`) and Context7 (`context7.json`).
- **In-repo design and usage notes** live in `wiki/` as Markdown. Usage docs are UPPER-KEBAB (`BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`) and design docs use a `DESIGN-` prefix. There are also plans and reports (`insurance-parity-report.md`, `FHIR Terminology Service Parity — Implementation Plan.md`).
- **Upstream sync ledger:** `wiki/upstream-sync-version-16.md` records every cherry-picked upstream commit, organised in batches. Each table row gives the sha, the subject, an outcome (picked-clean, picked-with-conflict-resolution, already-present, skipped, deferred) and notes. Update it in the same PR as any sync work, with `docs(wiki): ...` commits.
- **PR docs gate:** `docs_checker.yml` fails `feat` PRs unless the body links to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs` or `backport`. The helper queries the earthians/biograph API.
- Code comments are sparse. Docstrings appear on whitelisted functions, and hooks.py keeps Frappe's commented template.
