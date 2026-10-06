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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - AGENTS.md
---

- **End-user docs** are published externally. The README points to DeepWiki, and upstream docs live on the `biograph.frappe.cloud` / `biograph.io` wiki. The **Documentation Required** workflow fails any PR whose title starts with `feat` unless the body links to a `/wiki` page on those hosts, or says `no-docs` or `backport`.
- **In-repo docs** live in `wiki/` as UPPER-KEBAB-CASE markdown files:
  - `DESIGN-*.md` for design documents.
  - `*-USAGE*.md` for usage guides.
  - Parity and plan reports.
  - `upstream-sync-version-16.md`, the **upstream sync ledger**. Every cherry-picked upstream commit gets a table row with its sha, subject, outcome (`picked-clean`, `picked-with-conflict-resolution`, `already-present` or `skipped`) and notes. Commits that only update the ledger use `docs(wiki): ...`.
- **README** covers the introduction, installation (bench), docs link, community (Telegram), license and the dev setup for pre-commit and semgrep.
- **Code comments:** sparse. Doctype files carry a copyright header. Explanations of non-obvious fork-versus-upstream decisions go in the ledger, not in code comments.
- `AGENTS.md` and `CLAUDE.md` are managed by Build (the `BEGIN BUILD GUIDES` block). Edit the source files under `.build/` instead of the rendered block.
