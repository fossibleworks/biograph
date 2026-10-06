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
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **User and product docs** are hosted outside the repo. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`).
- **The `wiki/` directory** holds in-repo design and usage documents. File names are UPPER-KEBAB-CASE markdown, such as `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md` and `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, plus parity and plan reports. Feature work usually adds a DESIGN doc and a USAGE doc here.
- **Upstream sync ledger:** `wiki/upstream-sync-version-16.md` records every cherry-picked upstream commit and its outcome (picked-clean, picked-with-conflict-resolution, already-present, skipped). Sync commits update it with `docs(wiki): ...` commits.
- **PR docs gate (upstream):** `docs_checker.yml` fails a `feat` PR unless the body links a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs` or `backport`.
- The PR template asks you to explain the change, attach screenshots or GIFs, and put `closes #XXXX`.
