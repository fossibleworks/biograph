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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **README.md** covers the product overview, installation through bench, development (pre-commit and semgrep), and links. End-user documentation is hosted externally on DeepWiki (`deepwiki.com/Tacten/biograph`).
- **`wiki/`** holds in-repo markdown for fork-specific features and engineering records:
  - Design docs, in UPPER-KEBAB file names: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE.md`
  - Usage guides: `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - Plans and reports: `FHIR Terminology Service Parity — Implementation Plan.md`, `insurance-parity-report.md`
  - The upstream sync ledger `upstream-sync-version-16.md`. It records every cherry-picked upstream commit with an outcome (picked-clean / picked-with-conflict-resolution / already-present / skipped) and notes. Commits that update it use `docs(wiki): …`.
- **PR-level docs gate** (upstream workflow `docs_checker.yml`): a PR whose title starts with `feat` must link a docs page (a `/wiki` path on an allowed docs host), or say `no-docs` or `backport` in its body.
- The PR template asks contributors to "Update necessary Documentation" and to follow the ERPNext docs page format.
- Code comments are sparse. Docstrings are uncommon except in newer modules such as the `setup/` and duplicate-check code.
