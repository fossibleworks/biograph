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
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
---

- **User and product docs** live outside the repo: the README links to DeepWiki (`deepwiki.com/Tacten/biograph`), and the upstream `docs_checker.yml` expects `feat` PRs to link to a `/wiki` page on `biograph.frappe.cloud` / `biograph.io`.
- **In-repo `wiki/`** holds the fork's design and usage docs as Markdown, mostly in UPPER-KEBAB-CASE: `DESIGN-*.md` for designs, `*-USAGE*.md` for usage guides, plus parity and implementation-plan reports. Screenshots sit alongside them (`patient-duplicatecheck-thumbnail.png`). Usage docs open with a numbered table of contents.
- **Upstream sync ledger:** `wiki/upstream-sync-version-16.md` records each sync batch (picked, skipped, deferred commits and why). Update it with `docs(wiki): ...` commits whenever upstream commits are cherry-picked.
- **`patient_portal/README.md`** documents the SPA.
- **Agent docs:** `CLAUDE.md` (engine workflow), `AGENTS.md`, and `.build/RULES.md`.
- **Code comments:** sparse. Copyright headers in older files, and short docstrings on helpers.
