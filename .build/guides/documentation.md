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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Documentation

- **README.md** covers the overview, installation through bench, dev setup (pre-commit, semgrep), and a link to the full docs on **DeepWiki** (`deepwiki.com/Tacten/biograph`).
- **`wiki/`** holds the in-repo docs for fork features and engineering work. They come in two kinds:
  - **Usage docs** (`*-USAGE-DOC.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`): numbered sections and a table of contents, with steps written as `Healthcare → Setup → Healthcare Settings`, plus screenshots or demo links.
  - **Design and plan docs** (`DESIGN-*.md`, `* — Implementation Plan.md`, `insurance-parity-report.md`).
  - **Upstream sync ledger** (`upstream-sync-version-16.md`). Update it with `docs(wiki): ...` commits as each sync batch progresses.
- **PR docs gate:** `docs_checker.yml` fails `feat` PRs unless the body links to a docs URL (`/wiki` on biograph.frappe.cloud or biograph.io). To skip it, put `no-docs` or `backport` in the PR body. Note that this helper queries `earthians/biograph`.
- The PR template asks contributors to "Update necessary Documentation".
- Code comments are sparse. Use docstrings only for non-obvious logic.
