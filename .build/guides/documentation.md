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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **External user docs:** the README points to DeepWiki (`deepwiki.com/Tacten/biograph`). There is also a `context7.json` registration.
- **In-repo docs:** `wiki/` holds markdown design and usage docs with UPPER-KEBAB names (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`), parity reports (`insurance-parity-report.md`), plans, and the upstream sync ledger (`upstream-sync-version-16.md`, which records every cherry-picked upstream commit with its outcome and notes). Images sit next to the docs.
- **Docs-required check:** `docs_checker.yml` runs `.github/helper/documentation.py`. Any PR titled `feat…` must include a docs link (a `/wiki` URL on `biograph.frappe.cloud` or `biograph.io`), or put `no-docs` or `backport` in the body.
- **PR template:** explain the problem and details, attach screenshots or GIFs, and "Update necessary Documentation".
- **Code comments:** sparse. Doctype test files carry a copyright header, and `hooks.py` keeps Frappe's commented-out template sections.
