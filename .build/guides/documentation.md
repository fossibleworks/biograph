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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
---

- **User and product docs** are external: README links to DeepWiki (`deepwiki.com/Tacten/biograph`). `.github/helper/documentation.py` (the docs_checker workflow) requires `feat` PRs to link a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, unless the body contains `no-docs` or `backport`.
- **In-repo `wiki/`** holds fork design and usage docs as UPPER-KEBAB markdown files, e.g. `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, plus implementation plans and parity reports. The convention is a paired design doc and usage doc per feature. Screenshots sit next to them as png.
- **`wiki/upstream-sync-version-16.md`** is a living ledger. Each upstream sync batch adds entries (picked-clean, picked-with-conflict-resolution, already-present, skipped), and commits touching it use the `docs(wiki): ... (upstream sync B<n>)` prefix.
- Code comments are sparse. Short inline comments explain intent in controllers, and test classes carry a one-line docstring.
- `patient_portal/README.md` covers the SPA.
