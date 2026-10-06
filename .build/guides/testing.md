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
  - healthcare/healthcare/doctype/practitioner_availability/test_practitioner_availability.py
  - codecov.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's unittest-based test runner, run through bench (`bench --site test_site run-parallel-tests --app healthcare`). CI uses a MariaDB service and a fresh `test_site`.
- **Layout:** tests sit next to each doctype as `healthcare/healthcare/doctype/<name>/test_<name>.py`. The ERPNext overrides have their own tests (`custom_doctype/test_sales_invoice.py`). Shared fixtures and helpers are in `healthcare/tests/utils.py`, and utils tests are in `healthcare/tests/test_utils.py`.
- **Base class:** extend `HealthcareTestSuite` from `healthcare.tests.utils`. It builds on `erpnext.tests.utils.ERPNextTestSuite`. `BootStrapTestData` creates master data (company, practitioners, patients, templates, insurance payors, and so on) with `_Test` names such as `_Test Company` and `_Test Lab Test - with Sample`. Reuse these records instead of creating new ad-hoc ones.
- **Style:** use `self.assertEqual` and `self.assertTrue`. Use `self.assertRaises(frappe.ValidationError, doc.submit)` or `with self.assertRaises(frappe.ValidationError):` for validation paths. Toggle settings with `frappe.db.set_single_value("Healthcare Settings", …)` and reset them afterwards.
- **Coverage:** Codecov sets the **patch target to 85%** on PRs and allows a 0.5% project threshold. Coverage is collected only on non-PR (scheduled) runs.
- CI skips PRs that touch only `css/js/md/html/csv` files.
- Fork note: `biograph-fh` has no CI baseline yet (see the wiki ledger), so the first goal-PR run is the baseline.
