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
  - healthcare/healthcare/api/patient_portal.py
---

**Python** (ruff 0.15.18, configured in `pyproject.toml`):
- **Tabs** for indentation, **double quotes**, line length 110. E501 is ignored, so long lines are tolerated.
- Lint rule sets: F, E, W, I, UP, B, RUF, with a documented ignore list (F401 unused imports, E402, B904 and others).
- isort section order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Separate each group with a blank line, as the test files do.
- DocType controllers are `class PatientAppointment(Document)` in `doctype/<snake>/<snake>.py`. Module-level functions are snake_case. Whitelisted APIs use `@frappe.whitelist()`.
- Prefer `frappe.qb` (query builder) or `frappe.get_all` / `get_list(..., pluck=...)` for queries. Raw `frappe.db.sql` appears in older code and tests.
- Wrap every user-facing string in `_()` (Python) or `__()` (JS). Use `.format()` placeholders inside `_()`, not f-strings.
- About 620 legacy files are listed in `.pre-commit-config.yaml`'s `exclude`, so pre-commit skips them. When you edit them, still match ruff style and don't add new findings (the upstream-sync ledger checks ruff counts before and after).

**JavaScript / Vue:**
- Prettier: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`. `patient_portal/` and a few large form scripts are excluded.
- ESLint flat config (`eslint:recommended`) with the globals `frappe`, `erpnext`, `$`, `jQuery`, `Vue`.
- Form scripts use `frappe.ui.form.on("<DocType>", {...})`. Vue SFCs are PascalCase (`BookAppointmentModel.vue`).

**Commits:** Conventional Commits, enforced by commitlint. Types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Use a lower-case type. Scopes are optional (`fix(tests): ...`, `docs(wiki): ...`).
