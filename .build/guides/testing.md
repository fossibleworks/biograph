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
  - healthcare/healthcare/doctype/lab_test_sample/test_lab_test_sample.py
  - healthcare/healthcare/doctype/nursing_task/test_nursing_task.py
  - codecov.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe and ERPNext integration tests run against a real MariaDB site through `bench run-tests` / `run-parallel-tests`.
- **Layout:** each doctype has a co-located `doctype/<name>/test_<name>.py`, about 85 test files in total. Shared fixtures live in `healthcare/tests/utils.py`.
- **Base class:** test classes extend **`HealthcareTestSuite`** from `healthcare.tests.utils`. It subclasses ERPNext's `ERPNextTestSuite`. Fork tests were migrated to this base class, so use it in new tests too. `BootStrapTestData` creates master data such as the company, items, practitioners, patients, and templates. Test records use the `_Test ...` naming.
- **Assertions:** standard unittest. Validation failures are checked with `self.assertRaises(frappe.ValidationError, doc.save)`.
- **Coverage:** Codecov requires an **85% patch target** on PRs (to develop) and allows a 0.5% project threshold. Coverage is captured on scheduled and non-PR runs.
- CI skips server tests for PRs that only touch `.js`, `.css`, `.md`, `.html`, or `.csv`.
- No JS or Vue unit test setup exists.
