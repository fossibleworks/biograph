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
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - AGENTS.md
---

# Documentation

- **README.md** gives the product overview, install steps (bench), and the development setup (pre-commit, semgrep). It points to the hosted docs on DeepWiki (`deepwiki.com/Tacten/biograph`) and a Telegram group.
- **`wiki/`** holds in-repo feature docs as Markdown. Each feature usually gets two kinds of document:
  - a **design/plan** doc (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE.md`, `FHIR Terminology Service Parity — Implementation Plan.md`, `insurance-parity-report.md`), and
  - a **user guide** (`*-USAGE.md` / `*-USAGE-DOC.md`) with an introduction, quick start, tables, and numbered steps that use Desk navigation paths in bold (e.g. **Healthcare > Patient Appointment**).
  - Images sit next to the docs (`patient-duplicatecheck-thumbnail.png`).
- File naming is UPPER-KEBAB-CASE for feature docs.
- **PR rule:** the `Documentation Required` workflow fails `feat` PRs unless the body links docs (`/wiki` on `biograph.frappe.cloud` or `biograph.io`), or says `no-docs`, or is a `backport`.
- The PR template asks contributors to "Update necessary Documentation".
- `AGENTS.md` contains a Build-managed guide index (do not edit inside the managed block).
