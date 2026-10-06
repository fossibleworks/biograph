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
  - healthcare/tests/test_utils.py
  - .github/workflows/ci.yml
  - codecov.yml
  - .github/labeler.yml
---

- **Framework:** Frappe's test runner (unittest-based). Tests subclass **`HealthcareTestSuite`** from `healthcare/tests/utils.py`, which builds on ERPNext's `ERPNextTestSuite`. `BootStrapTestData` creates the shared master data: company, service items, patients, practitioners, service units, templates and so on.
- **Layout:** tests are colocated with each DocType as `healthcare/healthcare/doctype/<name>/test_<name>.py`. There are about 85 `test_*.py` files. Cross-cutting tests live in `healthcare/tests/test_utils.py`, custom-doctype tests in `custom_doctype/test_sales_invoice.py`, and regional tests in `regional/india/abdm/test_abdm.py`.
- **Style:** a `Test<DocType>` class with `setUp()` that calls `super().setUp()` and clears relevant tables. Module-level factory helpers such as `create_appointment(...)` and `create_encounter(...)` are imported between test modules. Settings are toggled with `frappe.db.set_single_value("Healthcare Settings", ...)`. Use `self.assertEqual` and similar assertions.
- **CI:** `ci.yml` runs `bench --site test_site run-parallel-tests --app healthcare` against MariaDB on PRs (Python changes only, since css/js/md/html/csv paths are ignored) and nightly. Coverage is captured on non-PR runs and uploaded to Codecov.
- **Coverage expectations (`codecov.yml`):** patch target **85%** on PRs to `develop`, and project coverage must not drop by more than 0.5%.
- **Labeler:** PRs that touch `healthcare/**/*.py` without touching any `test*.py` get a `needs-tests` label automatically.
- **Fork caveat:** `biograph-fh` has no CI baseline. The first CI run on a goal PR becomes the baseline, and no local bench is assumed (see `wiki/upstream-sync-version-16.md`).
