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
  - healthcare/healthcare/doctype/patient/patient.py
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - commitlint.config.js
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs** for indentation (`indent-style = "tab"`), **double quotes**, line length 110. E501 is ignored, so long lines are tolerated.
- Lint rule sets: `F, E, W, I, UP, B, RUF`. Several rules are ignored (F401 unused imports, B904, E402, ...), so do not "fix" those in unrelated code.
- Import groups, in order: stdlib, third-party, `frappe`, `erpnext`, `healthcare`. Each group is separated by a blank line (see `test_patient_appointment.py`).
- `typing-modules = ["frappe.types.DF"]`, used for Frappe's auto-generated type hints.
- Many legacy files are listed in `.pre-commit-config.yaml`'s `exclude`, about 600 lines of paths. pre-commit skips them, so check them with ruff directly and **do not add new ruff findings** (the sync ledger tracks before → after counts).
- File header: `# Copyright (c) <year>, <owner> and contributors` + `# For license information, please see license.txt`.

**Frappe naming**
- DocType folders and modules use `snake_case` of the DocType name (`patient_appointment/`). Controller classes use the PascalCase DocType name (`class PatientAppointment(Document)`).
- Server methods called from JS are decorated with `@frappe.whitelist()` and referenced by full dotted path.
- Database access: both `frappe.db.sql` (about 90 uses) and `frappe.qb` (about 80) appear. Prefer `frappe.get_all`/`frappe.qb` in new code. Backtick-quote `tab<DocType>` names in raw SQL.
- All user-facing strings are wrapped with `_()` in Python and `__()` in JS.

**JavaScript and Vue**
- Prettier: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: "avoid"`. Prettier skips `patient_portal/` and a few large form scripts.
- ESLint flat config extends `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `__`, `$`, ...).
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})` in `<doctype>.js`.
- Portal: Vue 3 SFCs in `patient_portal/src/components/` with PascalCase filenames (`BookAppointmentModel.vue`), frappe-ui components and Tailwind classes, and the `@` alias for `src`.

**Commits:** Conventional Commits, lower-case type from `build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test`, for example `fix(linters): ...` or `feat(appointment): ...`.
