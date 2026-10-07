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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/helper/documentation.py
  - AGENTS.md
---

- **Product docs** are external. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`).
- **The `wiki/` directory** holds in-repo feature and design documents as Markdown:
  - Design docs: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`
  - Usage guides: `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - Plans and reports: the FHIR terminology parity plan, `insurance-parity-report.md`
  - The **upstream sync ledger** (`upstream-sync-version-16.md`). Each cherry-picked upstream commit is recorded there with an outcome (picked-clean, picked-with-conflict-resolution, already-present, or skipped) and notes. Commits like `docs(wiki): ...` keep it current.
- **`docs_checker.yml`** fails PRs whose title starts with `feat` unless the body links to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs` or `backport`.
- **Agent-facing docs:** `CLAUDE.md`, `AGENTS.md` (managed guides block), and `.build/RULES.md`.
