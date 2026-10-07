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
  - commitlint.config.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
---

**Python**, enforced by ruff through pre-commit
- Indent with **tabs**. Use **double quotes**. Line length is 110, but E501 is ignored.
- Lint rules: `F, E, W, I, UP, B, RUF`, with the ignores listed in `pyproject.toml`.
- Import order (isort sections): stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Separate each block with a blank line, as in `api/patient_portal.py`.
- Use absolute dotted imports, for example `from healthcare.healthcare.doctype.x.x import y`.
- Naming:
  - DocType folders and modules are `snake_case` of the DocType name (`patient_appointment/patient_appointment.py`).
  - Controller classes are PascalCase `Document` subclasses (`class PatientAppointment(Document)`).
  - Custom exceptions end in `Error` and subclass `frappe.ValidationError`.
- Functions called from the client or the portal are decorated with `@frappe.whitelist()`.
- Wrap user-facing strings in `_()` and use `.format()` placeholders, for example `_("Invalid Code Value: {0}").format(v)`. Avoid f-strings inside `_()`.
- Prefer `frappe.qb`, `frappe.get_all` or `frappe.db.get_value` over raw SQL. If you use raw SQL, parameterize it. Semgrep enforces the Frappe rules.
- A large historical exclude list in `.pre-commit-config.yaml` keeps legacy files from being reformatted. Do not reformat files you are not otherwise changing.

**JavaScript**
- Prettier settings: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`.
- ESLint 10 flat config extends `eslint:recommended`, with Frappe globals declared (`frappe`, `__`, `$`, `moment`, `erpnext`, …).
- Desk form scripts use `frappe.ui.form.on('<DocType>', {...})`. Wrap user-facing strings in `__()`.
- Patient portal: Vue 3 SFCs in PascalCase (`BookAppointmentModel.vue`), Tailwind utility classes and frappe-ui components. The portal is excluded from prettier.

**Commits** follow conventional commits, lower-case type (`feat`, `fix`, `chore`, `docs`, `refactor`, `perf`, `test`, `ci`, `build`, `style`, `revert`), enforced by commitlint and the semantic-commits workflow.
