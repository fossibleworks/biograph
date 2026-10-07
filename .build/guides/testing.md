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
  - .github/labeler.yml
---

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`). Tests run against a real MariaDB site that has erpnext, payments and healthcare installed.
- **Layout:** each test sits next to its doctype as `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 test files). Shared fixtures live in `healthcare/tests/utils.py`.
- **Base class:** subclass **`HealthcareTestSuite`** from `healthcare.tests.utils`. It extends ERPNext's `ERPNextTestSuite`, and `BootStrapTestData` builds the master data: `_Test Company`, patients, practitioners, service units, templates, insurance payors and so on. Recent commits moved all fork tests onto this suite. Call `super().setUp()`.
- **Style:** create data with helpers exported from other tests (for example `create_appointment` from `test_patient_appointment`). Configure `Healthcare Settings` inside the test and assert with `self.assertEqual`/`assertTrue` on `frappe.db.get_value`. Make tests deterministic: pick fixture records explicitly and do not depend on ordering.
- **CI:** `ci.yml` runs server tests on PRs (it skips PRs that touch only css/js/md/html/csv) and nightly. Coverage is captured only on non-PR runs and uploaded to Codecov.
- **Coverage expectations** (`codecov.yml`): patch target **85%** on PRs to `develop`; project coverage must not drop by more than 0.5%.
- **Labeller:** PRs that change `healthcare/**/*.py` without touching a `test*.py` file are labelled `needs-tests`, so add or adjust a test alongside Python changes.
- **Baseline note:** the fork's `biograph-fh` has no CI history, so the first CI run on a goal PR is the baseline (see the wiki ledger).
