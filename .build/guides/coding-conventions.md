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
  - .semgrepignore
  - commitlint.config.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/healthcare_settings/healthcare_settings.py
---

**Python (ruff, configured in `pyproject.toml`):**
- Indent with **tabs**. Use **double quotes**. Line length is 110, but E501 is ignored, so do not reflow existing code just to shorten lines. Target is py310.
- Lint rules are F, E, W, I, UP, B and RUF, with a long ignore list (F401, E402, B904, E741 and others).
- Import order uses custom isort sections: stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local, with a blank line between groups. Example: `import frappe` / `from frappe.utils import ...`, then `from erpnext...`, then `from healthcare...`.
- Many legacy files are excluded from pre-commit and semgrep (`.pre-commit-config.yaml` has a roughly 650-line exclude list, and `.semgrepignore` mirrors it). Do not mass-reformat excluded files. Keep diffs minimal so upstream cherry-picks stay clean.
- Use Frappe idioms. Write `frappe.get_doc`, `frappe.db.get_value`, `frappe.db.get_all` and `frappe.qb` rather than raw SQL where practical. Raw `frappe.db.sql` still appears in about 91 places, and `frappe.qb` in about 80. Wrap user-facing strings in `_()` and use `.format()` placeholders: `_("Invalid Code Value: {0}").format(code_value)`.
- Naming: DocTypes are Title Case ("Patient Appointment"). Folders and modules are snake_case (`patient_appointment/patient_appointment.py`). The controller class is the CamelCase DocType name. Methods and functions are snake_case and prefixed by intent (`validate_*`, `set_*`, `make_*`, `create_*`, `update_*`).
- Expose client-callable functions with `@frappe.whitelist()`.
- Files start with a copyright header comment: `# Copyright (c) <year>, <owner> and contributors` / `# For license information, please see license.txt`.

**JavaScript and Vue:**
- Prettier settings: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: "avoid"`. Prettier does not run on `patient_portal/`.
- ESLint uses flat config with `eslint:recommended` and declares Frappe globals (`frappe`, `erpnext`, `$`, `moment`, …).
- Desk form scripts use the `frappe.ui.form.on("<DocType>", {...})` pattern. Wrap UI strings with `__()`.
- The portal uses Vue SFCs with `<template>` and Tailwind utility classes, plus frappe-ui components (`Card`, …). The `@` alias maps to `patient_portal/src`.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test, all lower-case.
