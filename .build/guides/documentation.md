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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - patient_portal/README.md
---

# Documentation

- **User docs** are external. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`), and the upstream docs checker looks for links on `biograph.frappe.cloud` / `biograph.io` under `/wiki`.
- **In-repo `wiki/`** holds design docs and usage guides as flat markdown files with SCREAMING-KEBAB names: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, plus parity reports and implementation plans. Screenshots sit alongside them (`patient-duplicatecheck-thumbnail.png`).
- **Sync ledger**: `wiki/upstream-sync-version-16.md` records every upstream cherry-pick with its outcome (`picked-clean`, `picked-with-conflict-resolution`, `already-present`, `skipped`) and lint before/after counts. Upstream-sync work must update it, using `docs(wiki): ...` commits.
- **Docs-required gate**: `docs_checker.yml` fails `feat` PRs unless the PR body links docs or contains `no-docs` (or `backport`).
- `patient_portal/README.md` covers the portal.
- Agent and contributor guidance: `CLAUDE.md` (engine workflow), `.build/RULES.md` (rules source), `AGENTS.md` (Build-managed mirror).
