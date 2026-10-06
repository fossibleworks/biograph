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
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - AGENTS.md
---

- **Public docs:** README links to DeepWiki (`deepwiki.com/Tacten/biograph`) and the community Telegram group. Upstream user docs live on the biograph wiki (`biograph.frappe.cloud/.../wiki`, `biograph.io/.../wiki`).
- **In-repo `wiki/`:** Markdown design docs, usage docs and ledgers, named in UPPER-KEBAB or descriptive titles. Examples: `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md` (design), `BLOCK-APPOINTMENT-BOOKING-USAGE.md` and `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md` (usage), `insurance-parity-report.md`, and `upstream-sync-version-16.md` (the per-batch sync ledger: one table row per upstream commit with its outcome and notes). Changes to those docs are committed as `docs(wiki): ...`.
- **PR docs gate:** the `Documentation Required` workflow (`.github/helper/documentation.py`) fails `feat` PRs unless the body links a docs URL on the biograph wiki, or contains `no-docs` or `backport`.
- **PR template:** asks for details, screenshots or GIFs, docs updates and `closes #XXXX`.
- **Code docs:** sparse. Comments explain non-obvious behaviour (see the `on_login` comment in `hooks.py`). Docstrings are uncommon.
- `AGENTS.md` and `CLAUDE.md` carry the Build-managed guides and rules (`.build/RULES.md`, `.build/guides/`). Edit the source files, never the rendered block.
