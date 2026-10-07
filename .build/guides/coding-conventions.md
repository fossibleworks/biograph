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
  - commitlint.config.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/public/js/observation.js
---

**Python** (ruff, `pyproject.toml`)
- **Tabs for indentation**, double quotes, line length 110 (E501 is ignored, so long lines are tolerated). Formatted with `ruff format`.
- Lint rule sets: `F, E, W, I, UP, B, RUF`, with Frappe-friendly ignores (F401 unused imports, F403/F405 star imports, B904, E402, ...).
- Import order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Separate each group with a blank line.
- Type hints use `frappe.types.DF` for doctype fields.
- Naming: DocTypes are Title Case (`Patient Appointment`). Folders, modules and functions are snake_case (`patient_appointment.py`). Controller classes are PascalCase (`class PatientAppointment(Document)`). Custom exceptions end in `Error` and subclass `frappe.ValidationError`.
- Client-callable functions are decorated with `@frappe.whitelist()`.
- Wrap every user-facing string in `_()` (Python) or `__()` (JS) for translation.
- Test fixtures use the `_Test ` name prefix.

**JavaScript / Vue**
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. The `patient_portal/` folder is excluded from Prettier.
- ESLint flat config extends `eslint:recommended` with Frappe globals (`frappe`, `__`, `cur_frm`, `flt`, ...). `no-console` is a warning. Style rules such as semi, quotes and camelcase are off.
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})` in `<doctype>.js` next to the controller.
- Vue SPA: single-file components in PascalCase (`BookAppointmentModel.vue`). Import components from `frappe-ui`. The `@` alias points to `patient_portal/src`.

**Commits**: conventional commits, enforced by commitlint (`feat`, `fix`, `chore`, `docs`, `refactor`, `perf`, `test`, `style`, `ci`, `build`, `revert`; type in lower case).

Note: some existing code includes `print("DEBUG - ...")` statements (for example `patient_appointment.py`). Do not copy this pattern.
