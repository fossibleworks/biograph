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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
---

- **User and product docs** are external. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`). There is no `docs/` directory, and `healthcare/docs/current` is gitignored.
- **In-repo docs** live in `wiki/` as upper-case kebab Markdown files. They are either design docs (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `FHIR Terminology Service Parity — Implementation Plan.md`) or usage guides (`BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`), with images next to them.
- **Sync ledgers and reports** are also kept in `wiki/` (`upstream-sync-version-16.md`, `insurance-parity-report.md`). Upstream-sync work records every cherry-picked commit in a table with the outcome vocabulary `picked-clean`, `picked-with-conflict-resolution`, `already-present` and `skipped`, and adds `docs(wiki): ...` commits as batches progress.
- **The PR docs gate** (`docs_checker.yml` → `.github/helper/documentation.py`): a PR whose title starts with `feat` must link to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, unless the body contains `no-docs` or `backport`. Note that the script queries the `earthians/biograph` API.
- `patient_portal/README.md` documents the portal frontend.
- `healthcare/config/docs.py` holds Frappe docs config.
