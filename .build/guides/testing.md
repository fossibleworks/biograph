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
  - .github/workflows/ci.yml
---

# Testing

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`), which runs against a real MariaDB site (`test_site`).
- **Layout:** tests sit next to their DocType as `healthcare/healthcare/doctype/<name>/test_<name>.py`. There are about 85 test files. Shared helpers live in `healthcare/tests/`.
- **Base class:** test classes extend `HealthcareTestSuite` from `healthcare.tests.utils`, which builds on ERPNext's `ERPNextTestSuite`. `BootStrapTestData` creates master data (company, service items, practitioners, patients, service units, lab/observation templates, therapy types, etc.). Fixtures use the `_Test ...` naming, e.g. `"_Test Lab Test - with Sample"`.
- **Style:** methods are named `test_<behaviour>` and use `self.assertEqual` / `assertTrue` / `assertRaises(<SpecificError>)`. They use module-level factory helpers such as `create_lab_test(...)`. Assertions check DB state with `frappe.db.get_value` / `frappe.db.exists`.
- **Coverage:** Codecov enforces a **patch target of 85%** on PRs and allows the project to drop by at most 0.5%. Coverage is captured only on non-PR (scheduled/nightly) runs.
- **CI:** the `Server Tests` job in `ci.yml` runs on PRs that touch more than css/js/md/html/csv, and nightly.
- There are no JS or portal unit tests in the repo, so test UI changes manually. The PR template asks for UI and unit tests to pass locally.
