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
---

- End-user and product documentation lives on **DeepWiki** (linked from the README).
- In-repo design notes, usage guides and parity reports live in `wiki/` as Markdown. Long-form docs use UPPER-KEBAB names (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`). Ledgers and reports use lower-kebab names (`upstream-sync-version-16.md`, `insurance-parity-report.md`).
- Upstream sync work must be recorded batch by batch in `wiki/upstream-sync-version-16.md`, with an outcome per commit: picked-clean, picked-with-conflict-resolution, already-present, skipped or deferred.
- The `Documentation Required` workflow (`.github/helper/documentation.py`) fails `feat` PRs unless the body links a `/wiki` page on biograph.frappe.cloud or biograph.io, or contains `no-docs`.
- `patient_portal/README.md` documents the frontend.
- Docs commits use the `docs(wiki):` scope.
