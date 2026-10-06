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
  - patient_portal/src/components/PractitionerSelector.vue
---

**Python (ruff, configured in `pyproject.toml`)**
- Indent with **tabs**, use **double quotes**, line length 110. E501 is ignored, so long lines are tolerated. Target version is py310.
- Lint selection is `F, E, W, I, UP, B, RUF`. The many ignores (for example F401 unused imports and B904) match Frappe/ERPNext conventions.
- isort sections go in this order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Separate the groups with blank lines, as in `test_patient_appointment.py`.
- `typing-modules = ["frappe.types.DF"]`, so DocType controllers may carry auto-generated type annotations.
- Naming: DocType names are Title Case ("Patient Appointment"), their folders and modules are snake_case, and controller classes are PascalCase (`PatientAppointment(Document)`). Server functions are snake_case. Use absolute imports such as `from healthcare.healthcare.utils import ...`.
- Wrap user-facing strings in `_()` from `frappe`.
- Prefer `frappe.qb`, `frappe.get_all` and `frappe.db.get_value` over raw SQL. Raw SQL exists in older code and tests.

**JavaScript and Vue**
- Prettier settings: tabs (width 4), print width 88, `arrowParens: avoid`. ESLint uses `eslint:recommended` with the Frappe globals (`frappe`, `erpnext`, `__`, `$`, …).
- Wrap desk strings in `__()`.
- Vue components are PascalCase `.vue` files in `patient_portal/src/components`. Use `<script setup>`, Tailwind utility classes and frappe-ui components.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test, written in lower case.
