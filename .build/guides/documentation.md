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
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Documentation

- **README.md** covers the product overview, install steps, pre-commit/semgrep dev setup and links. The full user docs are external: [DeepWiki](https://deepwiki.com/Tacten/biograph).
- **`wiki/`** (in-repo) holds design and usage documents and engineering ledgers. They are ALL-CAPS or Title-Case markdown files:
  - `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md` and `BLOCK-APPOINTMENT-BOOKING-USAGE.md` (design + usage pairs)
  - `PATIENT-DUPLICATE*.md`
  - `FHIR Terminology Service Parity — Implementation Plan.md`
  - `insurance-parity-report.md`
  - `upstream-sync-version-16.md`: the cherry-pick ledger. It records every picked or skipped upstream commit and lint baselines. Update it in the same PR whenever upstream commits are synced, using `docs(wiki): ...` commits.
- **Docs gate inherited from upstream**: `docs_checker.yml` runs `.github/helper/documentation.py`. It fails `feat` PRs unless the body links a `/wiki` page on biograph.frappe.cloud or biograph.io, or contains `no-docs` or `backport`.
- The PR template asks you to "Update necessary Documentation" and to explain details, with screenshots.
- Do not write docs inside doctype JSON descriptions beyond field help text.
