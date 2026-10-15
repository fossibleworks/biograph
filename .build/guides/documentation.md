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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/helper/documentation.py
  - AGENTS.md
---

# Documentation

- **README.md** covers installation (bench), development setup (pre-commit, semgrep) and links to external docs at DeepWiki.
- **`wiki/`** (repo root) holds feature design docs and usage guides in Markdown:
  - usage docs (`*-USAGE.md`, `*-USAGE-DOC.md`) with numbered sections, a table of contents, and **bold** UI navigation paths ("Healthcare → Setup → Healthcare Settings")
  - design docs (`DESIGN-*.md`)
  - implementation plans and parity reports
  
  Images sit beside the docs.
- **The PR docs gate** (`docs_checker.yml` with `.github/helper/documentation.py`) applies to PRs titled `feat...`. Their body must link to a docs page (a `/wiki` URL on an approved domain) or contain `no-docs`.
- The PR template asks you to "Update necessary Documentation" and follow ERPNext doc guidelines.
- `.build/` holds Build-managed guides. `AGENTS.md` renders their index, so edit the sources, not the rendered block.
