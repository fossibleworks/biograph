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
  - .git-blame-ignore-revs
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs** for indentation, **double quotes**, line length 110. E501 is ignored, but keep lines reasonable. Docstring code is formatted.
- Lint rule sets are `F, E, W, I, UP, B, RUF`. Notable ignores: F401 (unused imports), B904, E402, E741, W191.
- Import order is enforced via isort sections: stdlib → third-party → `frappe` → `erpnext` → `healthcare`, with a blank line between groups (see `test_patient_appointment.py`).
- Use absolute imports: `from healthcare.healthcare.doctype.<dt>.<dt> import ...`.
- Doctype controllers are classes named after the DocType in PascalCase (e.g. `PatientAppointment(Document)`) with Frappe lifecycle methods (`validate`, `on_submit`, `on_cancel`, `before_insert`). Functions and modules are snake_case.
- Wrap user-facing strings in `_()` (`from frappe import _`) with positional `{0}` placeholders.
- Prefer `frappe.qb` or the ORM (`frappe.get_list`, `frappe.db.get_value`) for queries. Raw `frappe.db.sql` is common in older code. Semgrep's Frappe rules flag unsafe usage, and `# nosemgrep` is used only where justified.
- Expose server methods to the client with `@frappe.whitelist()`.

**JavaScript/Vue** (ESLint `eslint:recommended` flat config + Prettier)
- Prettier settings: tabs (`useTabs: true`, tabWidth 4), printWidth 88, `arrowParens: avoid`.
- Frappe globals (`frappe`, `__`, `cur_frm`, `$`, `moment`, …) are declared in `eslint.config.mjs`.
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})` and wrap strings in `__()`.
- The Patient Portal uses Vue SFCs with PascalCase component files (`BookAppointmentModel.vue`), Tailwind utility classes and frappe-ui components. `patient_portal/` is excluded from Prettier.

**Legacy exclusions:** many legacy files are listed in the pre-commit/semgrep exclude list. Don't remove them from the list without reformatting them in a dedicated `style:` commit, and add mass-reformat commits to `.git-blame-ignore-revs`.
