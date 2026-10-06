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
---

**Python** (ruff, `pyproject.toml`)
- Indent with **tabs** and use **double quotes**. Line length is 110, and E501 is ignored. Target is py310.
- Lint rules: F, E, W, I, UP, B, RUF, with Frappe-style ignores (F401, E402, B904, etc.).
- Import order uses custom isort sections: future → stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local, with a blank line between each group.
- Naming: DocTypes are Title Case (`Patient Appointment`). Their folder, module and file names are snake_case (`patient_appointment/patient_appointment.py`). Controller classes are PascalCase (`class PatientAppointment(Document)`). Custom exceptions subclass `frappe.ValidationError` and end in `Error` (`OverlapError`, `MaximumCapacityError`).
- Wrap user-facing strings in `_()` and use positional `.format()` placeholders: `_("Patient {0} is not admitted in the service unit {1}").format(...)`.
- Mark API endpoints with `@frappe.whitelist()`. For new queries prefer `frappe.qb` (about 80 uses) over raw `frappe.db.sql` (about 91 legacy uses).
- Keep the copyright/license header seen in existing files (`# Copyright (c) ..., ESS LLP and Contributors / # See license.txt`).

**JavaScript** (Prettier and ESLint)
- Prettier settings: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. Prettier skips `patient_portal/`.
- ESLint uses `eslint:recommended` with Frappe Desk globals (`frappe`, `erpnext`, `$`, `moment`, ...).
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})` in `<doctype>.js`.

**Vue portal:** SFCs are PascalCase (`BookAppointmentModel.vue`), use frappe-ui components and Tailwind utility classes, and use the `@` alias for `src`.

**Fork hygiene:** the large per-file `exclude` list in `.pre-commit-config.yaml` holds legacy files that are not yet linted. Do not add new files to it.
