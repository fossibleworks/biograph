---
title: Tech stack
category: tech-stack
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - pyproject.toml
  - package.json
  - patient_portal/package.json
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - yarn.lock
---

- **Backend:** Python >= 3.10 (ruff target `py310`; CI runs Python 3.14). Built as a **Frappe framework** app on **ERPNext** and `payments`, targeting the `version-16` branches. The package builds with `flit_core`. Runtime dependencies are minimal: `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), plus Redis through Frappe.
- **Desk UI:** plain Frappe form, list and calendar scripts in JavaScript (`<doctype>.js`, `<doctype>_list.js`, `<doctype>_calendar.js`), with Jinja/HTML templates. Bundled through `healthcare/public/js/healthcare.bundle.js`.
- **Patient Portal:** Vue 3, vue-router, **frappe-ui**, Tailwind CSS 3.4, built with Vite 4 (`patient_portal/`). The root `package.json` sets up yarn workspaces.
- **Tooling:** ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Frappe semgrep rules, detect-secrets, pip-audit, commitlint, semantic-release, Crowdin for translations.
- **Node:** v24 in CI.
