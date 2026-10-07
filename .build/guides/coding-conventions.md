---
title: Coding Conventions
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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - patient_portal/src/components/DepartmentSelector.vue
---

**Python** (ruff, `pyproject.toml`)
- Indent with **tabs** (`indent-style = "tab"`). Use double quotes. Line length is 110 (E501 is ignored).
- Lint set: `F, E, W, I, UP, B, RUF`, with the ignores listed in pyproject (e.g. F401 unused imports, B904, E402).
- Imports are sorted into sections in this order: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local. Each section is separated by a blank line (see `test_patient_appointment.py`).
- `frappe.types.DF` is registered as a typing module.
- Naming:
  - Doctype folders and modules use snake_case of the DocType name (`patient_appointment/patient_appointment.py`).
  - Controller classes are PascalCase and extend `Document`.
  - Whitelisted functions are snake_case and decorated with `@frappe.whitelist()`.
- Wrap user-facing strings in `_()` from `frappe`.
- Use the Frappe ORM (`frappe.get_doc`, `frappe.db.get_value/get_all`, `frappe.get_list(..., pluck=...)`). Raw `frappe.db.sql` exists (~91 uses) but prefer the ORM for new code.
- Many files start with the header `# Copyright (c) <year>, <owner> and contributors` / `# See license.txt`.

**JavaScript** (Prettier + ESLint)
- Prettier: tabs, `tabWidth: 4`, `printWidth: 88`, `arrowParens: "avoid"`.
- ESLint uses the flat config with `eslint:recommended` and the globals `frappe`, `erpnext`, `$`, `jQuery`, `Vue`.
- Prettier skips `patient_portal/` and a few large form scripts.
- Desk form scripts follow the `frappe.ui.form.on("DocType", {...})` pattern.

**Vue (portal):** Single File Components named in PascalCase. Components end in `Model.vue` for dialogs (e.g. `BookAppointmentModel.vue`). Import from `frappe-ui` (`Button`, `Dialog`, `Card`). The `@` alias points to `patient_portal/src`.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Types must be lowercase.
