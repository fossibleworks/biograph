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
  - .github/workflows/ci.yml
  - .github/labeler.yml
  - codecov.yml
---

**Framework:** Frappe's unittest-based runner. Tests subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`, which builds on ERPNext's `ERPNextTestSuite`. `BootStrapTestData` seeds master data under the `_Test` prefix: `_Test Company`, `_Test Medical Department`, `_Test Insurance Payor`, and others.

**Layout:** each doctype keeps its tests next to it as `doctype/<name>/test_<name>.py`. There are about 110 test files. Shared helpers live in `healthcare/tests/`, and `custom_doctype/test_sales_invoice.py` covers the ERPNext extensions.

**Style:**
- `setUp` calls `super().setUp()` and cleans tables with `frappe.db.sql("delete from `tab...`")`.
- Fixtures are built through module-level helpers such as `create_appointment(...)` and `create_encounter(...)`.
- Settings are toggled per test with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- Assertions use `self.assertEqual`, often against `frappe.db.get_value`.

**CI:**
- `ci.yml` runs `bench run-parallel-tests --app healthcare` on PRs, skipping PRs that change only css/js/md/html/csv. It also runs nightly.
- Coverage is captured only on non-PR runs and uploaded to Codecov. `codecov.yml` sets `require_ci_to_pass`.
- The labeler adds `needs-tests` when `healthcare/**/*.py` changes without a `test*.py` change.

**Caveat:** the fork has no CI baseline yet. The ledger notes that the first CI run on a goal PR becomes the baseline, and there is no local bench.
