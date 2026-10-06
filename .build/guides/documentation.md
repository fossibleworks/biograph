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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - AGENTS.md
---

- **User and product docs** live outside the repo. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`). The upstream `docs_checker` workflow requires every `feat:` PR body to link a wiki page on `biograph.frappe.cloud` or `biograph.io` (`/wiki` in the path), unless the body contains `no-docs` or `backport`.
- **In-repo engineering docs** live in `wiki/` as flat Markdown files. File names are UPPER-KEBAB for feature docs: `DESIGN-<feature>.md` for designs, `<FEATURE>-USAGE[-DOC].md` for usage guides, and descriptive names for plans and reports (`insurance-parity-report.md`, `FHIR Terminology Service Parity — Implementation Plan.md`). Images sit next to them.
- **Upstream-sync ledger:** `wiki/upstream-sync-version-16.md` records every cherry-picked upstream commit with an outcome (picked-clean, picked-with-conflict-resolution, already-present, skipped). Update it in `docs(wiki): ...` commits whenever sync work happens.
- Agent and contributor rules: `CLAUDE.md` (Build engine workflow), `AGENTS.md` (managed guides index), `.build/RULES.md`, `.github/instructions/`.
- Code comments are sparse. Use the copyright header plus short inline comments that explain *why*. `hooks.py` keeps Frappe's boilerplate section headers.
