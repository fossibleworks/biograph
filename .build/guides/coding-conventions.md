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
- Indent with **tabs**, use **double quotes**, line length 110, target py310.
- Lint rule sets: F, E, W, I, UP, B, RUF. Several are ignored: E501, F401, W191, B904 and others.
- Imports use isort with custom section order: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local, with a blank line between each group.
- Type hints come from `frappe.types.DF`.
- Use absolute module paths: `from healthcare.healthcare.doctype.<x>.<x> import ...`.
- Each DocType controller is `class PascalCaseName(Document)` in `<snake_name>.py`. Use the Frappe lifecycle methods (`validate`, `on_submit`, `on_cancel`, …).
- Methods exposed to the client are module-level functions decorated with `@frappe.whitelist()`.
- Prefer `frappe.qb` (query builder) and `frappe.get_all`/`get_list(..., pluck=...)` over raw SQL.
- Wrap every user-facing string in `_()`.

**JavaScript/Vue:**
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`.
- ESLint flat config extends `eslint:recommended`, with globals `frappe`, `erpnext`, `$`, `jQuery`, `__`, etc.
- Desk form scripts use `frappe.ui.form.on("DocType", {...})` and wrap strings in `__()`.
- The portal uses Vue SFCs with `createResource` from frappe-ui.

**Naming:**
- DocType names are Title Case with spaces ("Patient Appointment") and their folders are snake_case.
- Test fixtures use the `_Test` prefix.
