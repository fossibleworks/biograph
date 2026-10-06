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
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Documentation

- **README.md** covers the product overview, installation through bench, pre-commit and Semgrep setup, and links to the external docs at **DeepWiki** (`deepwiki.com/Tacten/biograph`) and the Telegram group.
- **`wiki/`** holds the fork's in-repo design and usage docs as Markdown. Existing pairs are:
  - a design doc and a usage doc (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md` and `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE.md` and `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`)
  - parity reports and plans (`insurance-parity-report.md`, `FHIR Terminology Service Parity — Implementation Plan.md`)
  - the upstream sync ledger `upstream-sync-version-16.md`. Every upstream sync batch records its outcomes there in `docs(wiki): ...` commits.
- Upper-case kebab names are the norm for feature docs. Images sit next to the docs that use them.
- The upstream *Documentation Required* workflow fails `feat` PRs whose body has no `/wiki` link on biograph.frappe.cloud or biograph.io, unless the body contains `no-docs` or `backport`.
- The PR template asks contributors to update the relevant documentation.
