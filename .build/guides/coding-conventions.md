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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
  - .git-blame-ignore-revs
---

**Python** (ruff, `pyproject.toml`)
- Indent with **tabs**, use double quotes, line length 110 (E501 is ignored), and target py310.
- Enabled lint rules: F, E, W, I, UP, B and RUF. Frappe-friendly ignores include F401, F403/F405, E402 and B904.
- Import order is enforced by isort sections: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local. Put a blank line between the frappe, erpnext and healthcare groups.
- Import with absolute dotted paths, for example `from healthcare.healthcare.doctype.patient_appointment.patient_appointment import create_appointment`.
- Doctype folders and modules use snake_case (`fee_validity/fee_validity.py`). Controller classes are CamelCase subclasses of `Document`. DocType names are Title Case with spaces ("Patient Appointment").
- Wrap user-facing strings in `_()` and format with `.format()`: `_("Invalid Code Value: {0}").format(code_value)`.
- Prefer `frappe.qb` (query builder) and `frappe.db.get_value`/`exists` over raw SQL. Raw `frappe.db.sql` mostly appears in tests.
- Expose client-callable functions with `@frappe.whitelist()` (182 call sites).
- Files start with a copyright header, for example `# Copyright (c) 2015, ESS LLP and Contributors`.

**JavaScript and Vue** (Prettier and ESLint)
- Prettier settings: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`.
- ESLint uses the flat config extending `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `__`, `$`, `moment`, and others).
- Desk scripts use `frappe.ui.form.on(...)` and wrap strings in `__()`.
- Vue uses `<script setup>`, the `@/` alias for `src`, and frappe-ui components (`Button`, `Dialog`, `Tabs`, `createResource`).

**Commits:** follow Conventional Commits, enforced by commitlint. The allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test, in lower case.
