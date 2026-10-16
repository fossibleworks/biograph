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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - AGENTS.md
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **User docs:** these live outside the repo. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`).
- **Docs gate on PRs:** the `docs_checker.yml` workflow fails a PR whose title starts with `feat` unless the body links to a wiki page on `biograph.frappe.cloud` / `biograph.io` (`/wiki` path). The body can instead contain `no-docs`, or `backport` for backports.
- **In-repo `wiki/`:** design docs, usage docs and reports as UPPER-KEBAB or descriptive Markdown files. Examples:
  - `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`
  - `BLOCK-APPOINTMENT-BOOKING-USAGE.md`
  - `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - `insurance-parity-report.md`
  - `upstream-sync-version-16.md`, a running ledger of upstream cherry-picks with outcome vocabulary: picked-clean / picked-with-conflict-resolution / already-present / skipped
  
  A feature usually gets a design doc and a usage doc. Usage docs have a numbered table of contents (Overview, Configuration, User Experience, Examples).
- **Agent guides:** `AGENTS.md` renders a managed block that lists `.build/RULES.md` and the guides under `.build/guides/`.
- **PR template:** asks for change details and doc updates, plus `closes #XXXX`.
