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
  - wiki/PATIENT-DUPLICATE.md
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Where docs live**
- `README.md`: product intro, install with bench, and the dev setup for pre-commit and Semgrep. The public docs are linked out to DeepWiki (`deepwiki.com/Tacten/biograph`).
- `wiki/`: in-repo markdown for fork features and engineering records. Files use UPPER-KEBAB-CASE names, sometimes with a `DESIGN-` or `-USAGE` suffix:
  - Design docs: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `FHIR Terminology Service Parity — Implementation Plan.md`.
  - Usage guides: `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`.
  - Problem/feature write-ups: `PATIENT-DUPLICATE.md`, which has a "Tag:" line naming the customer and a problem statement.
  - Reports and ledgers: `insurance-parity-report.md`, `upstream-sync-version-16.md`. The sync ledger records method, conflict policy, a per-commit outcome (`picked-clean`, `picked-with-conflict-resolution`, `already-present`, `skipped`) and lint baselines.
  - Images sit next to the docs, for example `patient-duplicatecheck-thumbnail.png`.
- Wiki updates are committed as `docs(wiki): ...`.

**Documentation gate in CI:** `docs_checker.yml` runs `.github/helper/documentation.py`. Any PR whose title starts with `feat` must link a docs page on `biograph.frappe.cloud` or `biograph.io` under `/wiki`, unless the body contains `no-docs` or `backport`.

**PR template:** asks for details of the change, screenshots or GIFs, "Update necessary Documentation", and `closes #XXXX`.
