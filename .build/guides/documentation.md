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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **Public docs** are linked from the README and hosted outside the repo on **DeepWiki** (`deepwiki.com/Tacten/biograph`).
- **In-repo docs** live in **`wiki/`** as flat Markdown files:
  - Design docs: `DESIGN-*.md`
  - Usage guides: `*-USAGE*.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - Parity and implementation plans: `insurance-parity-report.md`, `FHIR Terminology Service Parity — Implementation Plan.md`
  - Upstream-sync ledger: `upstream-sync-version-16.md`
  - Usage guides start with a table of contents and numbered sections. Images sit alongside the Markdown.
- **Upstream sync work** is recorded in the ledger, with per-commit outcomes (picked-clean, picked-with-conflict-resolution, already-present, skipped, deferred). These changes use `docs(wiki): ...` commits.
- **PR docs requirement:** the inherited `docs_checker.yml` fails a `feat` PR unless its body links a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs` or `backport`.
- The PR template asks contributors to update the relevant documentation and to add `closes #XXXX`.
