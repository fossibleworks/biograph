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
  - healthcare/healthcare/api/patient_portal.py
---

**Python (Ruff, configured in `pyproject.toml`):**
- Indent with **tabs**, use **double quotes**, line length 110 (E501 itself is ignored). Target py310, and pyupgrade (`UP`) is on.
- Lint sets enabled: `F, E, W, I, UP, B, RUF`. Several are ignored, including F401 unused imports, E402 and B904.
- Imports are ordered by isort in custom sections: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Leave a blank line between each group, as in `patient_appointment.py`.
- Use absolute dotted imports (`from healthcare.healthcare.doctype.fee_validity.fee_validity import ...`).
- Names are snake_case for functions and modules, and CamelCase for DocType controller classes (`class PatientAppointment(Document)`). DocType folders and files are the snake_case DocType name.
- Whitelisted functions use `@frappe.whitelist()`, and there are about 180 of them. Prefer `frappe.qb` for new queries; about 90 legacy `frappe.db.sql` calls still exist.
- Wrap every user-facing string in `_()`, and use `.format()` for placeholders: `_("Invalid Code Value: {0}").format(code_value)`.
- Typing modules: `frappe.types.DF` (DocType type hints).
- A large legacy file list is excluded from pre-commit (about 620 paths in `.pre-commit-config.yaml`). New files are not excluded and must pass.

**JavaScript (Desk):**
- ESLint `eslint:recommended` (flat config) declares Frappe globals (`frappe`, `erpnext`, `$`, `moment`, …).
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. `patient_portal/` and a few large doctype JS files are excluded from prettier.
- Form scripts use `frappe.ui.form.on('<DocType>', {...})` and `frappe.call`. Wrap strings in `__()`.

**Vue (portal):** use `<script setup>`-style components in `patient_portal/src/components/*.vue` (PascalCase file names), frappe-ui components and `createResource`, and Tailwind utility classes.

**Commits:** follow Conventional Commits with lowercase types (see the workflow guide).
