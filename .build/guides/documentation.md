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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
---

# Documentation

- **User docs** are external: the README links to DeepWiki (`deepwiki.com/Tacten/biograph`). The inherited `docs_checker` workflow requires `feat` PRs to link to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, unless the PR body contains `no-docs` or `backport`.
- **In-repo design and usage docs** live in `wiki/` as Markdown:
  - feature design docs: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`
  - usage docs: `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - implementation plans and parity reports: `FHIR Terminology Service Parity — Implementation Plan.md`, `insurance-parity-report.md`
  - the upstream-sync ledger: `upstream-sync-version-16.md`
  
  Most files use UPPER-KEBAB names. Images sit next to the docs that use them.
- The **upstream-sync ledger** is a running log. Each sync batch updates it with `docs(wiki): ...` commits. It uses a fixed outcome vocabulary (picked-clean, picked-with-conflict-resolution, already-present, skipped) and records lint baselines.
- `patient_portal/README.md` covers the portal.
- Code comments are sparse and explain why rather than what. Doctype descriptions live in the doctype JSON.
