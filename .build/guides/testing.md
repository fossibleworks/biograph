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
  - healthcare/healthcare/doctype/lab_test/test_lab_test.py
  - healthcare/healthcare/doctype/practitioner_availability/test_practitioner_availability.py
  - .github/workflows/ci.yml
  - codecov.yml
  - .github/labeler.yml
---

# Testing

- **Framework:** Frappe/ERPNext integration tests, based on `unittest` and run through bench against a real MariaDB site. There are 85 `test_*.py` files.
- **Layout:** tests sit next to their DocType, at `healthcare/healthcare/doctype/<name>/test_<name>.py`. Shared fixtures are in `healthcare/tests/utils.py`.
- **Base class:** subclass **`HealthcareTestSuite`**, which extends `erpnext.tests.utils.ERPNextTestSuite`. Fork tests were migrated to it, so do not use `FrappeTestCase` or bare `unittest.TestCase` for new tests.
- **Fixtures:** `BootStrapTestData` creates master data with `_Test`-prefixed names, e.g. `_Test Company`, `_Test Lab Test - with Sample`, `_Test Insurance Payor`. Reuse these records, and add new masters there through `make_records`.
- **Assertions:** check DB state with `frappe.db.get_value`/`exists`. Check validation failures with `self.assertRaises(frappe.ValidationError, doc.submit)` or a domain error subclass. Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- **Determinism:** recent fixes made patient initialisation deterministic. Avoid relying on dates or ordering.
- **CI:** `bench --site test_site run-parallel-tests --app healthcare`. Coverage is collected on non-PR runs and uploaded to Codecov.
- **Coverage expectations (`codecov.yml`):** patch target **85%** on PRs, and the project may not drop by more than 0.5%. The labeler adds **`needs-tests`** to PRs that touch `healthcare/**/*.py` without any `test*.py` change.
- There are no JS or Vue unit tests. `cypress/` is referenced in excludes but not present.
