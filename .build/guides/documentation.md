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
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
---

# Documentation

- **README.md** covers the product overview, install steps (bench get-app / install-app), pre-commit and semgrep setup, and links. The full user documentation is external: [DeepWiki](https://deepwiki.com/Tacten/biograph).
- **`wiki/`** holds the fork's in-repo docs as UPPER-KEBAB or descriptive Markdown files:
  - design docs (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`)
  - usage guides with a TOC and numbered sections (`PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`)
  - implementation plans and parity reports (`FHIR Terminology Service Parity — Implementation Plan.md`, `insurance-parity-report.md`)
  - the **upstream-sync ledger** (`upstream-sync-version-16.md`). It has one table row per upstream commit, using a fixed outcome vocabulary: picked-clean / picked-with-conflict-resolution / already-present / skipped.
- Usage docs give UI navigation in bold breadcrumbs, e.g. **Healthcare → Setup → Healthcare Settings**.
- **`docs_checker.yml`**: a PR titled `feat…` must link to docs on `biograph.frappe.cloud` or `biograph.io` under `/wiki`, or include `no-docs` or `backport` in the body. The helper queries the `earthians/biograph` API.
- Upstream-sync work records its decisions in the ledger with `docs(wiki): …` commits.
