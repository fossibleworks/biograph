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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
---

- **README.md** covers the product intro, install via `bench get-app` / `install-app`, the pre-commit and semgrep setup, and community links. The full user docs live externally on DeepWiki.
- **`wiki/`** holds in-repo Markdown for feature design and usage. Files use UPPER-KEBAB names: `DESIGN-<FEATURE>.md` for design docs, `<FEATURE>-USAGE[-DOC].md` for user guides (e.g. `BLOCK-APPOINTMENT-BOOKING-USAGE.md`), and reports or plans such as `insurance-parity-report.md` and the FHIR terminology implementation plan. Images sit next to the docs.
  - `wiki/upstream-sync-version-16.md` is the **upstream sync ledger**. It records the method, conflict policy, and per-commit outcomes (picked-clean, picked-with-conflict-resolution, already-present, skipped). Update it with `docs(wiki): ...` commits whenever upstream sync batches land.
- **PR docs gate.** `docs_checker.yml` runs `.github/helper/documentation.py`. It fails `feat` PRs that lack a `/wiki` docs link on biograph.frappe.cloud or biograph.io in the body, unless the body says `no-docs` or `backport`. It currently queries the upstream `earthians/biograph` repo.
- Python docstrings are sparse. Hooks and complex logic get short explanatory comments (see the `on_login` comment in `hooks.py`).
