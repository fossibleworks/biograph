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

- **User and product docs** live outside the repo. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`). The PR docs checker accepts wiki links on `biograph.frappe.cloud` / `biograph.io` (`/wiki`).
- **`feat` PRs need a docs link.** `docs_checker.yml` runs `.github/helper/documentation.py`. For PRs whose title starts with `feat`, the PR body must contain a docs URL on an allowed host with `/wiki` in the path, unless the body contains `no-docs` or `backport`.
- **In-repo `wiki/`** holds fork-specific markdown with UPPER-KEBAB file names:
  - design documents (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `FHIR Terminology Service Parity — Implementation Plan.md`)
  - usage guides (`BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`)
  - reports and ledgers (`insurance-parity-report.md`, `upstream-sync-version-16.md`). Update the sync ledger with each upstream-sync batch, using `docs(wiki): ...` commits.
- `patient_portal/README.md` documents the SPA.
- `.build/RULES.md` and `AGENTS.md` (Build-managed guides block) hold the agent and contributor rules. `CLAUDE.md` imports `RULES.md`.
- Code comments are sparse. Docstrings are short. Commented-out hook templates in `hooks.py` are the standard Frappe scaffolding.
