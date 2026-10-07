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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - AGENTS.md
---

- **User docs** are external: the README links DeepWiki (`deepwiki.com/Tacten/biograph`). The upstream `docs_checker.yml` workflow fails `feat:` PRs that don't link to a `/wiki` page on `biograph.frappe.cloud` / `biograph.io`. Opt out with `no-docs` in the PR body. Backports skip the check.
- **In-repo `wiki/`** holds Markdown design and usage docs with SCREAMING-KEBAB names (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`) plus reports and ledgers (`insurance-parity-report.md`, `upstream-sync-version-16.md`). Usage docs follow this structure: a table of contents, then Overview, Configuration (UI navigation in **bold** like **Healthcare → Setup → Healthcare Settings**), User Experience, Examples.
- **Ledgers:** long multi-batch work such as the upstream sync keeps a running Markdown table (upstream sha, subject, outcome, notes) and is committed as `docs(wiki): ...`.
- **Agent guides:** `AGENTS.md` renders guides from `.build/guides/` and `.build/RULES.md`. Edit the sources, not the managed block.
- **Docstrings:** sparse. Add one where intent isn't obvious.
