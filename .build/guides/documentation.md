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
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
---

# Documentation

- End-user documentation lives externally on **DeepWiki** (linked from the README). The upstream docs host is `biograph.frappe.cloud/wiki`.
- In-repo design and usage docs go in **`wiki/`** as Markdown files.
  - Naming is UPPER-KEBAB for feature docs, e.g. `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`.
  - The folder also holds plans and reports (`FHIR Terminology Service Parity — Implementation Plan.md`, `insurance-parity-report.md`).
- Long-running efforts keep a **ledger** in `wiki/`. `upstream-sync-version-16.md` records method, outcomes per commit and lint baselines. Update it as the work progresses, with `docs(wiki): ...` commits.
- The `docs_checker.yml` CI (`.github/helper/documentation.py`) requires `feat` PRs to link a docs URL (`biograph.frappe.cloud` / `biograph.io` with `/wiki`). To opt out, put `no-docs` in the PR body.
- The PR template asks contributors to update the relevant docs.
