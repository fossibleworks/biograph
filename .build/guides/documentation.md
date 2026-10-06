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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
---

- **README.md** is short: intro, key features, bench install, and links to DeepWiki (`deepwiki.com/Tacten/biograph`) and the Telegram group.
- **`wiki/`** holds the in-repo design and usage docs as UPPER-KEBAB or descriptive-title Markdown files. Examples: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`, `insurance-parity-report.md`, `upstream-sync-version-16.md`. Usage docs have a table of contents, numbered sections, Desk navigation paths in bold (**Healthcare → Setup → Healthcare Settings**) and screenshots or demo links.
- **Upstream sync ledger:** `wiki/upstream-sync-version-16.md` records every upstream commit in a table with these outcomes: picked-clean, picked-with-conflict-resolution, already-present, skipped, deferred. It also records batch totals and lint baselines. Recent commits update it with `docs(wiki): ...`.
- **Docs gate:** the `docs_checker.yml` workflow requires a `feat` PR to include a docs link (an http URL) in its body, or to say `no-docs`.
- Code docs are light: short docstrings, plus a copyright header on each file.
