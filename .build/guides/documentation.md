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
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **README.md** covers the product overview, installation, pre-commit and Semgrep setup. It links out for full docs: DeepWiki (`deepwiki.com/Tacten/biograph`) and a Telegram group.
- **`wiki/`** (in repo) holds feature-level design and usage docs as upper-case-hyphenated Markdown. Some are design docs (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, the FHIR Terminology Service plan, `insurance-parity-report.md`). Others are user guides (`*-USAGE-DOC.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`). The usage docs have a numbered table of contents (Overview, Configuration, User Experience, Examples). Images are stored next to the docs.
- **Docs gate on features:** the `Documentation Required` workflow fails any PR whose title starts with `feat` unless its body links to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs` (backports are exempt).
- PRs should explain the change and include screenshots or GIFs for UI changes, per the PR template.
- Code comments are sparse. Docstrings are not systematically used.
