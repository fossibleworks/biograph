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
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - patient_portal/README.md
---

- **README.md** gives the overview, install steps, and pre-commit/semgrep setup. It links to the full user docs on **DeepWiki** (`deepwiki.com/Tacten/biograph`) and to the Telegram community.
- **`wiki/`** holds design docs, usage guides and engineering ledgers as Markdown with UPPER-KEBAB or descriptive names. Examples: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, `insurance-parity-report.md`, and `upstream-sync-version-16.md`, which logs every upstream cherry-pick with its outcome. Images sit next to the docs.
- `patient_portal/README.md` documents the SPA.
- Upstream CI (`docs_checker.yml`) fails `feat` PRs unless the body links to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs` or `backport`.
- Commit doc-only changes as `docs(...)`, for example `docs(wiki): ...`.
