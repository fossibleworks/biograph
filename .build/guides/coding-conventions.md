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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/public/js/sales_invoice.js
  - commitlint.config.js
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs** for indentation, **double quotes**, line length 110 (E501 is ignored, so this is a soft limit). Docstring code is formatted.
- Lint rules: F, E, W, I, UP, B, RUF, with Frappe-friendly ignores (F401 unused imports, F403/F405 star imports, B904, E402, W191, and others).
- **Import order** (isort): future → stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local. Separate each group with a blank line, as `test_patient_appointment.py` does.
- Type hints use `frappe.types.DF` (`typing-modules`).
- Naming follows Frappe: snake_case doctype folders and modules (`patient_appointment/patient_appointment.py`), `class PatientAppointment(Document)`, DocType names in Title Case with spaces (`"Patient Appointment"`). Server endpoints are module-level functions marked `@frappe.whitelist()`.
- Wrap all user-facing strings in `_()` and use `.format()` placeholders: `_("Invalid Code Value: {0}").format(code_value)`.
- Put business logic and validation **on the server** (PR template rule).
- `.pre-commit-config.yaml` and `.semgrepignore` exclude a long list of legacy files from linting. Do not add to that list. Upstream-sync notes in the wiki track ruff counts per touched file and require "no new findings".

**JavaScript**
- Prettier: tabs, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`. Prettier skips `patient_portal/` and a few Jinja-containing doctype JS files.
- ESLint flat config extends `eslint:recommended` and declares Frappe globals (`frappe`, `__`, `cur_frm`, `erpnext`, `$`, `moment`, …).
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})`. Wrap user strings in `__()`.
- The Vue portal uses `<script setup>` style, frappe-ui components, and the `@` alias to `src/`.

**Commits:** Conventional Commits, enforced by commitlint (`fix:`, `feat:`, `chore:`, …, lowercase type). In this fork, upstream cherry-picks use `git cherry-pick -x`, and follow-up fixes carry an `(upstream sync Bn)` suffix.
