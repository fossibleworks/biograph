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
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - AGENTS.md
  - .github/instructions/build-rules.instructions.md
---

- **README.md** covers the product introduction, install steps (`bench get-app`, `install-app healthcare`) and developer setup (pre-commit, semgrep). Full user docs are external, on DeepWiki (`deepwiki.com/Tacten/biograph`).
- **`wiki/`** holds the in-repo design and usage docs as UPPER-KEBAB markdown: `DESIGN-*.md` for designs (for example block-based therapy booking), `*-USAGE*.md` for how-tos, implementation plans and parity reports, and the **upstream sync ledger** (`upstream-sync-version-16.md`). Recent commits update the ledger as `docs(wiki): …`.
- **PR docs gate:** `docs_checker.yml` runs `.github/helper/documentation.py`. Any PR titled `feat…` must link to a docs page whose path contains `/wiki` on `biograph.frappe.cloud` or `biograph.io`, unless the body contains `no-docs` or `backport`. Note that the helper queries `earthians/biograph`.
- `AGENTS.md`, `CLAUDE.md` and `.github/instructions/*` are generated or managed by Build from `.build/RULES.md`. Edit the source file, not the rendered copies.
