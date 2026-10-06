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
  - patient_portal/README.md
---

- **README.md** gives the overview, installation, the development (pre-commit and semgrep) steps, and a link to the external docs on DeepWiki (`deepwiki.com/Tacten/biograph`). Community support is on Telegram.
- **`wiki/`** holds in-repo markdown for fork features and processes, named in UPPER-KEBAB-CASE or descriptive titles:
  - design docs, e.g. `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md` and `FHIR Terminology Service Parity — Implementation Plan.md`
  - usage guides, e.g. `BLOCK-APPOINTMENT-BOOKING-USAGE.md` and `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md` (images such as `patient-duplicatecheck-thumbnail.png` sit alongside)
  - reports and ledgers, e.g. `insurance-parity-report.md` and `upstream-sync-version-16.md`. The ledger records every upstream pick with an outcome (picked-clean, picked-with-conflict-resolution, already-present, skipped) and notes.
- Commit wiki updates as `docs(wiki): ...`.
- **Upstream PR rule:** the `docs_checker.yml` workflow fails `feat` PRs that lack a docs link (biograph wiki domain) unless the body contains `no-docs` or `backport`.
- `patient_portal/README.md` documents the SPA.
- Docstrings are sparse. Code comments are short and explain why.
