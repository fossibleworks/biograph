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
  - AGENTS.md
---

- **User and product docs** live outside the repo. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`). The `docs_checker` workflow requires every `feat…` PR to link a wiki page on `biograph.frappe.cloud` or `biograph.io` (a URL containing `/wiki`), unless the PR body contains `no-docs` or `backport`.
- **In-repo design docs and ledgers** go in `wiki/` as Markdown. Names are UPPER-KEBAB for feature docs (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`), with paired design and usage docs per feature, plus reports and plans (`insurance-parity-report.md`, `FHIR Terminology Service Parity — Implementation Plan.md`).
- **Upstream sync** is recorded in `wiki/upstream-sync-version-16.md`: one table row per upstream commit with an outcome (`picked-clean`, `picked-with-conflict-resolution`, `already-present`, `skipped`) and notes. Commits that change the ledger use `docs(wiki): …`.
- **Code-level docs:** docstrings are sparse. Hook-wired functions note how they are applied (see `auth.py`). Comments in `hooks.py` explain non-obvious hooks.
- `AGENTS.md` and `CLAUDE.md` hold Build-managed guide blocks. Edit the source under `.build/`, not the rendered block.
