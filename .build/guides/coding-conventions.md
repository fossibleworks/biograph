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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient/patient.js
  - .pre-commit-config.yaml
---

**Python (ruff, see `pyproject.toml`):**
- Indent with **tabs**, use **double quotes**, and keep lines to about 110 characters (E501 is ignored).
- Lint rule sets: F, E, W, I, UP, B, RUF. Some rules are deliberately ignored, for example F401 unused imports and B904.
- Import order: future, stdlib, third-party, `frappe`, `erpnext`, `healthcare`, local. Put a blank line between each section, as in `api/patient_portal.py`.
- Translatable strings use `from frappe import _`, written as `_('...').format(...)`. Bold values in messages with `frappe.bold`.
- Type stubs use `frappe.types.DF`.
- DocType controllers are classes named after the DocType (for example `PatientAppointment(Document)`) in `doctype/<snake_name>/<snake_name>.py`. Modules and folders use snake_case and DocType names use Title Case.
- Expose an API with `@frappe.whitelist()` on module-level functions (about 180 in the codebase). Use `frappe.qb` for complex queries.
- File header: `# Copyright (c) <year>, <owner> and contributors` / `# See license.txt`.

**JS/Vue:**
- Prettier: tabs, `tabWidth 4`, `printWidth 88`, `arrowParens: avoid`. ESLint uses a flat config (`eslint.config.mjs`).
- Desk scripts use `frappe.ui.form.on(...)` and wrap strings in `__()`.
- Portal components are PascalCase `.vue` files in `patient_portal/src/components`, and the import alias `@` maps to `patient_portal/src`.

**Commits:** use Conventional Commits, enforced by commitlint. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test. Types are lower-case. A scope is optional, for example `fix: ...` or `docs(wiki): ...`.

The pre-commit `exclude` list covers many legacy files. Do not add new files to it.
