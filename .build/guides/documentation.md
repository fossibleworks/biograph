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
  - wiki/FHIR Terminology Service Parity — Implementation Plan.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
---

**Where documentation lives**
- `README.md`: overview, install, pre-commit and semgrep setup. It links to the external docs at DeepWiki (`deepwiki.com/Tacten/biograph`) and to a Telegram group.
- `wiki/`: in-repo design, usage and process docs, written in Markdown.
  - Feature designs use UPPER-KEBAB names: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE.md`.
  - Usage guides end in `-USAGE` or `-USAGE-DOC` (`BLOCK-APPOINTMENT-BOOKING-USAGE.md`).
  - Implementation plans and parity reports use descriptive titles (`FHIR Terminology Service Parity — Implementation Plan.md`, `insurance-parity-report.md`).
  - Ledgers record process work (`upstream-sync-version-16.md`).
- Design docs open with Context/Problem statement, then Goal, then plan sections. They reference PR numbers and the doctypes and files involved.

**Doc requirement on PRs**
- `docs_checker.yml` fails any `feat` PR whose body lacks a docs link (biograph.frappe.cloud or biograph.io `/wiki`).
- To opt out, put `no-docs` in the PR body; backports are exempt.
- In practice, the fork records documentation as `docs(wiki): ...` commits under `wiki/`.

**Other places**
- Code comments and docstrings are sparse but explain why something is done, for example the `on_login` hook comment.
- Issue templates (`bug_report.yaml`, `feature_request.yaml`) and the PR template live in `.github/ISSUE_TEMPLATE/`.
