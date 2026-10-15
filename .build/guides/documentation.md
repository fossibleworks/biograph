---
title: Documentation
category: documentation
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - README.md
  - AGENTS.md
---

- **End-user and design docs** go in top-level `wiki/` as UPPER-KEBAB-CASE markdown (`PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`), plus plans and parity reports. Usage docs have a table of contents, numbered sections, click paths in bold (**Healthcare → Setup → Healthcare Settings**), tables, and optional screenshots or video thumbnails stored next to the doc.
- **Public docs** are on DeepWiki (`deepwiki.com/Tacten/biograph`), linked from the README, with Context7 configured in `context7.json`.
- **PR docs gate:** `docs_checker.yml` fails `feat` PRs unless the body links to a `/wiki` page on `biograph.frappe.cloud` / `biograph.io`, or says `no-docs` (backports are exempt). Its API call targets `earthians/biograph`.
- The PR template asks you to "Update necessary Documentation" and to reference issues with `closes #XXXX`.
- `healthcare/docs/current` is git-ignored.
- `AGENTS.md` holds a Build-managed guides index that points to `.build/RULES.md`.
