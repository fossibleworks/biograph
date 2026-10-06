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
  - .github/workflows/docs_checker.yml
---

- Published end-user documentation is external: the README links to DeepWiki (`deepwiki.com/Tacten/biograph`).
- **In-repo design and usage docs** live in `wiki/` as upper-case kebab-case Markdown files: `DESIGN-*.md` for designs, `*-USAGE*.md` for how-tos, and parity reports and plans. Screenshots sit alongside them.
- **`wiki/upstream-sync-version-16.md`** is the ledger for upstream cherry-picks. Each batch gets a table with columns #, upstream sha, subject, outcome (picked-clean, picked-with-conflict-resolution, already-present, skipped, deferred) and notes. Record every sync decision there in a `docs(wiki): ...` commit.
- **The PR docs gate** (`docs_checker.yml`): a PR whose title starts with `feat` must link a `/wiki` URL on biograph.frappe.cloud or biograph.io in its body, or include `no-docs` (or `backport`).
- Code comments are sparse. Docstrings appear on whitelisted APIs.
