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
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
---

## Python
- **ruff** (pinned v0.15.18 in pre-commit). `line-length = 110`, `target-version = py310`. Lint rule sets: `F, E, W, I, UP, B, RUF`, with the ignore list in `pyproject.toml`.
- **Format:** `ruff format` with **tabs** for indentation and **double quotes**.
- **Import order** (isort sections): future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Put a blank line between each group, as in `test_fee_validity.py`.
- File header comment: `# Copyright (c) <year>, ... and Contributors` / `# See license.txt`.
- Naming: snake_case modules and functions. DocType classes use PascalCase of the DocType name (for example `TestFeeValidity`). DocType names in strings use Title Case with spaces (`"Patient Appointment"`).
- Mark API methods with `@frappe.whitelist()`. Prefer type hints on whitelisted arguments (upstream practice).
- Wrap every user-visible string in `_()` (Python) or `__()` (JS) so it is translatable.
- Use `frappe.db.get_value` / `frappe.get_doc` / `frappe.qb`. Raw `frappe.db.sql` exists (about 90 calls), but new code should prefer the query builder.
- Use `# nosemgrep` only with a reason. Semgrep runs with the Frappe rules.

## JavaScript / Vue
- **Prettier:** tabs (`useTabs`, `tabWidth 4`), `printWidth 88`, `arrowParens: avoid`. The portal and some large form scripts are excluded.
- **ESLint** flat config (`eslint:recommended`) with Frappe globals (`frappe`, `erpnext`, `__`, `$`, `moment`, …).
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})` in `<doctype>.js`.
- Portal: Vue SFCs in PascalCase (`BookAppointmentModel.vue`) under `patient_portal/src/components`, with the `@` alias pointing to `src`.

## Legacy exclusions
`.pre-commit-config.yaml` excludes about 600 legacy paths from pre-commit. Many existing files therefore don't follow the formatter. When you touch an excluded file, don't reformat the whole file, and don't add **new** ruff findings (compare the ruff count before and after, as the sync ledger does).
