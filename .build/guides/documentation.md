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
  - wiki/PATIENT-DUPLICATE.md
  - .github/helper/documentation.py
  - .github/workflows/docs_checker.yml
  - context7.json
---

# Documentation

- **User docs** live outside the repo. The README points to DeepWiki (`deepwiki.com/Tacten/biograph`), and `context7.json` registers the project with Context7.
- **Feature design and usage notes** go in the top-level `wiki/` folder as Markdown, one file per feature in UPPER-KEBAB-CASE: `DESIGN-<FEATURE>.md` for designs, `<FEATURE>-USAGE[-DOC].md` for usage, and parity or implementation reports. Images sit alongside them (e.g. `patient-duplicatecheck-thumbnail.png`). Design docs follow a *Problem statement → Proposed solution* structure.
- **PR docs gate**: `docs_checker.yml` runs `.github/helper/documentation.py`. Any PR whose title starts with `feat` must link a docs page (`biograph.frappe.cloud` or `biograph.io` with `/wiki` in the path) in the body, unless the body contains `no-docs` or `backport`.
- Code comments are sparse. Use docstrings or comments for non-obvious hook behaviour (see `on_login` comment in `hooks.py`).
- `healthcare/docs/current` is gitignored (generated).
