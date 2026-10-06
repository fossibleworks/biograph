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
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - patient_portal/README.md
---

- **Public docs** are hosted externally. The README links to DeepWiki (`deepwiki.com/Tacten/biograph`). The upstream docs checker looks for links to `biograph.frappe.cloud` or `biograph.io` `/wiki` pages.
- **The in-repo `wiki/` directory** holds fork design docs and records. Files use descriptive names, mostly UPPER-KEBAB-CASE `.md`:
  - design docs (`DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `FHIR Terminology Service Parity — Implementation Plan.md`)
  - usage docs (`BLOCK-APPOINTMENT-BOOKING-USAGE.md`, `PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`)
  - parity reports (`insurance-parity-report.md`)
  - the **upstream sync ledger** (`upstream-sync-version-16.md`), which is updated in `docs(wiki): ...` commits for each sync batch. It records each upstream commit's outcome: picked-clean, picked-with-conflict-resolution, already-present, skipped or deferred.
- **`docs_checker.yml`** requires every PR whose title starts with `feat` to include a docs link in the body, unless the body contains `no-docs` or `backport`.
- The PR template asks for a details section, screenshots or GIFs, an updated docs section, and `closes #XXXX`.
- `patient_portal/README.md` covers the portal sub-project.
- Commits that touch only docs use the `docs:` or `docs(wiki):` type.
