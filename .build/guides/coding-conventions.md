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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
  - .pre-commit-config.yaml
---

**Python** (ruff, configured in `pyproject.toml`):
- **Indent with tabs.** Use double quotes and a line length of 110.
- Lint rule sets: F, E, W, I, UP, B, RUF. Many rules are ignored, e.g. E501, F401, B904.
- isort section order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Put a blank line between each group, as in `test_patient_appointment.py`.
- Naming:
  - Modules, functions, and fields: snake_case.
  - Controller classes: CamelCase named after the DocType (`PatientAppointment`).
  - Custom exceptions: `XxxError(frappe.ValidationError)`.
- Translate user-facing strings with `from frappe import _` and `_("...")`. Use `.format()` placeholders `{0}`; avoid f-strings inside `_()`.
- New queries should use the `frappe.qb` query builder (about 80 uses) or `frappe.db.get_value/get_all`. Raw `frappe.db.sql` still exists (about 91 uses), mostly in older code and tests.
- Public endpoints use `@frappe.whitelist()`.
- Frappe semgrep rules are enforced. Use `# nosemgrep` only with justification.

**JavaScript (Desk):**
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`.
- ESLint (`eslint:recommended`) with Frappe globals (`frappe`, `erpnext`, `__`, `$`).
- Wrap user-facing strings in `__("...")`.
- Form scripts use `frappe.ui.form.on('<DocType>', {...})`.

**Vue (patient_portal):**
- `<script setup>` style with frappe-ui components and `createResource`.
- Excluded from the repo-root prettier hook. It has its own `patient_portal/.prettierrc.json`.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style, and test. Types must be lower-case.
