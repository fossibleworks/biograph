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
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

**Framework:** Frappe's unittest-based server tests, run with `bench run-tests` or `bench run-parallel-tests --app healthcare` against a real MariaDB site (`test_site`). There are no JS or UI test suites in the repo.

**Layout:** tests live next to their DocType as `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 files). Shared base classes and fixtures are in `healthcare/tests/utils.py`.

**Base class:** every test class subclasses **`HealthcareTestSuite`** from `healthcare.tests.utils`, which builds on ERPNext's `ERPNextTestSuite`. The fork recently migrated all remaining tests to it. Master data (company, items, practitioners, patients, templates, insurance payors, ...) comes from `BootStrapTestData`. Reference these records by their `_Test ...` names, and don't create ad-hoc companies in tests.

**Style:** `class TestLabTest(HealthcareTestSuite)` with `test_*` methods. Use `self.assertRaises(frappe.ValidationError, doc.submit)` for validation paths. Toggle settings with `frappe.db.set_single_value(...)` and reset them afterwards. Call `super().setUp()` when you override `setUp`. Keep tests deterministic, because recent commits fixed non-deterministic patient and appointment tests.

**Coverage expectations:**
- Codecov **patch target is 85%** on PRs, and the project threshold is 0.5%.
- CI collects coverage only on non-PR (scheduled) runs.
- The labeler adds a `needs-tests` label when a PR changes `healthcare/**/*.py` without touching any `test*.py` file.
