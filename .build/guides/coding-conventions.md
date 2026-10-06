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
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
  - healthcare/healthcare/utils.py
---

## Python
- **Ruff** sets the format: **tabs** for indentation, **double quotes**, line length 110 (E501 is ignored).
- Lint rule sets F, E, W, I, UP, B and RUF are enabled. Several are ignored, including F401 unused imports, but recent commits still remove unused imports, so keep files clean.
- **Import order** (isort sections): future, stdlib, third-party, `frappe`, `erpnext`, `healthcare`, first-party, local. Separate each group with a blank line, as in the test files: `import frappe`, then `from erpnext...`, then `from healthcare...`.
- Type hints: use `frappe.types.DF` typing for doctypes. Add type hints to whitelisted methods (recent commits do this).
- Translatable strings: wrap them in `_()` from `frappe`. Format with `.format()` and `{0}` placeholders, for example `_("Invalid Code Value: {0}").format(code_value)`.
- Queries: prefer `frappe.qb` (pypika) and `frappe.db.get_value/exists/get_list(pluck=...)`. Avoid raw SQL in new code.
- Naming: snake_case modules and functions. Doctype folders are snake_case versions of the DocType name. Controller classes are PascalCase DocType names.
- Expose server methods to JS only through `@frappe.whitelist()` (182 uses in the repo).
- Many legacy files are listed in `.pre-commit-config.yaml`'s global `exclude`, which skips their pre-commit hooks. For those files, run ruff directly and **do not add new findings** (the upstream-sync ledger records baseline counts).

## JavaScript / Vue
- **Prettier**: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`. It applies to desk JS, CSS and Vue. `patient_portal/` is excluded from Prettier.
- **ESLint** flat config (`eslint:recommended`) with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, …).
- Desk JS wraps user-facing strings in `__()`.
- Vue SPA: single-file components in PascalCase (`BookAppointmentModel.vue`). Style with Tailwind utility classes and frappe-ui components.

## Commits
Use Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Types are lower-case. Scopes are common, e.g. `fix(tests): …` and `docs(wiki): …`.
