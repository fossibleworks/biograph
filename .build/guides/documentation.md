---
title: Documentation
category: documentation
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - README.md
---

- **Fork design and usage docs** live in `wiki/` as upper-case kebab Markdown files. Examples: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, plus parity reports and plans. Pair a `DESIGN-*` doc with a `*-USAGE*` doc for larger features.
- **Upstream sync ledger:** `wiki/upstream-sync-version-16.md` records every cherry-picked, skipped and deferred commit from earthians/marley, batch by batch. Update it in `docs(wiki):` commits whenever you sync upstream.
- **Public docs:** the README points to DeepWiki (`deepwiki.com/Tacten/biograph`).
- **Docs gate on PRs:** `docs_checker.yml` runs `.github/helper/documentation.py`. A PR whose title starts with `feat` must link a docs URL (`biograph.frappe.cloud` or `biograph.io` with `/wiki` in the path), or say `no-docs` or `backport` in the body.
- The PR template asks contributors to update the relevant documentation and to write `closes #XXXX`.
