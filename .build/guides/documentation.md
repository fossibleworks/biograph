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
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **End-user documentation is hosted outside the repo.** The README points to DeepWiki (`deepwiki.com/Tacten/biograph`). The `docs_checker.yml` workflow makes PRs whose titles start with `feat` include a docs link to `biograph.frappe.cloud` or `biograph.io` under `/wiki`. To skip the check, put `no-docs` or `backport` in the PR body.
- **In-repo design and usage docs live in `wiki/`** as Markdown. File names are UPPER-KEBAB-CASE: `DESIGN-<FEATURE>.md` for designs and `<FEATURE>-USAGE[-DOC].md` for usage guides. Screenshots sit next to the docs as `.png`. Some longer plans use free-form titles ("FHIR Terminology Service Parity — Implementation Plan.md").
- **Ledgers:** `wiki/upstream-sync-version-16.md` records every upstream sync batch: method, outcome vocabulary (picked-clean, picked-with-conflict-resolution, already-present, skipped), baselines and lint counts. Update it in `docs(wiki): …` commits.
- `patient_portal/README.md` covers the SPA.
- PR descriptions follow `.github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md`: explain the problem being solved, add screenshots/GIFs for UI changes, and use `closes #XXXX`.
