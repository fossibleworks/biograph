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
  - .github/workflows/ci.yml
  - codecov.yml
---

- **Framework:** Frappe's bench test runner on top of `unittest`. Tests subclass **`HealthcareTestSuite`** from `healthcare/tests/utils.py`, which extends ERPNext's `ERPNextTestSuite`. 84 of the 85 test files already use it, and the fork recently moved the remaining tests to it. Shared master data such as templates, payors and medications comes from `BootStrapTestData` in the same module.
- **Layout:** each test sits next to its DocType as `healthcare/healthcare/doctype/<name>/test_<name>.py`, plus `custom_doctype/test_sales_invoice.py` and `healthcare/tests/test_utils.py`. Test helpers such as `create_appointment` are imported from other DocTypes' test modules.
- **Style:** `setUp()` calls `super().setUp()` and often clears tables with `frappe.db.sql("delete from `tab...`")`. Settings are configured through `frappe.get_single("Healthcare Settings")`. Use `frappe.get_list(..., pluck="name")` for fixtures. Tests should be deterministic; recent commits fixed non-deterministic patient initialisation.
- **Running:** CI runs `bench --site test_site run-parallel-tests --app healthcare` against MariaDB on every PR, except PRs that only touch css/js/md/html/csv, and nightly.
- **Coverage:** collected on non-PR runs and uploaded to Codecov. `codecov.yml` targets **85% patch coverage** on PRs to `develop`, and the project coverage may drop by at most 0.5%.
- There are no JS or Vue unit tests.
- Note: per `wiki/upstream-sync-version-16.md`, the fork `biograph-fh` has no CI baseline yet. Record pre-existing failures there instead of assuming the suite is green.
