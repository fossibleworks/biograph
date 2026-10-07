---
title: Coding Conventions
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
  - healthcare/healthcare/doctype/fee_validity/fee_validity.py
  - healthcare/healthcare/api/patient_portal.py
---

**Python (ruff, configured in `pyproject.toml`):**
- Indent with **tabs**, use **double quotes**, line length 110, target py310.
- Lint selection is F, E, W, I, UP, B, RUF, with ignores for E501, F401, B904, and others.
- Import sections in order: future, stdlib, third-party, `frappe`, `erpnext`, `healthcare`, then local.
- Doctype controllers are `class PascalName(Document)` in `doctype/<snake_name>/<snake_name>.py`. Module functions use snake_case.
- Expose endpoints with `@frappe.whitelist()`.
- Prefer `frappe.qb` or `frappe.get_all` and `frappe.get_cached_value` over raw SQL.
- Wrap every user-facing string in `_()`.
- Files start with the existing copyright header.
- Many legacy files are listed in the `.pre-commit-config.yaml` exclude list. When you touch them, don't add new ruff findings. The wiki ledger tracks before/after ruff counts.

**JavaScript (Prettier and ESLint):**
- Tabs (tabWidth 4), printWidth 88, `arrowParens: avoid`.
- ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `__`, `$`, ...).
- Form scripts use `frappe.ui.form.on("DocType", {...})` and wrap strings in `__()`.

**Vue (patient_portal):** `<script setup>`, frappe-ui components, Tailwind utility classes, and the `@/` alias for `src`. Prettier excludes `patient_portal/`.

**Commits:** Conventional Commits with a lowercase type from build, chore, ci, docs, feat, fix, perf, refactor, revert, style, or test. Scopes are allowed, e.g. `fix(tests):` or `docs(wiki):`.
