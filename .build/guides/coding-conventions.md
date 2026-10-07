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
  - healthcare/healthcare/api/patient_portal.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Python (ruff, configured in `pyproject.toml`)**
- Format with **tabs**, double quotes and line length 110 (E501 is ignored).
- Lint rule sets: F, E, W, I, UP, B, RUF. Some rules are ignored, notably F401 (unused imports), B904, E402 and W191.
- **Import order:** future, stdlib, third-party, `frappe`, `erpnext`, `healthcare`, first-party, local. Each group is separated by a blank line, as in the test and api files.
- Absolute imports from the `healthcare.healthcare.doctype.<x>.<x>` path.
- Controllers are classes named after the DocType in PascalCase (`class PatientAppointment(Document)`). Modules and folders use snake_case. Each file starts with a copyright header.
- Data access: `frappe.qb` and `frappe.get_all`/`get_list` are preferred over raw SQL. Raw `frappe.db.sql` still appears in older code and tests.
- Mark endpoints with `@frappe.whitelist()`. Keep business logic and validation on the server, as the PR template asks.
- Wrap user-facing strings in `_()` (Python) or `__()` (JS).
- The long `exclude:` list in `.pre-commit-config.yaml` covers legacy files that are not ruff-clean. Do not add new ruff findings to them, and do not mass-reformat them, because that inflates upstream-sync diffs.

**JavaScript**
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. The patient_portal and a few large form scripts are excluded.
- ESLint uses `eslint:recommended` with Frappe globals (`frappe`, `erpnext`, `$`, `moment`, …).
- Desk form scripts use `frappe.ui.form.on('<DocType>', {...})` in `<doctype>.js`.

**Vue (patient_portal):** single-file components in PascalCase (`BookAppointmentModel.vue`), frappe-ui components and resources, Tailwind utility classes and the `@/` alias for `src`.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. The type is lower-case and the subject is required. Upstream cherry-picks use `git cherry-pick -x`.
