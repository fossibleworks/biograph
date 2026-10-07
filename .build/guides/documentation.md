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
  - AGENTS.md
---

- **User/product docs** are external. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`).
- The docs check helper (`.github/helper/documentation.py`, run by `docs_checker.yml`) wants every `feat` PR to link a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, unless the PR body says `no-docs` or `backport`. Note that the helper currently queries the upstream repo's PR API.
- **In-repo design and usage docs** live in `wiki/` as UPPER-KEBAB or descriptive Markdown files. There are design docs (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`), usage guides (`BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`), parity reports and implementation plans.
- **Operational ledgers** go in `wiki/` too. `upstream-sync-version-16.md` records each upstream pick with an outcome from a fixed vocabulary: picked-clean, picked-with-conflict-resolution, already-present or skipped. Commits that update it use `docs(wiki): ...`.
- `patient_portal/README.md` covers the SPA.
- AI and agent guidance: `CLAUDE.md`, `AGENTS.md` (managed Build guides block), `.build/RULES.md` and `.github/instructions/`.
