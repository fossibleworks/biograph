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
  - eslint.config.mjs
  - .prettierrc.yaml
  - .pre-commit-config.yaml
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - commitlint.config.js
---

**Python** (ruff, `pyproject.toml`)
- Indent with **tabs**, use **double quotes**, and keep lines to 110 characters (E501 is ignored, so long lines are tolerated). Target py310.
- Lint rule sets F, E, W, I, UP, B, RUF, with a Frappe-friendly ignore list (F401, E402, B904, and others).
- Imports are sorted into sections in this order: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, local. Use full dotted absolute imports such as `from healthcare.healthcare.doctype.x.x import ...`.
- Use Frappe idioms:
  - Wrap user-facing strings in `_()`.
  - Expose client-callable functions with `@frappe.whitelist()` (about 180 uses).
  - Query with `frappe.get_all`/`get_list` (`pluck=`), `frappe.db.get_value`/`set_value`, `frappe.qb`.
  - Use `frappe.utils` helpers (`getdate`, `flt`, `nowdate`, `add_days`).
- Doctype controllers are classes named after the DocType in PascalCase (`PatientAppointment(Document)`). Files and folders use snake_case versions of the DocType name. Use `frappe.types.DF` typing for auto-generated type hints.
- Patches go in `healthcare/patches/vNN_0/<verb_description>.py` and define `execute()`.

**JavaScript** (ESLint flat config `eslint.config.mjs` with eslint:recommended, plus Prettier for js/ts/vue/css)
- Desk scripts use `frappe.ui.form.on("DocType", {...})`. The globals `frappe`, `erpnext`, `$` and `moment` are allowed.
- Wrap user-facing strings in `__()`.
- Prettier excludes `patient_portal/` and a few large legacy form scripts.

**Vue (patient_portal)**
- SFCs use PascalCase filenames (`BookAppointmentModel.vue`), frappe-ui components, and Tailwind utility classes. Use the `@/` alias for `src/`.

**Commits:** Conventional Commits (`feat:`, `fix(tests):`, `docs(wiki):`, `chore:`, `refactor:`), enforced by commitlint.
