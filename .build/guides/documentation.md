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
  - .github/workflows/docs_checker.yml
  - .github/helper/documentation.py
  - context7.json
---

- **README.md** gives the overview, installation, development setup (pre-commit, semgrep) and a link to external docs (DeepWiki: `deepwiki.com/Tacten/biograph`). `context7.json` registers the repo with Context7.
- **`wiki/`** holds in-repo feature docs as UPPER-KEBAB-CASE Markdown:
  - **Design docs:** `DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md`, `PATIENT-DUPLICATE.md`, `insurance-parity-report.md`, the FHIR Terminology implementation plan.
  - **Usage guides:** `*-USAGE.md` / `*-USAGE-DOC.md`.
  - Usage guides use a table of contents, numbered sections, **bold** UI navigation paths ("Healthcare → Setup → Healthcare Settings"), and screenshots or video thumbnails stored next to them.
- **Feature PRs need docs:** the `Documentation Required` workflow (`.github/helper/documentation.py`) fails `feat` PRs whose body has no wiki link on an allowed docs host. Add `no-docs` to the PR body to opt out; `backport` PRs are exempt.
- The PR template asks contributors to update the relevant documentation.
