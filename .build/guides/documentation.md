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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **User and developer docs** live outside the repo. The README points to [DeepWiki](https://deepwiki.com/Tacten/biograph), and the Telegram group is the community channel.
- **In-repo design and usage docs** are in `wiki/` as standalone Markdown files.
  - Names are UPPER-KEBAB, for example `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`.
  - Some files are descriptive, such as `FHIR Terminology Service Parity — Implementation Plan.md` and `insurance-parity-report.md`.
  - Convention: a DESIGN doc plus a USAGE doc per larger feature. Images (thumbnails) sit next to the doc.
- **Upstream sync ledger:** `wiki/upstream-sync-version-16.md` records each cherry-picked upstream commit and its outcome (`picked-clean`, `picked-with-conflict-resolution`, `already-present`, `skipped`). It also records lint baselines. Doc updates are committed as `docs(wiki): …`.
- **PR docs gate:** `docs_checker.yml` runs `.github/helper/documentation.py`, which requires `feat` PRs to link a `/wiki` page on `biograph.frappe.cloud` or `biograph.io` unless the body contains `no-docs` or `backport`. The script queries the upstream `earthians/biograph` repo.
- The PR template asks contributors to "Update necessary Documentation" and add `closes #XXXX`.
- Python code uses short docstrings on helpers and inline `#` comments for intent. Legacy files carry copyright headers.
