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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **User and product docs** live outside the repo. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`).
- **The upstream docs check** (`docs_checker.yml` / `.github/helper/documentation.py`) fails `feat:` PRs unless the PR body links a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs` or `backport`. It queries the upstream `earthians/biograph` repo.
- **In-repo design and usage docs** go in `wiki/` as Markdown, named with UPPER-KEBAB-CASE titles. Examples:
  - `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md` (design)
  - `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md` (usage)
  - parity reports and plans
- **The upstream-sync ledger** is `wiki/upstream-sync-version-16.md`. It records each cherry-picked upstream commit in a table with these outcome values: picked-clean, picked-with-conflict-resolution, already-present, skipped. Each row gives a reason. Update it in `docs(wiki): ...` commits.
- **Code comments** are sparse and explain *why*. `hooks.py` keeps Frappe's commented scaffold sections.
- The PR template asks you to "Update necessary Documentation" and to add screenshots or GIFs for UI changes.
- **Agent rules** are in `CLAUDE.md`, `AGENTS.md` (managed by Build) and `.build/RULES.md`, which is still an unfilled template.
