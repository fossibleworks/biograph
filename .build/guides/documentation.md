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

- **User and product docs** are external: the README points to DeepWiki (`deepwiki.com/Tacten/biograph`). The upstream docs-checker accepts links on `biograph.frappe.cloud` / `biograph.io` under `/wiki`.
- **In-repo docs** live in `wiki/` as Markdown. File names are UPPER-KEBAB-CASE, e.g. `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md` and `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`. There are also design plans and parity reports (`insurance-parity-report.md`, `upstream-sync-version-16.md`).
- **Upstream-sync work** must update the ledger in `wiki/upstream-sync-version-16.md`. Commits use the form `docs(wiki): ...`.
- **Docs check in CI:** `docs_checker.yml` fails `feat` PRs whose body lacks a docs link, unless the body contains `no-docs` or `backport`.
- **PR template:** asks for an explanation of the change, updated docs, and `closes #XXXX`.
