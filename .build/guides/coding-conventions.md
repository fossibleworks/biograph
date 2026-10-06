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
  - commitlint.config.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
  - patient_portal/src/components/Payment.vue
---

**Python** (ruff, configured in `pyproject.toml`)
- **Tabs for indentation**, double quotes, line length 110 (E501 is ignored, so long lines are tolerated), target py310.
- Lint rule sets: `F, E, W, I, UP, B, RUF`. Some are ignored on purpose, including F401 unused imports, F403/F405 star imports, E402, E741 and B904.
- **Import order** uses custom isort sections: stdlib → third-party → `frappe` → `erpnext` → `healthcare` → first-party → local. Put a blank line between groups, as in `patient_appointment.py`.
- File header: `# Copyright (c) <year>, <org> and contributors` / `# See license.txt`.
- Frappe idioms:
  - one DocType per folder `doctype/<snake_case>/<snake_case>.py`, with a `class PascalCaseName(Document)`
  - functions callable from the client are marked `@frappe.whitelist()`
  - prefer `frappe.qb` query-builder queries over raw `frappe.db.sql` (the code base has about 80 `qb` uses against about 90 raw-SQL uses)
  - wrap user-facing strings in `_()` from `frappe`
- `typing-modules = ["frappe.types.DF"]` is set for the auto-generated type annotations.
- The pre-commit config excludes a long list of legacy upstream files from hooks. Don't reformat those files wholesale; it creates noisy diffs against upstream.

**JavaScript (Desk)**
- Prettier settings: `useTabs: true`, `tabWidth: 4`, `printWidth: 88`, `arrowParens: "avoid"`.
- ESLint uses the flat config `eslint.config.mjs` (eslint:recommended plus Frappe globals such as `frappe`, `erpnext`, `__`, `$`).
- Form scripts use `frappe.ui.form.on("Doctype Name", {...})`. Wrap strings in `__()`, with `{0}` placeholders and an args array.

**Vue (patient_portal)**
- Vue 3 SFCs named in PascalCase (`BookAppointmentModel.vue`, `PractitionerSelector.vue`), Tailwind utility classes, and frappe-ui components (`Card`, etc.). The `@` alias points to `patient_portal/src`. Prettier excludes `patient_portal/`.

**Commits:** Conventional Commits, enforced by commitlint. Types are `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, in lower case. Upstream-sync commits add a scope suffix, e.g. `fix: … (upstream sync B2)`.
