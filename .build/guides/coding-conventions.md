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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Python (ruff, configured in `pyproject.toml`)**
- **Tabs** for indentation, **double quotes**, and a line length of 110. E501 is ignored. Target is py310.
- Lint rule sets: `F, E, W, I, UP, B, RUF`, with Frappe-typical ignores (F401, F403/F405, E402, W191, B904, and others).
- isort section order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Each section is separated by a blank line, as in `test_patient_appointment.py`.
- Type hints use `frappe.types.DF` (`typing-modules`).
- Naming: modules and functions are `snake_case`. A doctype folder or file name is the snake_case of the DocType name (`patient_appointment/patient_appointment.py`), and the controller class is the PascalCase DocType name (`class PatientAppointment(Document)`). Custom exceptions subclass `frappe.ValidationError` (`OverlapError`, `MaximumCapacityError`).
- Client-callable functions are decorated with `@frappe.whitelist()`. Queries prefer `frappe.qb` or `frappe.db.get_all/get_value`. Raw `frappe.db.sql` still appears in 31 files, mostly older code and tests.
- All user-facing strings are wrapped in `_()` (`from frappe import _`).
- Business logic and validations belong on the **server side** (PR template).

**JavaScript**
- Prettier: tabs, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`. The `patient_portal/` directory is excluded from Prettier.
- ESLint flat config (`eslint:recommended`) with Frappe globals (`frappe`, `__`, `erpnext`, `$`, `jQuery`, ...).
- Desk scripts use `frappe.ui.form.on('<DocType>', {...})` and wrap strings in `__()`.
- The portal uses Vue 3 SFCs (`PascalCase.vue`, Composition API `ref/computed/watch`), frappe-ui components and Tailwind utility classes.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test, in lower case, with a non-empty subject. Scopes are used, for example `fix(tests):` and `docs(wiki):`.

**Security:** detect-secrets runs against `.secrets.baseline`, and Frappe semgrep rules run in CI.
