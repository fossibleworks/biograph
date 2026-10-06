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

## Where documentation lives
- **End-user and product docs** are external: DeepWiki for the Tacten repo, and the upstream docs at `biograph.frappe.cloud` / `biograph.io` under `/wiki`.
- **Fork design and usage docs** live in the repo-root `wiki/` as Markdown with UPPER-KEBAB names. There are two kinds:
  - Design docs (`DESIGN-...md`, implementation plans).
  - Usage guides (`...-USAGE.md` / `-USAGE-DOC.md`, with images placed next to them).
- **`wiki/upstream-sync-version-16.md`** is a living ledger for the upstream cherry-pick sync. Record batch outcomes, skipped commits and lint baselines there, using `docs(wiki): ...` commits. Its outcome vocabulary is picked-clean, picked-with-conflict-resolution, already-present, skipped.

## Documentation in PRs
- The `Documentation Required` workflow fails `feat` PRs unless the body links a docs page (biograph.frappe.cloud or biograph.io with `/wiki`) or contains `no-docs` or `backport`.
- Use the PR template in `.github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md`.

## Code comments
Comment sparingly, mainly to explain intent, for example the `on_login` explanation in `hooks.py`. Docstrings are uncommon.
