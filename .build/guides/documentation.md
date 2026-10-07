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
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Documentation

- **User docs** are external. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`). The `docs_checker.yml` workflow requires every `feat` PR to link a docs page whose URL host is `biograph.frappe.cloud` or `biograph.io` and whose path contains `/wiki`. A `feat` PR without that link fails the check.
- **In-repo engineering docs** live in `wiki/` as Markdown:
  - Design docs: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `FHIR Terminology Service Parity — Implementation Plan.md`.
  - Usage docs: `*-USAGE*.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md` (numbered table of contents, overview → configuration → examples).
  - Ledgers and reports: `upstream-sync-version-16.md`, `insurance-parity-report.md`.
  - File names are mostly UPPER-KEBAB-CASE. Images sit next to the docs.
- Commits that touch these docs use `docs(wiki): ...`. The upstream-sync ledger is updated in the same branch as each sync batch.
- The PR template asks for a problem statement, details, and screenshots/GIFs for UI changes.
- In code, comments are sparse and inline. Short docstrings appear on helper classes.
- `patient_portal/README.md` covers the SPA.
