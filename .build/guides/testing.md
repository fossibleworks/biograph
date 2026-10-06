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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - codecov.yml
  - .github/workflows/ci.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`) against a real MariaDB site (`test_site`).
- **Layout:** each DocType keeps its tests next to it in `healthcare/healthcare/doctype/<name>/test_<name>.py`. The repo has 85 test files.
- **Base class:** test classes extend **`HealthcareTestSuite`** from `healthcare.tests.utils`, which subclasses ERPNext's `ERPNextTestSuite`. Recent commits moved all fork tests onto it. Call `super().setUp()` in `setUp`.
- **Fixtures:** importing `healthcare.tests.utils` runs `BootStrapTestData()`. That creates deterministic master data with a `_Test` prefix: `_Test Company`, `_Test Medical Department`, `_Test Insurance Payor`, practitioners, service units, templates and so on. Reuse these records rather than creating companies or ad-hoc masters (see the commit "remove company creation in before tests").
- Tests often clear tables in `setUp` with `frappe.db.sql("delete from `tabX`")`.
- **Coverage:** Codecov requires **85% patch coverage** on PRs (threshold 0%). Project coverage may drop by at most 0.5%. Coverage is captured on scheduled runs, not on PRs.
- The PR template asks that all tests pass locally and that business logic and validations live server-side, where they can be tested.
