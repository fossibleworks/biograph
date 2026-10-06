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
  - .pre-commit-config.yaml
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
---

**Python** (ruff, `pyproject.toml`)
- **Tabs** for indentation, **double quotes**, line length 110 (E501 is ignored, so long lines are tolerated).
- Lint rule sets: `F, E, W, I, UP, B, RUF`. Several rules are explicitly ignored, including F401 unused imports, E402 and B904.
- Import order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Each group is separated by a blank line (see `test_patient_appointment.py`).
- Use absolute imports from `healthcare.healthcare...`.
- DocType controllers are `class PatientAppointment(Document)`: PascalCase from the DocType name. The file and folder names are the snake_case form of the DocType.
- Use `frappe.qb` (query builder) for new queries. Older code uses `frappe.db.sql`.
- Wrap every user-facing string with `_()` and use `.format()` placeholders: `_("Invalid Code Value: {0}").format(code_value)`.
- Mark server endpoints with `@frappe.whitelist()`.
- A large legacy file list in `.pre-commit-config.yaml` is excluded from linting. New files are linted, so do not add new files to that exclude list.

**JavaScript** (Prettier and ESLint)
- Tabs (width 4), printWidth 88, `arrowParens: avoid`. ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `__`, `$`).
- Desk scripts use `frappe.ui.form.on("<DocType>", {...})`. Wrap strings in `__()`.
- Portal code is Vue 3 SFCs in PascalCase (`BookAppointmentModel.vue`). Prettier skips `patient_portal/`.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Types are lowercase and an optional scope is allowed, e.g. `feat(appointment): ...`.
