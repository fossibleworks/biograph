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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - commitlint.config.js
---

**Python** (ruff, configured in `pyproject.toml`):
- **Indent with tabs**, use double quotes, and keep lines to 110 characters (E501 is ignored, so long lines are tolerated). The target version is py310.
- Lint rules `F,E,W,I,UP,B,RUF` are enabled, with several Frappe-friendly ignores (F401, F403/F405, E402, B904…).
- **Import order:** stdlib, then third-party, then `frappe`, then `erpnext`, then `healthcare`, with a blank line between groups. The sections are enforced by isort config.
- Use absolute dotted imports, e.g. `from healthcare.healthcare.doctype.patient_appointment.patient_appointment import ...`.
- **Naming:** doctype directories and modules use snake_case of the DocType name (`patient_appointment/patient_appointment.py`). Controller classes use CamelCase of the DocType (`class PatientAppointment(Document)`). Exception classes end in `Error`.
- Translate every user-facing string with `_()` (from `frappe import _`) and use `.format()` placeholders: `_("Invalid Code Value: {0}").format(code_value)`. Never put `.format()` inside `_()`.
- Prefer `frappe.qb` or `frappe.db.get_value/get_all` over raw SQL in production code.
- Expose server methods with `@frappe.whitelist()`. Recent upstream work adds type hints to whitelisted method arguments.
- **Legacy:** a large set of older files is listed in the `.pre-commit-config.yaml` `exclude` block, so pre-commit skips them. Don't add new ruff findings to them. Measure before and after with `ruff check`, as the sync ledger does.

**JavaScript** (desk form scripts):
- Prettier uses tabs, tabWidth 4, printWidth 88 and `arrowParens: avoid`. ESLint runs `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `$`, `moment`…).
- Form scripts follow `frappe.ui.form.on("<DocType>", { refresh(frm) {...} })`. Translate strings with `__()`.
- `patient_portal/` (Vue) is excluded from prettier. Follow the existing 2-space style in that directory.

**Commits:** use conventional commits with a lower-case type from `build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test` and a non-empty subject (commitlint).
