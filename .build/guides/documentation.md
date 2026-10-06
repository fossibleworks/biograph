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
  - .github/workflows/docs_checker.yml
---

- **Public docs:** the README points to DeepWiki (`deepwiki.com/Tacten/biograph`) and a Telegram group.
- **Fork docs live in `wiki/`** as Markdown. Each feature gets a design doc and/or a usage doc in UPPER-KEBAB names, for example:
  - `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`
  - `BLOCK-APPOINTMENT-BOOKING-USAGE.md`
  - `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`

  The folder also holds implementation plans and parity reports (`insurance-parity-report.md`, `FHIR Terminology Service Parity — Implementation Plan.md`) and the upstream sync ledger `upstream-sync-version-16.md`.
- Doc-only commits use `docs(wiki): ...`.
- **Docs check (inherited from upstream):** the `docs_checker` workflow fails PRs titled `feat...` unless the body links to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs`, or is a backport.
- Code comments are sparse. `hooks.py` keeps the Frappe scaffold comments.
