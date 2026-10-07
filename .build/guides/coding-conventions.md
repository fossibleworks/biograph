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
  - commitlint.config.js
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Python (ruff, configured in `pyproject.toml`)**
- **Indentation is tabs.** Use double quotes and a line length of 110 (E501 is ignored). Target py310.
- Lint selects `F,E,W,I,UP,B,RUF`, with notable ignores (F401 unused imports, E402, B904, etc.).
- isort sections: future → stdlib → third-party → **frappe** → **erpnext** → **healthcare** → first-party → local, with a blank line between each.
- Doctype controllers are named `class <PascalDocTypeName>(Document)`, in `doctype/<snake_name>/<snake_name>.py`. Validation is split into small `validate_*` / `set_*` methods called from `validate()`.
- Client-callable functions use `@frappe.whitelist()`. Import other modules by full dotted path from `healthcare.`.
- Prefer `frappe.qb` or the ORM (`frappe.db.get_value`, `get_list(..., pluck="name")`) over raw SQL for new code.
- Wrap all user-facing strings with `_()` in Python and `__()` in JS. Use `.format()` placeholders like `_("Invalid Code Value: {0}").format(x)`.
- Business logic and validation belong on the server (PR template).
- Note: many legacy files are listed in the pre-commit/semgrep exclude lists. New files are **not** excluded and must pass the hooks.

**JavaScript**
- Prettier: tabs, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`. ESLint uses `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `$`, `__`, etc.).
- Desk scripts use `frappe.ui.form.on("DocType", {...})` and `frappe.call` for whitelisted methods.
- Portal Vue uses SFCs with `<script setup>`, the `@/` alias for `src`, and frappe-ui components and resources.

**Commits:** Conventional Commits (`feat|fix|chore|docs|refactor|test|perf|style|ci|build|revert`, lowercase type, optional scope), e.g. `fix(tests): ...`, `docs(wiki): ...`.
