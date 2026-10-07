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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
---

- **User-facing docs** live outside the repo. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`). The `docs_checker.yml` workflow runs `.github/helper/documentation.py`, which fails any `feat` PR whose body has no wiki link on `biograph.frappe.cloud`/`biograph.io` (a `/wiki` path), unless the body says `no-docs` or `backport`.
- **In-repo design and usage docs** go in `wiki/` as Markdown. Existing examples are a design doc (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`), usage guides (`BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`), parity reports and plans (`insurance-parity-report.md`, the FHIR Terminology plan) and the upstream-sync ledger (`upstream-sync-version-16.md`). Most names are UPPER-KEBAB-CASE, and images sit next to the doc.
- Upstream-sync work must update the ledger in `wiki/upstream-sync-version-16.md`, recording each commit's outcome (picked-clean, picked-with-conflict-resolution, already-present or skipped), in commits such as `docs(wiki): ...`.
- Inside the code: the copyright header, short docstrings, and comments in `hooks.py` that explain non-obvious hooks.
- Agent and contributor rules come from `.build/RULES.md`, which is mirrored into AGENTS.md, `.claude`, `.cursor` and `.github/instructions`.
