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
  - context7.json
---

- The **README** covers the introduction, installation, and development setup (pre-commit, semgrep). It links to the full docs on DeepWiki (`deepwiki.com/Tacten/biograph`) and to a Telegram community.
- **`wiki/`** holds in-repo markdown for each feature, in two kinds:
  - **Design docs**: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE.md`, and `FHIR Terminology Service Parity — Implementation Plan.md`.
  - **End-user usage guides**: `BLOCK-APPOINTMENT-BOOKING-USAGE.md` and `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`. These are task-oriented, with an introduction, quick start tables, and numbered steps that use bold UI paths like **Healthcare > Patient Appointment**.
  - Reports such as `insurance-parity-report.md` also live there.
  - File names are mostly UPPER-KEBAB-CASE.
- The **Documentation Required** CI check (`.github/helper/documentation.py`) fails `feat` PRs unless the PR body links a wiki page (biograph.frappe.cloud/biograph.io `/wiki`) or contains `no-docs`. Backports are exempt.
- `context7.json` exposes the repo for documentation indexing.
