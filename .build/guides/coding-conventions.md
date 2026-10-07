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
  - .git-blame-ignore-revs
---

**Python** (configured by ruff in `pyproject.toml`)
- **Tabs** for indentation, double quotes, line length 110 (E501 is ignored, so long lines are tolerated). Docstring code is formatted.
- Lint rule sets: F, E, W, I, UP, B, RUF, with legacy ignores (F401 unused imports, B904, E402, …).
- Import order puts each framework in its own isort section: `future → stdlib → third-party → frappe → erpnext → healthcare → first-party → local`.
- Use absolute dotted imports, e.g. `from healthcare.healthcare.doctype.x.x import fn`.
- Translate every user-facing string with `_("...")` (`from frappe import _`) and fill placeholders with `.format()`, e.g. `_("{0} is a holiday").format(...)`.
- Doctype controllers subclass `frappe.model.document.Document` with a PascalCase class (`PatientAppointment`). They implement the lifecycle hooks `validate`, `on_submit`, `on_cancel`, etc. Module-level functions marked `@frappe.whitelist()` are client-callable.
- Naming: doctype folders and files use snake_case of the DocType name. DocType names use Title Case with spaces ("Patient Appointment"). Custom exceptions use PascalCase and end in `Error`.
- **Legacy exclusion list:** about 640 existing files are excluded from all pre-commit hooks in `.pre-commit-config.yaml`. Do not reformat them wholesale; keep diffs minimal so upstream syncs stay clean. New files are linted.

**JavaScript (desk)**
- Prettier: tabs, tabWidth 4, printWidth 88, `arrowParens: avoid`. ESLint uses `eslint:recommended` (flat config) with Frappe globals (`frappe`, `erpnext`, `$`, `__`, …).
- Wrap UI strings in `__("...")`.
- Form scripts use `frappe.ui.form.on("<DocType>", {...})` in `<doctype>.js`.

**Vue (patient_portal)**
- Vue 3 SFCs with PascalCase component files (`BookAppointmentModel.vue`). The `@` alias maps to `src`. Style with Tailwind and frappe-ui components.
- Prettier excludes `patient_portal/`, so follow the formatting of the surrounding file.

**Commits:** Conventional Commits with a lowercase type from: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Scopes are used, e.g. `docs(wiki): …`, and suffixes such as `(upstream sync B2)` appear.
