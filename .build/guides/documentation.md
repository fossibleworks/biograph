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

- **Where docs live:**
  - The README links the full product documentation on DeepWiki (`deepwiki.com/Tacten/biograph`). There is also a Context7 index (`context7.json`).
  - Feature design docs and user guides are in-repo Markdown under **`wiki/`**. Names are UPPER-KEBAB (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`), with images placed alongside.
- **Pairing:** larger features usually ship a *design* doc (`DESIGN-*` or plan) and a *usage* guide (`*-USAGE*.md`).
  - Usage guides use an Introduction, a Quick Start with tables, and numbered steps that reference Desk paths in bold (e.g. **Healthcare > Patient Appointment**).
- **PR gate:** `docs_checker.yml` runs `.github/helper/documentation.py`.
  - It fails `feat` PRs unless the body links docs on `biograph.frappe.cloud` / `biograph.io` with a `/wiki` path, or contains `no-docs` or `backport`.
  - That script still queries `earthians/biograph`.
- **Code-level:** controller files start with copyright/license header comments. Docstrings are sparse; explanatory inline comments are common in newer code.
