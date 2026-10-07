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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **User/product docs are external.** The README points to DeepWiki (`deepwiki.com/Tacten/biograph`). The `docs_checker.yml` workflow expects `feat` PRs to link a docs page on `biograph.frappe.cloud` / `biograph.io` under `/wiki`.
- **In-repo design and usage docs** live in `wiki/` as uppercase or descriptive Markdown files, e.g.:
  - `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`
  - `BLOCK-APPOINTMENT-BOOKING-USAGE.md`
  - `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - `insurance-parity-report.md`
  - `FHIR Terminology Service Parity — Implementation Plan.md`
  - `upstream-sync-version-16.md`: an append-only ledger of upstream cherry-picks with outcome vocabulary (picked-clean, picked-with-conflict-resolution, already-present, skipped)
- Design docs pair with usage docs. Images such as screenshots sit next to them.
- The PR template asks contributors to explain the change, add screenshots/GIFs, update the necessary documentation, and reference `closes #XXXX`.
- Agent and contributor rules: `CLAUDE.md`, `AGENTS.md` (managed Guides block), and `.build/RULES.md`. The latter is the single source rendered into `.claude/rules` and `.github/instructions`.
