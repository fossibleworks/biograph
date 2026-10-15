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
  - wiki/PATIENT-DUPLICATE.md
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - AGENTS.md
  - context7.json
---

## Where docs live

- **README.md** gives the product intro, install steps, pre-commit and Semgrep instructions, and links to external docs at **DeepWiki** (`deepwiki.com/Tacten/biograph`). `context7.json` registers the repo with Context7.
- **`wiki/`** holds in-repo feature design and usage docs as UPPER-KEBAB-CASE markdown: `DESIGN-*.md` for designs, `*-USAGE*.md` for user guides, plus parity reports and implementation plans. They usually have a problem statement, a proposed solution, then usage steps, with screenshots stored alongside (e.g. `patient-duplicatecheck-thumbnail.png`).
- **`patient_portal/README.md`** documents the SPA.
- **AGENTS.md** and the Build-managed guide block point to `.build/RULES.md` and `.build/guides/`.

## PR documentation gate

- `docs_checker.yml` runs `.github/helper/documentation.py`. If a PR title starts with **`feat`**, the body must link to a wiki page on `biograph.frappe.cloud` or `biograph.io` (with a `/wiki` path). The check is skipped when the body contains **`no-docs`** or `backport`.
- The PR template asks contributors to "Update necessary Documentation" and use `closes #XXXX`.

## Conventions for new docs

Add significant feature designs or usage guides under `wiki/`, following the existing naming. Code comments are sparse, and DocType files keep the standard Frappe copyright header.
