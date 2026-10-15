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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - context7.json
---

- **README.md** gives a product overview, bench install steps and dev setup (pre-commit, semgrep). It points to the full docs on DeepWiki (`deepwiki.com/Tacten/biograph`). `context7.json` registers the repo with Context7.
- **`wiki/`** holds in-repo feature documents in UPPER-KEBAB-CASE markdown. There are two kinds:
  - design and implementation plans, such as `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE.md`, `insurance-parity-report.md` and the FHIR terminology parity plan
  - user-facing usage guides (`*-USAGE*.md`) with a table of contents, overview, configuration and examples, plus screenshots stored next to them
- **PR docs gate:** `docs_checker.yml` runs `.github/helper/documentation.py`. Any PR whose title starts with `feat` must link a wiki page on `biograph.frappe.cloud` or `biograph.io` (path containing `/wiki`) in the PR body. Writing `no-docs` or `backport` in the body skips the check.
- The PR template asks contributors to "Update necessary Documentation" and to attach screenshots or GIFs.
- Docstrings and comments are sparse. Code comments explain the reason for non-obvious logic.
