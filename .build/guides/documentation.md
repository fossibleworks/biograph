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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - patient_portal/README.md
---

- **User and product docs** live outside the repo. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`). The docs-checker workflow looks for wiki links on `biograph.frappe.cloud` / `biograph.io` with a `/wiki` path.
- **PR rule (docs_checker.yml):** any PR whose title starts with `feat` must link to the docs wiki in its body, or include `no-docs` (or be a `backport`). Otherwise the check fails.
- **In-repo `wiki/`:** Markdown design and usage notes named in UPPER-KEBAB or descriptive titles: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, an implementation plan for FHIR terminology parity, `insurance-parity-report.md`, and the **upstream sync ledger** `upstream-sync-version-16.md`. Put a design doc there for significant features (DESIGN-*.md), and a usage doc (*-USAGE*.md) for user-visible flows.
- **Upstream sync work:** record every cherry-pick outcome (picked-clean / picked-with-conflict-resolution / already-present / skipped) in the ledger with `docs(wiki): ... (upstream sync Bn)` commits.
- `patient_portal/README.md` covers the SPA.
- Agent and project rules: `CLAUDE.md` and `.build/RULES.md` (the source of truth); `AGENTS.md` and the tool mirrors are generated from them.
