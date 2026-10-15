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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - AGENTS.md
---

# Documentation

- **README.md** covers the overview, install steps (bench), dev setup (pre-commit, semgrep), and a link to the external docs on DeepWiki and the Telegram group.
- **wiki/** holds in-repo feature docs as UPPER-KEBAB markdown. Two kinds are paired:
  - *Design* docs: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE.md`, `FHIR Terminology Service Parity — Implementation Plan.md`, `insurance-parity-report.md`.
  - *Usage* guides: `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`.
  - Usage guides are written for end users. They have an Introduction, a Quick Start, step-by-step sections with bold UI paths (**Healthcare > Patient Appointment**), and tables.
- **PR docs gate**: the `docs_checker.yml` workflow runs `.github/helper/documentation.py`. It requires any PR titled `feat...` to link to docs on `biograph.frappe.cloud`/`biograph.io` under `/wiki`. Add `no-docs` to the PR body to opt out; backports are skipped.
- The PR template asks contributors to update the relevant documentation and add screenshots or GIFs.
- Build guides live under `.build/` (`RULES.md`, guides). They are rendered into AGENTS.md between the managed markers, so do not edit that block by hand.
