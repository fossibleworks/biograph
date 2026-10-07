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
  - .git-blame-ignore-revs
---

# Coding conventions

## Python (ruff, `pyproject.toml`)
- **Indent with tabs.** Use **double quotes**. Line length is 110, but E501 is ignored.
- Lint rule sets: `F,E,W,I,UP,B,RUF`. The ignore list matches Frappe's (F401 unused imports, E402, B904, etc.).
- Import order uses custom isort sections: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local.
- Naming follows Frappe:
  - Doctype folders and modules are snake_case (`patient_appointment/patient_appointment.py`).
  - Controller classes are CamelCase subclasses of `Document` (`class PatientAppointment(Document)`).
  - Lifecycle methods are `validate`, `on_submit`, `on_cancel`, etc.
  - Module-level helpers are snake_case. Client-callable functions are decorated with `@frappe.whitelist()`.
- Wrap user-facing strings in `_()`. Use `.format()` with `{0}` placeholders and `frappe.bold()` for emphasis.
- Type hints are being added in places (`fix: add type hints`). Typing uses `frappe.types.DF`.
- Database access mixes `frappe.db.*`, `frappe.get_all/get_list` and `frappe.qb`. Raw `frappe.db.sql` must be parameterised, which the Frappe semgrep rules check.

## JavaScript
- Prettier: tabs, `tabWidth 4`, `printWidth 88`, `arrowParens: avoid`.
- ESLint flat config extends `eslint:recommended` and declares Frappe desk globals (`frappe`, `cur_frm`, `__`, `$`, etc.).
- Desk form scripts use `frappe.ui.form.on('<DocType>', {...})` and translate strings with `__()`.
- The portal (Vue SFCs) is excluded from Prettier and keeps its existing 2-space style.

## Legacy exemptions
`.pre-commit-config.yaml` excludes about 620 legacy files (most existing doctype files, inherited from upstream) from all hooks. When you touch one of them:
- Do not introduce new lint findings.
- Do not mass-reformat it. That would wreck upstream-sync diffs.

`.git-blame-ignore-revs` lists formatting commits.
