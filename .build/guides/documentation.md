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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - patient_portal/README.md
---

- **User docs** are external: the README points to DeepWiki (`deepwiki.com/Tacten/biograph`). The upstream docs checker (`docs_checker.yml` + `.github/helper/documentation.py`) **fails `feat` PRs** unless the PR body links a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs` or `backport`.
- **In-repo docs** live in `wiki/` as Markdown. Fork features get design docs and usage docs, named in upper kebab case (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`), plus parity reports and plans (`insurance-parity-report.md`, `FHIR Terminology Service Parity — Implementation Plan.md`).
- **Upstream sync ledger:** `wiki/upstream-sync-version-16.md` records the method, conflict policy and per-commit outcomes. Batches append to it with `docs(wiki): …` commits.
- `patient_portal/README.md` documents the SPA.
- AI/agent guidance is in `CLAUDE.md`, `AGENTS.md` (Build guides block) and `.build/RULES.md` (still a template).
