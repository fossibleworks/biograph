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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - .github/workflows/ci.yml
  - codecov.yml
  - .github/labeler.yml
---

- **Framework**: Frappe's unittest-based runner. Tests subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`. That class extends ERPNext's `ERPNextTestSuite`.
- **Shared fixtures**: `BootStrapTestData` in `healthcare/tests/utils.py` creates master data. This includes company, service items, patients, practitioners, service units, templates and insurance payors, using `_Test …` names.
- **Layout**: one `test_<doctype>.py` inside each DocType folder, about 85 test files. Cross-cutting tests live in `healthcare/tests/` and `healthcare/healthcare/custom_doctype/test_sales_invoice.py`.
- **Style**:
  - Clean up in `setUp` with `frappe.db.sql("delete from `tab…`")`.
  - Configure `Healthcare Settings` inside the test.
  - Reuse factory helpers exported by other tests, for example `create_appointment` from `test_patient_appointment`.
  - Assert on DB state with `frappe.db.get_value` and `self.assertEqual` / `self.assertTrue`.
- **Running**: `bench --site test_site run-parallel-tests --app healthcare` in CI. This runs against MariaDB with ERPNext and payments installed.
- **Coverage expectations**:
  - Codecov patch target is **85%** on PRs to `develop`. The project threshold is 0.5%.
  - Coverage is uploaded only on non-PR (scheduled) runs.
  - The labeler adds `needs-tests` when a PR changes `healthcare/**/*.py` without touching any `test*.py`.
