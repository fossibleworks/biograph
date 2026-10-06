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

- **README.md** covers the overview, installation (bench), and development setup (pre-commit, semgrep). It links the full docs on DeepWiki (`deepwiki.com/Tacten/biograph`).
- **`wiki/`** holds in-repo markdown for feature design and usage. Design docs use the `DESIGN-*.md` prefix, usage docs use `*-USAGE*.md`, and there are parity/implementation plans and the upstream sync ledger (`upstream-sync-version-16.md`, which records the per-commit outcomes picked-clean, picked-with-conflict-resolution, already-present, and skipped). Images sit next to their docs.
- **PR rule:** the `Documentation Required` workflow fails any `feat` PR whose body lacks a docs link to `biograph.frappe.cloud`/`biograph.io` `/wiki`, unless the body says `no-docs` or `backport`.
- The PR template asks contributors to update the relevant docs and to put `closes #XXXX` in the description.
