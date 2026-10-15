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
  - wiki/insurance-parity-report.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **README.md** gives the product overview, install instructions (bench get-app/install-app) and the developer setup (pre-commit, semgrep). It points to external docs on DeepWiki (`deepwiki.com/Tacten/biograph`) and to a Telegram group.
- **`wiki/`** holds in-repo docs as UPPER-KEBAB-CASE markdown files of two kinds:
  - **Usage docs**: `*-USAGE-DOC.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`. These have a numbered table of contents, Overview/Configuration/User Experience/Examples sections, and desk navigation paths in bold (e.g. **Healthcare → Setup → Healthcare Settings**). Images sit next to the doc.
  - **Design / parity docs**: `DESIGN-*.md`, `insurance-parity-report.md`, the FHIR terminology implementation plan. These have scope tables and branch/status matrices.
- **PR-level docs:** the `Documentation Required` workflow (`.github/helper/documentation.py`) fails `feat` PRs unless the PR body links to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`. To skip the check, put `no-docs` (or `backport`) in the PR body.
- The PR template asks contributors to "Update necessary Documentation" and to put `closes #XXXX` in the PR.
- Code comments are sparse and practical. Docstrings are uncommon. `healthcare/docs/current` is git-ignored.
