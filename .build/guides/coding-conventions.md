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
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
  - patient_portal/src/patient_portal.js
---

## Python (ruff, configured in `pyproject.toml`)

- **Tabs** for indentation. Double quotes. Line length 110 (E501 is ignored). Target py310.
- Lint rule sets: F, E, W, I, UP, B, RUF. Several rules are ignored, including F401 unused imports, E402 and B904.
- **Import order:** future, stdlib, third-party, `frappe`, `erpnext`, `healthcare`, first-party, local. Groups are separated by blank lines, as in `test_patient_appointment.py`.
- Use `frappe.types.DF` for typing.
- **Naming:** a DocType "Patient Appointment" lives at `doctype/patient_appointment/patient_appointment.py` with class `PatientAppointment(Document)`. Functions use snake_case. Methods called from JS or the portal get `@frappe.whitelist()`.
- Wrap user-facing strings in `_()`, as in `frappe.throw(_("...{0}").format(x))`.
- Prefer `frappe.qb` or `frappe.get_all`/`get_list(..., pluck=...)`. Raw `frappe.db.sql` is common in existing code, but semgrep frappe rules apply. Suppress a rule only with a justified `# nosemgrep`.
- **Legacy exclusion:** `.pre-commit-config.yaml` has a large `exclude:` list (about 640 lines) of existing files that are exempt from hooks. Do not add new files to it. Keep new code hook-clean.

## JavaScript (Desk)

- prettier: tabs, `tabWidth 4`, `printWidth 88`, `arrowParens: avoid`.
- eslint is `eslint:recommended` with Frappe globals (`frappe`, `__`, `$`, `moment`, `erpnext` …).
- Wrap UI strings in `__("...")`.

## Vue portal

- `patient_portal/` is excluded from prettier.
- Components are PascalCase `.vue` files in `src/components`.
- Use frappe-ui components (`Button`, `Dialog`, `Badge`, `Card`, `Tooltip`, `FeatherIcon`).
- Import paths use the `@` alias for `src`.
