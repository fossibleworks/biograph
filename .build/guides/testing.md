---
title: Testing
category: testing
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/doctype/allergy/test_allergy.py
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/tests/utils.py
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
  - healthcare/hooks.py
---

**Framework:** Frappe's unittest-based test runner, run with `bench run-tests` or `bench run-parallel-tests`. Tests run against a real MariaDB site that has ERPNext installed. `before_tests` in hooks.py (`healthcare.healthcare.utils.before_tests`) prepares fixtures.

**Layout**
- Each DocType has `doctype/<name>/test_<name>.py`, about 85 test files in total.
- Tests subclass `frappe.tests.IntegrationTestCase`, which newer code uses, or `frappe.tests.utils.FrappeTestCase`, which older code uses.
- Shared helpers are in `healthcare/tests/utils.py` and `healthcare/tests/test_utils.py`. Larger tests define module-level factory functions such as `create_healthcare_docs()` and `create_appointment(...)`, which other tests import.
- `setUp` often clears tables with `frappe.db.sql("delete from `tabX`")` and toggles settings with `frappe.db.set_single_value`.
- Many stub tests are empty (`pass`).

**Expectations**
- The PR labeler adds `needs-tests` when Python under `healthcare/` changes without any `test*.py` change, so ship a test with each logic change.
- Codecov patch coverage target: **85%** on PRs. Project coverage must not drop by more than 0.5%.
- CI runs server tests on PRs, except PRs that touch only css/js/md/html/csv. It also runs a nightly scheduled run, which collects coverage.
- There are no JS or UI test suites in the repo.
