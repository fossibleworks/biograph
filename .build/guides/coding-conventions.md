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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .git-blame-ignore-revs
---

**Python (ruff, config in pyproject.toml):**
- **Tabs** for indentation, **double quotes**, line length 110 (E501 is ignored, so long lines are tolerated).
- Lint rules F, E, W, I, UP, B, RUF are enabled, with a long ignore list (F401 unused imports, E402, B904 and others).
- isort section order: stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party. Imports use the full dotted path, e.g. `from healthcare.healthcare.doctype.fee_validity.fee_validity import ...`.
- Doctype controllers subclass `frappe.model.document.Document` and are named in PascalCase after the doctype. Files and folders use snake_case of the doctype name.
- Wrap user-facing strings in `_()` (`from frappe import _`). Client-callable functions use `@frappe.whitelist()`.
- Put business logic and validations **on the server side** (PR template rule).
- Note: about 620 legacy files are listed in the pre-commit global `exclude`, so they are not linted. Do not reformat them wholesale. Reformat commits belong in `.git-blame-ignore-revs`.

**JavaScript (desk):** Prettier with tabs, tabWidth 4, printWidth 88 and `arrowParens: avoid`. ESLint uses `eslint:recommended` with the Frappe globals (`frappe`, `cur_frm`, `__`, `erpnext`, …). Translate UI strings with `__()`.

**Vue portal:** Composition API (`ref`, `computed`), `@/` alias to `patient_portal/src`, frappe-ui components and Tailwind classes. `patient_portal/` is excluded from Prettier.
