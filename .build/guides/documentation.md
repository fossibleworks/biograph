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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
---

- **User-facing docs** are external: README links to DeepWiki (`deepwiki.com/Tacten/biograph`). The upstream doc-check helper looks for links to `biograph.frappe.cloud` or `biograph.io` `/wiki` pages.
- **In-repo docs** live in `wiki/` as flat Markdown files, usually in UPPER-KEBAB-CASE:
  - design docs: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `FHIR Terminology Service Parity — Implementation Plan.md`
  - usage guides: `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - reports and ledgers: `insurance-parity-report.md`, `upstream-sync-version-16.md`
  - images sit next to them (`patient-duplicatecheck-thumbnail.png`)
- **Feature PRs:** the `Documentation Required` workflow fails a `feat:` PR unless its body links to docs or includes `no-docs` (or `backport`).
- **Commit type:** documentation-only commits use `docs(wiki): ...`.
- **Agent guidance:** `CLAUDE.md`, `.build/RULES.md`, the managed guides block in `AGENTS.md`, and `.github/instructions/build-rules.instructions.md`.
