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
  - AGENTS.md
---

- **README.md**: product intro, install (`bench get-app` / `install-app`), developer setup (pre-commit, semgrep). It links to Deep-Wiki (`deepwiki.com/Tacten/biograph`) for full docs and to the Telegram group.
- **`wiki/`** holds in-repo design and usage docs for fork features. File names are UPPER-KEBAB, e.g. `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`. There are also reports and ledgers (`insurance-parity-report.md`, `upstream-sync-version-16.md`). The usual pattern is a *DESIGN* doc plus a *USAGE* doc per feature.
- **Upstream-sync ledger** (`wiki/upstream-sync-version-16.md`): each cherry-picked upstream commit gets a table row (sha, subject, outcome, notes). Outcomes use a fixed vocabulary: picked-clean, picked-with-conflict-resolution, already-present, skipped. Commits that only update the ledger use `docs(wiki): …`.
- **PR docs gate** (`docs_checker.yml`): a PR titled `feat…` must link docs on `biograph.frappe.cloud`/`biograph.io` under `/wiki`, unless the body contains `no-docs` or `backport`. Note that the helper queries the **earthians/biograph** API, so on this fork it may not resolve PRs correctly.
- Agent/tool guide indexes are managed by Build: `AGENTS.md` and `.build/RULES.md`, mirrored into `.claude/rules`, `.cursor/rules` and `.github/instructions`. Edit the source file in `.build/`, not the mirrors.
