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
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
---

- **User and product docs** live outside the repo. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`). Upstream feature docs live on the Biograph Frappe wiki (`biograph.frappe.cloud` or `biograph.io` `/wiki`).
- **Docs gate for `feat` PRs:** `docs_checker.yml` runs `.github/helper/documentation.py`. It fails any PR titled `feat...` whose body has no link to a `biograph.frappe.cloud` or `biograph.io` URL containing `/wiki`. To bypass it, put `no-docs` or `backport` in the PR body.
- **In-repo design docs:** the fork keeps design, usage and planning docs as Markdown in `wiki/`. Examples: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, `insurance-parity-report.md`, and the upstream sync ledger `upstream-sync-version-16.md`. Names are UPPER-KEBAB for design and usage docs. Images sit alongside the docs.
- **Ledgers:** upstream-sync work is recorded in `wiki/upstream-sync-version-16.md` (method, outcome vocabulary, per-batch results), using `docs(wiki): ...` commits.
- **Code comments:** `hooks.py` keeps Frappe's scaffold comments. Add a short explanatory comment block when you add non-obvious hooks, as the `on_login` comment does.
