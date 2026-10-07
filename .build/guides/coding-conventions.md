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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

## Python

- Format and lint with **ruff**. Indent with **tabs**, use **double quotes**, and keep lines to 110 (E501 is ignored). Lint rule sets are F, E, W, I, UP, B and RUF, with the ignore list in `pyproject.toml`.
- isort sections run in this order: stdlib, third-party, `frappe`, `erpnext`, `healthcare`, then first-party. Each section is separated by a blank line.
- Names follow Frappe conventions. Modules and folders use snake_case of the DocType name (`patient_appointment`). Classes are PascalCase DocType names (`PatientAppointment`, `TestPatientAppointment`). Functions use snake_case.
- Methods callable from the client are marked `@frappe.whitelist()`.
- Use `frappe.get_doc`, `frappe.db.get_value`, `frappe.get_list(..., pluck="name")`, `frappe.qb` and `frappe.utils` helpers (`getdate`, `flt`, `nowdate`).
- Wrap user-facing strings in `_()` and use `.format()` placeholders.
- Put business logic and validations **on the server side**, as the PR template requires.
- Semgrep runs the Frappe rules. Suppress a rule only with a justified `# nosemgrep`.

## JavaScript

- **Prettier** settings: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. **ESLint** uses `eslint:recommended`, with Frappe globals (`frappe`, `__`, `cur_frm`, `flt`, …) declared in `eslint.config.mjs`.
- Desk form scripts use `frappe.ui.form.on("<DocType>", {...})` in `doctype/<name>/<name>.js`, and wrap strings in `__()`.
- The portal uses Vue 3 SFCs with PascalCase component files (`BookAppointmentModel.vue`). Data is fetched through frappe-ui `createResource`.

## Commits

Use Conventional Commits (commitlint). Types are lower-case: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Upstream picks use `git cherry-pick -x`.
