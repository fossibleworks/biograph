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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
---

- **README.md** covers the product intro, bench install, and dev setup (pre-commit, semgrep). It links to the full user docs on **DeepWiki** (`deepwiki.com/Tacten/biograph`) and to the Telegram community.
- **`wiki/`** holds the fork's in-repo design and usage docs as Markdown with UPPER-KEBAB names:
  - design docs (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `FHIR Terminology Service Parity — Implementation Plan.md`)
  - usage guides (`BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, with a table of contents, numbered sections and a screenshot or demo link)
  - reports and ledgers (`insurance-parity-report.md`, `upstream-sync-version-16.md`). Commits that update these use the `docs(wiki): ...` prefix.
- **Upstream docs check:** `docs_checker.yml` runs `.github/helper/documentation.py`. It fails `feat` PRs whose body lacks a `/wiki` link on `biograph.frappe.cloud` or `biograph.io`, unless the body contains `no-docs` or `backport`. It queries the `earthians/biograph` API, so in this fork it may not reflect fork PRs.
- **In code:** Frappe's `hooks.py` comment template is kept. Docstrings are sparse, and short comments explain non-obvious business rules (see the test comments in `test_fee_validity.py`).
- When adding a user-visible feature, add or extend a usage doc under `wiki/` and mention `no-docs` in the PR body if none is needed.
