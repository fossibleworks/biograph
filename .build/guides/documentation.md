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
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**End-user documentation** lives outside this repo:
- The README points to DeepWiki (`deepwiki.com/Tacten/biograph`).
- Upstream docs are on the Frappe Cloud wiki (`biograph.frappe.cloud` / `biograph.io` `/wiki`).

**In-repo docs (`wiki/`):** fork design, usage, and process documents in UPPER-KEBAB or kebab-case markdown. Examples:
- `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md` and `BLOCK-APPOINTMENT-BOOKING-USAGE.md` (a design + usage pair)
- `PATIENT-DUPLICATE.md` and `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
- `insurance-parity-report.md`
- `upstream-sync-version-16.md`: the cherry-pick ledger, recording method, conflict policy, and per-commit outcomes

Ledger and wiki updates are committed as `docs(wiki): ...`.

**PR documentation gate:** `docs_checker.yml` runs `.github/helper/documentation.py`. Any PR titled `feat...` must link a `/wiki` page on `biograph.frappe.cloud` or `biograph.io` in its body, unless the body contains `no-docs` or `backport`.

The PR template asks contributors to update the relevant documentation and to put `closes #XXXX` in the PR body.
