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
---

- **README.md**: product overview, installation through bench, a link to the public docs on DeepWiki, and developer pre-commit and semgrep setup.
- **`wiki/`** holds the repo's design and usage docs as Markdown. File names are UPPER-KEBAB for design and usage docs, e.g. `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`. The wiki also has parity and implementation plans (`insurance-parity-report.md`, `FHIR Terminology Service Parity — Implementation Plan.md`) and the upstream sync ledger (`upstream-sync-version-16.md`). Images sit next to the doc that uses them.
- Commit doc changes as `docs(wiki): …`.
- The **upstream sync ledger** records every cherry-picked upstream commit in a table (#, sha, subject, outcome, notes) under each batch, with fixed outcome values: picked-clean, picked-with-conflict-resolution, already-present, skipped, deferred. Keep it up to date when you sync.
- **Docs gate for features**: `docs_checker.yml` fails any `feat` PR whose body has no wiki link on `biograph.frappe.cloud` or `biograph.io` (`/wiki`). Writing `no-docs` or `backport` in the PR body skips the check. The PR template also asks contributors to update the documentation.
