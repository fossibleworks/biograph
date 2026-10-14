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
  - .github/helper/documentation.py
  - context7.json
---

# Documentation

- **User and product docs** are external. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`), and `context7.json` registers the repo with Context7.
- **Fork design docs** live in `wiki/` as standalone Markdown files:
  - `DESIGN-<FEATURE>.md` for design
  - `<FEATURE>-USAGE.md` / `...-USAGE-DOC.md` for how-to
  - `*-report.md` and `*Implementation Plan.md` for parity analyses
  - Images sit alongside, e.g. `patient-duplicatecheck-thumbnail.png`
- **The upstream sync ledger** is `wiki/upstream-sync-version-16.md`. It records method, conflict policy, and the outcome of each batch and commit (picked-clean, picked-with-conflict-resolution, already-present, skipped). Commits updating it use `docs(wiki): ...`.
- **PR docs check:** `docs_checker.yml` runs `.github/helper/documentation.py`. Any PR titled `feat...` must link a `/wiki` page on `biograph.frappe.cloud` or `biograph.io` in its body. Otherwise the body must contain `no-docs` or `backport`.
- The PR template asks contributors to "Update necessary Documentation" and links Frappe/ERPNext doc guidelines.
- Code comments are sparse and explain non-obvious intent, e.g. `# Skip certain validations for unavailability appointments`. Docstrings are short one-liners.
