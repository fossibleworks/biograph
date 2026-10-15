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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - context7.json
---

- **User and product docs live outside the repo.** The README links to DeepWiki (`deepwiki.com/Tacten/biograph`), and `context7.json` registers the repo with Context7.
- **Feature design and usage docs** go in **`wiki/`** as UPPER-KEBAB markdown. Examples: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, `insurance-parity-report.md`, and an FHIR terminology implementation plan. They are structured with numbered sections and a table of contents, and can include screenshots (`patient-duplicatecheck-thumbnail.png`).
- **The PR docs gate:** the `Documentation Required` workflow (`.github/helper/documentation.py`) fails any PR whose title starts with `feat` unless one of these applies:
  - the body links to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`
  - the body contains `no-docs`
  - it is a backport
- The PR template asks contributors to "Update necessary Documentation" and to add screenshots or GIFs.
- **Build-managed docs:** `CLAUDE.md`, `AGENTS.md` and `.build/` (vision, RULES, guides) are managed by Interactor Build. Edit the source files under `.build/`, not the generated "BEGIN BUILD GUIDES" blocks.
- **In-code documentation** is light. Comments in `hooks.py` explain hook intent, and docstrings are sparse.
