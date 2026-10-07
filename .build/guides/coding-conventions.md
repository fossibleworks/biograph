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
  - patient_portal/src/PatientPortal.vue
---

**Python (ruff, configured in `pyproject.toml`):**
- Indent with **tabs**, use double quotes, and keep lines at 110 characters.
- Lint rule sets: F, E, W, I, UP, B, RUF. The ignores (F401, E501, B904, etc.) are listed in `pyproject.toml`.
- isort section order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Each section is separated by a blank line, as in the test files.
- Files carry a license header comment, e.g. `# Copyright (c) 2015, ESS LLP and Contributors` / `# See license.txt`.
- Doctype controllers are classes named after the DocType in PascalCase (`PatientAppointment`). Module-level functions are snake_case, and RPC entry points use `@frappe.whitelist()`.
- Use `frappe.db.get_value` / `set_single_value` / `get_list(pluck=...)` for data access. Raw `frappe.db.sql` with backtick `tab<Doctype>` names also appears.
- Wrap user-facing strings in `_()`, and fill placeholders with `.format()` *after* translation.

**JavaScript (Desk):**
- ESLint flat config extends `eslint:recommended`, with the Frappe globals (`frappe`, `erpnext`, `$`, `moment`, ...).
- Prettier settings: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`.
- Wrap strings in `__()`.
- Form scripts follow the `frappe.ui.form.on('<DocType>', {...})` pattern.

**Vue (patient portal):**
- Use `<script setup>`, `ref` / `computed`, and frappe-ui components.
- Import with the `@/components/...` alias. Component files are PascalCase (`BookAppointmentModel.vue`).
- Prettier does not run on `patient_portal/`.

**Pre-commit exclusions:** many legacy files are excluded from pre-commit (a long `exclude` list). Do not add new findings to them, and do not mass-reformat them.

**Commits:** Conventional Commits, enforced by commitlint. Types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style, and test, lower-case, with a required subject.
