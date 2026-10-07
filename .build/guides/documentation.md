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
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
---

- **Public docs:** the README points to DeepWiki (`deepwiki.com/Tacten/biograph`) for full documentation, with Telegram for community support.
- **Fork design and usage docs** live in the flat `wiki/` directory as Markdown, named in UPPER-KEBAB or descriptive titles. Examples: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md` with a thumbnail image, `insurance-parity-report.md`, and `FHIR Terminology Service Parity — Implementation Plan.md`.
  - Usage docs open with a Table of Contents and an Overview / Configuration / User Experience / Examples structure.
- **Living ledgers:** `wiki/upstream-sync-version-16.md` is updated with `docs(wiki): …` commits as each upstream sync batch progresses. It records method, outcomes vocabulary (picked-clean, picked-with-conflict-resolution, already-present, skipped) and lint baselines.
- **Docs-required check:** `docs_checker.yml` fails `feat` PRs whose body lacks a wiki link (biograph.frappe.cloud / biograph.io `/wiki`) unless it says `no-docs` or `backport`. Note that the script queries `earthians/biograph`.
- **Code-level docs:** sparse. Rely on descriptive comments in `hooks.py` and docstrings only where non-obvious.
