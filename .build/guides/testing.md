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
  - codecov.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's unittest-based runner, executed with `bench run-tests` / `run-parallel-tests --app healthcare` against a real MariaDB site.
- **Layout:** tests sit next to the code as `doctype/<dt>/test_<dt>.py` (about 85 files). The shared helpers are in `healthcare/tests/utils.py`.
- **Base class:** every test class subclasses `HealthcareTestSuite`, which extends ERPNext's `ERPNextTestSuite`. Recent commits migrated all remaining fork tests to it. `BootStrapTestData` creates the deterministic master data: `_Test Company`, practitioners, patients, service units, templates, insurance payors, etc.
- **Conventions:**
  - Call `super().setUp()` in `setUp`.
  - Look records up deterministically (`frappe.get_list(..., pluck="name")`).
  - Reuse factory helpers exported from sibling tests, e.g. `create_appointment` from `test_patient_appointment`.
  - Configure `Healthcare Settings` in the test and save with `ignore_permissions=True`.
  - Test record names use the `_Test …` prefix.
- **Coverage:** captured on scheduled/non-PR runs and uploaded to Codecov.
  - Patch target: **85%** on PRs (develop).
  - Project: `auto` with a 0.5% threshold.
- **Baseline caveat:** the fork has no CI history on `biograph-fh`, so the first goal-PR CI run is the baseline. Compare failures against the introducing commit.
