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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
---

- **User and public docs** live outside the repo. The README points to DeepWiki, and the PR docs checker expects a link to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`.
- **The PR docs gate** is `.github/workflows/docs_checker.yml`, which runs `.github/helper/documentation.py`. A PR titled `feat...` fails unless its body links to those wiki hosts, or contains `no-docs`, or contains `backport`.
- **In-repo `wiki/`** holds fork feature docs, written in Markdown:
  - design docs in UPPERCASE, e.g. `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`
  - user guides, e.g. `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - reports and plans, e.g. `insurance-parity-report.md`
  - the upstream sync ledger, `upstream-sync-version-16.md`, which is updated with `docs(wiki): ...` commits
  - images sit alongside the docs
- `patient_portal/README.md` covers the SPA.
- Agent rules: `CLAUDE.md`, `AGENTS.md` (managed guides block) and `.build/RULES.md`, which is currently an unfilled template.
