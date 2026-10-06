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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **User and product docs** are external. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`), and the issue templates point to `biograph.frappe.cloud/docs`.
- **In-repo design and usage docs** live in **`wiki/`** as UPPER-KEBAB or descriptive Markdown files. Examples: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md` (design), `BLOCK-APPOINTMENT-BOOKING-USAGE.md` and `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md` (usage guides), and `insurance-parity-report.md`, `FHIR Terminology Service Parity — Implementation Plan.md` (plans and reports). Images sit alongside them.
- **`wiki/upstream-sync-version-16.md`** is the running ledger for upstream cherry-picks. It records the method, the conflict policy, per-batch outcomes (picked-clean, picked-with-conflict-resolution, already-present, skipped) and lint baselines. Update it whenever you do sync work, and use `docs(wiki): ...` commits.
- **PR docs gate:** `docs_checker.yml` fails `feat` PRs unless the body links to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs` or `backport`.
- The PR template asks contributors to update the relevant documentation and to link issues with `closes #XXXX`.
- Agent and contributor guidance lives in `CLAUDE.md`, `AGENTS.md` and `.build/RULES.md`, which Build manages.
