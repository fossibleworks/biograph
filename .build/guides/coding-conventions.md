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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
---

**Python** (ruff, `pyproject.toml`):
- Indent with **tabs**, use **double quotes**, and keep lines to 110 characters (E501 is ignored). Target is py310.
- Lint selects `F,E,W,I,UP,B,RUF`, with a documented ignore list (F401 unused imports, E402, B904 and others).
- isort section order: future, stdlib, third-party, **frappe, erpnext, healthcare**, first-party, local. Separate the frappe, erpnext and healthcare import groups with blank lines.
- `typing-modules = ["frappe.types.DF"]`.
- Naming follows Frappe: doctype folders and modules are `snake_case` versions of the DocType name (`patient_appointment/patient_appointment.py`). The controller class is the CamelCase doctype name. Custom exceptions end in `Error` and subclass `frappe.ValidationError`.
- Wrap user-facing strings in `_()`. Use Frappe APIs (`frappe.get_doc`, `frappe.db.get_value`, `frappe.qb`, `frappe.get_list(..., pluck="name")`) instead of raw SQL where practical.
- Expose client-callable functions with `@frappe.whitelist()`.
- A long list of legacy files is excluded from pre-commit. Do not mass-reformat them, because that churns upstream merges.

**JavaScript** (prettier and ESLint flat config):
- **Tabs**, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`.
- `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `__`, `$`, ...).
- Wrap translatable strings in `__()`.
- `patient_portal/` is excluded from prettier and keeps its own Vue SFC style (`<script setup>`-style imports from `frappe-ui`, Tailwind classes).

**Commits:** follow Conventional Commits. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test, all lower-case. Upstream sync picks use `git cherry-pick -x`.
