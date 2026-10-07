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
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **End-user and product docs are external.** The README links to DeepWiki. Upstream docs were hosted on a `/wiki` site.
- The `Documentation Required` workflow (`.github/helper/documentation.py`) fails any PR titled `feat…` unless the body contains a docs link to `biograph.frappe.cloud` or `biograph.io` with a `/wiki` path. It also passes when the body contains `no-docs` or `backport`.
- **In-repo docs** live in `wiki/` as free-form Markdown:
  - Design docs: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`
  - Usage docs: `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`
  - Implementation plans and parity reports: `FHIR Terminology Service Parity — Implementation Plan.md`, `insurance-parity-report.md`
  - The upstream-sync ledger: `upstream-sync-version-16.md`
  Usage docs follow a numbered Table of Contents with sections: Overview, Configuration, User Experience, Examples.
- `patient_portal/README.md` documents the SPA.
- In code, comments are short and explain *why*, as in the `on_login` comment in `hooks.py`. Docstrings are sparse.
- PR descriptions follow `.github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md`: details of the problem solved, screenshots or GIFs for UI changes, and `closes #XXXX`.
