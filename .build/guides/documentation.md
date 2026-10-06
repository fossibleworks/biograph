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
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **Public docs** live outside the repo. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`) and the Telegram community.
- **`wiki/`** holds the in-repo fork documentation as flat Markdown. Two naming styles are in use:
  - `DESIGN-<FEATURE>.md` / `<FEATURE>.md` for design notes, e.g. `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE.md`
  - `<FEATURE>-USAGE[-DOC].md` for user guides, e.g. `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`
  - Plans and reports, e.g. `FHIR Terminology Service Parity — Implementation Plan.md`, `insurance-parity-report.md`
  - Ledgers, e.g. `upstream-sync-version-16.md`. It records every upstream cherry-pick, its outcome (picked-clean / picked-with-conflict-resolution / already-present / skipped), and lint baselines. Changes to it are committed as `docs(wiki): ...`.
  - Images sit next to the docs (`patient-duplicatecheck-thumbnail.png`).
- **Docs gate (inherited upstream):** `docs_checker.yml` fails a `feat` PR unless the body links to a docs page (`/wiki` on an allowed host), or contains `no-docs` or `backport`.
- The PR template asks contributors to update the relevant docs and explain the change in detail.
- `AGENTS.md` and `CLAUDE.md` carry agent/process guidance. `.build/RULES.md` is the source for the generated rule copies.
