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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
---

**Python (ruff, configured in `pyproject.toml`):**
- **Tabs** for indentation (`indent-style = "tab"`), line length **110**, target `py310`.
- Lint rule sets: `F, E, W, I, UP, B, RUF`, with some B/E rules ignored.
- Imports are ordered by isort in custom sections: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Separate each group with a blank line.
- Wrap user-facing strings in `_()` (`from frappe import _`).
- Use snake_case modules and functions, and PascalCase controller classes named after the DocType (`class PatientAppointment(Document)`).
- Server methods called from JS are decorated `@frappe.whitelist()`.
- Older files open with a `# Copyright (c) ..., ESS LLP and Contributors` header.
- Many legacy files are listed in the top-level `exclude:` of `.pre-commit-config.yaml`, so they skip hooks. Don't reformat them wholesale. Keep diffs minimal so upstream cherry-picks stay clean.

**JavaScript and Vue (prettier plus eslint):**
- Tabs, `tabWidth: 4`, `printWidth: 88`, `arrowParens: "avoid"`.
- ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, ...).
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})`. Translatable strings use `__("...")`.
- Portal Vue components use PascalCase file names (`BookAppointmentModel.vue`).

**Naming:** a DocType folder and its files use the snake_case form of the DocType name, for example `patient_appointment/patient_appointment.{json,py,js}`.
