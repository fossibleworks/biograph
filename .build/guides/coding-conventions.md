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
  - .pre-commit-config.yaml
  - .semgrepignore
  - healthcare/healthcare/doctype/lab_test/lab_test.py
  - healthcare/healthcare/doctype/lab_test/lab_test.js
  - patient_portal/src/components/Payment.vue
---

# Coding conventions

## Python (ruff, `pyproject.toml`)
- **Indent with tabs.** Use double quotes and a line length of 110 (`ruff format`, `indent-style = "tab"`).
- Lint rules: `F, E, W, I, UP, B, RUF`, with ignores for legacy patterns. Notably `F401` (unused imports) and `E501` are ignored. Commits still remove unused imports introduced by upstream picks.
- **Import order** (isort sections): future, stdlib, third-party, **frappe**, **erpnext**, **healthcare**, first-party, local. Separate each block with a blank line, as in `lab_test.py`.
- Use absolute dotted imports for app code: `from healthcare.healthcare.doctype.x.x import ...`. Put deferred imports inside functions to avoid cycles.
- Name controller classes in PascalCase after the DocType (`class LabTest(Document)`). Use snake_case for methods and the DocType lifecycle names (`validate`, `on_submit`, `on_cancel`, `validate_<thing>`).
- Mark API methods with `@frappe.whitelist()`. Prefer `frappe.qb` (query builder) for queries. Raw `frappe.db.sql` still appears in about 90 places.
- Wrap **every user-facing string in `_()`**. Use positional `{0}` formatting via `.format()`, never f-strings inside `_()`.
- File header: a `# Copyright (c) <year>, <owner> and contributors` comment.

## JavaScript / Vue
- Prettier settings: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: avoid`. ESLint uses a flat config based on `eslint:recommended`, with Frappe globals (`frappe`, `erpnext`, `__`, `$`).
- Desk scripts: `frappe.ui.form.on("<DocType>", {...})`, `frappe.call({method: "healthcare.healthcare...."})`, and `__()` for strings.
- Vue SPA files are **excluded from prettier**. They use `<template>` + Tailwind utility classes + frappe-ui components, the `@` alias for `src/`, and tab indentation.

## Legacy exclusions
`.pre-commit-config.yaml` and `.semgrepignore` exclude roughly 620 pre-existing files from lint. **New files are not excluded**, so they must pass every hook. Do not add new paths to those exclude lists.
