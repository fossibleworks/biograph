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
---

- **Framework:** Frappe's test runner (unittest-based) against a real MariaDB site. CI runs `bench --site test_site run-parallel-tests --app healthcare`.
- **Layout:** tests sit next to their DocType as `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 test files). Shared fixtures live in `healthcare/tests/utils.py`.
- **Base class:** every test class extends `HealthcareTestSuite` (`from healthcare.tests.utils import HealthcareTestSuite`), which subclasses ERPNext's `ERPNextTestSuite`. The fork recently migrated all tests to this class. Do not use `FrappeTestCase` or `IntegrationTestCase` directly.
- **Master data:** `BootStrapTestData.make_master_data()` creates the `_Test Company`, practitioners, patients, service units, templates, insurance payors and so on. Use `_Test ...` names for test records and look up existing ones with `frappe.get_list(..., pluck="name")`.
- **Naming:** classes are `Test<DocType>`, methods are `test_<behaviour>`. Call `super().setUp()` in `setUp`. Module-level helpers like `create_appointment(...)` build documents.
- Tests must be deterministic. Recent commits fixed non-deterministic patient initialisation.
- **Coverage:** codecov requires a **patch target of 85%** on PRs to develop, and a project threshold of 0.5% drop (target auto). CI captures coverage on non-PR runs.
