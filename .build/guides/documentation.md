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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - AGENTS.md
---

- **Public docs:** the README points to DeepWiki (`deepwiki.com/Tacten/biograph`) for full documentation, and to a Telegram group for community support.
- **In-repo docs live in `wiki/`** as upper-case kebab-case Markdown files grouped by feature, with images stored alongside:
  - feature design docs, e.g. `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md` and `FHIR Terminology Service Parity — Implementation Plan.md`
  - usage guides, e.g. `BLOCK-APPOINTMENT-BOOKING-USAGE.md` and `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md` (with a table of contents and numbered sections)
  - reports and ledgers, e.g. `insurance-parity-report.md` and `upstream-sync-version-16.md` (a running record of how each upstream commit was handled)
- When a feature or sync batch changes, update its wiki page in a `docs(wiki): …` commit. Recent history shows the upstream-sync ledger is updated alongside each batch.
- **Docs gate (upstream workflow):** for a `feat` PR, `.github/helper/documentation.py` requires a docs link in the PR body, unless the body contains `no-docs` or `backport`. It still targets `earthians/biograph` and `biograph.frappe.cloud` / `biograph.io` `/wiki` URLs.
- The PR template asks contributors to "Update necessary Documentation".
- `.build/RULES.md` and `AGENTS.md` hold AI-session rules managed by Interactor Build. `RULES.md` is still an unfilled template.
