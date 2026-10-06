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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Documentation

- **Public docs** are external. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`), and upstream docs live on a `/wiki` site.
- **In-repo docs** live in `wiki/` as UPPER-KEBAB or title-case Markdown files. Each feature has a design doc and a usage doc. Examples:
  - `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md` + `BLOCK-APPOINTMENT-BOOKING-USAGE.md`
  - `PATIENT-DUPLICATE.md` + `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - Parity and implementation plans: `insurance-parity-report.md`, `FHIR Terminology Service Parity — Implementation Plan.md`
  - Upstream sync ledger: `upstream-sync-version-16.md`. Each sync batch is logged there (commit outcomes picked-clean / picked-with-conflict-resolution / already-present / skipped, with reasons), and commits to it use `docs(wiki): ...`.
- **PR docs gate:** `docs_checker.yml` fails `feat` PRs unless the body links to a `/wiki` page on an allowed docs host, or says `no-docs` or `backport`.
- The PR template asks for an explanation of the change, screenshots/GIFs, and `closes #XXXX`.
- In code, docstrings and comments are sparse. Add comments only where the logic is non-obvious (see the `on_login` comment in `hooks.py`).
