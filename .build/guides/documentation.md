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
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **The user-facing docs live outside the repo.** The README links to DeepWiki (`deepwiki.com/Tacten/biograph`).
- **The in-repo `wiki/` directory** holds markdown for fork features:
  - design docs (`DESIGN-*.md`)
  - usage guides (`*-USAGE*.md`)
  - parity reports and implementation plans
  - the **upstream sync ledger** (`upstream-sync-version-16.md`)
- Screenshots go next to the markdown (for example `patient-duplicatecheck-thumbnail.png`).
- Docs commits use the `docs(wiki): ...` conventional-commit scope.
- **`feat` PRs are checked for docs.** The `docs_checker` workflow fails a `feat` PR unless its body links to a `/wiki` page on the configured docs hosts, or says `no-docs` or `backport`.
- The PR template asks contributors to update the relevant documentation.
- `patient_portal/README.md` covers the portal frontend.
