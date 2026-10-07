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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - .pre-commit-config.yaml
---

**Python (ruff, `pyproject.toml`):**
- Indent with **tabs**, use double quotes, line length 110 (E501 is ignored).
- Lint rule sets: F, E, W, I, UP, B, RUF, with Frappe-style ignores (F401 unused imports, E402, W191, B904, …).
- Import order is enforced with custom isort sections: stdlib → third-party → `frappe` → `erpnext` → `healthcare` → local. Use absolute imports such as `from healthcare.healthcare.doctype.x.x import ...`.
- Doctype controllers are `class PatientAppointment(Document)` with Frappe lifecycle hooks (`validate`, `before_save`, `on_update`, `after_insert`, `on_submit`). Helpers are named `validate_*`, `set_*`, `make_*`.
- Methods callable from the client or portal use `@frappe.whitelist()`.
- Wrap every user-facing string in `_()`. Use `.format()` placeholders (`_("... {0}").format(...)`), not f-strings inside `_()`.
- Many legacy files are listed in `.pre-commit-config.yaml`'s exclude list. Do not reformat them wholesale. Keep lint counts on touched files from going up (see the ruff baseline in `wiki/upstream-sync-version-16.md`).

**JavaScript:**
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`.
- ESLint flat config extends `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `__`, `$`, `moment`).
- Form scripts use `frappe.ui.form.on("<DocType>", {...})`. Wrap UI strings in `__()`.
- The `patient_portal/` folder is excluded from prettier.

**Vue portal:** Use SFCs in `src/components/` (PascalCase file names), the `@` alias to `src`, and frappe-ui `createResource` for API calls.

**Naming:** Folders are snake_case doctypes (e.g. `patient_appointment`). Doctype labels are Title Case ("Patient Appointment"). Test records use the `_Test ...` prefix.
