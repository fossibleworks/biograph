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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - AGENTS.md
---

- **User and feature docs** are hosted externally. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`).
- **The `docs_checker.yml` gate:** a PR titled `feat...` must link to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io` in its body. Without that link, the body must contain `no-docs` (or `backport`). Note that the helper calls the upstream `earthians/biograph` API.
- **The in-repo `wiki/` folder** holds the fork's markdown docs:
  - feature usage guides (`BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`)
  - design docs (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE.md`)
  - implementation plans and parity reports (`FHIR Terminology Service Parity — Implementation Plan.md`, `insurance-parity-report.md`)
  - the upstream sync ledger (`upstream-sync-version-16.md`)
- Usage guides start with an H1 `<Feature> - User Guide`, then Introduction, a "This guide covers" bullet list and Quick Start, with `---` between sections.
- The upstream-sync ledger records every cherry-picked upstream commit and its outcome (picked-clean, picked-with-conflict-resolution, already-present, skipped). Commits that update it use `docs(wiki): ...`.
- `patient_portal/README.md` documents the portal build.
- `AGENTS.md` is a managed index of `.build/guides/` and `.build/RULES.md`. Edit those source files, not the index.
