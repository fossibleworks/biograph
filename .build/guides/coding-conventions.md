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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
  - commitlint.config.js
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs** for indentation, **double quotes**, line length 110. Formatting is `ruff format`.
- Enabled lint rules: `F, E, W, I, UP, B, RUF`. Several rules are ignored on purpose, including F401 unused imports, E501, B904 and W191.
- **Import order** uses custom isort sections in this order: stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local. Put a blank line between groups. Example:
  ```python
  import datetime

  import frappe
  from frappe import _

  from erpnext...

  from healthcare.healthcare.utils import ...
  ```
- Use absolute dotted imports from `healthcare.healthcare.doctype.<name>.<name>`.
- `typing-modules = ["frappe.types.DF"]`, so DocType controllers may carry auto-generated type annotations.
- Naming follows Frappe norms:
  - DocType names are Title Case with spaces ("Patient Appointment"), and folders and modules use snake_case (`patient_appointment`).
  - Controller classes are PascalCase subclasses of `Document`.
  - Functions are snake_case.
  - Endpoints are marked with `@frappe.whitelist()`.
- Wrap every user-facing string in `_()`, with `.format()` placeholders like `{0}`.
- For new queries, prefer `frappe.qb` (query builder) and `frappe.db.get_value/get_list` over raw `frappe.db.sql`. Raw SQL still appears in older code.
- `.pre-commit-config.yaml` lists many legacy files that are excluded from linting. Do not add new paths to that list. Upstream-sync work tracks before/after ruff counts so that no new findings are introduced.

**JavaScript / Vue**
- Prettier: tabs (`useTabs: true`, `tabWidth: 4`), `printWidth: 88`, `arrowParens: avoid`.
- ESLint 10 flat config extends `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `$`, `__`, …).
- Desk form scripts use `frappe.ui.form.on("DocType", {...})`. Wrap user strings in `__()`.
- The Vue portal uses SFCs in `patient_portal/src/components/` with PascalCase file names. Use frappe-ui components and Tailwind utility classes.

**Commits** follow Conventional Commits, enforced by commitlint. Allowed types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, lower-case, and the subject must not be empty.
