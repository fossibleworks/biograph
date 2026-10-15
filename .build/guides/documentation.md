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
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **User documentation** lives outside the repo. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`), and the upstream docs live on `biograph.frappe.cloud` / `biograph.io` `/wiki`.
- **The docs check is enforced for features:** `.github/workflows/docs_checker.yml` runs `.github/helper/documentation.py`. Any PR whose title starts with `feat` must include a docs link to `biograph.frappe.cloud` or `biograph.io` under `/wiki` in its body. Write `no-docs` in the body to opt out explicitly, and backports are exempt.
- **In-repo `wiki/`** holds design docs and usage guides for larger features, as UPPER-KEBAB-CASE markdown: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, the FHIR terminology implementation plan and the insurance parity report. They typically pair a design or plan doc with a user guide, opening with an H1, then an Overview/Context section and a TOC.
- The PR template asks for problem details, screenshots or GIFs, and `closes #XXXX`.
- `hooks.py` uses Frappe's commented-template style. Code comments are sparse.
