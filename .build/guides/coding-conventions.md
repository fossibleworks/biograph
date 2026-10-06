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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
---

**Python** (ruff, configured in `pyproject.toml`)
- **Indent with tabs** (`indent-style = "tab"`), use double quotes, and target py310. The line-length setting is 110, but E501 is ignored.
- Enabled lint rules: `F, E, W, I, UP, B, RUF`. Several are ignored, including F401 unused imports, E402, B904, and E741.
- **isort section order:** future, stdlib, third-party, `frappe`, `erpnext`, `healthcare`, first-party, local. Put a blank line between the frappe, erpnext, and healthcare groups.
- `typing-modules = ["frappe.types.DF"]`. Controllers carry auto-generated type hints.
- Use absolute imports from the package root (`from healthcare.healthcare.doctype.x.x import ...`).
- Wrap every user-facing string in `_()` (`from frappe import _`), e.g. `frappe.throw(_("..."))`.
- Prefer Frappe APIs (`frappe.get_doc`, `frappe.db.get_value`, `frappe.get_list(..., pluck="name")`, `frappe.qb`) over raw SQL, though `frappe.db.sql` still appears in older code.
- Names: snake_case for modules, folders, and functions; PascalCase for DocType controller classes (`class PatientAppointment(Document)`). Custom exceptions are `<Thing>Error(frappe.ValidationError)`.
- A large legacy exclude list in `.pre-commit-config.yaml` keeps many files out of pre-commit. New files are not excluded, so they must pass.

**JavaScript** (desk)
- Prettier: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`.
- ESLint flat config extends `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `__`, `$`, `moment`, ...).
- Form scripts use `frappe.ui.form.on("<DocType>", {...})`. Wrap user-visible strings in `__()`.
- `patient_portal/` is excluded from Prettier.

**Vue portal:** SFCs in `patient_portal/src/components` are PascalCase (`BookAppointmentModel.vue`). They use frappe-ui components and resources (`Card`, `ErrorMessage`, `getCachedResource`), the `@` alias for `src`, and Tailwind classes.

**Commits:** conventional commits. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style, and test, all lower-case. Scopes are common, e.g. `fix(tests):` and `docs(wiki):`.
