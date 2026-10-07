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
  - healthcare/healthcare/api/patient_portal.py
  - .git-blame-ignore-revs
---

**Python** (ruff, configured in `pyproject.toml`)
- Indent with **tabs** (`indent-style = "tab"`). Use **double quotes**. Line length is 110, though E501 is ignored.
- Lint rule sets: `F, E, W, I, UP, B, RUF`. Ignores include F401, E402, B904 and E741.
- **Import order** (isort sections): future, stdlib, third-party, `frappe`, `erpnext`, `healthcare`, first-party, local. Put a blank line between the frappe, erpnext and healthcare blocks, as in `patient_appointment.py`.
- Use absolute imports from `healthcare.healthcare.doctype.<x>.<x>`.
- Naming:
  - Classes are PascalCase and match the DocType name (`PatientAppointment(Document)`).
  - Functions and fields are snake_case.
  - Controller methods use the `validate_*` and `set_*` prefixes.
- Translate every user string with `from frappe import _` and `_("...")`, using `.format()` placeholders like `{0}`.
- Queries: prefer `frappe.qb` (query builder) or `frappe.get_list`/`frappe.db.get_value`. Raw `frappe.db.sql` still exists in legacy code and tests.
- Mark API endpoints with `@frappe.whitelist()`.

**JavaScript**
- Prettier settings: tabs, tab width 4, print width 88, `arrowParens: avoid`.
- ESLint 10 flat config uses `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, `__`, and others).
- Desk scripts use `frappe.ui.form.on(...)` and `__("...")` for translatable strings.
- The `patient_portal/` Vue code is excluded from prettier. Follow its existing two-space style.

**Legacy exclusions**
- `.pre-commit-config.yaml` has a top-level `exclude` list of about 600 legacy files. ruff and prettier therefore skip most existing doctype files.
- When you touch one of those files, do not reformat it wholesale. Make sure your change adds no new ruff findings; the upstream-sync ledger compares before and after counts.
- Bulk-reformat commits go in `.git-blame-ignore-revs`.
