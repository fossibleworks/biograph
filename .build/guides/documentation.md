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
  - patient_portal/README.md
---

- **User docs** live outside the repo. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`), and the Telegram group is the community channel.
- **The docs gate:** `.github/workflows/docs_checker.yml` runs `.github/helper/documentation.py` on PRs. A PR whose title starts with `feat` must link to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or say `no-docs`, or be a `backport`.
- **In-repo design docs** go in `wiki/` as UPPER-KEBAB markdown. The pattern is `DESIGN-*.md` for designs and `*-USAGE*.md` for usage guides (e.g. `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`). Plans and reports use free-form names, e.g. `insurance-parity-report.md` and `FHIR Terminology Service Parity — Implementation Plan.md`.
- **Upstream sync work** is tracked in the `wiki/upstream-sync-version-16.md` ledger: method, outcome vocabulary (picked-clean / picked-with-conflict-resolution / already-present / skipped) and per-batch notes. Commits update it with `docs(wiki): ...`.
- `patient_portal/README.md` covers the SPA.
- Agent and project rules live in `CLAUDE.md`, `AGENTS.md` and `.build/RULES.md`.
