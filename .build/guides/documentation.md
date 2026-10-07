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
  - .github/helper/documentation.py
---

- **Public docs** live outside the repo: the README points to DeepWiki (`deepwiki.com/Tacten/biograph`).
- **In-repo design and usage docs** are in `wiki/` as UPPER-KEBAB or descriptive Markdown files. Examples: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md` (design), `BLOCK-APPOINTMENT-BOOKING-USAGE.md` and `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md` (usage), `insurance-parity-report.md`, the FHIR terminology implementation plan, and the running ledger `upstream-sync-version-16.md`. Images sit next to their docs.
- **Ledger docs are living records.** Upstream-sync work appends outcomes (picked-clean / picked-with-conflict-resolution / already-present / skipped) and commits them as `docs(wiki): ...`.
- **PR docs check:** `docs_checker.yml` fails `feat` PRs unless the body links to a `/wiki` URL on biograph.frappe.cloud or biograph.io, or contains `no-docs` or `backport`.
- Doctype field descriptions in the JSON schemas act as inline user docs.
