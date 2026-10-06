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

- **Framework:** Frappe's unittest-based test runner. Tests run inside a bench against a real MariaDB site (`bench --site test_site run-parallel-tests --app healthcare`). There are no JS or Vue tests.
- **Layout:** each doctype has `test_<doctype>.py` next to its controller (85 test files). Shared fixtures live in `healthcare/tests/utils.py`.
- **Base class:** subclass `HealthcareTestSuite` (from `healthcare.tests.utils`, built on ERPNext's `ERPNextTestSuite`). `BootStrapTestData` seeds master data: company, service items, patients, practitioners, service units, templates, insurance payors and more. Test records use the `_Test ...` naming prefix.
- **Patterns:** call `super().setUp()`, then clean tables with `frappe.db.sql("delete from `tabX`")` and change `Healthcare Settings` with `save(ignore_permissions=True)`. Reuse helper factories from other tests, e.g. `create_appointment` and `update_status` from `test_patient_appointment`. Assert with `assertEqual`/`assertTrue` on `frappe.db.get_value` results.
- **CI:** `ci.yml` runs the server tests on PRs, except PRs that touch only css/js/md/html/csv, and nightly. Coverage is captured only on non-PR runs and uploaded to Codecov.
- **Coverage expectations** (`codecov.yml`): project coverage must not drop more than 0.5%. **Patch coverage target is 85%** on PRs to `develop`.
- The fork's `biograph-fh` branch has no CI baseline yet. `wiki/upstream-sync-version-16.md` records known local test failures, so compare against that ledger when you judge regressions.
