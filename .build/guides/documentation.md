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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **User/product docs** are external. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`), and the inherited docs checker expects a wiki link on `biograph.frappe.cloud` or `biograph.io`.
- **`docs_checker.yml`** fails a PR whose title starts with `feat` unless the body links a `/wiki` doc on an allowed host, or contains `no-docs` or `backport`. (Note: the helper queries the upstream `earthians/biograph` repo.)
- **In-repo `wiki/`** holds fork-specific design and usage docs as UPPER-KEBAB or title-case Markdown files (e.g. `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`) and parity/sync ledgers (`upstream-sync-version-16.md`, `insurance-parity-report.md`). Upstream-sync batches log every outcome in the ledger with `docs(wiki): ...` commits.
- **PR template** asks for: the target branch, a conventional title, passing tests, server-side validations, updated documentation, and `closes #XXXX`, plus details and screenshots.
- Code comments are sparse and explain *why*, e.g. the `on_login` comment in `hooks.py`.
