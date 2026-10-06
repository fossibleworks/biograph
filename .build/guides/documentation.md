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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - AGENTS.md
---

- **User and developer docs:** `README.md` links to DeepWiki (`deepwiki.com/Tacten/biograph`) as the complete documentation. There is no `docs/` tree, and `healthcare/docs/current` is gitignored.
- **`wiki/`** holds in-repo Markdown for fork features and engineering records:
  - usage guides (`PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`)
  - design documents (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `FHIR Terminology Service Parity — Implementation Plan.md`)
  - parity reports (`insurance-parity-report.md`)
  - the upstream sync ledger (`upstream-sync-version-16.md`)
- Usage docs follow this pattern: a numbered Table of Contents, then Overview, Configuration, then step-by-step navigation in bold (**Healthcare → Setup → Healthcare Settings**), then examples. Screenshots and thumbnails sit next to the doc in `wiki/`.
- Doc-only commits use `docs(wiki): …`.
- **PR docs gate:** `docs_checker.yml` runs `.github/helper/documentation.py`. It fails a `feat…` PR unless the body links to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs` or `backport`. (It queries the upstream `earthians/biograph` API.)
- `patient_portal/README.md` documents the SPA.
- `AGENTS.md` and `CLAUDE.md` hold the Build-managed agent guidance.
