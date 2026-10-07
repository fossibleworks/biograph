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
---

- **External user docs:** the README points to DeepWiki (`deepwiki.com/Tacten/biograph`). Upstream feature docs live on a hosted wiki (`biograph.frappe.cloud` / `biograph.io` `/wiki`).
- **`wiki/` (in repo):** Markdown design and usage documents in UPPER-KEBAB or descriptive names. Examples: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, `insurance-parity-report.md`, and an implementation plan for FHIR terminology parity. Write a design doc and a usage doc for substantial features.
- **`wiki/upstream-sync-version-16.md`** is the ledger for upstream cherry-pick batches: method, conflict policy, per-commit outcome (`picked-clean`, `picked-with-conflict-resolution`, `already-present`, `skipped`), and lint and test baselines. Sync work must update it, using `docs(wiki): ...` commits.
- **Docs-required check:** `.github/workflows/docs_checker.yml` runs `.github/helper/documentation.py`. A PR whose title starts with `feat` must link a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, unless the body contains `no-docs` or `backport`. That helper queries `earthians/biograph`, so on the fork it reflects upstream behaviour.
- In-code docs are sparse. Use short docstrings and section comments as in `hooks.py`. Don't add heavy docstring layers.
