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
  - healthcare/healthcare/doctype/fee_validity/fee_validity.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - .pre-commit-config.yaml
---

**Python** (ruff config is in `pyproject.toml`)
- Indent with **tabs** and use double quotes. Line length is 110; E501 is ignored.
- Lint rule sets: F, E, W, I, UP, B, RUF. Many are ignored for legacy reasons, including F401, B904 and E402.
- isort section order: stdlib, third-party, **frappe**, **erpnext**, **healthcare**, then first-party and local, with blank lines between groups. Examples: `import frappe` / `from frappe.utils import ...`, then `from erpnext...`, then `from healthcare...`.
- DocType controllers:
  - Class name in PascalCase, matching the DocType name (`class FeeValidity(Document)`).
  - Files and folders in snake_case, matching the doctype.
  - Use lifecycle hooks: `validate`, `on_submit`, `on_cancel`, and so on.
  - Module-level helper functions use snake_case.
- Server methods called from JS take `@frappe.whitelist()`. The codebase has about 180.
- Prefer `frappe.get_cached_value`, `frappe.db.get_value` and `frappe.qb` over raw SQL. `frappe.db.sql` still appears in about 90 places; when you use it, always use parameterized queries.
- Wrap every user-facing string in `_()`.
- Files start with a copyright/license header (`# Copyright (c) <year>, ... and contributors`).
- Many legacy files are listed in the giant `exclude` block of `.pre-commit-config.yaml`, so ruff does not run on them in pre-commit. Do not add new files to that list, and do not reformat whole excluded files in unrelated PRs.

**JavaScript (desk)**
- Prettier: tabs, width 4, printWidth 88, `arrowParens: avoid`.
- ESLint uses the recommended rules, with Frappe globals (`frappe`, `erpnext`, `__`, `$`).
- Form scripts use `frappe.ui.form.on('<DocType>', { setup, onload, refresh, <fieldname>(frm) {...} })`.
- Server calls go through `frappe.call` / `frm.call`. Wrap UI strings in `__()`.

**Vue (portal)**
- Uses SFCs in `patient_portal/src/components` with PascalCase names (`BookAppointmentModel.vue`).
- Imports use the `@/` alias.
- Use frappe-ui components and Tailwind classes. Prettier skips this folder.

**Commits**
- Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Types are lower-case.
- Fork work often adds a scope or a suffix, for example `fix: ... (upstream sync B2)`.
