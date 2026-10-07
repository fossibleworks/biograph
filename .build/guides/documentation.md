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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **README.md** covers installation (bench), development setup (pre-commit, semgrep) and links to the external docs at DeepWiki (`deepwiki.com/Tacten/biograph`).
- **`wiki/`** holds in-repo design and usage docs. Files use UPPER-KEBAB-CASE names: `DESIGN-<FEATURE>.md` for designs, `<FEATURE>-USAGE[-DOC].md` for usage guides, and images sit beside them. It also holds plans and reports (`FHIR Terminology Service Parity — Implementation Plan.md`, `insurance-parity-report.md`) and the upstream sync ledger `upstream-sync-version-16.md`. Commits to the wiki use `docs(wiki): ...`.
- **PR docs check**: `docs_checker.yml` fails a `feat` PR unless its body links to a `/wiki` page on `biograph.frappe.cloud` or `biograph.io`, or contains `no-docs`. Backports are exempt.
- The PR template asks for an explanation of the change, screenshots or GIFs, and `closes #XXXX`.
- Code comments are sparse. Doctype descriptions live in the doctype JSON.
