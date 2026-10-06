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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
---

- The public docs are hosted on DeepWiki (linked from the README). The upstream check (`docs_checker.yml` → `.github/helper/documentation.py`) requires every `feat` PR to link a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`. You can opt out by writing `no-docs` (or `backport`) in the PR body.
- In this fork, feature docs, design notes and operational ledgers live in **`wiki/`** as UPPER-KEBAB or descriptive Markdown files. Examples: `*-USAGE-DOC.md` / `*-USAGE.md` for end-user guides, `DESIGN-*.md` for design docs, `upstream-sync-version-16.md` for the cherry-pick ledger, and parity reports/plans. Images sit next to them (e.g. `patient-duplicatecheck-thumbnail.png`).
- Usage docs start with a Table of Contents and an Overview, then cover configuration, user experience, and examples.
- Upstream-sync work is recorded in the ledger as `docs(wiki): ...` commits. Each upstream commit gets an outcome: picked-clean, picked-with-conflict-resolution, already-present, or skipped.
- `patient_portal/README.md` documents the SPA.
