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
  - .github/helper/install.sh
---

- **Framework**: Frappe's unittest-based test runner, run through `bench run-tests` / `run-parallel-tests`. There is no pytest config.
- **Base class**: `healthcare.tests.utils.HealthcareTestSuite`, which subclasses `erpnext.tests.utils.ERPNextTestSuite`. `BootStrapTestData` in the same module creates shared master data: company, items, departments, users, patients, practitioners, service units, templates and so on.
- **Layout**: tests sit next to their DocType as `healthcare/healthcare/doctype/<name>/test_<name>.py`. There are about 85 such files. Cross-cutting tests live in `healthcare/tests/`.
- **Style**:
  - Use `setUp` with `super().setUp()`.
  - Clean tables explicitly with `frappe.db.sql("delete from `tabX`")`.
  - Configure `Healthcare Settings` inside the test.
  - Reuse factories exported from other test modules, e.g. `create_appointment` from `test_patient_appointment`.
  - ERPNext fixtures such as `make_pos_profile` are fine to use.
- **CI**:
  - Runs on PRs (except PRs touching only css/js/md/html/csv) and nightly.
  - Uses a fresh bench on MariaDB 11.8 with frappe/erpnext/payments on the matching branch. Fork branches (`biograph-fh`, `goal/*`) fall back to `version-16`.
  - Coverage is captured only on non-PR runs and uploaded to Codecov.
- **Coverage expectations** (`codecov.yml`): project coverage must not drop more than 0.5%. Patch coverage target is **85%** on PRs to `develop`.
- **Fork caveat**: the fork has no CI baseline yet. The first CI run on a goal PR becomes the baseline (see the upstream-sync ledger).
