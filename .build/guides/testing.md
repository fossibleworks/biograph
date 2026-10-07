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
  - healthcare/healthcare/doctype/practitioner_availability/test_practitioner_availability.py
  - .github/workflows/ci.yml
  - codecov.yml
  - .github/labeler.yml
---

- **Framework:** Frappe's unittest-based test runner. Test classes subclass `HealthcareTestSuite`, defined in `healthcare/tests/utils.py`, which extends `erpnext.tests.utils.ERPNextTestSuite`.
- **Fixtures:** `BootStrapTestData` in `healthcare/tests/utils.py` creates the shared master data: `_Test Company`, service and stock items, departments, users, patients, practitioners, service units, templates, insurance payors and so on. Reuse these records and the `make_*` helpers, and add new master data there rather than in each test. Test record names use the `_Test ...` prefix.
- **Layout:** each doctype keeps its test next to it as `healthcare/healthcare/doctype/<name>/test_<name>.py` (85 test files). Tests import builders from other doctype tests, for example `create_appointment` from `test_patient_appointment`.
- **Style:** `setUp` calls `super().setUp()` and then clears the relevant tables. Assertions use `assertEqual`/`assertTrue`, and validation paths use `assertRaises(frappe.ValidationError)` or a custom error class.
- **CI:** `ci.yml` runs `bench --site test_site run-parallel-tests --app healthcare` against MariaDB on pull requests (unless the PR only touches css/js/md/html/csv) and every night. Coverage is captured only on runs that are not PRs and is uploaded to Codecov.
- **Coverage expectations** (`codecov.yml`): patch target **85%** on PRs, and the project may not drop more than 0.5%.
- The PR labeler adds a **`needs-tests`** label when `healthcare/**/*.py` changes and no `test*.py` file changes. A Python change should come with a test.
- There are no JS or portal unit tests.
