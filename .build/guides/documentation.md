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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - AGENTS.md
---

- **README.md** covers the overview, installation through bench, development setup (pre-commit, semgrep) and links. Full user docs are external, on DeepWiki (`deepwiki.com/Tacten/biograph`).
- **`wiki/`** holds the fork's in-repo design and usage docs. They are Markdown files with UPPER-KEBAB or descriptive names:
  - design docs (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`)
  - usage guides (`*-USAGE.md`)
  - parity reports and plans
  - the upstream sync ledger (`upstream-sync-version-16.md`, which records each upstream commit's outcome)
  
  Add new feature designs and usage docs here, and update the sync ledger alongside sync work.
- **`docs_checker.yml`:** PRs whose title starts with `feat` must link a docs page (`biograph.frappe.cloud` or `biograph.io` with `/wiki` in the path). Otherwise the PR body must contain `no-docs`, or `backport` for backports.
- **AI and agent guides:** `CLAUDE.md`, `AGENTS.md`, `.build/RULES.md`, and mirrors in `.claude/rules/`, `.cursor/` and `.github/instructions/`. The block in AGENTS.md is managed by Build; edit `.build/` sources, not the mirrors.
- Inline docs are light: short comments, plus the commented template sections in `hooks.py`.
