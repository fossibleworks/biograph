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
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- The **README** links to the full user documentation on **DeepWiki** (`deepwiki.com/Tacten/biograph`) and to a Telegram community group.
- **`wiki/`** holds the in-repo design and usage docs, written as Markdown with UPPER-KEBAB names:
  - feature design: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`
  - usage guides: `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - parity and implementation plans: `insurance-parity-report.md`, `FHIR Terminology Service Parity — Implementation Plan.md`
  - the upstream sync ledger: `upstream-sync-version-16.md`
- Images that go with a doc sit next to it (`patient-duplicatecheck-thumbnail.png`).
- **Upstream-sync ledger convention:** each cherry-picked upstream commit gets a table row with `#`, upstream sha, subject, an outcome from a fixed vocabulary (`picked-clean`, `picked-with-conflict-resolution`, `already-present`, `skipped`) and notes. Ledger updates are committed as `docs(wiki): ...`.
- **Docs check in CI:** `.github/workflows/docs_checker.yml` fails `feat` PRs unless the body links a `/wiki` page on `biograph.frappe.cloud` / `biograph.io`, or contains `no-docs` or `backport`.
- The PR template asks for documentation updates and `closes #XXXX`.
