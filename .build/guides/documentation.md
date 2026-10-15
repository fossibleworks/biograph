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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

## Where docs live

- **`README.md`** covers the overview, installation (bench), dev setup (pre-commit, semgrep) and links. Full user documentation is hosted externally on **DeepWiki** (`deepwiki.com/Tacten/biograph`). There is also a `context7.json` registration.
- **`wiki/`** holds in-repo feature docs as Markdown, usually written in UPPER-KEBAB-CASE. There are two kinds:
  - *Design/plan docs*: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `FHIR Terminology Service Parity — Implementation Plan.md`, `PATIENT-DUPLICATE.md`, `insurance-parity-report.md`.
  - *Usage docs*: `*-USAGE.md` / `*-USAGE-DOC.md`. These have a table of contents, numbered sections, step-by-step navigation in bold (e.g. **Healthcare → Setup → Healthcare Settings**), and screenshots or a demo-video thumbnail stored next to them.
- `healthcare/config/docs.py` holds Frappe's in-app docs config.

## PR documentation requirement

- The `Documentation Required` workflow (`.github/helper/documentation.py`) fails any **`feat`** PR whose body lacks a link to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`. You can opt out by writing `no-docs` in the PR body; backport PRs are exempt.
- The PR template asks you to "Update necessary Documentation" and to attach screenshots/GIFs.
