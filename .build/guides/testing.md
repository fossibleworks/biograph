---
title: Testing
category: testing
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/tests/utils.py
  - codecov.yml
  - .github/labeler.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **Framework:** the Frappe test runner (`bench run-tests`), with unittest-style classes on top of ERPNext's test infrastructure.
- **Base class:** `HealthcareTestSuite` (in `healthcare/tests/utils.py`, extends `erpnext.tests.utils.ERPNextTestSuite`). 84 test modules use it. `BootStrapTestData` in the same file creates master data (company, service items, practitioners, patients, service units, appointment types, lab/observation templates, therapy, medications, insurance payors). Reuse these fixtures; do not build ad-hoc masters.
- **Layout:** tests sit next to their doctype as `healthcare/healthcare/doctype/<name>/test_<name>.py` (85 files). Cross-cutting tests go in `healthcare/tests/`, e.g. `test_utils.py`.
- **Test data naming:** records use a `_Test` prefix (e.g. `"_Test Insurance Payor"`). Dates use `frappe.utils` helpers (`nowdate`, `add_days`, `getdate`).
- **Coverage expectations:** Codecov sets the **patch target to 85%** on PRs and allows the project total to drop by 0.5%. The labeler adds a `needs-tests` label when a PR changes `healthcare/**/*.py` without touching any `test*.py`.
- **CI caveat:** this fork has no server-test workflow (`ci.yml`) checked in and no CI history (see the upstream-sync ledger). Run tests on a local bench, and say so in the PR when no bench was available.
