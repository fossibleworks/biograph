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
---

**Python** (ruff, configured in `pyproject.toml`):
- **Tabs** for indentation, **double quotes**, line length 110 (E501 is ignored).
- Lint set: `F, E, W, I, UP, B, RUF`, with some ignores (e.g. F401 unused imports and B904 are allowed).
- isort section order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Keep frappe, erpnext and healthcare imports in separate blocks.
- Type hints for doctype fields come from `frappe.types.DF`.
- Naming: snake_case modules and functions. Doctype controllers are `class PatientAppointment(Document)` in `patient_appointment.py`. Custom exceptions subclass `frappe.ValidationError` and are named `*Error`.
- Methods callable from the client use `@frappe.whitelist()`. Wrap all user-facing strings in `_()`.
- Each file starts with a copyright header comment (`# Copyright (c) ..., ... and Contributors` / `# See license.txt`).

**JavaScript (desk)**:
- Prettier settings: tabs (tabWidth 4), printWidth 88, `arrowParens: avoid`. ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, …).
- Form scripts use `frappe.ui.form.on('<DocType>', {...})`. Wrap user-facing strings in `__()`.

**Vue portal**: SFCs in `patient_portal/src/components/PascalCase.vue`, using frappe-ui components and `createResource`. Prettier skips `patient_portal/`.

**Legacy exclusions:** `.pre-commit-config.yaml` has a very long `exclude` list of existing upstream files, so pre-commit does not lint them. New files are linted. When you touch an excluded file, run ruff on it directly and **do not raise its existing finding count** (this is the method the sync ledger uses).
