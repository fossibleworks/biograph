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
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's test runner on unittest. Run `bench --site test_site run-parallel-tests --app healthcare`, which needs a full bench with ERPNext and MariaDB, as in `ci.yml`.
- **Location:** tests sit next to the code as `test_<doctype>.py` inside each doctype folder (85 test files). Cross-cutting tests go in `healthcare/tests/`.
- **Base class:** every test class subclasses `HealthcareTestSuite` (`healthcare/tests/utils.py`, which extends ERPNext's `ERPNextTestSuite`). `BootStrapTestData` seeds shared masters: `_Test Company`, `_Test Medical Department`, practitioners, patients, items, templates and insurance payors. Recent commits migrated all fork tests to this base. Call `super().setUp()` first.
- **Fixtures:** reuse helpers exported from other tests, e.g. `create_appointment` and `update_status` from `test_patient_appointment.py`. Prefix test record names with `_Test`. Toggle `Healthcare Settings` inside the test and save with `ignore_permissions=True`.
- **Coverage:** Codecov requires **85% patch coverage** on PRs to `develop`. Project coverage is `auto` with a 0.5% threshold. Coverage is only collected on non-PR (scheduled) CI runs.
- The PR labeler adds `needs-tests` when Python files change but no `test*.py` file does.
