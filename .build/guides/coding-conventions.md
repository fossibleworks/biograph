---
title: Coding conventions
category: coding-conventions
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - pyproject.toml
  - .prettierrc.yaml
  - eslint.config.mjs
  - .pre-commit-config.yaml
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Python (ruff, configured in `pyproject.toml`):**
- Indent with **tabs**, use **double quotes**, line length 110, target py310.
- Lint rule sets are F, E, W, I, UP, B and RUF. Many rules are ignored, including F401, E501 and B904.
- Import order: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local, with each group separated by a blank line (see the imports in `test_patient_appointment.py`).
- A long list of legacy files is excluded from pre-commit. Do not reformat untouched legacy files: the upstream-sync ledger tracks ruff counts per file and expects them not to grow.
- Naming:
  - Doctype folders and modules use snake_case of the doctype name (`patient_appointment/patient_appointment.py`), and the controller class is the PascalCase doctype name.
  - Exceptions subclass `frappe.ValidationError` and end in `Error`.
- Whitelisted API functions use the `@frappe.whitelist()` decorator.
- User-facing strings go through `_()`; JS uses `__()`.
- Database access goes through `frappe.db.get_value/get_all/exists`. Raw `frappe.db.sql` is mostly found in tests.

**JavaScript / Vue:**
- Prettier settings: tabs (`useTabs: true`, width 4), printWidth 88, `arrowParens: avoid`.
- ESLint uses a flat config extending `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `$`, `__`, …).
- `patient_portal/` is excluded from prettier. Vue SFCs there use tab indentation and Tailwind utility classes.

**Business logic** belongs on the server side, as the PR template says.
