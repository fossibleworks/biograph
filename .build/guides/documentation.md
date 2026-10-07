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

- **Public documentation:** the README points to DeepWiki (deepwiki.com/Tacten/biograph) and a Telegram group.
- **In-repo design and usage docs:** these live in `wiki/` as UPPER-KEBAB markdown, for example:
  - `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`
  - `BLOCK-APPOINTMENT-BOOKING-USAGE.md`
  - `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - implementation plans and parity reports
- **Upstream sync ledger:** `wiki/upstream-sync-version-16.md` is a running record of every cherry-picked upstream commit, in tables per batch. Outcomes use a fixed vocabulary: picked-clean, picked-with-conflict-resolution, already-present, skipped. Update it as `docs(wiki): …` commits.
- **PR docs gate:** `docs_checker.yml` fails any `feat` PR whose body has no docs link (a `/wiki` URL on biograph.frappe.cloud or biograph.io) unless the body says `no-docs` or `backport`.
- **PR template:** asks for a description, screenshots and `closes #XXXX`.
