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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- The README links to the complete user docs on DeepWiki (`deepwiki.com/Tacten/biograph`).
- The in-repo `wiki/` directory holds fork feature docs and engineering records written as UPPER-KEBAB markdown files: usage guides (`*-USAGE*.md`), design docs (`DESIGN-*.md`), implementation plans, parity reports, and the upstream sync ledger (`upstream-sync-version-16.md`). Commits that touch these use the `docs(wiki): ...` type.
- The `docs_checker` workflow fails `feat` PRs unless the PR body links to a `/wiki` page on biograph.frappe.cloud or biograph.io, or contains `no-docs` or `backport`. That check still targets the upstream earthians repo API.
- The PR template asks contributors to update the relevant documentation.
