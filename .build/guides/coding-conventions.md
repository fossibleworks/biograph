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
  - commitlint.config.js
  - healthcare/healthcare/doctype/allergy/allergy.py
  - healthcare/healthcare/doctype/lab_test/lab_test.js
  - healthcare/healthcare/api/patient_portal.py
  - .pre-commit-config.yaml
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs** for indentation and **double quotes**. Line length is 110, though E501 is ignored.
- Lint selection: F, E, W, I, UP, B and RUF, with a documented ignore list (for example F401, E402 and B904).
- Import order is enforced by isort sections: future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Put a blank line between each group, for example `import frappe` / `import erpnext` / `from healthcare...`.
- Translate user-facing strings with `from frappe import _` and `_("...")`, using `.format()` for placeholders (`_("Invalid Code Value: {0}").format(code_value)`).
- Each DocType controller is a class named in PascalCase after the DocType (`class Allergy(Document)`), in `<snake_name>.py`. Whitelisted functions use `@frappe.whitelist()`, and newer code adds type hints.
- Files start with a copyright and licence header comment.
- Use `frappe.qb` or `frappe.db.get_all` with `fields` and `filters` for queries, not raw SQL strings.

**JavaScript** (Prettier and ESLint)
- Prettier: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: "avoid"`.
- ESLint flat config extends `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, `__`, ...).
- Form scripts use `frappe.ui.form.on("DocType Name", { setup(frm) {...}, refresh(frm) {...} })`, and all labels are wrapped in `__("...")`.
- The `patient_portal/` Vue code is excluded from Prettier. It uses `<script setup>`-style Vue 3, the `@/` alias and frappe-ui components.

**Naming:** DocTypes use Title Case with spaces ("Patient Appointment"). Directories and fieldnames are snake_case. Test fixture records are prefixed `_Test ` ("_Test Lab Test - with Sample").

**Commits** use Conventional Commits (commitlint). The allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test, always lower-case, with optional scopes such as `fix(tests):` and `docs(wiki):`.

Many legacy files are excluded in `.pre-commit-config.yaml`. Don't widen that list, and don't add new ruff findings to excluded files.
