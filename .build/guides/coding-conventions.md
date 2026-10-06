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
---

**Python (ruff, `pyproject.toml`):**
- Indent with **tabs**, use **double quotes**, line length 110. `ruff format` runs with `docstring-code-format`.
- Lint selects F, E, W, I, UP, B and RUF. Many rules are ignored, including E501, F401 and B904.
- Import order uses custom isort sections: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. A blank line separates each group. See `patient_appointment.py`.
- Wrap user-facing strings in `_()` (`from frappe import _`). Use `.format()` placeholders like `_("... {0}").format(x)`, not f-strings inside `_()`.
- Prefer `frappe.qb` / `frappe.db.get_value` / `frappe.get_list` over raw SQL in new code. Raw `frappe.db.sql` still exists in older code and tests.
- Naming:
  - DocTypes are Title Case (`Patient Appointment`).
  - Folders and modules are snake_case (`patient_appointment/patient_appointment.py`).
  - Controller classes are PascalCase and match the DocType.
  - Functions are snake_case. Client-callable ones are decorated with `@frappe.whitelist()`.
- Older files keep their copyright header (`# Copyright (c) 20xx, ... and contributors`).

**JavaScript (desk):**
- Prettier settings: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`.
- ESLint uses the flat config with `eslint:recommended` and Frappe globals (`frappe`, `erpnext`, `__`, `$`, ...).
- Form scripts use `frappe.ui.form.on("<DocType>", {...})`. Translate strings with `__()`.

**Vue portal:** Prettier excludes `patient_portal/`. It uses Vue 3 SFCs with frappe-ui components and Tailwind utility classes, and PascalCase component files (`BookAppointmentModel.vue`).

**Pre-commit exclusions:** a large exclude list (about 640 legacy paths) shields old files from the hooks. Do not add new files to it. New code must pass the hooks.

**Commits:** Conventional Commits, enforced by commitlint. Lower-case type, one of build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. An optional scope is allowed (`fix(tests): ...`).
