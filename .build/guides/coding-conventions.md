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
  - healthcare/healthcare/api/patient_portal.py
  - .git-blame-ignore-revs
---

**Python (ruff, configured in `pyproject.toml`)**
- Indent with **tabs** and use **double quotes**. Line length is 110, but E501 is ignored. Target is py310.
- Lint rule sets are F, E, W, I, UP, B and RUF, with a documented ignore list (F401, E402, B904, and others).
- isort section order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Separate each group with a blank line (see `api/patient_portal.py`).
- `frappe.types.DF` is a typing module (doctype type hints).
- Many legacy files are listed in the `.pre-commit-config.yaml` `exclude` list, so pre-commit does not run ruff on them. Don't reformat them wholesale. Keep diffs minimal, and for upstream-synced changes check ruff counts before and after.
- Naming: doctype folders and modules use snake_case of the DocType name. Controller classes use PascalCase (`class LabTest(Document)`). Test records use the `_Test …` prefix.
- User-facing strings are wrapped in `_()` for translation.
- Whitelisted API methods use `@frappe.whitelist()`. Prefer `frappe.qb` for joins.

**JavaScript**
- Prettier: tabs (`useTabs: true`, `tabWidth: 4`), `printWidth: 88`, `arrowParens: avoid`. `patient_portal/` and a few large doctype JS files are excluded.
- ESLint flat config (`eslint:recommended`) with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, …).
- Desk form scripts follow the `frappe.ui.form.on('<DocType>', {...})` pattern.

**Vue portal:** Vue 3 SFCs in `patient_portal/src/components` with PascalCase filenames (`BookAppointmentModel.vue`). The `@` alias points to `src`.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test, all lower-case.
