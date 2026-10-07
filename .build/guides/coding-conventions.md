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
  - healthcare/healthcare/doctype/fee_validity/fee_validity.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - .git-blame-ignore-revs
---

**Python** (Ruff, `pyproject.toml`)
- **Tabs** for indentation, double quotes, line length 110 (E501 ignored).
- Lint set: `F, E, W, I, UP, B, RUF`, with many Frappe-friendly ignores (F401, F403/F405, E402, B904, etc.).
- Import order uses isort sections: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local.
- Files start with a copyright/license header comment.
- DocType controllers are `class <PascalDocType>(Document)` in `<snake_doctype>.py`. Module-level helper functions are snake_case. Public RPCs use `@frappe.whitelist()`.
- Use `frappe.db.get_value`, `frappe.get_doc`, `frappe.get_all/get_list`, and `frappe.qb`. Raw `frappe.db.sql` appears in older code.
- Wrap all user-facing strings in `_()` (Python) and `__()` (JS).
- Do not use `print`/`breakpoint` (the `debug-statements` hook enforces this).

**JavaScript** (Prettier + ESLint)
- Tabs (width 4), printWidth 88, `arrowParens: avoid`, `eslint:recommended` with globals `frappe`, `erpnext`, `$`, `__`, and others.
- Form scripts follow `frappe.ui.form.on("<DocType>", { refresh(frm) {...} })`.
- A few large legacy form scripts and the `patient_portal/` sources are excluded from prettier.

**Vue (patient_portal):** SFC components in PascalCase (`BookAppointmentModel.vue`), the `@` alias for `src`, and Tailwind utility classes.

**Naming:** DocType folders and modules are snake_case versions of the DocType title (`patient_appointment` ↔ "Patient Appointment"). Patches go in `patches/v<major>_0/<descriptive_name>.py` and are registered in `patches.txt`.
