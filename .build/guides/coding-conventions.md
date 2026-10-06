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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs** for indentation, **double quotes**, line length 110, target py310. Format with `ruff format`.
- Lint rule families: F, E, W, I, UP, B, RUF. Many are ignored for Frappe idioms (E501, F401, F403/F405, W191, B904…).
- **Import order** uses custom isort sections: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local. Put a blank line between groups.
- Translatable strings use `from frappe import _` and `_("Text {0}").format(x)`.
- Docs and types: `typing-modules = ["frappe.types.DF"]`, so DocType controllers may carry auto-generated type-hint blocks.
- Naming follows Frappe conventions:
  - DocType folders and modules are snake_case of the DocType name (`patient_appointment/patient_appointment.py`).
  - Controller classes are PascalCase (`class PatientAppointment(Document)`).
  - Module-level helpers are snake_case.
  - Whitelisted endpoints are marked `@frappe.whitelist()`.
- Queries: prefer `frappe.qb` (about 80 uses) or `frappe.get_all/get_list`. Raw `frappe.db.sql` still appears (about 91 uses), mostly in older code and tests.
- Large legacy areas are listed in the `.pre-commit-config.yaml` `exclude` block (most of `healthcare/healthcare/doctype/**`), so pre-commit skips them. When you touch those files, run ruff on them directly and do not add *new* findings. The upstream-sync ledger records before/after ruff counts.

**JavaScript**
- Prettier: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: "avoid"`.
- ESLint 10 flat config with `eslint:recommended`, and Frappe globals declared (`frappe`, `erpnext`, `$`, `moment`, `__`…).
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})`. User-visible strings are wrapped in `__()`.
- The Vue portal (`patient_portal/`) is excluded from Prettier. It uses `<script setup>`-style SFCs with frappe-ui components and Tailwind classes.

**Commits**: Conventional Commits, lower-case type, enforced by commitlint (e.g. `fix(appointment): …`, `feat: …`). Upstream picks keep the `(cherry picked from commit …)` trailer from `git cherry-pick -x`.

File header convention in older files: `# Copyright (c) <year>, ESS LLP and Contributors` / `# See license.txt`.
